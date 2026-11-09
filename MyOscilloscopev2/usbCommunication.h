/* =============================================================================
 * MyOscilloscope — firmware para Raspberry Pi Pico 2 (RP2350)
 *
 * Arquivo     : usbCommunication.h
 * Autor       : Matheus Arantes Tomaz
 * Instituição : Escola Politécnica da Universidade de São Paulo
 *
 * Descrição:
 *   Interface da comunicação USB (core0) e do motor de trigger (core1).
 *   Protocolo e funcionamento descritos em usbCommunication.c.
 * ============================================================================= */

#ifndef _USB_COMMUNICATION_H_
#define _USB_COMMUNICATION_H_

#include "pico/stdlib.h"
#include "pico/util/queue.h"

extern queue_t usb_queue;   // mantida por compatibilidade

void send_params(const uint16_t DCOffset);   // envia dt, conversão e offset (handshake)
void sendDMA();                              // laço do core0: handshake + streaming
void core1_entry();                          // core1: ADC/DMA + trigger

#endif
