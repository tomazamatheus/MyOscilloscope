/* =============================================================================
 * MyOscilloscope — firmware para Raspberry Pi Pico 2 (RP2350)
 *
 * Arquivo     : adc.c
 * Autor       : Matheus Arantes Tomaz
 * Instituição : Escola Politécnica da Universidade de São Paulo
 *
 * Descrição:
 *   Configuração do ADC: entradas CH1 (GPIO 26) e CH2 (GPIO 27), taxa máxima
 *   e FIFO alimentando o DMA. Também define os buffers ping/pong.
 * ============================================================================= */

#include "adc.h"

uint16_t ping[BUFFER_SIZE * 2];
uint16_t pong[BUFFER_SIZE * 2];

void init_adc() {
    adc_init();
    adc_gpio_init(26);  // CH1
    adc_gpio_init(27);  // CH2

    // O ADC usa clk_adc = 48 MHz (não o clock do sistema de 150 MHz).
    // clkdiv = 0 → 1 conversão a cada 96 ciclos = 500 kSps no total
    //            = 250 kSps por canal (CH1/CH2 intercalados, defasados 2 µs).
    adc_set_clkdiv(ADC_CLKDIV);

    adc_fifo_setup(
        true,   // Escrita no FIFO ativada
        true,   // DMA ativado
        1,      // DREQ com 1 amostra
        false,  // Bit de erro desligado: amostras são compactadas em 12 bits
        false   // SHIFT desativado: mantém os 12 bits originais
    );

    adc_set_round_robin(0x03);  // CH1 e CH2 alternados
    adc_select_input(0);        // começa pelo CH1
}
