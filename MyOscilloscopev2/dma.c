/* =============================================================================
 * MyOscilloscope — firmware para Raspberry Pi Pico 2 (RP2350)
 *
 * Arquivo     : dma.c
 * Autor       : Matheus Arantes Tomaz
 * Instituição : Escola Politécnica da Universidade de São Paulo
 *
 * Descrição:
 *   Dois canais de DMA encadeados (ping → pong → ping ...) copiam o FIFO do
 *   ADC continuamente; o ADC nunca para. A IRQ apenas avisa o core1 qual
 *   buffer terminou e prepara o canal para a próxima volta.
 * ============================================================================= */

#include "dma.h"
#include "adc.h"
#include "hardware/irq.h"
#include "hardware/adc.h"

int dma_channel_ping;
int dma_channel_pong;
queue_t dma_queue;

// -----------------------------------------------------------------------------
// Configura os dois canais (16 bits, lê sempre o FIFO, escreve incrementando)
// e encadeia um no outro. Chamada pelo core1.
// -----------------------------------------------------------------------------
void init_DMA() {
    dma_channel_ping = dma_claim_unused_channel(true);
    dma_channel_pong = dma_claim_unused_channel(true);

    // --- Canal ping ---
    dma_channel_config c_ping = dma_channel_get_default_config(dma_channel_ping);
    channel_config_set_transfer_data_size(&c_ping, DMA_SIZE_16);
    channel_config_set_read_increment(&c_ping, false);
    channel_config_set_write_increment(&c_ping, true);
    channel_config_set_dreq(&c_ping, DREQ_ADC);
    channel_config_set_chain_to(&c_ping, dma_channel_pong);
    dma_channel_configure(dma_channel_ping, &c_ping,
                          ping, &adc_hw->fifo, BUFFER_SIZE * 2, false);

    // --- Canal pong ---
    dma_channel_config c_pong = dma_channel_get_default_config(dma_channel_pong);
    channel_config_set_transfer_data_size(&c_pong, DMA_SIZE_16);
    channel_config_set_read_increment(&c_pong, false);
    channel_config_set_write_increment(&c_pong, true);
    channel_config_set_dreq(&c_pong, DREQ_ADC);
    channel_config_set_chain_to(&c_pong, dma_channel_ping);
    dma_channel_configure(dma_channel_pong, &c_pong,
                          pong, &adc_hw->fifo, BUFFER_SIZE * 2, false);

    // --- Interrupção de fim de buffer ---
    dma_channel_set_irq0_enabled(dma_channel_ping, true);
    dma_channel_set_irq0_enabled(dma_channel_pong, true);
    irq_set_exclusive_handler(DMA_IRQ_0, dma_interrupt_handler);
    irq_set_enabled(DMA_IRQ_0, true);
}

// -----------------------------------------------------------------------------
// O chain_to já iniciou o próximo canal — o ADC nunca para.
// A IRQ apenas enfileira o buffer concluído e rearma o canal que terminou.
// -----------------------------------------------------------------------------
void dma_interrupt_handler() {
    if (dma_channel_get_irq0_status(dma_channel_ping)) {
        dma_channel_acknowledge_irq0(dma_channel_ping);
        uint16_t *ptr = ping;
        queue_try_add(&dma_queue, &ptr);
        dma_channel_set_trans_count(dma_channel_ping, BUFFER_SIZE * 2, false);
        dma_channel_set_write_addr(dma_channel_ping, ping, false);
    }
    else if (dma_channel_get_irq0_status(dma_channel_pong)) {
        dma_channel_acknowledge_irq0(dma_channel_pong);
        uint16_t *ptr = pong;
        queue_try_add(&dma_queue, &ptr);
        dma_channel_set_trans_count(dma_channel_pong, BUFFER_SIZE * 2, false);
        dma_channel_set_write_addr(dma_channel_pong, pong, false);
    }
}
