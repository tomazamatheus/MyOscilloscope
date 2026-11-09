from PySide6.QtWidgets import QDialog, QLabel, QComboBox, QLineEdit, QPushButton, QSpinBox, QDoubleSpinBox, QApplication
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtCore import Qt, QSignalBlocker
from button import Button
import numpy as np



def openCalibManual(self):
    if not self.screenName == "" and not self.screenName == "Help":
        p = self.width()/1920
        if self.screenName == "Main": self.screen1.setGeometry(int(self.p * 10), int(self.p * 360), int(self.p * 1000), int(self.p * 320))
        elif self.screenName == "FFT": self.screen1.setGeometry(int(self.p * 10), int(self.p * 360), int(self.p * 1000), int(self.p * 320))
        elif self.screenName == "Freq Resp": self.screen1.setGeometry(int(self.p * 10), int(self.p * 360), int(self.p * 1000), int(self.p * 320))
        elif self.screenName == "Phas Diag": self.screen1.setGeometry(int(self.p * (-130)), int(self.p * 360), int(self.p * 1120), int(self.p * 320))
        

        if self.screenName == "Main": self.calibManualScr.setStyleSheet("background-color: rgb(5, 5, 18)")
        elif self.screenName == "FFT": self.calibManualScr.setStyleSheet("background-color: rgb(16, 5, 5)")
        elif self.screenName == "Freq Resp": self.calibManualScr.setStyleSheet("background-color: rgb(5, 16, 5)") 
        else: self.calibManualScreen.setStyleSheet("background-color: rgb(18, 18, 0)")
        self.calibManualScreen.setGeometry(int(self.p *5), int(self.p *700), int(self.p *1000), int(self.p *150))
        self.calibManualScreen.raise_()

        self.secondaryScreen.setCurrentIndex(12)
        self.calibManual_isOn = True

def closeCalibManual(self):
    p = self.width()/1920
    if not self.screenName == "Phas Diag": self.screen1.setGeometry(int(self.p * (-130)), int(self.p * 360), int(self.p * 1120), int(self.p * 560))
    else: self.screen1.setGeometry(int(self.p * 10), int(self.p * 360), int(self.p * 1000), int(self.p * 460))

    if self.screenName == "Main": self.screen1.setGeometry(int(self.p * 10), int(self.p * 360), int(self.p * 1000), int(self.p * 460))
    elif self.screenName == "FFT": self.screen1.setGeometry(int(self.p * 10), int(self.p * 360), int(self.p * 1000), int(self.p * 460))
    elif self.screenName == "Freq Resp": self.screen1.setGeometry(int(self.p * 10), int(self.p * 360), int(self.p * 1000), int(self.p * 460))
    elif self.screenName == "Phas Diag": self.screen1.setGeometry(int(self.p * (-130)), int(self.p * 360), int(self.p * 1120), int(self.p * 560))
    else: self.screen1.setGeometry(int(self.p * 17), int(self.p * 336), int(self.p * 990), int(self.p * 511))
    self.calibManualScreen.setGeometry(0, 0, 0, 0)
    self.calibManual_isOn = False

    if self.screenName == "Main":
            if self.currentMainScr2_Scr == 1: self.secondaryScreen.setCurrentIndex(7)
            else:                             self.secondaryScreen.setCurrentIndex(8)

    elif self.screenName == "FFT":
        self.secondaryScreen.setCurrentIndex(5)
        self.cursorFFTLabel.hide()

    elif self.screenName == "Phas Diag":
        self.secondaryScreen.setCurrentIndex(4)

    elif self.screenName == "Freq Resp":
        self.secondaryScreen.setCurrentIndex(9)

    else: self.secondaryScreen.setCurrentIndex(0)

# ----------- offset_CH1 -----------------------
def onSpinBoxTyping_offsetCH1(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_offsetCH1 = True

def onSpinBoxEditingFinished_offsetCH1(self):
    if self.user_is_typing_offsetCH1:
        self.user_is_typing_offsetCH1 = False
        self.changeFrequency_Keyboard_offsetCH1()

def onSpinBoxValueChanged_offsetCH1(self):
    if not self.user_is_typing_offsetCH1:
        self.changeFrequency_Mouse_offsetCH1()

def changeFrequency_Mouse_offsetCH1(self):
    if self.calibManualScr.offsetCH1SB.value() > 20: self.calibManualScr.offsetCH1SB.setValue(20.000)
    self.mainScr.dataHandler.offsCH1 = self.calibManualScr.offsetCH1SB.value()

def changeFrequency_Keyboard_offsetCH1(self):
    if self.calibManualScr.offsetCH1SB.value() > 20: self.calibManualScr.offsetCH1SB.setValue(20.000)
    self.mainScr.dataHandler.offsCH1 = self.calibManualScr.offsetCH1SB.value()

# ----------------- offsetCH2 -----------------
def onSpinBoxTyping_offsetCH2(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_offsetCH2 = True

def onSpinBoxEditingFinished_offsetCH2(self):
    if self.user_is_typing_offsetCH2:
        self.user_is_typing_offsetCH2 = False
        self.changeFrequency_Keyboard_offsetCH2()

def onSpinBoxValueChanged_offsetCH2(self):
    if not self.user_is_typing_offsetCH2:
        self.changeFrequency_Mouse_offsetCH2()

def changeFrequency_Mouse_offsetCH2(self):
    if self.calibManualScr.offsetCH2SB.value() > 20: self.calibManualScr.offsetCH2SB.setValue(20.000)
    self.mainScr.dataHandler.offsCH2 = self.calibManualScr.offsetCH2SB.value()

def changeFrequency_Keyboard_offsetCH2(self):
    if self.calibManualScr.offsetCH2SB.value() > 20: self.calibManualScr.offsetCH2SB.setValue(20.000)
    self.mainScr.dataHandler.offsCH2 = self.calibManualScr.offsetCH2SB.value()

# ----------------- attnCH1 -----------------
def onSpinBoxTyping_attnCH1(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_attnCH1 = True

def onSpinBoxEditingFinished_attnCH1(self):
    if self.user_is_typing_attnCH1:
        self.user_is_typing_attnCH1 = False
        self.changeFrequency_Keyboard_attnCH1()

def onSpinBoxValueChanged_attnCH1(self):
    if not self.user_is_typing_attnCH1:
        self.changeFrequency_Mouse_attnCH1()

def changeFrequency_Mouse_attnCH1(self):
    if self.calibManualScr.attnCH1SB.value() > 20: self.calibManualScr.attnCH1SB.setValue(20.000)
    self.mainScr.dataHandler.attnCH1 = self.calibManualScr.attnCH1SB.value()

def changeFrequency_Keyboard_attnCH1(self):
    if self.calibManualScr.attnCH1SB.value() > 20: self.calibManualScr.attnCH1SB.setValue(20.000)
    self.mainScr.dataHandler.attnCH1 = self.calibManualScr.attnCH1SB.value()

# ----------------- attnCH2 -----------------
def onSpinBoxTyping_attnCH2(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_attnCH2 = True

def onSpinBoxEditingFinished_attnCH2(self):
    if self.user_is_typing_attnCH2:
        self.user_is_typing_attnCH2 = False
        self.changeFrequency_Keyboard_attnCH2()

def onSpinBoxValueChanged_attnCH2(self):
    if not self.user_is_typing_attnCH2:
        self.changeFrequency_Mouse_attnCH2()

def changeFrequency_Mouse_attnCH2(self):
    if self.calibManualScr.attnCH2SB.value() > 20: self.calibManualScr.attnCH2SB.setValue(20.000)
    self.mainScr.dataHandler.attnCH2 = self.calibManualScr.attnCH2SB.value()

def changeFrequency_Keyboard_attnCH2(self):
    self.mainScr.dataHandler.attnCH2 = self.calibManualScr.attnCH2SB.value()

# ----------------- phaseCorrection -----------------
def onSpinBoxTyping_phaseCorr(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_phaseCorr = True

def onSpinBoxEditingFinished_phaseCorr(self):
    if self.user_is_typing_phaseCorr:
        self.user_is_typing_phaseCorr = False
        self.changeFrequency_Keyboard_phaseCorr()

def onSpinBoxValueChanged_phaseCorr(self):
    if not self.user_is_typing_phaseCorr:
        self.changeFrequency_Mouse_phaseCorr()

def changeFrequency_Mouse_phaseCorr(self):
    if self.calibManualScr.phaseCorrectSB.value() > 30: self.calibManualScr.phaseCorrectSB.setValue(30.000)
    elif self.calibManualScr.phaseCorrectSB.value() < -30: self.calibManualScr.phaseCorrectSB.setValue(-30.000)
    self.mainScr.phaseCorrTime = self.calibManualScr.phaseCorrectSB.value()

def changeFrequency_Keyboard_phaseCorr(self):
    self.mainScr.phaseCorrTime = self.calibManualScr.phaseCorrectSB.value()

    # ----------------- samplingRate -----------------
def onSpinBoxTyping_samplingRate(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_samplingRate = True

def onSpinBoxEditingFinished_samplingRate(self):
    if self.user_is_typing_samplingRate:
        self.user_is_typing_samplingRate = False
        self.changeFrequency_Keyboard_samplingRate()

def onSpinBoxValueChanged_samplingRate(self):
    if not self.user_is_typing_samplingRate:
        self.changeFrequency_Mouse_samplingRate()

def changeFrequency_Mouse_samplingRate(self):
    value = self.calibManualScr.samplingRateSB.value() 
    if value % 2 == 0: self.mainScr.samplingRate = value
    else: self.mainScr.samplingRate = value + 1
    blocker = QSignalBlocker(self.calibManualScr.samplingRateSB)
    self.calibManualScr.samplingRateSB.setValue(self.mainScr.samplingRate)
    #self.reloadSamplingRate()

def changeFrequency_Keyboard_samplingRate(self):
    value = self.calibManualScr.samplingRateSB.value() 
    if value % 2 == 0: self.mainScr.samplingRate = value
    else: self.mainScr.samplingRate = value + 1
    
    blocker = QSignalBlocker(self.calibManualScr.samplingRateSB)
    self.calibManualScr.samplingRateSB.setValue(self.mainScr.samplingRate)
    #self.reloadSamplingRate()



def btSave_calibManual_clicked(self):
    self.mainScr.dataHandler.offsCH1 = self.calibManualScr.offsetCH1SB.value()
    self.mainScr.dataHandler.offsCH2 = self.calibManualScr.offsetCH2SB.value()
    self.mainScr.dataHandler.attnCH1 = self.calibManualScr.attnCH1SB.value()
    self.mainScr.dataHandler.attnCH2 = self.calibManualScr.attnCH2SB.value()
    self.mainScr.dataHandler.samplingRate = self.calibManualScr.samplingRateSB.value()
    #self.reloadSamplingRate()
    self.mainScr.phaseCorrTime = self.calibManualScr.phaseCorrectSB.value()

    self.saveCalibrationParams(self.mainScr.dataHandler.offsCH1, self.mainScr.dataHandler.offsCH2,
                                self.mainScr.dataHandler.attnCH1, self.mainScr.dataHandler.attnCH2,
                                self.mainScr.phaseCorrTime, self.mainScr.dataHandler.samplingRate)
    
    self.savedCalibScr.open()
    
def saveCalibrationParams(self, offsCH1, offsCH2, attnCH1, attnCH2, phaseCorr, samplingRate):

    filepath = self.PARAMETERS_FILE
    # Parâmetros a salvar
    params = {
        "offs_CH1": f"{offsCH1:.3f}",
        "offs_CH2": f"{offsCH2:.3f}",
        "attn_CH1": f"{attnCH1:.3f}",
        "attn_CH2": f"{attnCH2:.3f}",
        "phase_corr": f"{phaseCorr:.5f}",
        "samplingRate": f"{int(samplingRate)}",
    }

    # Lê o arquivo existente
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    keys_written = set()

    # Atualiza linhas existentes
    for i, line in enumerate(lines):
        for key, value in params.items():
            if line.strip().startswith(f"{key} ="):
                lines[i] = f"{key} = {value}\n"
                keys_written.add(key)

    # Adiciona parâmetros que não existiam
    for key, value in params.items():
        if key not in keys_written:
            lines.append(f"{key} = {value}\n")

    # Grava o arquivo novamente
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)


# def loadCalibrationParams() em mainScreen!


class CalibManual(QDialog):
    def __init__(self):
        super(CalibManual, self).__init__()
        self.setGeometry(70, 535, 1020, 130)
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.samplingRateLabel = QLabel("Fs (S/s):", self)
        self.samplingRateLabel.setGeometry(10, 30, 80, 22)
        self.samplingRateLabel.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.samplingRateLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.samplingRateLabel.setAlignment(Qt.AlignHCenter)
        self.samplingRateSB = QSpinBox(self)
        self.samplingRateSB.setRange(0, 250000)  # mínimo e máximo
        self.samplingRateSB.setSingleStep(2)  # incremento/decremento
        self.samplingRateSB.setValue(19232)
        self.samplingRateSB.setGeometry(115, 25, 100, 30)
        self.samplingRateSB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.samplingRateSB.setAlignment(Qt.AlignHCenter)
        self.samplingRateSB.setFont(QFont("Microsoft Sans Serif", 10))
        self.samplingRateSB.setReadOnly(False)

        self.offsetCH1Label = QLabel("Offset CH1:", self)
        self.offsetCH1Label.setGeometry(275, 30, 100, 22)
        self.offsetCH1Label.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.offsetCH1Label.setFont(QFont("Microsoft Sans Serif", 10))
        self.offsetCH1Label.setAlignment(Qt.AlignHCenter)
        self.offsetCH1SB = QDoubleSpinBox(self)
        self.offsetCH1SB.setRange(0, 1000000.000)  # mínimo e máximo
        self.offsetCH1SB.setSingleStep(0.010)  # incremento/decremento
        self.offsetCH1SB.setValue(1.500)
        self.offsetCH1SB.setDecimals(3)
        self.offsetCH1SB.setGeometry(380, 25, 100, 30)
        self.offsetCH1SB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.offsetCH1SB.setAlignment(Qt.AlignHCenter)
        self.offsetCH1SB.setFont(QFont("Microsoft Sans Serif", 10))
        self.offsetCH1SB.setReadOnly(False)

        self.offsetCH2Label = QLabel("Offset CH2:", self)
        self.offsetCH2Label.setGeometry(275, 90, 100, 22)
        self.offsetCH2Label.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.offsetCH2Label.setFont(QFont("Microsoft Sans Serif", 10))
        self.offsetCH2Label.setAlignment(Qt.AlignHCenter)
        self.offsetCH2SB = QDoubleSpinBox(self)
        self.offsetCH2SB.setRange(0, 1000000.000)  # mínimo e máximo
        self.offsetCH2SB.setSingleStep(0.010)  # incremento/decremento
        self.offsetCH2SB.setValue(1.500)
        self.offsetCH2SB.setDecimals(3)
        self.offsetCH2SB.setGeometry(380, 85, 100, 30)
        self.offsetCH2SB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.offsetCH2SB.setAlignment(Qt.AlignHCenter)
        self.offsetCH2SB.setFont(QFont("Microsoft Sans Serif", 10))
        self.offsetCH2SB.setReadOnly(False)

        self.attnCH1Label = QLabel("Attn CH1:", self)
        self.attnCH1Label.setGeometry(520, 30, 100, 22)
        self.attnCH1Label.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.attnCH1Label.setFont(QFont("Microsoft Sans Serif", 10))
        self.attnCH1Label.setAlignment(Qt.AlignHCenter)
        self.attnCH1SB = QDoubleSpinBox(self)
        self.attnCH1SB.setRange(0, 1000000.000)  # mínimo e máximo
        self.attnCH1SB.setSingleStep(0.010)  # incremento/decremento
        self.attnCH1SB.setValue(1.500)
        self.attnCH1SB.setDecimals(3)
        self.attnCH1SB.setGeometry(625, 25, 100, 30)
        self.attnCH1SB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.attnCH1SB.setAlignment(Qt.AlignHCenter)
        self.attnCH1SB.setFont(QFont("Microsoft Sans Serif", 10))
        self.attnCH1SB.setReadOnly(False)

        self.attnCH2Label = QLabel("Attn CH2:", self)
        self.attnCH2Label.setGeometry(520, 90, 100, 22)
        self.attnCH2Label.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.attnCH2Label.setFont(QFont("Microsoft Sans Serif", 10))
        self.attnCH2Label.setAlignment(Qt.AlignHCenter)
        self.attnCH2SB = QDoubleSpinBox(self)
        self.attnCH2SB.setRange(0, 1000000.000)  # mínimo e máximo
        self.attnCH2SB.setSingleStep(0.010)  # incremento/decremento
        self.attnCH2SB.setValue(1.500)
        self.attnCH2SB.setDecimals(3)
        self.attnCH2SB.setGeometry(625, 85, 100, 30)
        self.attnCH2SB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.attnCH2SB.setAlignment(Qt.AlignHCenter)
        self.attnCH2SB.setFont(QFont("Microsoft Sans Serif", 10))
        self.attnCH2SB.setReadOnly(False)

        self.phaseCorrectLabel = QLabel("Phase Corr.:", self)
        self.phaseCorrectLabel.setGeometry(10, 90, 100, 22)
        self.phaseCorrectLabel.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.phaseCorrectLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.phaseCorrectLabel.setAlignment(Qt.AlignHCenter)
        self.phaseCorrectSB = QDoubleSpinBox(self)
        self.phaseCorrectSB.setRange(-1000000, 1000000)  # mínimo e máximo
        self.phaseCorrectSB.setSingleStep(0.001)  # incremento/decremento
        self.phaseCorrectSB.setValue(0.00)
        self.phaseCorrectSB.setDecimals(5)
        self.phaseCorrectSB.setGeometry(115, 85, 100, 30)
        self.phaseCorrectSB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.phaseCorrectSB.setAlignment(Qt.AlignHCenter)
        self.phaseCorrectSB.setFont(QFont("Microsoft Sans Serif", 10))
        self.phaseCorrectSB.setReadOnly(False)

        self.btSave = Button(self, 790, 75, 170, 50, "Save",
                             "images/Bt_SaveCalib.png", "images/Bt_SaveCalib.png", False)
        
        self.btClose = Button(self, 790, 15, 170, 50, "Close",
                             "images/Bt_Close.png", "images/Bt_Close.png", False)
        
    def resizeEvent(self, event):
        p = self.width()/1020
        self.samplingRateLabel.setGeometry(
            int(p * 10), int(p * 30),
            int(p * 80), int(p * 22)
        )

        self.samplingRateSB.setGeometry(
            int(p * 115), int(p * 25),
            int(p * 100), int(p * 30)
        )

        self.offsetCH1Label.setGeometry(
            int(p * 275), int(p * 30),
            int(p * 100), int(p * 22)
        )

        self.offsetCH1SB.setGeometry(
            int(p * 380), int(p * 25),
            int(p * 100), int(p * 30)
        )

        self.offsetCH2Label.setGeometry(
            int(p * 275), int(p * 90),
            int(p * 100), int(p * 22)
        )

        self.offsetCH2SB.setGeometry(
            int(p * 380), int(p * 85),
            int(p * 100), int(p * 30)
        )

        self.attnCH1Label.setGeometry(
            int(p * 520), int(p * 30),
            int(p * 100), int(p * 22)
        )

        self.attnCH1SB.setGeometry(
            int(p * 625), int(p * 25),
            int(p * 100), int(p * 30)
        )

        self.attnCH2Label.setGeometry(
            int(p * 520), int(p * 90),
            int(p * 100), int(p * 22)
        )

        self.attnCH2SB.setGeometry(
            int(p * 625), int(p * 85),
            int(p * 100), int(p * 30)
        )

        self.phaseCorrectLabel.setGeometry(
            int(p * 0), int(p * 90),
            int(p * 110), int(p * 22)
        )

        self.phaseCorrectSB.setGeometry(
            int(p * 115), int(p * 85),
            int(p * 100), int(p * 30)
        )


        self.btSave.setGeometry(int(p * 790), int(p * 75), int(p * 170), int( p * 50))
        self.btSave.visual.setGeometry(int(p * 790), int(p * 75), int(p * 170), int(p * 50))
        self.btSave.visual.setPixmap(QPixmap(self.btSave.image_off_path).scaled(self.btSave.visual.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))

        self.btClose.setGeometry(int(p * 790), int(p * 15), int(p * 170), int( p * 50))
        self.btClose.visual.setGeometry(int(p * 790), int(p * 15), int(p * 170), int(p * 50))
        self.btClose.visual.setPixmap(QPixmap(self.btClose.image_off_path).scaled(self.btClose.visual.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))



if __name__ == '__main__':
    app = QApplication([])
    window = CalibManual()
    window.show()
    app.exec()

