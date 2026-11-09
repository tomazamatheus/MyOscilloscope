/* =============================================================================
 * MyOscilloscope — firmware para Raspberry Pi Pico 2 (RP2350)
 *
 * Arquivo     : MyOscilloscopev2.c
 * Autor       : Matheus Arantes Tomaz
 * Instituição : Escola Politécnica da Universidade de São Paulo
 *
 * Descrição:
 *   Ponto de entrada do firmware. Inicializa o USB, as filas entre IRQ e
 *   núcleos, o ADC e o PWM de teste, e entra no laço de comunicação
 *   (handshake → streaming → desconexão → handshake ...).
 * ============================================================================= */

#include "pico/stdlib.h"
#include "pico/multicore.h"
#include "usbCommunication.h"
#include "adc.h"
#include "dma.h"
#include "pwm.h"

int main() {
    stdio_init_all();

    // dma_queue: buffers concluídos pelo DMA (IRQ → core1)
    // usb_queue: mantida por compatibilidade (o envio hoje usa a fila de
    //            pedidos interna de usbCommunication.c)
    queue_init(&dma_queue, sizeof(uint16_t*), 2);
    queue_init(&usb_queue, sizeof(uint16_t*), 1);

    init_adc();
    setPWM();

    // Laço infinito: handshake → streaming → (desconexão) → handshake ...
    // Permite fechar e reabrir a aplicação sem reiniciar o Pico.
    sendDMA();
    return 0;
}
