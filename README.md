# MyOscilloscope

Osciloscópio de 2 canais com Raspberry Pi Pico 2 (RP2350) e interface em Python (PySide6 + pyqtgraph).

| Pasta | Conteúdo |
| --- | --- |
| `MyOscilloscope_Pi_Alpha_1.5_26_03_2026/` | Aplicação Python (`MyOscilloscope.py`; aquisição em `Main_Screen1.py`) |
| `MyOscilloscopev2/` | Firmware do Pico 2 (C, Pico SDK 2.2.0) |

**Firmware e aplicação andam juntos:** ao mudar o protocolo USB, atualize os dois.

## Características

- ADC a 500 kSps: 250 kSps por canal (2 canais) ou 500 kSps (só CH1, quando CH2 e Math estão desligados).
- Trigger no firmware (borda, histerese, média móvel, modo auto); o PC recebe só a janela visível.
- Frame cheio de 240 ms a cada ~1 s para a FFT.
- Frames com soma de verificação; reconexão sem reiniciar o Pico.

## Firmware

1. Compilar: `ninja -C MyOscilloscopev2/build` (ninja de `%USERPROFILE%\.pico-sdk\ninja`; a pasta `build` é gerada pela extensão Raspberry Pi Pico do VS Code).
2. Gravar: `picotool reboot -u -f` e copiar `build/MyOscilloscopev2.uf2` para o drive `RP2350` (ou segurar BOOTSEL ao conectar).

## Aplicação

1. Criar o ambiente: `python -m venv venv_pyside` e instalar PySide6, pyqtgraph, numpy e pyserial.
2. Rodar: `venv_pyside\Scripts\python.exe MyOscilloscope.py`.
