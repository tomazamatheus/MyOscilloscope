/* =============================================================================
 * MyOscilloscope — firmware para Raspberry Pi Pico 2 (RP2350)
 *
 * Arquivo     : pwm.h
 * Autor       : Matheus Arantes Tomaz
 * Instituição : Escola Politécnica da Universidade de São Paulo
 *
 * Descrição:
 *   Sinal de teste: onda quadrada no GPIO 0, para conferir as entradas
 *   do osciloscópio sem gerador externo.
 *   Frequência = 150 MHz / PWM_CLK_DIVIDER / (WRAP_VALUE + 1) ≈ 519 Hz.
 * ============================================================================= */

#ifndef _PWM_H_
#define _PWM_H_

#include "hardware/pwm.h"
#include "hardware/gpio.h"

// Configuração do PWM
#define PWM_CHANNEL     0                        // número do GPIO
#define PWM_CLK_DIVIDER 34
#define WRAP_VALUE      (250 * PWM_CLK_DIVIDER)
#define PWM_LEVEL       (WRAP_VALUE / 2)         // ciclo de trabalho de 50%

void setPWM(void);

#endif // _PWM_H_
