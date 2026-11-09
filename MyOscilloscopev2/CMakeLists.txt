# ==============================================================================
# MyOscilloscope — firmware para Raspberry Pi Pico 2 (RP2350)
#
# Arquivo     : CMakeLists.txt
# Autor       : Matheus Arantes Tomaz
# Instituição : Escola Politécnica da Universidade de São Paulo
#
# Descrição:
#   Configuração de compilação: Pico SDK 2.2.0, placa pico2, bibliotecas de
#   hardware, buffers do USB CDC e saída USB (stdio) em vez de UART.
# ==============================================================================

# == DO NOT EDIT THE FOLLOWING LINES for the Raspberry Pi Pico VS Code Extension to work ==
if(WIN32)
    set(USERHOME $ENV{USERPROFILE})
else()
    set(USERHOME $ENV{HOME})
endif()
set(sdkVersion 2.2.0)
set(toolchainVersion 14_2_Rel1)
set(picotoolVersion 2.2.0-a4)
set(picoVscode ${USERHOME}/.pico-sdk/cmake/pico-vscode.cmake)
if (EXISTS ${picoVscode})
    include(${picoVscode})
endif()
# ====================================================================================
set(PICO_BOARD pico2 CACHE STRING "Board type")

cmake_minimum_required(VERSION 3.13)

# Importa o Pico SDK
include(pico_sdk_import.cmake)

project(MyOscilloscopev2 C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

# Inicializa o SDK
pico_sdk_init()

# Executável
add_executable(MyOscilloscopev2
    MyOscilloscopev2.c
    adc.c
    dma.c
    pwm.c
    usbCommunication.c
)

# Bibliotecas de hardware (o nome deve ser o mesmo do executável acima)
target_link_libraries(MyOscilloscopev2
    pico_stdlib
    hardware_adc
    hardware_dma
    hardware_pwm
    hardware_irq      # interrupções do DMA
    hardware_clocks   # cálculos de frequência
    pico_multicore    # core1
    pico_util         # queue_t
)

# Buffers do USB CDC (o padrão do SDK é só 64 bytes, limitando a vazão).
# TX FIFO maior + transferências de 1 KB (16 pacotes de 64 B por transferência).
# O TinyUSB só re-arma a recepção quando o FIFO de RX tem >= EP_BUFSIZE livres;
# com RX_BUFSIZE = 2×EP_BUFSIZE ele aceita novos comandos mesmo com dados
# ainda não lidos (evita bloquear o write() do Python).
target_compile_definitions(MyOscilloscopev2 PRIVATE
    CFG_TUD_CDC_TX_BUFSIZE=8192
    CFG_TUD_CDC_EP_BUFSIZE=1024
    CFG_TUD_CDC_RX_BUFSIZE=2048
)

# stdio pela USB; UART desligada
pico_enable_stdio_usb(MyOscilloscopev2 1)
pico_enable_stdio_uart(MyOscilloscopev2 0)

# Gera o arquivo .uf2
pico_add_extra_outputs(MyOscilloscopev2)

# Inclui a pasta atual para encontrar os .h
target_include_directories(MyOscilloscopev2 PUBLIC ${CMAKE_CURRENT_LIST_DIR})
