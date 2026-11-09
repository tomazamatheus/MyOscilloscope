/* =============================================================================
 * MyOscilloscope — firmware para Raspberry Pi Pico 2 (RP2350)
 *
 * Arquivo     : usbCommunication.c
 * Autor       : Matheus Arantes Tomaz
 * Instituição : Escola Politécnica da Universidade de São Paulo
 *
 * Descrição:
 *   Coração do firmware: motor de trigger (core1) e comunicação USB (core0).
 *
 *   O DMA preenche ping e pong continuamente (ping → pong → ping ...).
 *   Juntos eles formam um ANEL de RING_PAIRS pares (CH1, CH2) = 480 ms.
 *   Cada par é endereçado por um índice ABSOLUTO (uint64) que só cresce.
 *
 *   core1: acompanha a posição de escrita do DMA ("head"), procura o trigger
 *          nos dados recém-chegados e, quando há dados suficientes, pede ao
 *          core0 o envio de um frame (janela de trigger ou pedaço do frame
 *          cheio para a FFT).
 *   core0: handshake, comandos vindos do Python e envio dos frames pela USB.
 *
 * FORMATO DO FRAME (little-endian):
 *   MARKER (8 bytes) | type u8 | flags u8 | pre u16 | n_pairs u32 | dados
 *   type : 0 = janela (tela)
 *          2 = pedaço do frame cheio (FFT, ~240 ms a cada ~1 s), enviado
 *              em pedaços intercalados com as janelas para não travar a tela
 *   flags: bit0 = disparado pelo trigger (0 = auto/free-run)
 *          bit1 = modo 1 canal (todas as amostras são do CH1, 2 µs)
 *          bit2 = último pedaço do frame cheio
 *   pre  : janela → índice do par onde ocorreu o trigger
 *          pedaço → posição (em pares) do pedaço dentro do frame cheio
 *   dados: n_pairs × 3 bytes (CH1 e CH2 de 12 bits compactados)
 *   + trailer u32: soma dos bytes de dados (mod 2^32) — verificação
 *
 * COMANDO DO PYTHON (linha ASCII):
 *   "C <en> <ch> <falling> <level> <hyst> <pre> <window> [avg] [single]\n"
 *   en      : 1 = trigger ativo, 0 = free-run
 *   ch      : 0 = CH1, 1 = CH2
 *   falling : 0 = borda de subida, 1 = descida
 *   level   : nível do trigger (contagens do ADC)
 *   hyst    : histerese (contagens do ADC)
 *   pre     : pré-trigger (pares)
 *   window  : tamanho da janela (pares)
 *   avg     : média móvel de N amostras usada só na DETECÇÃO do trigger
 *             (rejeita picos de ruído); opcional, padrão 1
 *   single  : 1 = modo 1 canal (só CH1 a 500 kSps); opcional, padrão 0.
 *             Nesse modo cada "par" são 2 amostras consecutivas do CH1 (2 µs).
 * ============================================================================= */

#include "usbCommunication.h"
#include "adc.h"
#include "dma.h"
#include "tusb.h"
#include "pico/multicore.h"
#include <stdio.h>
#include <stdlib.h>
#include "hardware/adc.h"
#include "hardware/dma.h"
#include "hardware/sync.h"

queue_t usb_queue;  // mantido por compatibilidade com usbCommunication.h

// Marcador de 8 bytes que inicia cada frame
static const uint16_t MARKER[4] = {0xABCD, 0xDCBA, 0xABCD, 0xDCBA};

// =============================================================================
// Constantes
// =============================================================================
#define RING_PAIRS             (2u * BUFFER_SIZE)
#define WIN_MIN                16u
#define WIN_MAX                100000u   // < RING_PAIRS: margem p/ envio seguro
#define FULL_INTERVAL_US       1000000u  // frame cheio (FFT) a cada 1 s
#define MIN_FRAME_INTERVAL_US  16000u    // no máximo ~60 janelas/s (taxa da tela)
#define AUTO_MIN_TIMEOUT_US    100000u   // modo auto: espera mínima por trigger
#define MAX_SCAN_LAG_PAIRS     20000u    // se o scan atrasar mais que isso, pula
#define CHUNK_PAIRS            512u

#define FRAME_WINDOW     0u
#define FRAME_FULL_CHUNK 2u
#define FLAG_TRIGGERED   0x01u
#define FLAG_SINGLE      0x02u
#define FLAG_LAST_CHUNK  0x04u

#define FULL_CHUNK_PAIRS     4096u    // 12 KB por pedaço (~17 ms de USB)
#define WIN_MAX_DURING_FULL  16384u   // janelas maiores esperam o frame cheio
                                      // terminar (senão os pedaços atrasam
                                      // demais e o DMA os sobrescreve)

// -----------------------------------------------------------------------------
// Configuração do trigger (escrita pelo core0, lida pelo core1)
// -----------------------------------------------------------------------------
typedef struct {
    uint8_t  enabled;
    uint8_t  channel;
    uint8_t  falling;
    uint16_t level;
    uint16_t hyst;
    uint32_t pre;
    uint32_t window;
    uint32_t avg;      // média móvel do trigger (1..TRIG_AVG_MAX amostras)
    uint8_t  single;   // 1 = modo 1 canal (só CH1, 500 kSps)
} trig_cfg_t;

#define TRIG_AVG_MAX 16u

static volatile trig_cfg_t cfg_shared = {0, 0, 0, 2048, 20, 0, 2500, 1, 0};
static volatile uint32_t   cfg_seq    = 0;

// -----------------------------------------------------------------------------
// Pedido de envio (core1 → core0)
// -----------------------------------------------------------------------------
typedef struct {
    uint64_t start;    // índice absoluto do 1º par
    uint32_t n;        // número de pares
    uint16_t pre;
    uint8_t  type;
    uint8_t  flags;
} frame_req_t;

static queue_t req_queue;
static volatile bool core0_busy = false;  // há pedido pendente/em envio
static volatile bool streaming  = false;  // core0 está no estado de streaming

// Buffers concluídos pelo DMA (só o core1 escreve)
static volatile uint32_t completed = 0;

// =============================================================================
// Utilidades
// =============================================================================

// Handshake: envia dt, fator de conversão e offset, uma linha cada
void send_params(const uint16_t DCOffset) {
    const float conv = 3.3f / 4095.0f;
    printf("%.8f\n", ADC_SAMPLE_PERIOD_S);  // dt por canal (4 µs @ 250 kSps)
    printf("%.8f\n", conv);
    printf("%d\n", DCOffset);
    stdio_flush();
}

// Ponteiro para o par de índice idx (relativo ao anel)
static inline const volatile uint16_t *ring_pair(uint32_t idx) {
    return (idx < BUFFER_SIZE) ? (const volatile uint16_t *)&ping[2u * idx]
                               : (const volatile uint16_t *)&pong[2u * (idx - BUFFER_SIZE)];
}

static bool poll_input(void);
static volatile bool handshake_pending = false;  // '1' recebido durante um envio

// -----------------------------------------------------------------------------
// send_bytes — envia um bloco pela USB CDC
//
// O tud_task() é executado em segundo plano pelo stdio_usb do SDK.
// Retorna false se o host desconectou (porta fechada) no meio do envio.
//
// IMPORTANTE: a entrada é lida também DURANTE o envio. O TinyUSB só volta a
// aceitar dados do PC quando o FIFO de RX esvazia; se o Pico parasse de ler
// enquanto envia um frame, o write() do Python bloquearia, o Python pararia
// de ler, e o Pico ficaria preso esperando espaço de TX → deadlock (tela
// congelada). Ler aqui quebra esse ciclo.
// -----------------------------------------------------------------------------
static bool send_bytes(const uint8_t *data, uint32_t total) {
    uint32_t sent = 0;
    while (sent < total) {
        if (poll_input()) handshake_pending = true;
        if (!tud_cdc_connected()) return false;
        uint32_t to_send = total - sent;
        if (to_send > 1024u) to_send = 1024u;  // seção crítica curta
        // Seção crítica: o stdio_usb do SDK roda tud_task() numa IRQ de
        // fundo, e ela também lê o FIFO de TX (tud_cdc_write_flush no fim de
        // cada transferência). Se essa IRQ entrar no meio do nosso
        // write/flush, bytes são perdidos/duplicados → frame desalinhado
        // ("bloco corrompido" na tela). Com IRQs desligadas, não há corrida.
        uint32_t irq = save_and_disable_interrupts();
        uint32_t available = tud_cdc_write_available();
        if (to_send > available) to_send = available;
        uint32_t w = 0;
        if (to_send) {
            w = tud_cdc_write(data + sent, to_send);
            tud_cdc_write_flush();
        }
        restore_interrupts(irq);
        if (w == 0) { tight_loop_contents(); continue; }
        sent += w;
    }
    return true;
}

// -----------------------------------------------------------------------------
// send_frame — envia um frame lendo direto do anel, compactando 12 bits
//   b0 = s0[7:0] | b1 = s0[11:8] | s1[3:0] << 4 | b2 = s1[11:4]
// -----------------------------------------------------------------------------
static bool send_frame(const frame_req_t *r) {
    static uint8_t chunk[CHUNK_PAIRS * 3];
    uint8_t hdr[8] = {
        r->type, r->flags,
        (uint8_t)(r->pre), (uint8_t)(r->pre >> 8),
        (uint8_t)(r->n), (uint8_t)(r->n >> 8),
        (uint8_t)(r->n >> 16), (uint8_t)(r->n >> 24),
    };
    if (!send_bytes((const uint8_t *)MARKER, sizeof(MARKER))) return false;
    if (!send_bytes(hdr, sizeof(hdr))) return false;

    uint32_t idx  = (uint32_t)(r->start % RING_PAIRS);
    uint32_t left = r->n;
    uint32_t sum  = 0;   // soma de verificação: soma dos bytes de dados (mod 2^32)
    while (left) {
        uint32_t k = left < CHUNK_PAIRS ? left : CHUNK_PAIRS;
        uint8_t *o = chunk;
        for (uint32_t i = 0; i < k; i++) {
            const volatile uint16_t *s = ring_pair(idx);
            uint16_t s0 = s[0] & 0x0FFF;
            uint16_t s1 = s[1] & 0x0FFF;
            uint8_t b0 = (uint8_t)(s0);
            uint8_t b1 = (uint8_t)((s0 >> 8) | (s1 << 4));
            uint8_t b2 = (uint8_t)(s1 >> 4);
            *o++ = b0; *o++ = b1; *o++ = b2;
            sum += (uint32_t)b0 + b1 + b2;
            if (++idx == RING_PAIRS) idx = 0;
        }
        if (!send_bytes(chunk, k * 3)) return false;
        left -= k;
    }
    // Trailer: o PC descarta o frame se a soma não bater (bytes perdidos no
    // caminho — ex.: driver do Windows descarta dados se o app demora a ler)
    uint8_t tr[4] = { (uint8_t)sum, (uint8_t)(sum >> 8),
                      (uint8_t)(sum >> 16), (uint8_t)(sum >> 24) };
    return send_bytes(tr, sizeof(tr));
}

// =============================================================================
// Comandos (core0)
// =============================================================================
static long clampl(long v, long lo, long hi) { return v < lo ? lo : (v > hi ? hi : v); }

// Interpreta "C ..." e publica a nova configuração para o core1
static void parse_cmd(const char *s) {
    if (s[0] != 'C') return;
    long v[9] = {0, 0, 0, 0, 0, 0, 0, 1, 0};   // 8º (média) e 9º (modo) opcionais
    const char *p = s + 1;
    char *end;
    for (int i = 0; i < 9; i++) {
        long x = strtol(p, &end, 10);
        if (end == p) {
            if (i >= 7) break;   // campos opcionais ausentes → padrão
            return;              // comando malformado → ignora
        }
        v[i] = x;
        p = end;
    }
    cfg_shared.avg     = (uint32_t)clampl(v[7], 1, TRIG_AVG_MAX);
    cfg_shared.single  = v[8] ? 1 : 0;
    cfg_shared.enabled = v[0] != 0;
    cfg_shared.channel = v[1] ? 1 : 0;
    cfg_shared.falling = v[2] ? 1 : 0;
    cfg_shared.level   = (uint16_t)clampl(v[3], 0, 4095);
    cfg_shared.hyst    = (uint16_t)clampl(v[4], 0, 2047);
    cfg_shared.window  = (uint32_t)clampl(v[6], WIN_MIN, WIN_MAX);
    cfg_shared.pre     = (uint32_t)clampl(v[5], 0, cfg_shared.window - 1);
    __dmb();
    cfg_seq++;
}

// Lê a entrada sem bloquear. Processa linhas de comando "C ...".
// Retorna true se chegou um '1' isolado (pedido de handshake).
static bool poll_input(void) {
    static char line[80];
    static uint32_t len = 0;
    int c;
    while ((c = stdio_getchar_timeout_us(0)) != PICO_ERROR_TIMEOUT) {
        if (len == 0) {
            if (c == '1') return true;
            if (c == 'C') line[len++] = 'C';
            continue;  // ignora '\r', '\n' e lixo fora de comando
        }
        if (c == '\n' || c == '\r') {
            line[len] = 0;
            parse_cmd(line);
            len = 0;
        } else if (len < sizeof(line) - 1) {
            line[len++] = (char)c;
        } else {
            len = 0;  // linha longa demais → descarta
        }
    }
    return false;
}

// '1' recebido agora ou durante um envio anterior
static bool handshake_requested(void) {
    if (handshake_pending) { handshake_pending = false; return true; }
    return poll_input();
}

static void wait_for_start_char(void) {
    while (!handshake_requested()) {
        sleep_us(500);
    }
}

static void handshake(void) {
    wait_for_start_char();
    send_params(0);
    wait_for_start_char();
}

static void drain_requests(void) {
    frame_req_t r;
    while (queue_try_remove(&req_queue, &r)) {}
    core0_busy = false;
}

// =============================================================================
// sendDMA — laço principal do core0
// =============================================================================
void sendDMA() {
    stdio_set_translate_crlf(&stdio_usb, false);
    queue_init(&req_queue, sizeof(frame_req_t), 1);

    // ADC + DMA + trigger rodam continuamente no core1
    multicore_launch_core1(core1_entry);

    while (true) {
        // ---------- Estado 1: aguardando a aplicação ----------
        streaming = false;
        handshake_pending = false;
        drain_requests();
        handshake();
        drain_requests();
        streaming = true;

        // ---------- Estado 2: streaming ----------
        while (true) {
            if (!tud_cdc_connected()) break;

            // '1' durante o streaming = aplicação reaberta → refaz handshake
            if (handshake_requested()) {
                streaming = false;
                drain_requests();
                send_params(0);
                wait_for_start_char();
                drain_requests();
                streaming = true;
                continue;
            }

            frame_req_t r;
            if (!queue_try_remove(&req_queue, &r)) {
                tight_loop_contents();
                continue;
            }
            bool ok = send_frame(&r);
            core0_busy = false;
            if (!ok) break;
        }

        tud_cdc_write_clear();
    }
}

// =============================================================================
// core1: posição do DMA + trigger
// =============================================================================

static uint64_t last_head = 0;       // reiniciado ao trocar o modo do ADC
static bool     single_mode = false; // modo atual da aquisição (core1)

// -----------------------------------------------------------------------------
// get_head — índice absoluto do próximo par a ser escrito pelo DMA (monotônico)
// -----------------------------------------------------------------------------
static uint64_t get_head(void) {
    uint32_t c = completed;
    int ch;
    uint32_t base, bp;
    if (dma_channel_is_busy(dma_channel_ping)) {
        ch = dma_channel_ping; base = (uint32_t)ping; bp = 0;
    } else if (dma_channel_is_busy(dma_channel_pong)) {
        ch = dma_channel_pong; base = (uint32_t)pong; bp = 1;
    } else {
        return last_head;  // instante da troca de canal
    }
    uint32_t off = (dma_hw->ch[ch].write_addr - base) / 4u;  // 4 bytes por par
    if (off > BUFFER_SIZE) off = BUFFER_SIZE;
    // Buffers pares = ping, ímpares = pong. Se a paridade não bate, o DMA já
    // trocou de buffer mas o core1 ainda não contou a conclusão.
    uint64_t buf_idx = ((c & 1u) == bp) ? (uint64_t)c : (uint64_t)c + 1u;
    uint64_t h = buf_idx * BUFFER_SIZE + off;
    if (h > last_head) last_head = h;
    return last_head;
}

// -----------------------------------------------------------------------------
// restart_acquisition — reinicia a aquisição no modo pedido
//   2 canais: round-robin CH1/CH2 → 250 kSps por canal (par = CH1, CH2)
//   1 canal : só CH1          → 500 kSps (par = 2 amostras seguidas do CH1)
// A taxa total do ADC (500 kSps) e a duração de um "par" (4 µs) não mudam,
// então toda a lógica de anel/trigger/janelas continua igual.
// Só pode ser chamada com o core0 parado (sem envio em andamento).
// -----------------------------------------------------------------------------
static void restart_acquisition(bool single) {
    adc_run(false);
    dma_channel_set_irq0_enabled(dma_channel_ping, false);
    dma_channel_set_irq0_enabled(dma_channel_pong, false);
    dma_channel_abort(dma_channel_pong);
    dma_channel_abort(dma_channel_ping);
    dma_channel_abort(dma_channel_pong);   // caso o abort do ping tenha encadeado
    dma_channel_acknowledge_irq0(dma_channel_ping);
    dma_channel_acknowledge_irq0(dma_channel_pong);
    adc_fifo_drain();

    uint16_t *p;
    while (queue_try_remove(&dma_queue, &p)) {}

    adc_select_input(0);                       // sempre começa pelo CH1
    adc_set_round_robin(single ? 0x00 : 0x03); // 0 = só a entrada selecionada

    dma_channel_set_write_addr(dma_channel_ping, ping, false);
    dma_channel_set_trans_count(dma_channel_ping, BUFFER_SIZE * 2, false);
    dma_channel_set_write_addr(dma_channel_pong, pong, false);
    dma_channel_set_trans_count(dma_channel_pong, BUFFER_SIZE * 2, false);

    completed   = 0;
    last_head   = 0;
    single_mode = single;

    dma_channel_set_irq0_enabled(dma_channel_ping, true);
    dma_channel_set_irq0_enabled(dma_channel_pong, true);
    dma_channel_start(dma_channel_ping);
    adc_run(true);
}

// Entrega um pedido de envio ao core0 (marca o modo 1 canal nas flags)
static void request_frame(uint64_t start, uint32_t n, uint16_t pre,
                          uint8_t type, uint8_t flags) {
    if (single_mode) flags |= FLAG_SINGLE;
    frame_req_t r = { start, n, pre, type, flags };
    core0_busy = true;
    if (!queue_try_add(&req_queue, &r)) core0_busy = false;
}

// =============================================================================
// core1_entry — laço principal do core1
// =============================================================================
void core1_entry() {
    init_DMA();
    adc_run(true);
    dma_channel_start(dma_channel_ping);

    trig_cfg_t cfg = {0, 0, 0, 2048, 20, 0, 2500, 1, 0};
    uint32_t seen_seq = 0xFFFFFFFFu;
    bool mode_change_pending = false;

    // Frame cheio (FFT) enviado em pedaços, à medida que o DMA grava
    bool     full_active = false;
    uint64_t full_start  = 0;
    uint32_t full_sent   = 0;
    bool     chunk_turn  = false;   // alterna pedaço ↔ janela

    // Estado da busca do trigger
    uint64_t scan_pos = 0, trig_pos = 0, last_end = 0;
    uint32_t scan_idx = 0;                    // scan_pos % RING_PAIRS (incremental)
    bool have_trig = false, armed = false, was_busy = false;
    uint32_t run_sum = 0, sum_n = 0;          // soma corrente da média do trigger
    uint64_t sum_pos = UINT64_MAX;            // scan_pos para o qual run_sum vale
    uint64_t t_last_full = 0, t_last_frame = 0, t_scan_start = 0;

    while (true) {
        // --- Conta buffers concluídos pelo DMA ---
        uint16_t *p;
        while (queue_try_remove(&dma_queue, &p)) {
            uint32_t c = completed;
            uint32_t expect = (p == ping) ? 0u : 1u;
            if ((c & 1u) != expect) c++;  // corrige se alguma conclusão se perdeu
            completed = c + 1u;
        }

        uint64_t head = get_head();
        uint64_t now  = time_us_64();

        // --- Nova configuração? ---
        uint32_t s = cfg_seq;
        if (s != seen_seq) {
            trig_cfg_t n;
            __dmb();
            n.enabled = cfg_shared.enabled;
            n.channel = cfg_shared.channel;
            n.falling = cfg_shared.falling;
            n.level   = cfg_shared.level;
            n.hyst    = cfg_shared.hyst;
            n.pre     = cfg_shared.pre;
            n.window  = cfg_shared.window;
            n.avg     = cfg_shared.avg;
            n.single  = cfg_shared.single;
            __dmb();
            if (cfg_seq != s) continue;  // mudou durante a cópia → tenta de novo
            seen_seq = s;
            if (n.single != cfg.single) mode_change_pending = true;

            // Só mudanças "estruturais" reiniciam a busca. Mudar apenas o
            // nível/histerese (ex.: trigger automático seguindo a média do
            // sinal, várias vezes por segundo) NÃO pode reiniciar nada —
            // senão a busca nunca termina e a tela congela.
            bool structural = n.enabled != cfg.enabled || n.channel != cfg.channel ||
                              n.falling != cfg.falling || n.pre != cfg.pre ||
                              n.window != cfg.window || n.avg != cfg.avg;
            cfg = n;
            if (structural) {
                have_trig = false;
                armed     = false;
                scan_pos  = head;
                scan_idx  = (uint32_t)(scan_pos % RING_PAIRS);
            }
            // t_scan_start NÃO é zerado: o modo auto continua garantindo
            // atualização da tela mesmo sob mudanças contínuas.
        }

        if (!streaming || core0_busy) { was_busy = true; continue; }
        // Acabou um envio (ex.: frame cheio de ~250 ms): o tempo gasto
        // enviando não conta para o modo auto, senão ele dispararia antes
        // de dar chance ao trigger → janela sem disparo (tela "pulando").
        if (was_busy) { was_busy = false; t_scan_start = now; }

        // --- Troca de modo (1 ↔ 2 canais): só com o core0 parado ---
        if (mode_change_pending) {
            restart_acquisition(cfg.single != 0);
            mode_change_pending = false;
            scan_pos = 0; scan_idx = 0; last_end = 0;
            have_trig = false; armed = false;
            sum_pos = UINT64_MAX;
            full_active = false;
            t_scan_start = now;
            continue;
        }

        const uint32_t W = cfg.window;
        const uint32_t P = cfg.pre;

        // --- 1) Frame cheio (FFT) em pedaços, intercalado com as janelas ---
        // Começa no head ATUAL e acompanha o DMA: cada pedaço é enviado logo
        // que gravado, então os dados nunca correm risco de ser sobrescritos
        // e a tela não para por ~0,3 s como no envio de uma vez só.
        if (!full_active && now - t_last_full >= FULL_INTERVAL_US) {
            full_active = true;
            full_start  = head;
            full_sent   = 0;
            t_last_full = now;
        }
        if (full_active) {
            uint32_t remaining = BUFFER_SIZE - full_sent;
            uint32_t k = remaining < FULL_CHUNK_PAIRS ? remaining : FULL_CHUNK_PAIRS;
            uint64_t avail = head - (full_start + full_sent);
            bool lagging = avail >= 2u * FULL_CHUNK_PAIRS;   // não deixa acumular
            if (avail >= k && (chunk_turn || lagging)) {
                uint8_t fl = (full_sent + k == BUFFER_SIZE) ? FLAG_LAST_CHUNK : 0;
                request_frame(full_start + full_sent, k, (uint16_t)full_sent,
                              FRAME_FULL_CHUNK, fl);
                full_sent += k;
                if (full_sent >= BUFFER_SIZE) full_active = false;
                chunk_turn = false;
                continue;
            }
            // Janelas grandes demorariam a enviar e atrasariam os pedaços
            if (W > WIN_MAX_DURING_FULL) continue;
        }
        if (head < W + P + 1u) continue;  // aguarda dados suficientes p/ a janela

        // Intervalo mínimo entre janelas: 2× a duração da janela. Mais rápido
        // que isso só reenviaria dados sobrepostos e saturaria a USB (o ADC
        // gera 750 kB/s; a USB entrega ~720 kB/s) — com a USB saturada, o
        // driver do Windows descarta dados quando o app atrasa a leitura.
        // Carga máxima: 750/2 + frame cheio (180 kB/s) ≈ 555 kB/s.
        {
            uint64_t min_iv = 2u * (uint64_t)W * 4u;   // 4 µs por par
            if (min_iv < MIN_FRAME_INTERVAL_US) min_iv = MIN_FRAME_INTERVAL_US;
            if (now - t_last_frame < min_iv) continue;
        }

        // --- 2) Free-run ---
        if (!cfg.enabled) {
            request_frame(head - W, W, 0, FRAME_WINDOW, 0);
            t_last_frame = now;
            chunk_turn   = true;
            continue;
        }

        // --- 3) Trigger encontrado: espera chegar o fim da janela ---
        if (have_trig) {
            if (head >= trig_pos - P + W) {
                request_frame(trig_pos - P, W, (uint16_t)P, FRAME_WINDOW, FLAG_TRIGGERED);
                last_end     = trig_pos - P + W;
                have_trig    = false;
                armed        = false;
                t_last_frame = now;
                chunk_turn   = true;
                t_scan_start = now;
                scan_pos     = last_end;
                scan_idx     = (uint32_t)(scan_pos % RING_PAIRS);
            }
            continue;
        }

        // --- 4) Procura o trigger nos dados novos ---
        if (scan_pos < last_end) {
            scan_pos = last_end;
            scan_idx = (uint32_t)(scan_pos % RING_PAIRS);
        }
        // Scan atrasado (ex.: após enviar frame cheio) → recomeça perto do head,
        // mantendo pelo menos P pares antes para o pré-trigger.
        if (head - scan_pos > MAX_SCAN_LAG_PAIRS) {
            scan_pos = head - (P + 1u);
            scan_idx = (uint32_t)(scan_pos % RING_PAIRS);
            armed    = false;
        }
        // Não dispara antes de haver P pares de histórico
        if (scan_pos < P) {
            scan_pos = P;
            scan_idx = (uint32_t)(scan_pos % RING_PAIRS);
        }

        const uint16_t level = cfg.level;
        const uint16_t lo = (level > cfg.hyst) ? level - cfg.hyst : 0;
        const uint16_t hi = (level + cfg.hyst < 4095) ? level + cfg.hyst : 4095;
        const uint32_t chn = cfg.channel;
        // Detecção sobre a MÉDIA MÓVEL das últimas N amostras (filtro de
        // ruído do trigger): picos isolados de ruído não armam/disparam.
        // Compara somas (N×valor) para evitar divisão.
        const uint32_t N = cfg.avg;
        const uint32_t lvlN = (uint32_t)level * N, loN = (uint32_t)lo * N, hiN = (uint32_t)hi * N;

        // Soma corrente O(1) por amostra: run_sum guarda as N-1 amostras
        // anteriores a scan_pos. Se scan_pos foi reposicionado, recalcula.
        if (sum_pos != scan_pos || sum_n != N) {
            run_sum = 0;
            uint32_t k = scan_idx;
            for (uint32_t i = 1; i < N; i++) {
                k = (k == 0) ? RING_PAIRS - 1 : k - 1;
                run_sum += ring_pair(k)[chn] & 0x0FFF;
            }
            sum_pos = scan_pos;
            sum_n   = N;
        }

        while (scan_pos < head) {
            // janela da média: [scan_idx-N+1 .. scan_idx]
            uint32_t sumv = run_sum + (ring_pair(scan_idx)[chn] & 0x0FFF);
            if (!cfg.falling) {
                if (sumv < loN) armed = true;
                else if (armed && sumv >= lvlN) { have_trig = true; }
            } else {
                if (sumv > hiN) armed = true;
                else if (armed && sumv <= lvlN) { have_trig = true; }
            }
            if (have_trig) {
                // A média atrasa (N-1)/2 amostras: compensa para o disparo
                // cair no cruzamento real
                trig_pos = scan_pos - (N - 1u) / 2u;
                sum_pos  = UINT64_MAX;   // estado da soma inválido após o disparo
                break;
            }
            // Avança: entra a amostra atual, sai a mais antiga da janela
            uint32_t oldest = (scan_idx >= N - 1u) ? scan_idx - (N - 1u)
                                                   : scan_idx + RING_PAIRS - (N - 1u);
            run_sum = sumv - (ring_pair(oldest)[chn] & 0x0FFF);
            scan_pos++;
            if (++scan_idx == RING_PAIRS) scan_idx = 0;
            sum_pos = scan_pos;
        }
        if (have_trig) continue;

        // --- 5) Modo auto: sem trigger por muito tempo → janela mais recente ---
        uint64_t win_us  = (uint64_t)W * 4u;  // 4 µs por par
        uint64_t timeout = 2u * win_us;
        if (timeout < AUTO_MIN_TIMEOUT_US) timeout = AUTO_MIN_TIMEOUT_US;
        if (now - t_scan_start > timeout) {
            request_frame(head - W, W, 0, FRAME_WINDOW, 0);
            last_end     = head;
            t_last_frame = now;
            chunk_turn   = true;
            t_scan_start = now;
            armed        = false;
        }
    }
}
