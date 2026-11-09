/* =============================================================================
 * MyOscilloscope — firmware para Raspberry Pi Pico 2 (RP2350)
 *
 * Arquivo     : adc.h
 * Autor       : Matheus Arantes Tomaz
 * Instituição : Escola Politécnica da Universidade de São Paulo
 *
 * Descrição:
 *   Parâmetros do ADC (taxa de amostragem) e dos buffers de aquisição
 *   ping/pong preenchidos pelo DMA.
 * ============================================================================= */

#ifndef _ADC_H_
#define _ADC_H_

#include "pico/stdlib.h"
#include "hardware/adc.h"

// -----------------------------------------------------------------------------
// Taxa de amostragem
//   clk_adc = 48 MHz, 96 ciclos por conversão → 500 kSps no total.
//   Round-robin em 2 canais → 250 kSps por canal.
//   ADC_CLKDIV = 0 → conversões back-to-back (máximo possível).
// -----------------------------------------------------------------------------
#define ADC_CLK_HZ     48000000.0
#define ADC_CLKDIV     0
#define ADC_NUM_CH     2

// Período entre amostras do MESMO canal (s): 2 × 96 / 48 MHz = 4 µs
#define ADC_SAMPLE_PERIOD_S \
    ((ADC_CLKDIV < 96 ? 96.0 : (ADC_CLKDIV + 1.0)) * ADC_NUM_CH / ADC_CLK_HZ)

// -----------------------------------------------------------------------------
// Buffers ping/pong
//   BUFFER_SIZE = 60000 pares (amostras por canal) por buffer
//   Tempo por buffer = 60000 / 250000 = 240 ms de dados contínuos
//   Ping + pong = 2 × 60000 × 2 canais × 2 bytes = 480 KB (RAM total: 520 KB)
// -----------------------------------------------------------------------------
#define BUFFER_SIZE 60000
#define DC_SAMPLES  100000

extern uint16_t ping[BUFFER_SIZE * 2];
extern uint16_t pong[BUFFER_SIZE * 2];

void init_adc();

#endif
