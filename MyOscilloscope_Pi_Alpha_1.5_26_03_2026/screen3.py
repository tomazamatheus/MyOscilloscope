from PySide6.QtWidgets import QDialog, QApplication, QLabel, QComboBox, QLineEdit, QPushButton, QSpinBox, QDoubleSpinBox, QProgressBar
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt, QThread, Signal, QObject, QTimer
from button import Button
from PySide6.QtGui import QPixmap
import sys, time
import numpy as np
import sounddevice as sd
import os
os.environ["PYQTGRAPH_QT_LIB"] = "PySide6" #necessário para pyqtgraph com PySide6
from pyqtgraph import QtCore
import sounddevice as sd
import threading
from knob import Knob


class BlackScreen(QDialog):
    def __init__(self):
        super(BlackScreen, self).__init__()
        self.setGeometry(1135, 70, 750, 165)
        self.setStyleSheet("background-color: rgb(40, 40, 40)")

class WFM_Thread:
    """NOTA: Testes permitiram concluir que a tensão em função da amplitude em a.u. satura em 66%"""
    def __init__(self, fs=44100):
        self.fs = fs
        self.freq = 500.0
        self.amplitude = 1
        self.phase = 0
        self.running = False
        self.lock = threading.Lock()
        self.waveType = "Sine"

    def audio_callback(self, outdata, frames, time_info, status):
        if not self.running:
            outdata.fill(0)
            return
        with self.lock:
            f = self.freq
            a = self.amplitude
        t = (np.arange(frames) + self.phase) / self.fs

        if self.waveType == "Sine": outdata[:] = (a * np.sin(2 * np.pi * f * t)).reshape(-1, 1)
        elif self.waveType == "Square": outdata[:] = (a * np.sign(np.sin(2 * np.pi * f * t))).reshape(-1, 1)
        elif self.waveType == "Triangle": outdata[:] = (2 * a * np.abs(2 * (t * f - np.floor(t * f + 0.5))) - a).reshape(-1, 1)
        elif self.waveType == "Sawtooth": outdata[:] = ( 2 * a * (t * f - np.floor(t * f)) - a).reshape(-1, 1)
        self.phase = (self.phase + frames) % self.fs

    def start(self):
        if not self.running:
            self.running = True
            self.stream = sd.OutputStream(
                channels=1,
                samplerate=self.fs,
                callback=self.audio_callback,
            )
            self.stream.start()

    def stop(self):
        if self.running:
            self.running = False
            self.stream.stop()
            self.stream.close()

    def set_freq(self, f):
        with self.lock:
            self.freq = f

    def set_amp(self, a):
        self.amplitude = a

        # with self.lock:
        #     self.amplitude = a

class Waveform_Generator(QDialog):
    def __init__(self):
        super(Waveform_Generator, self).__init__()
        self.setGeometry(1135, 70, 750, 165)
        self.setStyleSheet("background-color: rgb(210, 210, 210)")

        self.squareLabel = QLabel("", self)
        self.squareLabel.setGeometry(20, 85, 70, 70)
        self.squarePixmap = QPixmap("images/WFM_Square.png")
        self.squareLabel.setPixmap(
            self.squarePixmap.scaled(
                self.squareLabel.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )
        self.signalLabel = QLabel("", self)
        self.signalLabel.setGeometry(25, 90, 60, 60)
        self.sineWavePixmap = QPixmap("images/sineWave.png")
        self.squareWavePixmap = QPixmap("images/squareWave.png")
        self.triangleWavePixmap = QPixmap("images/triangleWave.png")
        self.sawtoothWavePixmap = QPixmap("images/sawtoothWave.png")
        self.generator = WFM_Thread()

        self.btOnOff = QPushButton("ON/OFF", self)
        self.btOnOff_isOn = False
        self.btOnOff.setGeometry(650, 70, 90, 65)
        self.btOnOff.setAutoDefault(False)
        self.btOnOff.setDefault(False)
        self.btOnOffImageLabel = QLabel("", self)
        self.btOnOffImageLabel.setGeometry(650, 70, 90, 65)
        self.btOFFPixmap = QPixmap("images_svg/Bt_WFM_OFF.svg")
        self.btONPixmap = QPixmap("images_svg/Bt_WFM_ON.svg")
        self.btOnOffImageLabel.setPixmap(self.btOFFPixmap.scaled(self.btOnOffImageLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
        self.btOnOffImageLabel.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)

        self.btOnOffLabel = QLabel("ON/OFF", self)
        self.btOnOffLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.btOnOffLabel.setGeometry(608, 140, 151, 22)
        self.btOnOffLabel.setStyleSheet(""" color: rgb(30, 30, 30) """)
        self.btOnOffLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.btOnOffLabel.setStyleSheet("color: rgb(50, 50, 50)")
        
        self.serialBlockingWFM = False

        self.signalTypeLabel = QLabel("Signal type:", self)
        self.signalTypeLabel.setGeometry(130, 85, 151, 22)
        self.signalTypeLabel.setStyleSheet(""" color: rgb(30, 30, 30) """)
        self.signalTypeLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.signalTypeCB = QComboBox(self)
        self.signalTypeCB.setGeometry(100, 115, 151, 30)
        self.signalTypeCB.setStyleSheet("""background-color: rgb(62, 200, 52); 
                                                    color: rgb(255, 255, 255)""")
        self.signalTypeCB.setFont(QFont("Microsoft Sans Serif", 11))
        self.signalTypeCB.currentTextChanged.connect(self.updateSignalType)


        self.amplitLabel = QLabel("Amplitude (%):", self)
        self.amplitLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.amplitLabel.setGeometry(435, 80, 151, 22)
        self.amplitLabel.setStyleSheet(""" color: rgb(30, 30, 30) """)
        self.amplitLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.amplitLE = QLineEdit(self)
        self.amplitLE.setGeometry(510, 110, 60, 30)
        self.amplitLE.setStyleSheet("background-color: rgb(62, 200, 52); color: rgb(240, 240, 240) ")
        self.amplitLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.amplitLE.setText("100")
        self.amplitLE.setFont(QFont("Microsoft Sans Serif", 12))
        

        self.amplitKnob = Knob(self, 420, 90, 70, 70,
                                "images/Knob2_Green.png", -5, 5, "Amplitude", 0, 100, 1)
        self.amplitKnob.raise_()
        self.amplitKnob.usefulValue = 100
        self.amplitKnob.buttonIsOn = True #trava normalmente usada nos outros knobs
        self.amplitKnob.valueChanged.connect(self.changeAmplitudeKnob)

        self.btQuestionMark = QPushButton("?", self)
        self.btQuestionMark_isOn = False
        self.btQuestionMark.setGeometry(595, 75, 30, 30)
        self.btQuestionMark.setAutoDefault(False)
        self.btQuestionMark.setDefault(False)
        self.btQuestionMark.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: rgb(0, 120, 0);   
                font-family: "Microsoft Sans Serif";
                font-size: 12pt;
                border-radius: 15px; 
            }
            """)

        self.freqLabel = QLabel("Frequency (Hz):", self)
        self.freqLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freqLabel.setGeometry(255, 85, 151, 22)
        self.freqLabel.setStyleSheet(""" color: rgb(30, 30, 30) """)
        self.freqLabel.setFont(QFont("Microsoft Sans Serif", 10))

        self.freq_SpinBox = QSpinBox(self)
        self.freq_SpinBox.setRange(20, 20000)  # mínimo e máximo
        self.freq_SpinBox.setSingleStep(100)  # incremento/decremento
        self.freq_SpinBox.setValue(500)
        self.freq_SpinBox.setGeometry(270, 115, 120, 30)
        self.freq_SpinBox.setStyleSheet("background-color: rgb(62, 200, 52); color: rgb(240, 240, 240) ")
        self.freq_SpinBox.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freq_SpinBox.setFont(QFont("Microsoft Sans Serif", 12))
        self.freq_SpinBox.setReadOnly(False)
    
        self.user_is_typing = False

        self.signalTypeCBItems = ["Sine Wave", "Square Wave", "Triangle Wave", "Sawtooth Wave"]
        self.signalTypeCB.addItems(self.signalTypeCBItems)

        self.backgroundSvg = QSvgWidget("images_svg/screen3_wfm_generator.svg", self)
        self.backgroundSvg.setGeometry(0, 0, 810, 119)
        self.backgroundSvg.lower()

        
        self.btOnOff.clicked.connect(self.WFMBtOnOff)
        self.freq_SpinBox.lineEdit().returnPressed.connect(self._onSpinBoxEditingFinished)
        self.freq_SpinBox.lineEdit().textEdited.connect(self._onSpinBoxTyping)
        self.freq_SpinBox.valueChanged.connect(self._onSpinBoxValueChanged)
        self.user_is_typing = False
        self.amplitLE.returnPressed.connect(self.changeAmplitude)


    def updateSignalType(self):
        if self.signalTypeCB.currentText() == "Sine Wave":
            self.signalLabel.setPixmap(self.sineWavePixmap.scaled(self.signalLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
                                                                
            self.generator.waveType = "Sine"

        elif self.signalTypeCB.currentText() == "Square Wave":
            self.signalLabel.setPixmap(self.squareWavePixmap.scaled(self.signalLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
            self.generator.waveType = "Square"

        elif self.signalTypeCB.currentText() == "Triangle Wave":
            self.signalLabel.setPixmap(self.triangleWavePixmap.scaled(self.signalLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
            self.generator.waveType = "Triangle"

        elif self.signalTypeCB.currentText() == "Sawtooth Wave":
            self.signalLabel.setPixmap(self.sawtoothWavePixmap.scaled(self.signalLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
            self.generator.waveType = "Sawtooth"

        if self.generator.running:
            self.generator.stop()
            self.generator.start()
  


    def WFMBtOnOff(self): #ajuste da imagem do botão
        if self.btOnOff_isOn == False and not self.serialBlockingWFM:
            self.btOnOff_isOn = True
            self.btOnOffImageLabel.setPixmap(self.btONPixmap.scaled(self.btOnOffImageLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
            if not self.generator.running: self.generator.start()

            #Para efeito de interação entre o on/off do wfm e a função de correção de pontos:
            self.changeFrequency_Mouse()

        else:
            self.btOnOff_isOn = False
            self.btOnOffImageLabel.setPixmap(self.btOFFPixmap.scaled(self.btOnOffImageLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
            
            if self.generator.running: self.generator.stop()

    
    

    #Separação a seguir entre mouse e teclado, para que edições temporárias do valor não sejam levadas em consideração:
    
    def _onSpinBoxTyping(self):
        # Qualquer digitação via teclado ativa essa flag
        self.user_is_typing = True

    def _onSpinBoxEditingFinished(self):
        if self.user_is_typing:
            self.user_is_typing = False
            self.changeFrequency_Keyboard()

    def _onSpinBoxValueChanged(self):
        if not self.user_is_typing:
            self.changeFrequency_Mouse()

    def changeFrequency_Mouse(self):
        self.generator.set_freq(self.freq_SpinBox.value())
        #self.frequencyRecentlyChanged = True

    def changeFrequency_Keyboard(self):
        self.generator.set_freq(self.freq_SpinBox.value())
        #self.frequencyRecentlyChanged = True
   
    def changeAmplitude(self):
        prevAmp = float(self.amplitLE.text())
        try:
            self.amplitude = float(self.amplitLE.text())/100
            if self.amplitude < 0: self.amplitude = 0
            elif self.amplitude > 1: self.amplitude = 1
            self.amplitLE.setText(f"{(self.amplitude * 100):.0f}")
            
        except ValueError:
            #A amplitude que de fato vai para a thread de geração de som passa por um fator que impede a saturação do som para 
            # um valor < que 100%
            self.amplitude = 0.435 * prevAmp
            self.amplitLE.setText(f"{(self.amplitude * 100):.0f}")

        amp = 0.435 * self.amplitude
        self.generator.set_amp(amp)

    def changeAmplitudeKnob(self):
        self.amplitude = self.amplitKnob.usefulValue/100
        self.amplitLE.setText(f"{(self.amplitKnob.usefulValue):.0f}")
        #A amplitude que de fato vai para a thread de geração de som passa por um fator que impede a saturação do som para 
        # um valor < que 100%
        amp = 0.435 * self.amplitude
        self.generator.set_amp(amp)


    def closeEvent(self, event):
        self.generator.stop()
        event.accept()
        
class Calibration(QDialog):
    def __init__(self):
        super(Calibration, self).__init__()
        self.setGeometry(1135, 70, 750, 165)
        
        self.setStyleSheet("background-color: rgb(210, 210, 210)")
        self.mainLabel = QLabel("Calibration options:", self)
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 12))
        self.mainLabel.setGeometry(250, 70, 250, 150)
    

        self.btCalibManual = Button(self, 60, 90, 200, 40, "ClbManual",
                             "images_svg/Bt_CalibManual.svg", "images_svg/Bt_CalibManual.svg", False)
        
        self.btCalibWizard = Button(self, 490, 90, 200, 40, "CalibWiz",
                             "images_svg/Bt_CalibWizard.svg", "images_svg/Bt_CalibWizard.svg", False)

        self.backgroundSvg = QSvgWidget("images_svg/screen3_calibration.svg", self)
        self.backgroundSvg.setGeometry(0, 0, 750, 119)
        self.backgroundSvg.lower()


class Export_forScreen3(QDialog):
    def __init__(self):
        super(Export_forScreen3, self).__init__()
        self.setGeometry(1135, 70, 750, 165)
        self.setStyleSheet("background-color: rgb(210, 210, 210)")

        self.backgroundSvg = QSvgWidget("images_svg/screen3_export.svg", self)
        self.backgroundSvg.setGeometry(0, 0, 750, 119)
        self.backgroundSvg.lower()

        self.mainLabel = QLabel("Export as:", self)
        self.mainLabel.setGeometry(0, 70, 750, 70)
        self.mainLabel.setStyleSheet(""" color: rgb(30, 30, 30) """)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 12))
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.btImage = Button(self, 440, 100, 200, 40, "Image",
                             "images_svg/Bt_Export_Image.svg", "images_svg/Bt_Export_Image.svg", False)
        self.btData = Button(self, 100, 100, 200, 40, "Data",
                              "images_svg/Bt_Export_Data.svg", "images_svg/Bt_Export_Data.svg", False)
        
class MathPlus_forScreen3(QDialog):
    def __init__(self):
        super(MathPlus_forScreen3, self).__init__()
        self.setGeometry(1135, 70, 750, 165)
        self.setStyleSheet("background-color: rgb(210, 210, 210)")
        self.mainLabel = QLabel("Choose the operation for \nMath Channel:", self)
        self.mainLabel.setGeometry(120, 70, 200, 42)
        self.mainLabel.setStyleSheet(""" color: rgb(30, 30, 30) """)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.simpleOperationsCB = QComboBox(self)
        self.simpleOperationsCB.setGeometry(120, 110, 195, 40)
        self.simpleOperationsCB.setStyleSheet("""background-color: rgb(36, 195, 238); 
                                                            color: rgb(255, 255, 255)""")
        self.simpleOperationsCB.setFont(QFont("Microsoft Sans Serif", 10))
        # self.additionalLabel = QLabel("or", self)
        # self.additionalLabel.setGeometry(430, 85, 20, 42)
        # self.additionalLabel.setStyleSheet(""" color: rgb(30, 30, 30) """)
        # self.additionalLabel.setFont(QFont("Microsoft Sans Serif", 12))
        # self.btMore = Button(self, 540, 90, 120, 40, "More...",
        #                      "images/Bt_Math+_More", "images/Bt_Math+_More", False)

        self.simpleOperationsCBItems = ["CH1 + CH2", "CH1 - CH2", "CH2 - CH1", "CH1 * CH2", "CH1 / CH2", "CH2 / CH1"]
        self.simpleOperationsCB.addItems(self.simpleOperationsCBItems)


        self.backgroundSvg = QSvgWidget("images_svg/screen3_math+.svg", self)
        self.backgroundSvg.setGeometry(0, 0, 750, 119)
        self.backgroundSvg.lower()

class MathPlus_BigScreen(QDialog):
    def __init__(self):
        super(MathPlus_BigScreen, self).__init__()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowContextHelpButtonHint)
        self.setStyleSheet("background-color: rgb(40, 40, 40)")
        self.setWindowTitle("Math+")
        self.setWindowIcon(QIcon("images/Bt_Math+.png"))
        self.setGeometry(800, 200, 300, 500)
        self.setFixedSize(300, 500)

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())
        

        self.iconLabel = QLabel("", self)
        self.iconLabel.setGeometry(40, 10, 220, 60)
        self.mathPlusPixmap = QPixmap("images/Math+.png")
        self.iconLabel.setPixmap(self.mathPlusPixmap.scaled(self.iconLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
        self.mainLabel = QLabel("Set the expression for \nMath Channel: ", self)
        self.mainLabel.setGeometry(55, 90, 200, 50)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 12))
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.expressionLE = QLineEdit(self)
        self.expressionLE.setStyleSheet("""background-color: rgb(31, 166, 203); 
                                                            color: rgb(255, 255, 255)""")
        self.expressionLE.setGeometry(20, 410, 260, 25)

        self.variablesLabel = QLabel("Add variable (optional): ", self)
        self.variablesLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.variablesLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.variablesLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.variablesLabel.setGeometry(55, 170, 200, 50)
        self.variablesLE = QLineEdit(self)
        self.variablesLE.setStyleSheet("""background-color: rgb(31, 166, 203); 
                                                            color: rgb(255, 255, 255)""")
        self.variablesLE.setGeometry(50, 200, 200, 20)
        self.bt_ViewVariables = Button(self, 150, 220, 100, 30, "Variables",
                                       "images/Bt_Math+_Variables", "images/Bt_Math+_Variables",
                                       False)

        self.addLabel = QLabel("Add:", self)
        self.addLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.addLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.addLabel.setGeometry(55, 270, 200, 50)
        self.addCB = QComboBox(self)
        self.addCB.setStyleSheet("""background-color: rgb(31, 166, 203); 
                                                            color: rgb(255, 255, 255)""")
        self.addCB.setGeometry(105, 285, 145, 20)
        self.addCBItems = ['Variable', 'Parenthesis', 'Channel', 'Operation']
        self.addCB.addItems(self.addCBItems)
        self.addCB.currentTextChanged.connect(self.UpdateAddCB)

        self.addAuxLabel = QLabel("Choose: ", self)
        self.addAuxLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.addAuxLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.addAuxLabel.setGeometry(25, 310, 200, 50)
        self.chooseCB = QComboBox(self)
        self.chooseCB.setStyleSheet("""background-color: rgb(31, 166, 203);    color: rgb(255, 255, 255)""")
        self.chooseCB.setGeometry(105, 325, 145, 20)
        self.chooseCBItems_variable = ['R', 'L', 'C']
        self.chooseCBItems_parenthesis = ['(', ')']
        self.chooseCBItems_channel = ['CH1', 'CH2']
        self.chooseCBItems_operation = ['Addition', 'Subtraction', 'Multiplication', 'Division',
                                        'Exponentiation', 'Derivation', 'Integration']
        self.chooseCB.addItems(self.chooseCBItems_variable)
        self.btAdd = Button(self, 155, 350, 100, 30, "Add",
                            "images/Bt_Add.png", "images/Bt_Add.png", False)

        self.expressionLabel = QLabel("Expression: ", self)
        self.expressionLabel.setGeometry(50, 385, 200, 25)
        self.expressionLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.expressionLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.expressionLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.expressionLE.setText("Math = C * deriv(CH1)")
        self.expressionLE.setReadOnly(True)
        self.expressionLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.btSubmit = Button(self, 90, 440, 120, 50, "Submit",
                               "images/Bt_Submit.png", "images/Bt_Submit.png", False)
        self.btSubmit.clicked.connect(self.SubmitClicked)
    def UpdateAddCB(self):
        self.chooseCB.clear()
        if self.addCB.currentText() == 'Variable':
            self.chooseCB.addItems(self.chooseCBItems_variable)
        elif self.addCB.currentText() == 'Parenthesis':
            self.chooseCB.addItems(self.chooseCBItems_parenthesis)
        elif self.addCB.currentText() == 'Channel':
            self.chooseCB.addItems(self.chooseCBItems_channel)
        elif self.addCB.currentText() == 'Operation':
            self.chooseCB.addItems(self.chooseCBItems_operation)

    def SubmitClicked(self):
        self.close()

class FreqRespSweepScr(QDialog):
    def __init__(self):
        super(FreqRespSweepScr, self).__init__()
        self.setGeometry(1135, 70, 750, 165)
        self.setStyleSheet("background-color: rgb(210, 210, 210)")

        self.backgroundSvg = QSvgWidget("images_svg/FreqRespSweepRunning_BackgScreen.svg", self)
        self.backgroundSvg.setGeometry(0, 0, 750, 165)
        self.backgroundSvg.lower()

        self.label1 = QLabel("Sweep is running! \nProgress:", self)
        self.label1.setGeometry(0, 55, 750, 50)
        self.label1.setStyleSheet(""" color: rgb(0, 0, 0); 
                                      background-color: transparent;
                                  """)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label1.setFont(QFont("Lucida Sans Console", 11))

        self.progressBar = QProgressBar(self)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(35)
        self.progressBar.setGeometry(10, 105, 720, 25)

        self.progressBar.setStyleSheet(f"""
                QProgressBar {{
                    border: 1px solid #555;
                    border-radius: 4px;
                    text-align: center;
                }}
                QProgressBar::chunk {{
                    background-color: rgb(70, 160, 80);
                }}
                """)

        self.label2 = QLabel("Sweep complete! Please press Stop Sweep button.", self)
        self.label2.setGeometry(0, 145, 750, 50)
        self.label2.setStyleSheet(""" color: rgb(240, 240, 240); """)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label2.setFont(QFont("Microsoft Sans Serif", 12))
        #self.startProgress(200) #varia a barra de progresso
        self.label2.hide()
        self.sweepRunning = False


    def startBlinkingLabel(self, label, interval_ms=500):
        label.show()
        self._blinkState = False
        self.blinkTimer = QTimer(self)
        self.blinkTimer.timeout.connect(
            lambda: self._toggleLabelColor(label)
        )
        self.blinkTimer.start(interval_ms)

    def _toggleLabelColor(self, label):
        if self._blinkState:
            label.setStyleSheet("color: rgb(240, 240, 240);")
        else:
            label.setStyleSheet("color: green;")

        self._blinkState = not self._blinkState

    def stopBlinkingLabel(self, label):
        if hasattr(self, "blinkTimer"):
            self.blinkTimer.stop()
            label.setStyleSheet("color: rgb(240, 240, 240);")
            label.hide()

    def updateProgressBar(self, value):
        self.progressBar.setValue(value)

        if value >= 100:
            self.label2.show()
            self.startBlinkingLabel(self.label2, 700)



    


if __name__ == '__main__':
    app = QApplication([])
    window = MathPlus_forScreen3()
    window.show()
    app.exec()
