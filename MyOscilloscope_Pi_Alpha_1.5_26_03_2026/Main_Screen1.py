import sys, math, time, serial, struct
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout
import os
os.environ["PYQTGRAPH_QT_LIB"] = "PySide6"
import pyqtgraph as pg
from pyqtgraph import PlotWidget, mkPen, QtCore
import numpy as np
from PySide6.QtCore import QThread, QObject, Signal, QTimer, Qt
from PySide6.QtGui import QIcon, QFont
from button import Button

# ==============================================================================
# Sincronize este valor com o BUFFER_SIZE definido no seu código C do Pico.
BUFFER_SIZE = 60000
# ==============================================================================


# ==============================================================================
# SerialAcquisition — Thread de leitura da serial
# Protocolo binário do Pico (12 bits compactados, DMA, USB CDC nativo).
# O handshake segue os printfs de send_params() no firmware C.
#
# Formato do frame enviado pelo firmware:
#   MARKER (8) | type u8 | flags u8 | pre u16 | n_pairs u32 |
#   n_pairs × 3 bytes | soma u32 (verificação)
#   type : 0 = janela de trigger (tela)
#          2 = pedaço do frame cheio (FFT) — 'pre' = posição do pedaço
#   flags: bit0 = disparado pelo trigger do firmware
#          bit1 = modo 1 canal (todas as amostras são do CH1)
#          bit2 = último pedaço do frame cheio
# ==============================================================================
class SerialAcquisition(QObject):
    # Signal emite (data, ftype, flags, pre):
    #   data : numpy uint16 intercalado [CH1, CH2, CH1, CH2, ...]
    #   ftype: 0 = janela (tela), 1 = frame cheio já remontado (FFT)
    raw_buffer = Signal(object)
    errorSignal = Signal(str)

    def __init__(self, serialPort):
        super().__init__()
        self.serialPort = serialPort
        self.running = True
        self.synchronized = False  # mantido para compatibilidade com outros módulos
        import threading
        self._cmd_lock = threading.Lock()
        self._pending_cmd = None
        self.badFrames = 0         # frames descartados pela soma de verificação
        self._full_parts = None    # pedaços do frame cheio sendo remontados
        self._full_next = 0

    # ------------------------------------------------------------------
    def send_command(self, cmd):
        """Agenda um comando para o Pico (thread-safe; enviado pelo thread serial).
        Se outro comando ainda não foi enviado, é substituído pelo mais novo."""
        with self._cmd_lock:
            self._pending_cmd = cmd

    # ------------------------------------------------------------------
    def run(self):
        try:
            # --- HANDSHAKE com o Pico ---
            # Sincronizado com send_params() no firmware:
            #   printf dt\n  →  printf volt_conv\n  →  printf DCOffset\n  →  aguarda '1'
            self.serialPort.reset_input_buffer()
            self.serialPort.write(b'1')
            for _ in range(3):
                self.serialPort.readline()   # consome dt, volt_conv, DCOffset
            self.serialPort.write(b'1')      # confirma início da aquisição

            # Limpa qualquer lixo acumulado durante o handshake
            time.sleep(0.1)
            self.serialPort.reset_input_buffer()
            self.synchronized = True

            # Cada par (CH1, CH2) de 12 bits vem compactado em 3 bytes
            MARKER = bytes([0xCD, 0xAB, 0xBA, 0xDC, 0xCD, 0xAB, 0xBA, 0xDC])
            HEADER_LEN = 16
            MAX_PAIRS = 2 * BUFFER_SIZE
            rx_buf = bytearray()

            # --- Leitura BLOQUEANTE e grande ---
            # Enquanto o thread está dentro do read(), o GIL fica livre e o
            # Windows entrega os dados direto no buffer do Python. O buffer
            # interno do driver serial é pequeno (~12-16 KB na prática): com
            # "in_waiting + sleep(1ms)", qualquer atraso >~15 ms do thread
            # (GIL ocupado pela interface) fazia o driver descartar bytes.
            self.serialPort.timeout = 0.02   # devolve o controle a cada 20 ms p/ enviar comandos
            READ_SIZE = 65536

            while self.running:
                # Envia comando pendente (configuração do trigger)
                with self._cmd_lock:
                    cmd, self._pending_cmd = self._pending_cmd, None
                if cmd is not None:
                    self.serialPort.write(cmd.encode("ascii"))

                chunk_in = self.serialPort.read(READ_SIZE)
                if chunk_in:
                    rx_buf += chunk_in

                while True:
                    # --- Sincronização pelo marcador ---
                    idx = rx_buf.find(MARKER)
                    if idx == -1:
                        del rx_buf[:max(0, len(rx_buf) - (len(MARKER) - 1))]
                        break
                    if idx > 0:
                        del rx_buf[:idx]
                    if len(rx_buf) < HEADER_LEN:
                        break

                    # --- Cabeçalho ---
                    ftype, flags, pre, n = struct.unpack_from("<BBHI", rx_buf, 8)
                    if ftype not in (0, 2) or n == 0 or n > MAX_PAIRS:
                        del rx_buf[:1]   # cabeçalho inválido → ressincroniza
                        continue
                    data_end = HEADER_LEN + 3 * n
                    total = data_end + 4   # + trailer (soma u32)
                    if len(rx_buf) < total:
                        break

                    # --- Soma de verificação ---
                    chunk = bytes(rx_buf[HEADER_LEN:data_end])
                    (checksum,) = struct.unpack_from("<I", rx_buf, data_end)
                    raw8 = np.frombuffer(chunk, dtype=np.uint8)
                    if int(raw8.sum(dtype=np.uint64)) & 0xFFFFFFFF != checksum:
                        # Frame corrompido (bytes perdidos no caminho): descarta
                        # só o marcador e ressincroniza no próximo
                        self.badFrames += 1
                        del rx_buf[:1]
                        continue
                    del rx_buf[:total]

                    # --- Desempacota 12 bits: [b0 b1 b2] → s0 (CH1), s1 (CH2) ---
                    #   s0 = b0 | (b1 & 0x0F) << 8
                    #   s1 = (b1 >> 4) | b2 << 4
                    b = np.frombuffer(chunk, dtype=np.uint8).reshape(-1, 3).astype(np.uint16)
                    data = np.empty(b.shape[0] * 2, dtype=np.uint16)
                    data[0::2] = b[:, 0] | ((b[:, 1] & 0x0F) << 8)
                    data[1::2] = (b[:, 1] >> 4) | (b[:, 2] << 4)

                    # --- Pedaço do frame cheio (FFT) ---
                    # Remonta pela posição ('pre'); se faltar um pedaço
                    # (descartado pela soma de verificação), abandona o frame.
                    if ftype == 2:
                        if pre == 0:
                            self._full_parts, self._full_next = [], 0
                        if self._full_parts is not None and pre == self._full_next:
                            self._full_parts.append(data)
                            self._full_next += n
                            if flags & 0x04:   # último pedaço
                                full = np.concatenate(self._full_parts)
                                self._full_parts = None
                                self.raw_buffer.emit((full, 1, flags, 0))
                        else:
                            self._full_parts = None
                        continue

                    self.raw_buffer.emit((data, ftype, flags, pre))
                # (sem sleep: o read() bloqueante já cede a CPU e o GIL)

        except Exception as e:
            self.errorSignal.emit(str(e))

    # ------------------------------------------------------------------
    def stop(self):
        self.running = False
        self.synchronized = False
        try:
            if self.serialPort and self.serialPort.is_open:
                self.serialPort.close()
        except Exception:
            pass


# ==============================================================================
# DataHandler — Processamento de sinais
# Converte os frames recebidos do Pico em tensão e os separa em:
#   - janela de trigger (tela)       → CH1Frame / CH2Frame / MathFrame
#   - frame cheio de ~240 ms (FFT)   → CH1Full  / CH2Full  / MathFull
# O trigger em si é feito no firmware.
# ==============================================================================
class DataHandler(QObject):
    def __init__(self, offsCH1, offsCH2, attnCH1, attnCH2, phaseCorr, samplingRate):
        super().__init__()

        self.offsCH1 = offsCH1
        self.attnCH1 = attnCH1
        self.offsCH2 = offsCH2
        self.attnCH2 = attnCH2
        self.phaseCorr = phaseCorr          # mantido por compatibilidade
        self.samplingRate = samplingRate

        self.triggerPossible = True
        self.triggerType = "Rising Edge"
        self.triggerChannel = "CH1"
        self.triggerValue = 0.0
        self.setDataEnable = True
        self.triggerPauseTimer = QtCore.QTimer()
        self.triggerPauseTimer.setSingleShot(True)

        # Estado de armamento do trigger (mantido por compatibilidade)
        self.triggerArmed = True

        self.mathMode = "CH1 + CH2"

        N = int(0.5 * self.samplingRate)
        # Buffers lidos por módulos externos (medidas, fase)
        self.CH1Buffer = np.zeros(N, dtype=np.float32)
        self.CH2Buffer = np.zeros(N, dtype=np.float32)
        self.MathBuffer = np.zeros(N, dtype=np.float32)

        # Janela de trigger enviada pelo firmware (tamanho = janela visível)
        self.CH1Frame = np.zeros(N, dtype=np.float32)
        self.CH2Frame = np.zeros(N, dtype=np.float32)
        self.MathFrame = np.zeros(N, dtype=np.float32)
        self._frame_ready = False    # True quando há uma janela nova
        self._frame_trig = False     # janela disparada pelo trigger do firmware
        self._frame_pre = 0          # índice do ponto de trigger na janela
        self._frame_single = False   # janela veio no modo 1 canal (500 kSps)
        self._full_single = False

        # Frame cheio (BUFFER_SIZE pares, ~240 ms) enviado a cada ~1 s — usado pela FFT
        self.CH1Full = np.zeros(BUFFER_SIZE, dtype=np.float32)
        self.CH2Full = np.zeros(BUFFER_SIZE, dtype=np.float32)
        self.MathFull = np.zeros(BUFFER_SIZE, dtype=np.float32)
        self._full_ready = False

        self._buf_size = N
        self._buf_idx = 0
        self.attnFactor_CH1 = "x1"
        self.attnFactor_CH2 = "x1"

        # Variáveis mantidas por compatibilidade com módulos externos
        self.CH1_raw = np.zeros(1, dtype=np.float32)
        self.CH2_raw = np.zeros(1, dtype=np.float32)

        # Referência à porta serial — preenchida por startSerial()
        self.serialPort_ref = None

        # Última amostra de cada canal (mantidas por compatibilidade)
        self._last_ch1 = np.float32(0.0)
        self._last_ch2 = np.float32(0.0)

        # Lock entre threads: processChannelsData roda no thread serial e
        # UpdateGraph no thread da UI
        import threading
        self._buffer_lock = threading.Lock()

    # ------------------------------------------------------------------
    def processChannelsData(self, frame):
        """
        Recebe (data, ftype, flags, pre) do SerialAcquisition.
          data : uint16 intercalado [CH1, CH2, ...] (12 bits)
          ftype: 0 = janela de trigger (tela), 1 = frame cheio (FFT)

        O trigger (com histerese) e o alinhamento agora são feitos no
        firmware, e os frames chegam íntegros (marcador + cabeçalho com
        tamanho). Por isso saíram a correção de costura e a sanidade de
        glitch — esta última descartava sinais legítimos, como ondas
        quadradas de excursão completa.
        """
        if isinstance(frame, tuple):
            arr, ftype, flags, pre = frame
        else:  # compatibilidade: array puro = janela sem trigger
            arr, ftype, flags, pre = frame, 0, 0, 0

        if len(arr) < 4:
            return

        # Separação dos canais
        single = bool(flags & 0x02)
        if single:
            # Modo 1 canal: todas as amostras são do CH1 (2 µs entre elas)
            ch1_raw = arr.astype(np.float32)
            ch2_raw = np.full(len(arr), 4095.0 * self.offsCH2 / 3.3, dtype=np.float32)  # CH2 = 0 V
        else:
            ch1_raw = arr[0::2].astype(np.float32)
            ch2_raw = arr[1::2].astype(np.float32)

        # Guarda referência dos raw para compatibilidade com módulos externos
        self.CH1_raw = ch1_raw
        self.CH2_raw = ch2_raw

        # Conversão para tensão — 12 bits, referência 3.3 V
        y_ch1 = ((ch1_raw * 3.3 / 4095.0) - self.offsCH1) * self.attnCH1
        y_ch2 = ((ch2_raw * 3.3 / 4095.0) - self.offsCH2) * self.attnCH2

        # Atenuação por jumper externo
        if self.attnFactor_CH1 == "x5": y_ch1 *= 5
        if self.attnFactor_CH2 == "x5": y_ch2 *= 5

        y_math = self._calcMath(y_ch1, y_ch2)

        # O trigger é decidido no firmware: toda janela recebida é exibida
        self.setDataEnable = True

        # Os arrays são SUBSTITUÍDOS (nunca alterados in-place), então quem
        # pegou a referência anterior sob o lock continua com dados íntegros.
        with self._buffer_lock:
            if ftype == 1:   # frame cheio → FFT
                self.CH1Full, self.CH2Full, self.MathFull = y_ch1, y_ch2, y_math
                self._full_single = single
                self._full_ready = True
            else:            # janela → tela
                self.CH1Frame, self.CH2Frame, self.MathFrame = y_ch1, y_ch2, y_math
                self._frame_trig = bool(flags & 1)
                self._frame_pre = int(pre)
                self._frame_single = single
                self._frame_ready = True

    # ------------------------------------------------------------------
    def getLinearBuffer(self):
        """Retorna cópias dos buffers de leitura — sempre contínuos,
        nunca em estado de wrap-around. Deve ser chamado sob _buffer_lock."""
        return (self.CH1BufferRead.copy(),
                self.CH2BufferRead.copy(),
                self.MathBufferRead.copy())

    # ------------------------------------------------------------------
    def _calcMath(self, ch1, ch2):
        with np.errstate(divide='ignore', invalid='ignore'):
            if self.mathMode == "CH1 + CH2": return ch1 + ch2
            if self.mathMode == "CH1 - CH2": return ch1 - ch2
            if self.mathMode == "CH2 - CH1": return ch2 - ch1
            if self.mathMode == "CH1 * CH2": return ch1 * ch2
            if self.mathMode == "CH1 / CH2":
                return np.divide(ch1, ch2, out=np.zeros_like(ch1), where=ch2 != 0)
            if self.mathMode == "CH2 / CH1":
                return np.divide(ch2, ch1, out=np.zeros_like(ch2), where=ch1 != 0)
        return ch1 + ch2


# ==============================================================================
# Main — Widget principal do osciloscópio (PlotWidget)
# Mantém compatibilidade com todos os módulos externos do projeto (MyO_*).
# Nenhum nome de atributo foi removido ou renomeado.
# ==============================================================================
class Main(PlotWidget):
    TRIG_HYST_V = 0.05   # histerese mínima do trigger (V, na escala exibida)

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.refreshRate = 16  # ms — taxa de atualização do gráfico
        self.serialThread = None
        self.serialPort = None
        self.serialWorker = None
        self._lastTrigCfg = None    # última config de trigger enviada ao Pico
        self._autoTrigStats = {}    # canal → (meio da excursão, pico-a-pico, ruído) em V
        self.PARAMETERS_FILE = "parameters.txt"

        savedParameters = self.loadCalibrationParams()
        self.samplingRate = savedParameters["samplingRate"]
        self.offsCH1 = savedParameters["offs_CH1"]
        self.offsCH2 = savedParameters["offs_CH2"]
        self.attnCH1 = savedParameters["attn_CH1"]
        self.attnCH2 = savedParameters["attn_CH2"]
        self.phaseCorrTime = savedParameters["phase_corr"]
        self.samplingPeriod = 1 / self.samplingRate
        # Taxa base por canal no modo 2 canais; no modo 1 canal (CH2 desligado)
        # o Pico amostra só o CH1 ao dobro dessa taxa
        self._baseRate = self.samplingRate

        # Correção de fase e filtro passa-baixa
        self.phaseCorrActive = True
        self.LPF_isOn = True
        self.cutoffFreq = int(self.samplingRate / 2)  # padrão: sem corte efetivo

        # ------------------------------------------------------------------
        # Configuração do PlotWidget
        # ------------------------------------------------------------------
        self.setGeometry(20, 285, 1120, 360)
        self.xBotLim = 0
        self.xTopLim = 0.01
        self.yBotLim = -4.6
        self.yTopLim = 4.6

        self.getPlotItem().getViewBox().setMouseEnabled(x=False, y=False)
        self.getPlotItem().hideButtons()
        self.setRange(xRange=(self.xBotLim, self.xTopLim), yRange=(self.yBotLim, self.yTopLim))
        self.setBackground((5, 5, 18))

        grid_pen = mkPen(color=(140, 140, 140), width=1)
        self.getPlotItem().getAxis('left').setPen(grid_pen)
        self.getPlotItem().getAxis('bottom').setPen(grid_pen)
        self.showGrid(x=True, y=True, alpha=0.5)
        self.getPlotItem().getAxis('bottom').setTickSpacing(0.001, 0.002)
        self.getPlotItem().getAxis('left').setTickSpacing(1, 1)
        self.getAxis('left').setStyle(showValues=False)
        self.getAxis('bottom').setStyle(showValues=False)

        # ------------------------------------------------------------------
        # Eixo de tempo e inicialização dos arrays de sinal
        # ------------------------------------------------------------------
        self.numPoints = int(self.samplingRate * 0.5)
        self.x = np.linspace(
            0, (self.numPoints - 1) / self.samplingRate,
            self.numPoints, dtype=np.float32
        )

        self.y_CH1 = np.zeros(int(0.5 * self.samplingRate), dtype=np.float32)
        self.y_CH2 = np.zeros(int(0.5 * self.samplingRate), dtype=np.float32)
        self.y_Math = np.zeros(int(0.5 * self.samplingRate), dtype=np.float32)

        # ------------------------------------------------------------------
        # Curvas do gráfico
        # ------------------------------------------------------------------
        self.graphStyleCH1 = mkPen(color="blue", width=2)
        self.graphStyleCH2 = mkPen(color="red", width=2)
        self.graphStyleMath = mkPen(color="cyan", width=1.5)

        self.graphicPlotting_CH1 = self.plot(self.x, self.y_CH1, pen=self.graphStyleCH1)
        self.graphicPlotting_CH2 = self.plot(self.x, self.y_CH2, pen=self.graphStyleCH2)
        self.graphicPlotting_Math = self.plot(self.x, self.y_Math, pen=self.graphStyleMath)
        self.removeItem(self.graphicPlotting_Math)
        self.mathMode = "CH1 + CH2"

        # ------------------------------------------------------------------
        # Atributos de escala — positionOffset_* é o nome canônico;
        # offset_* são aliases usados por outros módulos
        # ------------------------------------------------------------------
        self.timeScale = 1
        self.vdivCH1Scale = 0.5
        self.vdivCH2Scale = 0.5
        self.vdivMathScale = 0.5

        self.positionOffset_CH1 = 0
        self.positionOffset_CH2 = 0
        self.positionOffset_Math = 0
        self.offset_CH1 = 0   # alias
        self.offset_CH2 = 0
        self.offset_Math = 0

        # ------------------------------------------------------------------
        # Trigger
        # ------------------------------------------------------------------
        self.triggerEdgeValue = 0
        self.triggerUsefulEdgeValue = 0
        self.yPrev_CH1 = 0
        self.yCaptured_CH1 = self.y_CH1
        self.yPrev_CH2 = 0
        self.yCaptured_CH2 = self.y_CH2
        self.yPrev_Math = 0
        self.yCaptured_Math = self.y_Math
        self.triggerChannel = "CH1"
        self.yMinTrig = 0
        self.yMaxTrig = 0
        self.triggerType = "Rising Edge"
        self.triggerMode = "Manual"
        self.trigPrevValue = 0
        self.triggerOn = False

        # ------------------------------------------------------------------
        # Medidas
        # ------------------------------------------------------------------
        self.freqCH1 = 1;    self.freqCH2 = 1;    self.freqMath = 1
        self.periodCH1 = 1;  self.periodCH2 = 1;  self.periodMath = 1
        self.CH1MeanValue = 1; self.CH2MeanValue = 1; self.mathMeanValue = 1
        self.CH1VppValue = 1;  self.CH2VppValue = 1;  self.mathVppValue = 1
        self.CH1VRMSValue = 1; self.CH2VRMSValue = 1; self.mathVRMSValue = 1
        self.yMaxCH1 = 0; self.yMinCH1 = 0
        self.yMaxCH2 = 0; self.yMinCH2 = 0
        self.yMaxMath = 0; self.yMinMath = 0
        self.CH1Phase = 0; self.CH2Phase = 0; self.mathPhase = 0
        self.btMeasActivated = False
        self.freezeTime = False
        self.referencePhase = "CH1"
        self.CH1Activated = True
        self.CH2Activated = True
        self.mathActivated = False

        # ------------------------------------------------------------------
        # Flags e controles gerais
        # ------------------------------------------------------------------
        self.allowUpdateGraph = True
        self.acquisitionMode = "Real"
        self.COMPortON = False
        self.max_visible_points = 1500
        self.serialErrorFlag = False

        # ------------------------------------------------------------------
        # Cópias dos buffers para freeze e medidas
        # ------------------------------------------------------------------
        self.y_CH1_copy = self.y_CH1
        self.y_CH2_copy = self.y_CH2
        self.y_Math_copy = self.y_Math

        # ------------------------------------------------------------------
        # Variáveis de plot — inicializadas para que módulos externos
        # possam acessá-las mesmo antes da serial estar conectada.
        # ------------------------------------------------------------------
        self.visibleWindow = int(10 * (self.timeScale / 1000) / self.samplingPeriod)
        self.decimation = 1
        self.x_plot = self.x[:self.visibleWindow]
        self.y_CH1_pure = self.y_CH1[:self.visibleWindow]
        self.y_CH2_pure = self.y_CH2[:self.visibleWindow]
        self.y_Math_pure = self.y_Math[:self.visibleWindow]
        self.y_CH1_plot = np.zeros(self.visibleWindow, dtype=np.float32)
        self.y_CH2_plot = np.zeros(self.visibleWindow, dtype=np.float32)
        self.y_Math_plot = np.zeros(self.visibleWindow, dtype=np.float32)

        # ------------------------------------------------------------------
        # DataHandler e Timer de atualização
        # ------------------------------------------------------------------
        self.dataHandler = DataHandler(
            self.offsCH1, self.offsCH2,
            self.attnCH1, self.attnCH2,
            self.phaseCorrTime, self.samplingRate
        )

        self.updateTimer = QtCore.QTimer()
        self.updateTimer.timeout.connect(self.UpdateGraph)

        # Janela de porta COM
        self.COMPortScr = COM_Port_Window()

    # ==========================================================================
    # loadCalibrationParams — lê parameters.txt (valores padrão se não existir)
    # ==========================================================================
    def loadCalibrationParams(self):
        params = {
            "offs_CH1": 1.500,
            "offs_CH2": 1.500,
            "attn_CH1": 1.500,
            "attn_CH2": 1.500,
            "phase_corr": 0.00000,
            "samplingRate": 250000,   # Pico: 250 kS/s por canal
            "show_welcome": True,
            "language": "English",
        }
        try:
            with open(self.PARAMETERS_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, value = map(str.strip, line.split("=", 1))
                    if key not in params:
                        continue
                    if key == "show_welcome":
                        params[key] = value.lower() == "true"
                    elif key == "samplingRate":
                        params[key] = int(float(value))
                    elif key == "language":
                        params[key] = value
                    else:
                        params[key] = float(value)
        except FileNotFoundError:
            pass
        return params

    # ==========================================================================
    # UpdateGraph — roda no thread da UI via QTimer (16 ms)
    #
    # PIPELINE:
    #   1. Janela visível e decimação; envia a config do trigger ao Pico
    #   2. Pega os frames novos (janela p/ tela, frame cheio p/ FFT)
    #   3. Alinhamento pelo trigger (já feito no firmware, exceto em Math)
    #   4. Renderização — V/div + positionOffset + decimação
    # ==========================================================================
    def UpdateGraph(self):
        if self.COMPortON:
            self.numPoints = int(self.samplingRate * 0.5)

            # ------------------------------------------------------------------
            # 1. Janela visível e decimação
            # ------------------------------------------------------------------
            self.visibleWindow = int(10 * (self.timeScale / 1000) / self.samplingPeriod)
            self.decimation = max(1, int(self.visibleWindow / self.max_visible_points))

            # Mantém o trigger do firmware sincronizado com a interface
            self._sendTriggerConfig()

            # ------------------------------------------------------------------
            # 2. Pega os frames novos (as referências são trocadas, nunca
            #    alteradas in-place, então não precisa copiar)
            # ------------------------------------------------------------------
            dh = self.dataHandler
            with dh._buffer_lock:
                full_ready = dh._full_ready
                frame_ready = dh._frame_ready
                if full_ready:
                    f1, f2, fm = dh.CH1Full, dh.CH2Full, dh.MathFull
                    full_single = dh._full_single
                    dh._full_ready = False
                if frame_ready:
                    w1, w2, wm = dh.CH1Frame, dh.CH2Frame, dh.MathFrame
                    fw_trig = dh._frame_trig
                    win_single = dh._frame_single
                    dh._frame_ready = False

            # A taxa de amostragem segue o modo da janela recebida:
            # 2 canais → taxa base (250 kSps/canal); 1 canal → 2× (500 kSps)
            if frame_ready:
                want_rate = self._baseRate * (2 if win_single else 1)
                if want_rate != self.samplingRate:
                    self._applyRate(want_rate)
            # Frame cheio de outro modo (troca recente) seria lido com a taxa
            # errada pela FFT → descarta
            if full_ready and (self._baseRate * (2 if full_single else 1)) != self.samplingRate:
                full_ready = False

            # --- Frame cheio (~1×/s, 240 ms) → y_CH1/y_CH2/y_Math, usados pela FFT ---
            if full_ready:
                self.y_CH1, self.y_CH2 = self._conditionSignals(f1, f2)
                self.y_Math = fm
                dh.CH1Buffer, dh.CH2Buffer, dh.MathBuffer = self.y_CH1, self.y_CH2, self.y_Math
                # Estatísticas p/ o trigger Automatic: meio da excursão do sinal
                # num trecho longo (240 ms), resistente a picos de ruído, e
                # ruído (pela diferença entre amostras vizinhas: o sinal quase
                # não muda em 4 µs, então o que sobra é ruído; /√2 pois a
                # diferença soma o ruído de duas amostras)
                for name, sig in (("CH1", self.y_CH1), ("CH2", self.y_CH2), ("Math", self.y_Math)):
                    if len(sig) > 10:
                        lo, hi = np.percentile(sig, (1, 99))
                        noise = float(np.std(np.diff(sig))) / np.sqrt(2.0)
                        self._autoTrigStats[name] = ((lo + hi) / 2.0, hi - lo, noise)

            if not frame_ready:
                return  # aguarda janela nova

            # --- Janela de trigger → tela (correção de fase + filtro) ---
            win_CH1, win_CH2 = self._conditionSignals(w1, w2)
            win_Math = wm

            # ------------------------------------------------------------------
            # 3. Alinhamento pelo trigger
            #    Janela disparada pelo firmware já começa no ponto de trigger.
            #    Sem disparo (trigger em Math, ou modo auto), procura aqui.
            # ------------------------------------------------------------------
            vw = self.visibleWindow
            if fw_trig:
                trig_idx = 0
            else:
                trig_idx = self._findTrigger(win_CH1, win_CH2, win_Math, vw)

            self.y_CH1_pure = win_CH1[trig_idx: trig_idx + vw]
            self.y_CH2_pure = win_CH2[trig_idx: trig_idx + vw]
            self.y_Math_pure = win_Math[trig_idx: trig_idx + vw]

            # ------------------------------------------------------------------
            # 4. Renderização
            # ------------------------------------------------------------------
            if self.dataHandler.setDataEnable:
                actual_len = len(self.y_CH1_pure)
                # (x_plot só é atualizado junto com y_*_plot, abaixo — se a tela
                #  estiver congelada, ambos mantêm os valores anteriores e o
                #  mesmo tamanho)

                if not self.freezeTime:
                    # Cópias p/ "congelar" (plotUpdate re-fatia com a janela
                    # visível): completadas com zeros até numPoints para que
                    # trocar a base de tempo congelado não quebre tamanhos.
                    self.y_CH1_copy = self._padTo(win_CH1[trig_idx:], self.numPoints)
                    self.y_CH2_copy = self._padTo(win_CH2[trig_idx:], self.numPoints)
                    self.y_Math_copy = self._padTo(win_Math[trig_idx:], self.numPoints)

                    # Sincroniza aliases
                    self.offset_CH1 = self.positionOffset_CH1
                    self.offset_CH2 = self.positionOffset_CH2
                    self.offset_Math = self.positionOffset_Math

                    dec = self.decimation

                    # Salva as versões já decimadas — módulos externos como
                    # btCH1Clicked e btCH2Clicked usam x_plot e y_*_plot
                    # diretamente, então precisam ter o mesmo tamanho.
                    self.x_plot = self.x[:actual_len:dec]
                    self.y_CH1_plot = ((self.y_CH1_pure / self.vdivCH1Scale) + self.positionOffset_CH1)[::dec]
                    self.y_CH2_plot = ((self.y_CH2_pure / self.vdivCH2Scale) + self.positionOffset_CH2)[::dec]
                    self.y_Math_plot = ((self.y_Math_pure / self.vdivMathScale) + self.positionOffset_Math)[::dec]

                    self.graphicPlotting_CH1.setData(self.x_plot, self.y_CH1_plot)
                    self.graphicPlotting_CH2.setData(self.x_plot, self.y_CH2_plot)
                    self.graphicPlotting_Math.setData(self.x_plot, self.y_Math_plot)

        else:
            # Serial desconectada — mantém variáveis para módulos de medida
            self.visibleWindow = int(10 * (self.timeScale / 1000) / self.samplingPeriod)
            self.y_CH1_pure = self.y_CH1[:self.visibleWindow]
            self.y_CH2_pure = self.y_CH2[:self.visibleWindow]
            self.y_Math_pure = self.y_Math[:self.visibleWindow]

    # ==========================================================================
    # serialInit
    # ==========================================================================
    def serialInit(self, port, firstTry):
        try:
            serial_connection = serial.Serial(
                port,
                baudrate=2000000,  # ignorado pelo USB CDC; mantido por compatibilidade
                bytesize=8, parity='N', stopbits=1, timeout=1
            )
            try:
                serial_connection.set_buffer_size(1048576)
            except AttributeError:
                pass
            self.COMPortON = True
            return serial_connection
        except serial.SerialException:
            self.stopSerial()
            return None

    # ==========================================================================
    # startSerial
    # ==========================================================================
    def startSerial(self, port, firstTry, notViaMain):
        if notViaMain:
            self.stopSerial()
        if self.serialThread and self.serialThread.isRunning():
            return

        self.serialPort = self.serialInit(port, firstTry=firstTry)
        if self.serialPort is not None and self.serialPort.is_open:
            self.serialThread = QThread()
            self.serialWorker = SerialAcquisition(self.serialPort)
            self._lastTrigCfg = None   # nova conexão → reenvia config do trigger
            self.serialWorker.moveToThread(self.serialThread)

            self.serialThread.started.connect(self.serialWorker.run)
            self.serialWorker.raw_buffer.connect(self.dataHandler.processChannelsData)
            self.serialWorker.errorSignal.connect(self.serialError)

            self.serialThread.finished.connect(self.serialWorker.deleteLater)
            self.serialThread.finished.connect(self.serialThread.deleteLater)

            # Passa referência da porta ao DataHandler
            self.dataHandler.serialPort_ref = self.serialPort

            # Prioridade máxima: a leitura não pode atrasar, senão o driver
            # serial do Windows descarta dados (frames chegam corrompidos)
            self.serialThread.start(QThread.Priority.TimeCriticalPriority)

    # ==========================================================================
    # stopSerial
    # ==========================================================================
    def stopSerial(self):
        if self.serialWorker and self.serialWorker.running:
            self.serialWorker.running = False
        if self.serialWorker:
            self.serialWorker.stop()
        if self.serialThread is not None:
            self.serialThread.quit()
            self.serialThread.wait()

        self.serialWorker = None
        self.serialThread = None
        self.serialPort = None
        self.COMPortON = False
        self.dataHandler.serialPort_ref = None

        # Recria eixo X e arrays Y com o MESMO tamanho (a taxa pode ter mudado)
        self.numPoints = int(0.5 * self.samplingRate)
        self.x = np.linspace(
            0, (self.numPoints - 1) / self.samplingRate,
            self.numPoints, dtype=np.float32
        )
        self.y_CH1 = np.zeros(self.numPoints, dtype=np.float32)
        self.y_CH2 = np.zeros(self.numPoints, dtype=np.float32)
        self.y_Math = np.zeros(self.numPoints, dtype=np.float32)
        self.graphicPlotting_CH1.setData(self.x, self.y_CH1)
        self.graphicPlotting_CH2.setData(self.x, self.y_CH2)
        self.graphicPlotting_Math.setData(self.x, self.y_Math)

    # ------------------------------------------------------------------
    def closeEvent(self, event):
        self.stopSerial()

    # ------------------------------------------------------------------
    def serialError(self, msg=None):
        # msg=None mantém compatibilidade com assinatura sem argumento do original
        self.stopSerial()
        self.COMPortON = False
        self.serialErrorFlag = True

    # ==========================================================================
    # plot — protegido contra x/y de tamanhos diferentes
    #
    # Módulos externos (ex.: btCH1Clicked) recriam as curvas com
    # plot(x_plot, y_CH1_plot). Mas plotUpdate() (MyO_Time_Volt_...) troca
    # x_plot pela versão NÃO decimada sem atualizar y_*_plot, e o pyqtgraph
    # lança exceção. Aqui x é re-decimado para casar com y (mantendo a escala
    # de tempo correta); se ainda sobrar diferença, corta o mais longo.
    # ==========================================================================
    def plot(self, *args, **kwargs):
        if len(args) >= 2:
            x, y = args[0], args[1]
            try:
                nx, ny = len(x), len(y)
            except TypeError:
                nx = ny = None
            if nx is not None and nx != ny and ny > 0:
                if nx > ny:
                    dec = max(1, int(round(nx / ny)))
                    x = x[::dec]
                n = min(len(x), ny)
                args = (x[:n], y[:n]) + tuple(args[2:])
        # PlotWidget repassa plot() ao PlotItem via __getattr__
        return self.getPlotItem().plot(*args, **kwargs)

    # ==========================================================================
    # _padTo — completa um array com zeros até n pontos
    # ==========================================================================
    @staticmethod
    def _padTo(a, n):
        out = np.zeros(n, dtype=np.float32)
        k = min(len(a), n)
        out[:k] = a[:k]
        return out

    # ==========================================================================
    # _conditionSignals — correção de fase do CH2 + filtro passa-baixa
    # ==========================================================================
    def _conditionSignals(self, ch1, ch2):
        """Correção de fase do CH2 (FFT) + passa-baixa Butterworth (n=4)."""
        if self.phaseCorrActive and self.phaseCorrTime != 0 and len(ch2) > 1:
            fft_data = np.fft.rfft(ch2)
            length = len(ch2)
            freqs = np.fft.rfftfreq(length, d=1 / self.samplingRate)
            correction = np.exp(1j * 2 * np.pi * freqs * (self.phaseCorrTime * 1e-3))
            ch2 = np.fft.irfft(fft_data * correction, n=length)

        # Pulado quando cutoffFreq >= Nyquist (sem corte efetivo)
        if self.LPF_isOn and self.cutoffFreq < self.samplingRate / 2:
            fc, n = self.cutoffFreq, 4
            out = []
            for sig in (ch1, ch2):
                length = len(sig)
                freqs = np.fft.rfftfreq(length, d=1 / self.samplingRate)
                H = 1.0 / (1.0 + (freqs / fc) ** (2 * n))
                out.append(np.fft.irfft(np.fft.rfft(sig) * H, n=length))
            ch1, ch2 = out
        return ch1, ch2

    # ==========================================================================
    # _applyRate — troca a taxa de amostragem (modo 1 ↔ 2 canais)
    # ==========================================================================
    def _applyRate(self, rate):
        """Troca a taxa de amostragem exibida (modo 1 ↔ 2 canais) e refaz o
        eixo de tempo. Mantém o passa-baixa 'desligado' se ele estava no
        Nyquist antigo."""
        old = self.samplingRate
        self.samplingRate = rate
        self.samplingPeriod = 1.0 / rate
        self.dataHandler.samplingRate = rate
        if self.cutoffFreq >= old / 2:
            self.cutoffFreq = int(rate / 2)
        self.numPoints = int(rate * 0.5)
        self.x = np.linspace(0, (self.numPoints - 1) / rate, self.numPoints, dtype=np.float32)
        self.visibleWindow = int(10 * (self.timeScale / 1000) / self.samplingPeriod)
        self.decimation = max(1, int(self.visibleWindow / self.max_visible_points))
        self._autoTrigStats = {}   # estatísticas eram da taxa antiga

    # ==========================================================================
    # _wantSingleChannel — decide se o Pico deve usar o modo 1 canal
    # ==========================================================================
    def _wantSingleChannel(self):
        """Modo 1 canal (500 kSps) quando o CH2 e o Math estão desligados
        na tela e o trigger não usa o CH2. Detectado pelas curvas presentes
        no gráfico (o flag CH2Activated não é confiável)."""
        try:
            items = self.getPlotItem().listDataItems()
        except Exception:
            return False
        ch2_on = self.graphicPlotting_CH2 in items
        math_on = self.graphicPlotting_Math in items
        return (not ch2_on) and (not math_on) and self.triggerChannel != "CH2"

    # ==========================================================================
    # _triggerLevel — nível do trigger (Manual ou Automatic)
    # ==========================================================================
    def _triggerLevel(self):
        """Retorna (nível em V, trigger possível).

        Manual: valores definidos pela interface (knob do trigger).
        Automatic: meio da excursão do sinal medido no frame cheio de 240 ms.
          Antes o nível era a média da JANELA VISÍVEL — que começa no próprio
          ponto de disparo. Em bases de tempo curtas isso realimentava: a
          média puxava o nível para cima/baixo a cada quadro até perder o
          disparo, e a onda aparecia alternando de 'polaridade'."""
        dh = self.dataHandler
        if self.triggerMode == "Automatic":
            st = self._autoTrigStats.get(self.triggerChannel)
            if st is not None:
                mid, pp, _ = st
                return mid, pp > 4 * self._triggerHysteresis()   # sinal grande o bastante
        return dh.triggerValue, dh.triggerPossible

    # ==========================================================================
    # _triggerHysteresis — histerese adaptada ao ruído do sinal
    # ==========================================================================
    def _triggerHysteresis(self):
        """Histerese do trigger em V (escala exibida), adaptada ao ruído.

        Se o ruído for maior que a histerese, ele sozinho arma e dispara o
        trigger perto do cruzamento — em QUALQUER borda — e a onda aparece
        ora subindo, ora descendo. Por isso: 4× o ruído rms medido no frame
        cheio, limitado a 25% do pico-a-pico (para não perder sinais pequenos)
        e no mínimo TRIG_HYST_V."""
        st = self._autoTrigStats.get(self.triggerChannel)
        if st is None:
            return self.TRIG_HYST_V
        _, pp, noise = st
        h = max(self.TRIG_HYST_V, 4.0 * noise)
        if pp > 0:
            h = min(h, 0.25 * pp)
        return max(h, 0.0)

    # ==========================================================================
    # _findTrigger — busca o trigger no Python (quando o firmware não disparou)
    # ==========================================================================
    def _findTrigger(self, c1, c2, cm, vw):
        """Busca o 1º cruzamento do nível que ainda deixe vw amostras visíveis.
        Usado quando o firmware não disparou (trigger em Math / modo auto)."""
        val = self._triggerLevel()[0]
        src = c1 if self.triggerChannel == "CH1" else \
              (c2 if self.triggerChannel == "CH2" else cm)
        search_end = max(2, len(src) - vw + 1)
        s = src[:search_end]
        if self.triggerType == "Rising Edge":
            idx = np.where((s[:-1] <= val) & (s[1:] > val))[0]
        else:
            idx = np.where((s[:-1] >= val) & (s[1:] < val))[0]
        return int(idx[0]) if len(idx) > 0 else 0

    # ==========================================================================
    # _sendTriggerConfig — envia a configuração do trigger ao Pico
    # ==========================================================================
    def _sendTriggerConfig(self):
        """Envia ao Pico a configuração do trigger quando ela muda.
        Formato: 'C <en> <ch> <falling> <level> <hyst> <pre> <window> <avg> <single>\\n'
        window/pre/avg em PARES do firmware: 1 par = 4 µs nos dois modos
        (2 canais: CH1+CH2; 1 canal: 2 amostras seguidas do CH1)."""
        worker = self.serialWorker
        if worker is None:
            return
        dh = self.dataHandler
        ch = self.triggerChannel
        single = 1 if self._wantSingleChannel() else 0
        # Janela pela DURAÇÃO (10 divisões), independente do modo atual
        vw = max(16, int(round(10 * (self.timeScale / 1000) / 4e-6)))

        trig_level, trig_possible = self._triggerLevel()
        fw_capable = ch in ("CH1", "CH2")   # firmware não calcula o canal Math
        enabled = 1 if (trig_possible and fw_capable) else 0
        # Sem trigger no firmware em Math: pede 2× a janela p/ buscar no Python
        window = min(vw if fw_capable else 2 * vw, 100000)

        if ch == "CH2":
            offs, gain = dh.offsCH2, dh.attnCH2 * (5 if dh.attnFactor_CH2 == "x5" else 1)
        else:
            offs, gain = dh.offsCH1, dh.attnCH1 * (5 if dh.attnFactor_CH1 == "x5" else 1)
        if gain == 0:
            gain = 1.0

        # Inverso de: V = (raw * 3.3/4095 - offs) * gain
        to_counts = 4095.0 / 3.3
        level = int(round((trig_level / gain + offs) * to_counts))
        level = max(0, min(4095, level))
        hyst = max(4, int(round(self._triggerHysteresis() / gain * to_counts)))
        falling = 0 if self.triggerType == "Rising Edge" else 1

        # Filtro de ruído do trigger: média móvel de ~1/400 da janela visível
        # (1 a 16 amostras = até 64 µs) — curto o bastante para não deformar
        # sinais que cabem na tela, longo o bastante para ignorar picos.
        avg = max(1, min(16, vw // 400))

        cfg = (enabled, 1 if ch == "CH2" else 0, falling, level, hyst, 0, window, avg, single)
        last = self._lastTrigCfg
        if last is not None and cfg[:3] == last[:3] and cfg[5:] == last[5:]:
            # Só o nível/histerese mudou: ignora variações menores que meia
            # histerese (ex.: trigger automático seguindo a média do sinal)
            if abs(cfg[3] - last[3]) < max(2, hyst // 2) and cfg[4] == last[4]:
                return
        if cfg != last:
            self._lastTrigCfg = cfg
            worker.send_command("C %d %d %d %d %d %d %d %d %d\n" % cfg)


# ==============================================================================
# COM_Port_Window — Janela de aviso/configuração da porta COM
# ==============================================================================
class COM_Port_Window(QDialog):
    def __init__(self):
        super(COM_Port_Window, self).__init__()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setFixedSize(600, 200)
        self.setWindowTitle("Please set COM Port")
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        layout = QVBoxLayout(self)
        self.mainLabel = QLabel("Serial communication setup.", self)
        self.mainLabel.setStyleSheet("color: white;")
        layout.addWidget(self.mainLabel)

        self.OKButton = Button(
            self, 240, 160, 410, 30, "",
            "images/Bt_OK.png", "images/Bt_OK.png", False
        )
        self.OKButton.clicked.connect(self.close)

    def closeWindow(self):
        """Alias para compatibilidade com MyOscPiWindow.closeEvent."""
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    window = Main()
    window.show()
    app.exec()
