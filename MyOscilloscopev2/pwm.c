/* =============================================================================
 * MyOscilloscope — firmware para Raspberry Pi Pico 2 (RP2350)
 *
 * Arquivo     : pwm.c
 * Autor       : Matheus Arantes Tomaz
 * Instituição : Escola Politécnica da Universidade de São Paulo
 *
 * Descrição:
 *   Liga o sinal de teste (onda quadrada de 50%) no GPIO 0.
 * ============================================================================= */

#include "pwm.h"

void setPWM(void) {
    gpio_set_function(PWM_CHANNEL, GPIO_FUNC_PWM);

    uint slice_num = pwm_gpio_to_slice_num(PWM_CHANNEL);

    pwm_set_clkdiv(slice_num, PWM_CLK_DIVIDER);
    pwm_set_wrap(slice_num, WRAP_VALUE);
    pwm_set_chan_level(slice_num, pwm_gpio_to_channel(PWM_CHANNEL), PWM_LEVEL);

    pwm_set_enabled(slice_num, true);
}
