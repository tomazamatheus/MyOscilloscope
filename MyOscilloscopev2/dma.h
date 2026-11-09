/* =============================================================================
 * MyOscilloscope — firmware para Raspberry Pi Pico 2 (RP2350)
 *
 * Arquivo     : dma.h
 * Autor       : Matheus Arantes Tomaz
 * Instituição : Escola Politécnica da Universidade de São Paulo
 *
 * Descrição:
 *   Canais de DMA ping/pong que copiam o FIFO do ADC para os buffers, e a
 *   fila que avisa o core1 a cada buffer concluído.
 * ============================================================================= */

#ifndef _DMA_H_
#define _DMA_H_

#include "pico/stdlib.h"
#include "hardware/dma.h"
#include "pico/util/queue.h"

extern int dma_channel_ping;
extern int dma_channel_pong;
extern queue_t dma_queue;   // ponteiro do buffer concluído (IRQ → core1)

void init_DMA();
void dma_interrupt_handler();

#endif
