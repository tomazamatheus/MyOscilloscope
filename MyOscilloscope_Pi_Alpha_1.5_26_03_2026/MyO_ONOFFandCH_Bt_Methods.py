#Funções de liga/desliga do botão ON/OFF do osciloscópio e dos botões dos canais CH1, CH2 e Math

import numpy as np
from PySide6.QtCore import Qt, QCoreApplication, QTimer
from PySide6.QtGui import QResizeEvent, QPixmap
from pyqtgraph import QtCore, mkPen
import time

#Método associado ao botão de liga/desliga:
def ONOFF(self):
    if (self.btOnOff.isOn == True): #ligar osciloscópio

        #Fade-in
        self.i = 0
        self.fadeInTimer = QTimer()
        self.fadeInTimer.timeout.connect(self.fadeIn)
        self.fadeInTimer.start(5)

        self.standbyScr1.label.setPixmap(self.standbyScr1.pixmap1)
        self.btCH1.isOn = True
        self.btCH1._update_visual()
        self.vdivCH1Knob.changeImage("images/Knob2_BlueSimple.png")
        self.posCH1Knob.changeImage("images/Knob3_BlueSimple.png")
        self.btCH2.isOn = True
        self.btCH2._update_visual()
        self.vdivCH2Knob.changeImage("images/Knob2_RedSimple.png")
        self.posCH2Knob.changeImage("images/Knob3_RedSimple.png")
        self.standbyScr2.screenOn = True
        self.standbyScr2.changeStandbyScreen()

        self.tertiaryScreen.setCurrentIndex(1)
        self.quaternaryScreen.setCurrentIndex(1)

        """NOTA: A procura inicial por COM Ports ocorre no final do Fade in, função do arquivo principal"""
        self.searchCOMPorts()
        self.calibManualScr.samplingRateSB.setValue(self.mainScr.samplingRate)
        self.calibManualScr.offsetCH1SB.setValue(self.mainScr.offsCH1)
        self.calibManualScr.offsetCH2SB.setValue(self.mainScr.offsCH2)
        self.calibManualScr.attnCH1SB.setValue(self.mainScr.attnCH1)
        self.calibManualScr.attnCH2SB.setValue(self.mainScr.attnCH2)
        self.calibManualScr.phaseCorrectSB.setValue(self.mainScr.phaseCorrTime)
        
        self.vdivCH1Knob.usefulValue = -1
        self.vdivCH1Knob.setValue(self.vdivCH1Knob.value())
        self.UpdateVDivCH1(0)
        self.mainScr.vdivCH1Scale = 0.5
        self.CH1Label.setText(f"CH1: {self.mainScr.vdivCH1Scale} V/div")

        self.vdivCH2Knob.usefulValue = -1
        self.vdivCH2Knob.setValue(self.vdivCH2Knob.value())
        self.UpdateVDivCH2(0)
        self.mainScr.vdivCH2Scale = 0.5
        self.CH2Label.setText(f"CH2: {self.mainScr.vdivCH2Scale} V/div")


        self.vdivMathKnob.usefulValue = -1
        self.vdivMathKnob.setValue(self.vdivMathKnob.value())
        self.UpdateVDivMath(0)
        self.mainScr.vdivMathScale = 0.5
        self.mathvDivLabel.setText(f"Math: {self.mainScr.vdivMathScale} V/div")

        #para plotting na tela do cursor FFT:
        self.X1ValueFFT = 10
        self.X2ValueFFT = 10000 
        self.Y1ValueFFT = -65
        self.Y2ValueFFT = 15

        self.mainScr.updateTimer.start(self.mainScr.refreshRate)
        self.measurementsTimer.start(400)

    else: #desligar osciloscópio
        self.mainScr.obtainMeasureValues = False
        self.screenName = ""
        #time.sleep(0.5)

        self.stopSweep()
        self.freqResp_scr2.freqResp_page2.clearScreenPartialCheckBox.setChecked(False)
        self.clearSweeps()

        # Fade-out
        self.i = 190
        self.fadeOutTimer = QTimer()
        self.fadeOutTimer.timeout.connect(self.fadeOut)
        self.fadeOutTimer.start(5)
        self.standbyScr1.label.clear()
        self.primaryScreen.setCurrentIndex(0)
        self.secondaryScreen.setCurrentIndex(0)
        self.tertiaryScreen.setCurrentIndex(0)
        self.quaternaryScreen.setCurrentIndex(0)
        self.standbyScr2.screenOn = False
        self.standbyScr2.changeStandbyScreen()
        self.timeLabel.hide()
        self.CH1Label.hide()
        self.posCH1Label.hide()
        self.posCH2Label.hide()
        self.CH2Label.hide()
        self.triggerProportionLabel.hide()
        self.triggerLabel.hide()
        self.phaseLabel.hide()
        self.phaseLabel.setText("")
        self.cursorProportionalLabel.hide()
        self.cursorFFTLabel.hide()
        self.mathvDivLabel.hide()
        self.mathPosLabel.hide()
        self.cursorKnob.changeImage("images/Knob2.png")
        self.triggerKnob.changeImage("images/Knob2.png")
        self.vdivCH1Knob.changeImage("images/Knob2.png")
        self.posCH1Knob.changeImage("images/Knob3.png")
        self.vdivCH2Knob.changeImage("images/Knob2.png")
        self.posCH2Knob.changeImage("images/Knob3.png")
        self.vdivMathKnob.changeImage("images/Knob2.png")
        self.posMathKnob.changeImage("images/Knob3.png")
        if self.cursorLinesOn == True: self.removeCursorLines()
        self.cursorLinesFFT = False
        if self.btMath.isOn == True: self.mainScr.removeItem(self.mainScr.graphicPlotting_Math)
        self.cursorKnob.buttonIsOn = False
        self.mainScr.measureTime = False
        self.bt_Wfm.moveButton(1670, -40)
        self.bt_Calibration.moveButton(1730, -40)
        self.bt_Exp.moveButton(1740, -40)
        self.bt_MathPlus.moveButton(1790, -40)
        if self.WFMgeneratorScr.btOnOff_isOn: self.WFMgeneratorScr.WFMBtOnOff()
        self.turnEverythingToOFF(partialShutdown=False)
        self.btSite.visual.setEnabled(False)
        #self.btVideos.visual.setEnabled(False)
        self.mainScr.stopSerial()
        self.mainScr.COMPortON = False
        if self.calibManual_isOn: 
            self.closeCalibManual()
            self.calibManual_isOn = False
        self.mainScr.freezeTime = False
        self.freqResp_scr2.freqResp_page1.btSweep_Stop.clicked.emit()
        self.backgroundLabel5.setStyleSheet("""
            background-color: rgb(30, 30, 30);
            border-radius: 10px;
        """)
        self.mainScr.updateTimer.stop()
        self.measurementsTimer.stop()
        self.resetSystem() 
        
        
        

        
        


#Método associado ao botão de liga/desliga do Canal 1
def btCH1Clicked(self):
    if(self.btCH1.isOn == True and self.btOnOff.isOn == True):
        if(self.screenName == "Main"):
            self.CH1Label.show()
            if not self.posCH1Knob.usefulValue == 0:
                self.posCH1Label.show()


        else:
            self.CH1Label.hide()
            self.posCH1Label.hide()
            self.posCH2Label.hide()
        self.mainScr.graphicPlotting_CH1 = self.mainScr.plot(self.mainScr.x_plot, self.mainScr.y_CH1_plot,
                                                             pen=self.mainScr.graphStyleCH1)
        self.mainScr.graphicPlotting_CH1.setDownsampling(auto=True, method='peak')
        self.FFTScr.graphicPlotting_CH1 = self.FFTScr.plot(self.FFTScr.FFT_freqs_CH1, self.FFTScr.FFT_amplits_CH1_dB, 
                                                           pen = self.FFTScr.graphStyleCH1)
        
                                                 
        self.FFTScr.CH1_Active = True
        
        self.vdivCH1Knob.buttonIsOn = True
        self.posCH1Knob.buttonIsOn = True

        
        self.measure.channelSelectCB.insertItem(0, "CH1")
        self.vdivCH1Knob.changeImage("images/Knob2_BlueSimple.png")
        self.posCH1Knob.changeImage("images/Knob3_BlueSimple.png")
        self.mainScr.CH1Activated = True
    else:
        self.CH1Label.hide()
        self.posCH1Label.hide()
        self.vdivCH1Knob.changeImage("images/Knob2.png")
        self.posCH1Knob.changeImage("images/Knob3.png")
        self.posCH1Knob.buttonIsOn = False
        if (self.mainScr.triggerChannel == "CH1"):
            if(self.btTrigger.isOn == True): self.triggerProportionLabel.hide()
            if(self.btMeas.isOn == True): self.phaseLabel.hide()

        self.mainScr.removeItem(self.mainScr.graphicPlotting_CH1)
        try:
            self.FFTScr.removeItem(self.FFTScr.graphicPlotting_CH1)
        except AttributeError:
            pass
        self.FFTScr.CH1_Active = False
        self.vdivCH1Knob.buttonIsOn = False
        
        index = self.measure.channelSelectCB.findText("CH1")
        self.measure.channelSelectCB.removeItem(index)
        self.mainScr.CH1Activated = False

    if(self.btOnOff.isOn == False): #Impede o botão ativar com o osciloscópio desligado
        self.btCH1.isOn = False
        self.btCH1._update_visual()
        

    #Um reinício da segunda tela para evitar problemas:
    self.btTrigger.isOn = False
    self.btMeas.isOn = False
    self.btCursor.isOn = False
    if self.screenName == "": self.secondaryScreen.setCurrentIndex(0)
    else:
        if self.screenName == "Main": 
            if self.currentMainScr2_Scr == 1: self.secondaryScreen.setCurrentIndex(7)
            else:                            self.secondaryScreen.setCurrentIndex(8)
        elif self.screenName == "FFT":
            self.secondaryScreen.setCurrentIndex(5)
        
        elif self.screenName == "Phas Diag":
            self.phaseLabel.setText(f"Reference Channel: \n{self.mainScr.referencePhase}")
            self.phaseLabel.show()
            self.secondaryScreen.setCurrentIndex(4)
    self.secondaryScreenName = ""
    self.UpdateSecondaryButtons()
    

    

#Método associado ao botão de liga/desliga do Canal 2
def btCH2Clicked(self):
    if(self.btCH2.isOn == True and self.btOnOff.isOn == True):
        if (self.screenName == "Main"):
            self.CH2Label.show()
            if not self.posCH2Knob.usefulValue == 0:
                self.posCH2Label.show()
                
        else:
            self.CH2Label.hide()
        self.mainScr.graphicPlotting_CH2 = self.mainScr.plot(self.mainScr.x_plot, self.mainScr.y_CH2_plot, pen=self.mainScr.graphStyleCH2)
        self.vdivCH2Knob.buttonIsOn = True
        
        self.measure.channelSelectCB.insertItem(1, "CH2")
        self.posCH2Knob.buttonIsOn = True
        self.vdivCH2Knob.changeImage("images/Knob2_RedSimple.png")
        self.posCH2Knob.changeImage("images/Knob3_RedSimple.png")

        self.FFTScr.graphicPlotting_CH2 = self.FFTScr.plot(self.FFTScr.FFT_freqs_CH2, self.FFTScr.FFT_amplits_CH2_dB, pen = self.FFTScr.graphStyleCH2)
        self.FFTScr.CH2_Active = True
        self.mainScr.CH2Activated = True
    else:
        self.CH2Label.hide()
        self.posCH2Label.hide()
        self.vdivCH2Knob.changeImage("images/Knob2.png")
        self.posCH2Knob.changeImage("images/Knob3.png")
        if (self.mainScr.triggerChannel == "CH2"):
            if(self.btTrigger.isOn == True): self.triggerProportionLabel.lower()
            if(self.btMeas.isOn == True): self.phaseLabel.lower()
        self.mainScr.removeItem(self.mainScr.graphicPlotting_CH2)
        try:
            self.FFTScr.removeItem(self.FFTScr.graphicPlotting_CH2)
        except AttributeError:
            pass
        self.FFTScr.CH2_Active = False
        self.vdivCH2Knob.buttonIsOn = False
        
        index = self.measure.channelSelectCB.findText("CH2")
        self.measure.channelSelectCB.removeItem(index)
        self.posCH2Knob.buttonIsOn = False
        self.mainScr.CH1Activated = False

        
    if(self.btOnOff.isOn == False): #Impede o botão ativar com o osciloscópio desligado
        self.btCH2.isOn = False
        self.btCH2._update_visual()

    #Um reinício da segunda tela para evitar problemas:
    self.btTrigger.isOn = False
    self.btMeas.isOn = False
    self.btCursor.isOn = False
    if self.screenName == "": self.secondaryScreen.setCurrentIndex(0)
    else:
        if self.screenName == "Main": 
            if self.currentMainScr2_Scr == 1: self.secondaryScreen.setCurrentIndex(7)
            else:                            self.secondaryScreen.setCurrentIndex(8)
        elif self.screenName == "FFT":
            self.secondaryScreen.setCurrentIndex(5)
        
        elif self.screenName == "Phas Diag":
            self.phaseLabel.setText(f"Reference Channel: \n{self.mainScr.referencePhase}")
            self.phaseLabel.show()
            self.secondaryScreen.setCurrentIndex(4)
    self.secondaryScreenName = ""
    self.UpdateSecondaryButtons()

#Método associado ao botão de liga/desliga de Math
def btMathClicked(self):
    if(self.btOnOff.isOn == False): #Impede o botão ativar com o osciloscópio desligado
        self.btMath.isOn = False
        self.btMath._update_visual()
        self.vdivMathKnob.changeImage("images/Knob2.png")
        self.posMathKnob.changeImage("images/Knob3.png")


    if self.btMath.isOn == True:
        self.mainScr.graphicPlotting_Math = self.mainScr.plot(self.mainScr.x_plot,
                                                              self.mainScr.y_Math_plot, pen=self.mainScr.graphStyleMath)
        self.FFTScr.graphicPlotting_Math = self.FFTScr.plot(self.FFTScr.FFT_freqs_Math, self.FFTScr.FFT_amplits_Math_dB, pen = self.FFTScr.graphStyleMath)
        self.FFTScr.Math_Active = True
        self.vdivMathKnob.buttonIsOn = True
        self.posMathKnob.buttonIsOn = True
        self.vdivMathKnob.changeImage("images/Knob2_CyanSimple.png")
        self.posMathKnob.changeImage("images/Knob3_CyanSimple.png")
        if self.btOnOff.isOn == True and self.screenName == "Main":
            self.mathvDivLabel.show()
            if not self.posMathKnob.usefulValue == 0 and self.screenName == "Main" and self.btMath.isOn == True:
                self.mathPosLabel.show()
        else:
            self.mathvDivLabel.hide()
            self.mathPosLabel.hide()
        self.mainScr.mathActivated = True
    else:
        self.mainScr.removeItem(self.mainScr.graphicPlotting_Math)
        try:
            self.FFTScr.removeItem(self.FFTScr.graphicPlotting_Math)
        except AttributeError:
            pass
        self.FFTScr.Math_Active = False
        self.vdivMathKnob.changeImage("images/Knob2.png")
        self.posMathKnob.changeImage("images/Knob3.png")
        self.mathvDivLabel.hide()
        self.mathPosLabel.hide()
        self.vdivMathKnob.buttonIsOn = False
        self.posMathKnob.buttonIsOn = False
        self.mainScr.CH1Activated = False

    #Um reinício da segunda tela para evitar problemas:
    self.btTrigger.isOn = False
    self.btMeas.isOn = False
    self.btCursor.isOn = False
    if self.screenName == "": self.secondaryScreen.setCurrentIndex(0)
    else:
        if self.screenName == "Main": 
            if self.currentMainScr2_Scr == 1: self.secondaryScreen.setCurrentIndex(7)
            else:                            self.secondaryScreen.setCurrentIndex(8)
        elif self.screenName == "FFT":
            self.secondaryScreen.setCurrentIndex(5)
        
        elif self.screenName == "Phas Diag":
            self.phaseLabel.setText(f"Reference Channel: \n{self.mainScr.referencePhase}")
            self.phaseLabel.show()
            self.secondaryScreen.setCurrentIndex(4)
    self.secondaryScreenName = ""
    self.UpdateSecondaryButtons()
