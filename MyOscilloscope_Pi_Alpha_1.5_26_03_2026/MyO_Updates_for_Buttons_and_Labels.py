#Funções auxiliares às funções em Screen1_Methods, funções das ferramentas como Cursor, Measure, Trigger, Freeze, e funções 
#presentes em ONOFFandCH_Bt_Methods (ou seja, aqui estão funções associadas aos botões que não sejam de ligar canais)


import numpy as np
from PySide6.QtCore import Qt, QCoreApplication, QTimer
from PySide6.QtGui import QPixmap
from pyqtgraph import mkPen


#Ajustes relacionados a alterações da subjanela principal
def UpdatePrimaryButtons(self): #Atualiza os botões principais e coisas relacionadas
    if not self.screenName == "Main":
        self.btMain.isOn = False
        self.btMain._update_visual()
        self.mainScr.removeItem(self.graphicPlottingTrigger)
        self.triggerKnob.buttonIsOn = False

        self.triggerProportionLabel.hide()
        self.timeLabel.hide()
        self.CH1Label.hide()
        self.posCH1Label.hide()
        self.posCH2Label.hide()
        self.CH2Label.hide()
        self.mathvDivLabel.hide()
        self.mathPosLabel.hide()
        self.vdivCH1Knob.buttonIsOn = False
        self.vdivCH2Knob.buttonIsOn = False
        self.vdivMathKnob.buttonIsOn = False
        self.posCH1Knob.buttonIsOn = False
        self.posCH2Knob.buttonIsOn = False
        self.posMathKnob.buttonIsOn = False
        self.timeKnob.buttonIsOn = False
        self.blackLabel1.hide()
        self.blackLabel2.hide()

    if not self.screenName == "FFT":
        self.btFFT.isOn = False
        self.btFFT._update_visual()
        if self.secondaryScreen.currentIndex() == 5:
            self.secondaryScreen.setCurrentIndex(0)
        self.cursorFFTLabel.hide()
        self.cursorLinesFFT = False
        

    if not self.screenName == "Freq Resp":
        self.btFreqResp.isOn = False
        self.btFreqResp._update_visual()

    if not self.screenName == "Phas Diag":
        self.btPhasDiag.isOn = False
        self.btPhasDiag._update_visual()
        if self.secondaryScreen.currentIndex() == 7 or self.secondaryScreen.currentIndex() == 8:
            self.secondaryScreen.setCurrentIndex(0)

    if not self.screenName == "Help":
        self.btHelp.isOn = False
        self.btHelp._update_visual()
        



    #se nenhuma aba nem Help estiver ativada (= standbyScreen)
    if (self.btMain.isOn == False and self.btFFT.isOn == False and self.btFreqResp.isOn == False
            and self.btPhasDiag.isOn == False and self.btHelp.isOn == False):
        self.mainScr.removeItem(self.graphicPlottingTrigger)
        self.screenName = ""
        self.primaryScreen.setCurrentIndex(0)
        self.secondaryScreen.setCurrentIndex(0)
        self.cursorKnob.changeImage("images/Knob2.png")
        self.triggerKnob.changeImage("images/Knob2.png")
        self.timeLabel.hide()
        self.CH1Label.hide()
        self.posCH1Label.hide()
        self.CH2Label.hide()
        self.posCH2Label.hide()
        self.triggerLabel.hide()
        self.triggerProportionLabel.hide()
        self.phaseLabel.hide()
        self.cursorProportionalLabel.hide()
        self.mathvDivLabel.hide()
        self.mathPosLabel.hide()
        self.cursorFFTLabel.hide()
        #self.exportLabel.lower()
        self.blackLabel1.hide()
        self.blackLabel2.hide()
        if self.cursorLinesOn == True: self.removeCursorLines()
        self.cursorKnob.buttonIsOn = False
        self.turnEverythingToOFF(partialShutdown= True)
        self.mainScr.allowUpdateGraph = False
        p = self.width()/1920
        self.screen1.setGeometry(int(self.p * 17), int(self.p * 336), int(self.p * 990), int(self.p * 511))
        if self.calibManual_isOn: 
            self.closeCalibManual()
            self.calibManual_isOn = False
        self.backgroundLabel5.setStyleSheet("""
            background-color: rgb(30, 30, 30);
            border-radius: 10px;
        """)

    #desativar a tela de trigger e impedir abrir fora ao sair de Main:
    if not self.screenName == "Main" and self.btTrigger.isOn == True:
        self.btTrigger.isOn = False
        self.btTrigger._update_visual()
        self.secondaryScreen.setCurrentIndex(0)
        self.triggerLabel.hide()
        self.triggerKnob.changeImage("images/Knob2.png")

    #desativar o botão do cursor se não estiver na aba Main, FFT ou Freq Resp:
    if self.btCursor.isOn == True and (self.screenName == "" or self.screenName == "Phas Diag" or self.screenName == "Help"):
        self.btCursor.isOn = False
        self.cursorKnob.changeImage("images/Knob2.png")
        self.btCursor._update_visual()
        self.secondaryScreen.setCurrentIndex(0)
        self.cursorProportionalLabel.hide()
        if self.cursorLinesOn == True: self.removeCursorLines()
        self.cursorKnob.buttonIsOn = False

    #Funções de interação com telas secundárias de duas abas:
    if self.screenName == "Main":
        if self.currentMainScr2_Scr == 1: self.secondaryScreen.setCurrentIndex(7)
        else:                           self.secondaryScreen.setCurrentIndex(8)

    if self.screenName == "FFT":
        self.secondaryScreen.setCurrentIndex(5)

    if self.screenName == "Phas Diag":
        self.secondaryScreen.setCurrentIndex(4)

    else:
        if not self.btMeas.isOn: self.phaseLabel.hide()

    if self.screenName == "Freq Resp":
        self.secondaryScreen.setCurrentIndex(9)

    if self.screenName == "Help":
        self.secondaryScreen.setCurrentIndex(0)




#Ajustes associados à subjanela secundária
def UpdateSecondaryButtons(self):
    if not self.secondaryScreenName == "Measure":
        self.btMeas.isOn = False
        self.btMeas._update_visual()
        self.mainScr.measureTime = False
        self.phaseLabel.hide()

    if not self.secondaryScreenName == "Cursor":
        self.btCursor.isOn = False
        self.btCursor._update_visual()
        self.cursorKnob.changeImage("images/Knob2.png")
        self.cursorProportionalLabel.hide()
        if self.cursorLinesOn == True: 
            self.removeCursorLines()
        self.cursorKnob.buttonIsOn = False

    

    if not self.secondaryScreenName == "Trigger":
        self.btTrigger.isOn = False
        self.btTrigger._update_visual()
        self.triggerKnob.changeImage("images/Knob2.png")
        self.mainScr.removeItem(self.graphicPlottingTrigger)
        self.triggerKnob.buttonIsOn = False
        self.triggerLabel.hide()
        self.triggerProportionLabel.hide()
    


    
#Usado para causar o desligamento de várias funções e/ou recuo de várias labels num único comando
def turnEverythingToOFF(self, partialShutdown):
    self.screenName = ""
    if self.btMain.isOn == True:
        self.btMain.isOn = False
        self.btMain._update_visual()
    if self.btFFT.isOn == True:
        self.btFFT.isOn = False
        self.btFFT._update_visual()
    if self.btFreqResp.isOn == True:
        self.btFreqResp.isOn = False
        self.btFreqResp._update_visual()
    if self.btPhasDiag.isOn == True:
        self.btPhasDiag.isOn = False
        self.btPhasDiag._update_visual()
    if self.btHelp.isOn == True:
        self.btHelp.isOn = False
        self.btHelp._update_visual()

    if self.btMeas.isOn == True:
        self.btMeas.isOn = False
        self.btMeas._update_visual()
    if self.btCursor.isOn == True:
        self.btCursor.isOn = False
        self.btCursor._update_visual()
    if self.btTrigger.isOn == True:
        self.btTrigger.isOn = False
        self.btTrigger._update_visual()
    if self.btFreeze.isOn == True:
        self.btFreeze.isOn = False
        self.btFreeze._update_visual()


    if partialShutdown == False: # partialShutdown = False indica que nem os botões dos canais devem sair ilesos
        if self.btCH1.isOn == True:
            self.btCH1.isOn = False
            self.btCH1._update_visual()
        if self.btCH2.isOn == True:
            self.btCH2.isOn = False
            self.btCH2._update_visual()
        
        if self.btMath.isOn == True:
            self.btMath.isOn = False
            self.btMath._update_visual()
    self.vdivCH1Knob.buttonIsOn = False
    self.vdivCH2Knob.buttonIsOn = False
    self.vdivMathKnob.buttonIsOn = False
    self.timeKnob.buttonIsOn = False
    self.triggerKnob.buttonIsOn = False

        
def resetSystem(self): #A função coloca os parâmetros dos elementos da interface nos valores-padrão (pensado caso o usuário queira reiniciar o osciloscópio mas não o programa)
    self.mainScr.triggerEdgeValue = 0
    self.mainScr.triggerUsefulEdgeValue = 0
    self.yTrigger = (np.ones_like(self.xTrigger) * 0.0)
    self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)
    self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")
    self.mainScr.removeItem(self.graphicPlottingTrigger)
    self.triggerKnob.usefulValue = 0

    self.X1Value = 0
    self.X2Value = 0.01
    self.Y1Value = -5
    self.Y2Value = 5

    self.y_X1 = np.arange(-6, 6)
    self.x_X1 = np.ones_like(self.y_X1) * self.X1Value
    self.X1LineStyle = mkPen(color="white", width=1.7)
    self.graphicPlottingX1Line = self.mainScr.plot(self.x_X1, self.y_X1, pen=self.X1LineStyle)

    self.y_X2 = np.arange(-6, 6)
    self.x_X2 = np.ones_like(self.y_X2) * self.X2Value
    self.X2LineStyle = mkPen(color="white", width=1.7)
    self.graphicPlottingX2Line = self.mainScr.plot(self.x_X2, self.y_X2, pen=self.X2LineStyle)

    self.x_Y1 = np.arange(-2, 2)
    self.y_Y1 = np.ones_like(self.x_Y1) * self.Y1Value
    self.Y1LineStyle = mkPen(color="white", width=1.7)
    self.graphicPlottingY1Line = self.mainScr.plot(self.x_Y1, self.y_Y1, pen=self.Y1LineStyle)

    self.x_Y2 = np.arange(-2, 2)
    self.y_Y2 = np.ones_like(self.x_Y2) * self.Y2Value
    self.Y2LineStyle = mkPen(color="white", width=1.7)
    self.graphicPlottingY2Line = self.mainScr.plot(self.x_Y2, self.y_Y2, pen=self.Y2LineStyle)

    self.cursor.cursorX1LE.setText(f"{self.X1Value * 1000:.2f}")
    self.cursor.cursorX2LE.setText(f"{self.X2Value * 1000:.2f}")
    self.cursor.cursorY1LE.setText(f"{self.Y1Value:.2f}")
    self.cursor.cursorY2LE.setText(f"{self.Y2Value:.2f}")
    self.cursor.cursorDeltaX_LE.setText(f"{((self.X2Value - self.X1Value) * 1000):.2f}")
    self.cursor.cursorDeltaY_LE.setText(f"{(self.Y2Value - self.Y1Value):.2f}")
    self.cursor.cursorSelectCB.setCurrentIndex(0)
    self.removeCursorLines()

    self.timeKnob.usefulValue = 0
    self.timeKnob.scaleValue = 1
    self.UpdateTimeScale(0)
    self.mainScr.timeScale = self.timeKnob.scaleValue
    self.timeLabel.setText(f"Time: {self.mainScr.timeScale:.0f} ms/div")


    

    self.posCH1Knob.usefulValue = 0
    self.UpdatePositionCH1()
    self.posCH2Knob.usefulValue = 0
    self.UpdatePositionCH2()
    self.posMathKnob.usefulValue = 0
    self.UpdatePositionMath()

    self.WFMgeneratorScr.signalTypeCB.setCurrentIndex(0)
    self.WFMgeneratorScr.amplitLE.setText("100")
    self.WFMgeneratorScr.amplitLE.returnPressed.emit()
    self.WFMgeneratorScr.freq_SpinBox.lineEdit().setText("500")
    self.helpScr.HelpPagesStack.setCurrentIndex(0)
    self.helpScr.sectionCB.setCurrentIndex(0)
    self.helpScr.instrument_spin.spin.setValue(1)