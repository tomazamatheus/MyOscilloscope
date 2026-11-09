import numpy as np
from pyqtgraph import mkPen
from PySide6.QtCore import Qt

#Métodos de Cursor
def CursorActivated(self):
    if (self.btOnOff.isOn == True and self.btCursor.isOn == True
            and not self.screenName == "" and not self.screenName == "Phas Diag"):
        self.secondaryScreenName = "Cursor"
        if self.screenName == "Main": 
            self.secondaryScreen.setCurrentIndex(3)
            
        elif self.screenName == "FFT": 
            self.secondaryScreen.setCurrentIndex(6)

        elif self.screenName == "Freq Resp":
            if self.freqResp_scr2.freqResp_page2.y_AxisCB.currentIndex() == 0:
                self.secondaryScreen.setCurrentIndex(10)
            else:
                self.secondaryScreen.setCurrentIndex(11)
            
        self.cursorKnob.changeImage("images/Knob2_OrangeSimple.png")

        #plotting na tela Main:
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

        
        #FFT
        self.y_X1_FFT = np.arange(-100, 100)
        self.x_X1_FFT = np.ones_like(self.y_X1_FFT) * self.X1ValueFFT
        self.X1LineStyle_FFT = mkPen(color="white", width=2)
        self.graphicPlottingX1Line_FFT = self.FFTScr.plot(self.x_X1_FFT, self.y_X1_FFT, pen=self.X1LineStyle_FFT)

        self.y_X2_FFT = np.arange(-100, 100)
        self.x_X2_FFT = np.ones_like(self.y_X2_FFT) * self.X2ValueFFT
        self.X2LineStyle_FFT = mkPen(color="white", width=2)
        self.graphicPlottingX2Line_FFT = self.FFTScr.plot(self.x_X2_FFT, self.y_X2_FFT, pen=self.X2LineStyle_FFT)

        self.x_Y1_FFT = np.arange(1, 100000, 50000)
        self.y_Y1_FFT = np.ones_like(self.x_Y1_FFT) * self.Y1ValueFFT
        self.Y1LineStyle_FFT = mkPen(color="white", width=2)
        self.graphicPlottingY1Line_FFT = self.FFTScr.plot(self.x_Y1_FFT, self.y_Y1_FFT, pen=self.Y1LineStyle_FFT)

        self.x_Y2_FFT = np.arange(1, 100000, 50000)
        self.y_Y2_FFT = np.ones_like(self.x_Y2_FFT) * self.Y2ValueFFT
        self.Y2LineStyle_FFT = mkPen(color="white", width=2)
        self.graphicPlottingY2Line_FFT = self.FFTScr.plot(self.x_Y2_FFT, self.y_Y2_FFT, pen=self.Y2LineStyle_FFT)

        #Freq Resp Magnitude
        self.y_X1_FreqResp_Magn = np.arange(-100, 100)
        self.x_X1_FreqResp_Magn = np.ones_like(self.y_X1_FreqResp_Magn) * self.X1ValueFreqResp_Magn
        self.X1LineStyle_FreqResp_Magn = mkPen(color="yellow", width=1.6)
        self.graphicPlottingX1Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_X1_FreqResp_Magn, self.y_X1_FreqResp_Magn, pen=self.X1LineStyle_FreqResp_Magn)

        self.y_X2_FreqResp_Magn = np.arange(-100, 100)
        self.x_X2_FreqResp_Magn = np.ones_like(self.y_X2_FreqResp_Magn) * self.X2ValueFreqResp_Magn
        self.X2LineStyle_FreqResp_Magn = mkPen(color="yellow", width=1.6)
        self.graphicPlottingX2Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_X2_FreqResp_Magn, self.y_X2_FreqResp_Magn, pen=self.X2LineStyle_FreqResp_Magn)

        self.x_Y1_FreqResp_Magn = np.arange(1, 100000, 50000)
        self.y_Y1_FreqResp_Magn = np.ones_like(self.x_Y1_FreqResp_Magn) * self.Y1ValueFreqResp_Magn
        self.Y1LineStyle_FreqResp_Magn = mkPen(color="yellow", width=1.6)
        self.graphicPlottingY1Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_Y1_FreqResp_Magn, self.y_Y1_FreqResp_Magn, pen=self.Y1LineStyle_FreqResp_Magn)

        self.x_Y2_FreqResp_Magn = np.arange(1, 100000, 50000)
        self.y_Y2_FreqResp_Magn = np.ones_like(self.x_Y2_FreqResp_Magn) * self.Y2ValueFreqResp_Magn
        self.Y2LineStyle_FreqResp_Magn = mkPen(color="yellow", width=1.6)
        self.graphicPlottingY2Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_Y2_FreqResp_Magn, self.y_Y2_FreqResp_Magn, pen=self.Y2LineStyle_FreqResp_Magn)

        #Freq Resp Phase
        self.y_X1_FreqResp_Phase = np.arange(-300, 300)
        self.x_X1_FreqResp_Phase = np.ones_like(self.y_X1_FreqResp_Phase) * self.X1ValueFreqResp_Phase
        self.X1LineStyle_FreqResp_Phase = mkPen(color="cyan", width=1.6)
        self.graphicPlottingX1Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_X1_FreqResp_Phase, self.y_X1_FreqResp_Phase, pen=self.X1LineStyle_FreqResp_Phase)

        self.y_X2_FreqResp_Phase = np.arange(-300, 300)
        self.x_X2_FreqResp_Phase = np.ones_like(self.y_X2_FreqResp_Phase) * self.X2ValueFreqResp_Phase
        self.X2LineStyle_FreqResp_Phase = mkPen(color="cyan", width=1.6)
        self.graphicPlottingX2Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_X2_FreqResp_Phase, self.y_X2_FreqResp_Phase, pen=self.X2LineStyle_FreqResp_Phase)

        self.x_Y1_FreqResp_Phase = np.arange(1, 100000, 50000)
        self.y_Y1_FreqResp_Phase = np.ones_like(self.x_Y1_FreqResp_Phase) * self.Y1ValueFreqResp_Phase
        self.Y1LineStyle_FreqResp_Phase = mkPen(color="cyan", width=1.6)
        self.graphicPlottingY1Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_Y1_FreqResp_Phase, self.y_Y1_FreqResp_Phase, pen=self.Y1LineStyle_FreqResp_Phase)

        self.x_Y2_FreqResp_Phase = np.arange(1, 100000, 50000)
        self.y_Y2_FreqResp_Phase = np.ones_like(self.x_Y2_FreqResp_Phase) * self.Y2ValueFreqResp_Phase
        self.Y2LineStyle_FreqResp_Phase = mkPen(color="cyan", width=1.6)
        self.graphicPlottingY2Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_Y2_FreqResp_Phase, self.y_Y2_FreqResp_Phase, pen=self.Y2LineStyle_FreqResp_Phase)

        self.cursorKnob.buttonIsOn = True
        if self.screenName == "Main":
            if(self.mainScr.referencePhase == "CH1"):
                self.cursorProportionalLabel.show()
                if self.language == "English":
                    if not self.currentForCH1Scale:
                        self.cursorProportionalLabel.setText("Lines Y1 and Y2 are adjusted to \nCH1 V/div scale")
                    else:
                        self.cursorProportionalLabel.setText("Lines Y1 and Y2 are adjusted to \nCH1 A/div scale")
                else:
                    if not self.currentForCH1Scale:
                        self.cursorProportionalLabel.setText("Linhas Y1 e Y2 ajustadas à\nescala de V/div do CH1")
                    else:
                        self.cursorProportionalLabel.setText("Linhas Y1 e Y2 ajustadas à\nescala de A/div do CH1")

                    
            elif(self.mainScr.referencePhase == "CH2"):
                self.cursorProportionalLabel.show()
                if self.language == "English":
                    if not self.currentForCH2Scale:
                        self.cursorProportionalLabel.setText("Lines Y1 and Y2 are adjusted to \nCH2 V/div scale")
                    else:
                        self.cursorProportionalLabel.setText("Lines Y1 and Y2 are adjusted to \nCH2 A/div scale")
                else:
                    if not self.currentForCH2Scale:
                        self.cursorProportionalLabel.setText("Linhas Y1 e Y2 ajustadas à\nescala de V/div do CH2")
                    else:
                        self.cursorProportionalLabel.setText("Linhas Y1 e Y2 ajustadas à\nescala de A/div do CH2")

                    
            elif (self.mainScr.referencePhase == "Math"):
                self.cursorProportionalLabel.show()
                if self.language == "English":
                    if not self.currentForMathScale:
                        self.cursorProportionalLabel.setText("Lines Y1 and Y2 are adjusted to \nMath V/div scale")
                    else:
                        self.cursorProportionalLabel.setText("Lines Y1 and Y2 are adjusted to \nMath A/div scale")
                else:
                    if not self.currentForMathScale:
                        self.cursorProportionalLabel.setText("Linhas Y1 e Y2 ajustadas à\nescala de V/div do Math")
                    else:
                        self.cursorProportionalLabel.setText("Linhas Y1 e Y2 ajustadas à\nescala de A/div do Math")
            
        self.cursorLinesOn = True

        if self.screenName == "FFT":
            self.cursorFFTLabel.show()
            self.cursorFFTLabel.setStyleSheet( """ color: white; 
                                        background-color: transparent""")
            self.cursorLinesFFT = True   
        elif self.screenName == "Freq Resp":
            if self.freqResp_scr2.freqResp_page2.y_AxisCB.currentText() == "Magnitude":
                self.cursorFFTLabel.show()
                self.cursorFFTLabel.setStyleSheet( """ color: yellow; 
                                        background-color: transparent""")
            else: #Phase
                self.cursorFFTLabel.show()
                self.cursorFFTLabel.setStyleSheet( """ color: cyan; 
                                        background-color: transparent""")

    else:
        self.btCursor._update_visual()
        if self.cursorLinesOn == True: self.removeCursorLines()
        self.cursorKnob.buttonIsOn = False

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
            self.cursorFFTLabel.hide()
            
        else: self.secondaryScreen.setCurrentIndex(0)

        self.cursorLinesFFT = False
        self.cursorProportionalLabel.hide()
        
        self.cursorKnob.changeImage("images/Knob2.png")
        self.cursorKnob.buttonIsOn = False
    self.UpdateSecondaryButtons()

#Funções para o Cursor de Main:
def CursorSelectCBChanged(self):
    if self.cursor.cursorSelectCB.currentText() == "X1":
        self.cursorKnobLineAssigned_FFT = "X1"
    elif self.cursor.cursorSelectCB.currentText() == "X2":
        self.cursorKnobLineAssigned_FFT = "X2"
    elif self.cursor.cursorSelectCB.currentText() == "Y1":
        self.cursorKnobLineAssigned_FFT = "Y1"
    elif self.cursor.cursorSelectCB.currentText() == "Y2":
        self.cursorKnobLineAssigned_FFT = "Y2"

def Cursor_X1_LEChanged(self):

    text = self.cursor.cursorX1LE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = float(text)
        if value > 10 * self.mainScr.timeScale:

            self.cursor.cursorX1LE.setText(f"{10 * self.mainScr.timeScale:.2f}")
            self.X1Value = 0.01 * self.mainScr.timeScale
        elif value >= 0:
            self.X1Value = value / 1000 * self.mainScr.timeScale
            self.cursor.cursorX1LE.setText(f"{value:.2f}")
        else:
            self.cursor.cursorX1LE.setText("0.00")
            self.X1Value = 0.00

        self.x_X1 = np.ones_like(self.y_X1) * self.X1Value / self.mainScr.timeScale
        self.mainScr.removeItem(self.graphicPlottingX1Line)
        self.graphicPlottingX1Line = self.mainScr.plot(self.x_X1, self.y_X1, pen=self.X1LineStyle)
    except ValueError:
        self.cursor.cursorX1LE.setText(f"{self.X1Value * 1000:.2f}")
    self.UpdateCursorDeltaX()

def Cursor_X2_LEChanged(self):
    text = self.cursor.cursorX2LE.text()

    try:
        value = float(text)

        if value > 10 * self.mainScr.timeScale:
            self.cursor.cursorX2LE.setText(f"{10 * self.mainScr.timeScale:.2f}")
            self.X2Value = 0.01 * self.mainScr.timeScale
        elif value >= 0:
            self.X2Value = value / 1000 * self.mainScr.timeScale
            self.cursor.cursorX2LE.setText(f"{value:.2f}")
        else:
            self.cursor.cursorX2LE.setText("0.00")
            self.X2Value = 0.00

        self.x_X2 = np.ones_like(self.y_X2) * self.X2Value / self.mainScr.timeScale
        self.mainScr.removeItem(self.graphicPlottingX2Line)
        self.graphicPlottingX2Line = self.mainScr.plot(self.x_X2, self.y_X2, pen=self.X2LineStyle)
    except ValueError:
        self.cursor.cursorX2LE.setText(f"{self.X2Value * 1000:.2f}")
    self.UpdateCursorDeltaX()

def Cursor_Y1_LEChanged(self):
    text = self.cursor.cursorY1LE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = float(text)
        if self.mainScr.referencePhase == "CH1":
            if (value > 5 * self.mainScr.vdivCH1Scale and not self.currentForCH1Scale) or \
                (value > 50000 * self.mainScr.vdivCH1Scale/self.shuntRes_CH1 and self.currentForCH1Scale):
                self.cursor.cursorY1LE.setText(f"{(5 * self.mainScr.vdivCH1Scale):.2f}")
                self.Y1Value = 5
            elif (value > -5 * self.mainScr.vdivCH1Scale and not self.currentForCH1Scale) or \
                (value > -50000 * self.mainScr.vdivCH1Scale/self.shuntRes_CH1 and self.currentForCH1Scale):
                self.cursor.cursorY1LE.setText(f"{value:.2f}")
                
                if not self.currentForCH1Scale: self.Y1Value = value
                else: self.Y1Value = value/1000 * self.shuntRes_CH1 #valor recebido em corrente (mA), mas o sistema trabalha com tensão
            else:
                self.cursor.cursorY1LE.setText(f"{(-5 * self.mainScr.vdivCH1Scale):.2f}")
                self.Y1Value = -5
        elif self.mainScr.referencePhase == "CH2":
            if (value > 5 * self.mainScr.vdivCH2Scale and not self.currentForCH2Scale) or \
                (value > 50000 * self.mainScr.vdivCH2Scale/self.shuntRes_CH2 and self.currentForCH2Scale):
                self.cursor.cursorY1LE.setText(f"{(5 * self.mainScr.vdivCH2Scale):.2f}")
                self.Y1Value = 5
            elif (value > 5 * self.mainScr.vdivCH2Scale and not self.currentForCH2Scale) or \
                (value > 50000 * self.mainScr.vdivCH2Scale/self.shuntRes_CH2 and self.currentForCH2Scale):
                self.cursor.cursorY1LE.setText(f"{value:.2f}")
                if not self.currentForCH2Scale: self.Y1Value = value
                else: self.Y1Value = value/1000 * self.shuntRes_CH2 #valor recebido em corrente (mA), mas o sistema trabalha com tensão
            else:
                self.cursor.cursorY1LE.setText(f"{(-5 * self.mainScr.vdivCH2Scale):.2f}")
                self.Y1Value = -5
        else:
            if (value > 5 * self.mainScr.vdivMathScale and not self.currentForMathScale) or \
                (value > 50000 * self.mainScr.vdivMathScale/self.shuntRes_Math and self.currentForMathScale):
                    self.cursor.cursorY1LE.setText(f"{(5 * self.mainScr.vdivMathScale):.2f}")
                    self.Y1Value = 5
            elif (value > -5 * self.mainScr.vdivMathScale and not self.currentForMathScale) or \
                (value > -50000 * self.mainScr.vdivMathScale/self.shuntRes_Math and self.currentForMathScale):
                self.cursor.cursorY1LE.setText(f"{value:.2f}")

                if not self.currentForMathScale: self.Y1Value = value
                else: self.Y1Value = value/1000 * self.shuntRes_Math #valor recebido em corrente (mA), mas o sistema trabalha com tensão
            else:
                self.cursor.cursorY1LE.setText(f"{(-5 * self.mainScr.vdivCH2Scale):.2f}")
                self.Y1Value = -5

        if (self.mainScr.referencePhase == "CH1"):
            self.y_Y1 = np.ones_like(self.x_Y1) * self.Y1Value / self.mainScr.vdivCH1Scale
        elif (self.mainScr.referencePhase == "CH2"):
            self.y_Y1 = np.ones_like(self.x_Y1) * self.Y1Value / self.mainScr.vdivCH2Scale
        else:
            self.y_Y1 = np.ones_like(self.x_Y1) * self.Y1Value / self.mainScr.vdivMathScale
        self.mainScr.removeItem(self.graphicPlottingY1Line)
        self.graphicPlottingY1Line = self.mainScr.plot(self.x_Y1, self.y_Y1, pen=self.Y1LineStyle)
    except ValueError:
        self.cursor.cursorY1LE.setText(f"{self.Y1Value:.2f}")
    self.UpdateCursorDeltaY()

def Cursor_Y2_LEChanged(self):
    text = self.cursor.cursorY2LE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = float(text)
        if self.mainScr.referencePhase == "CH1":
            if (value > 5 * self.mainScr.vdivCH1Scale and not self.currentForCH1Scale) or \
                (value > 50000 * self.mainScr.vdivCH1Scale/self.shuntRes_CH1 and self.currentForCH1Scale):
                self.cursor.cursorY2LE.setText(f"{(5 * self.mainScr.vdivCH1Scale):.2f}")
                self.Y2Value = 5
            elif (value > -5 * self.mainScr.vdivCH1Scale and not self.currentForCH1Scale) or \
                (value > -50000 * self.mainScr.vdivCH1Scale/self.shuntRes_CH1 and self.currentForCH1Scale):
                self.cursor.cursorY2LE.setText(f"{value:.2f}")
                
                if not self.currentForCH1Scale: self.Y2Value = value
                else: self.Y2Value = value/1000 * self.shuntRes_CH1 #valor recebido em corrente (mA), mas o sistema trabalha com tensão
            else:
                self.cursor.cursorY2LE.setText(f"{(-5 * self.mainScr.vdivCH1Scale):.2f}")
                self.Y2Value = -5
        elif self.mainScr.referencePhase == "CH2":
            if (value > 5 * self.mainScr.vdivCH2Scale and not self.currentForCH2Scale) or \
                (value > 50000 * self.mainScr.vdivCH2Scale/self.shuntRes_CH2 and self.currentForCH2Scale):
                self.cursor.cursorY2LE.setText(f"{(5 * self.mainScr.vdivCH2Scale):.2f}")
                self.Y2Value = 5
            elif (value > 5 * self.mainScr.vdivCH2Scale and not self.currentForCH2Scale) or \
                (value > 50000 * self.mainScr.vdivCH2Scale/self.shuntRes_CH2 and self.currentForCH2Scale):
                self.cursor.cursorY2LE.setText(f"{value:.2f}")
                if not self.currentForCH2Scale: self.Y2Value = value
                else: self.Y2Value = value/1000 * self.shuntRes_CH2 #valor recebido em corrente (mA), mas o sistema trabalha com tensão
            else:
                self.cursor.cursorY2LE.setText(f"{(-5 * self.mainScr.vdivCH2Scale):.2f}")
                self.Y2Value = -5
        else:
            if (value > 5 * self.mainScr.vdivMathScale and not self.currentForMathScale) or \
                (value > 50000 * self.mainScr.vdivMathScale/self.shuntRes_Math and self.currentForMathScale):
                    self.cursor.cursorY2LE.setText(f"{(5 * self.mainScr.vdivMathScale):.2f}")
                    self.Y2Value = 5
            elif (value > -5 * self.mainScr.vdivMathScale and not self.currentForMathScale) or \
                (value > -50000 * self.mainScr.vdivMathScale/self.shuntRes_Math and self.currentForMathScale):
                self.cursor.cursorY2LE.setText(f"{value:.2f}")

                if not self.currentForMathScale: self.Y2Value = value
                else: self.Y2Value = value/1000 * self.shuntRes_Math #valor recebido em corrente (mA), mas o sistema trabalha com tensão
            else:
                self.cursor.cursorY2LE.setText(f"{(-5 * self.mainScr.vdivCH2Scale):.2f}")
                self.Y2Value = -5

        if (self.mainScr.referencePhase == "CH1"):
            self.y_Y2 = np.ones_like(self.x_Y2) * self.Y2Value / self.mainScr.vdivCH1Scale
        elif (self.mainScr.referencePhase == "CH2"):
            self.y_Y2 = np.ones_like(self.x_Y2) * self.Y2Value / self.mainScr.vdivCH2Scale
        else:
            self.y_Y2 = np.ones_like(self.x_Y2) * self.Y2Value / self.mainScr.vdivMathScale
        self.mainScr.removeItem(self.graphicPlottingY2Line)
        self.graphicPlottingY2Line = self.mainScr.plot(self.x_Y2, self.y_Y2, pen=self.Y2LineStyle)
    except ValueError:
        self.cursor.cursorY2LE.setText(f"{self.Y2Value:.2f}")
    self.UpdateCursorDeltaY()

def UpdateCursorDeltaX(self):
    self.cursor.cursorDeltaX_LE.setText(f"{((self.X2Value - self.X1Value) * 1000):.2f}")

def UpdateCursorDeltaY(self):
    if self.mainScr.referencePhase == "CH1":
        if not self.currentForCH1Scale: 
            self.cursor.cursorDeltaY_LE.setText(f"{(self.Y2Value - self.Y1Value):.2f}")
        else:
            self.cursor.cursorDeltaY_LE.setText(f"{((self.Y2Value - self.Y1Value) * 1e3/self.shuntRes_CH1):.2f}")

    elif self.mainScr.referencePhase == "CH2":
        if not self.currentForCH2Scale: 
            self.cursor.cursorDeltaY_LE.setText(f"{(self.Y2Value - self.Y1Value):.2f}")
        else:
            self.cursor.cursorDeltaY_LE.setText(f"{((self.Y2Value - self.Y1Value) * 1e3/self.shuntRes_CH2):.2f}")

    else:
        if not self.currentForMathScale: 
            self.cursor.cursorDeltaY_LE.setText(f"{(self.Y2Value - self.Y1Value):.2f}")
        else:
            self.cursor.cursorDeltaY_LE.setText(f"{((self.Y2Value - self.Y1Value) * 1e3/self.shuntRes_Math):.2f}")


def CursorKnob(self):
    if self.screenName == "Main":
        if self.cursorKnob.buttonIsOn == True:
            if self.cursorKnobLineAssigned_FFT == "X1":
                if self.cursorKnob.levelUp == True:
                    if (self.X1Value < 0.5):
                        self.X1Value += 0.00001
                    self.cursor.cursorX1LE.setText(f"{(self.X1Value * 1000 / self.mainScr.timeScale):.2f}")
                    self.cursorKnob.levelUp = False
                if self.cursorKnob.levelDown == True:
                    if (self.X1Value > 0): self.X1Value -= 0.00001
                    self.cursor.cursorX1LE.setText(f"{(self.X1Value * 1000 / self.mainScr.timeScale):.2f}")
                    self.cursorKnob.levelDown = False
                self.x_X1 = np.ones_like(self.y_X1) * self.X1Value / self.mainScr.timeScale
                self.mainScr.removeItem(self.graphicPlottingX1Line)
                self.graphicPlottingX1Line = self.mainScr.plot(self.x_X1, self.y_X1, pen=self.X1LineStyle)
                self.UpdateCursorDeltaX()

            elif self.cursorKnobLineAssigned_FFT == "X2":
                if self.cursorKnob.levelUp == True:

                    if (self.X2Value < 0.5): self.X2Value += 0.00001
                    self.cursor.cursorX2LE.setText(f"{(self.X2Value * 1000 / self.mainScr.timeScale):.2f}")
                    self.cursorKnob.levelUp = False
                if self.cursorKnob.levelDown == True:
                    if (self.X2Value > 0): self.X2Value -= 0.00001
                    self.cursor.cursorX2LE.setText(f"{(self.X2Value * 1000 / self.mainScr.timeScale):.2f}")
                    self.cursorKnob.levelDown = False
                self.x_X2 = np.ones_like(self.y_X2) * self.X2Value / self.mainScr.timeScale
                self.mainScr.removeItem(self.graphicPlottingX2Line)
                self.graphicPlottingX2Line = self.mainScr.plot(self.x_X2, self.y_X2, pen=self.X2LineStyle)
                self.UpdateCursorDeltaX()

            elif self.cursorKnobLineAssigned_FFT == "Y1":
                if self.cursorKnob.levelUp == True:
                    if (self.Y1Value < 5): 
                        self.Y1Value += 0.01
                        self.cursorKnob.levelUp = False
            
                if self.cursorKnob.levelDown == True:
                    if (self.Y1Value > -5): 
                        self.Y1Value -= 0.01
                        self.cursorKnob.levelDown = False

                if (self.mainScr.referencePhase == "CH1"):
                    if not self.currentForCH1Scale: 
                        self.cursor.cursorY1LE.setText(f"{(self.Y1Value * self.mainScr.vdivCH1Scale):.2f}")
                    else:
                        self.cursor.cursorY1LE.setText(f"{((self.Y1Value * self.mainScr.vdivCH1Scale) * 1000/self.shuntRes_CH1):.2f}")
                elif (self.mainScr.referencePhase == "CH2"):
                    if not self.currentForCH2Scale: 
                        self.cursor.cursorY1LE.setText(f"{(self.Y1Value * self.mainScr.vdivCH2Scale):.2f}")
                    else:
                        self.cursor.cursorY1LE.setText(f"{((self.Y1Value * self.mainScr.vdivCH2Scale) * 1000/self.shuntRes_CH2):.2f}")
                elif (self.mainScr.referencePhase == "Math"):
                    if not self.currentForMathScale: 
                        self.cursor.cursorY1LE.setText(f"{(self.Y1Value * self.mainScr.vdivMathScale):.2f}")
                    else:
                        self.cursor.cursorY1LE.setText(f"{((self.Y1Value * self.mainScr.vdivMathScale) * 1000/self.shuntRes_Math):.2f}")
                    
                self.y_Y1 = np.ones_like(self.x_Y1) * self.Y1Value
                self.mainScr.removeItem(self.graphicPlottingY1Line)
                self.graphicPlottingY1Line = self.mainScr.plot(self.x_Y1, self.y_Y1, pen=self.Y1LineStyle)
                self.UpdateCursorDeltaY()

            elif self.cursorKnobLineAssigned_FFT == "Y2":
                if self.cursorKnob.levelUp == True:
                    if (self.Y2Value < 5): 
                        self.Y2Value += 0.01
                        self.cursorKnob.levelUp = False
            
                if self.cursorKnob.levelDown == True:
                    if (self.Y2Value > -5): 
                        self.Y2Value -= 0.01
                        self.cursorKnob.levelDown = False

                if (self.mainScr.referencePhase == "CH1"):
                    if not self.currentForCH1Scale: 
                        self.cursor.cursorY2LE.setText(f"{(self.Y2Value * self.mainScr.vdivCH1Scale):.2f}")
                    else:
                        self.cursor.cursorY2LE.setText(f"{((self.Y2Value * self.mainScr.vdivCH1Scale) * 1000/self.shuntRes_CH1):.2f}")
                elif (self.mainScr.referencePhase == "CH2"):
                    if not self.currentForCH2Scale: 
                        self.cursor.cursorY2LE.setText(f"{(self.Y2Value * self.mainScr.vdivCH2Scale):.2f}")
                    else:
                        self.cursor.cursorY2LE.setText(f"{((self.Y2Value * self.mainScr.vdivCH2Scale) * 1000/self.shuntRes_CH2):.2f}")
                elif (self.mainScr.referencePhase == "Math"):
                    if not self.currentForMathScale: 
                        self.cursor.cursorY2LE.setText(f"{(self.Y2Value * self.mainScr.vdivMathScale):.2f}")
                    else:
                        self.cursor.cursorY2LE.setText(f"{((self.Y2Value * self.mainScr.vdivMathScale) * 1000/self.shuntRes_Math):.2f}")

                self.y_Y2 = np.ones_like(self.x_Y2) * self.Y2Value
                self.mainScr.removeItem(self.graphicPlottingY2Line)
                self.graphicPlottingY2Line = self.mainScr.plot(self.x_Y2, self.y_Y2, pen=self.Y2LineStyle)
                self.UpdateCursorDeltaY()

#Funções para o Cursor de FFT:
def CursorSelectCBChanged_FFT(self):
    if self.cursorFFT.cursorSelectCB.currentText() == "X1":
        self.cursorKnobLineAssigned_FFT = "X1"
    elif self.cursorFFT.cursorSelectCB.currentText() == "X2":
        self.cursorKnobLineAssigned_FFT = "X2"
    elif self.cursorFFT.cursorSelectCB.currentText() == "Y1":
        self.cursorKnobLineAssigned_FFT = "Y1"
    elif self.cursorFFT.cursorSelectCB.currentText() == "Y2":
        self.cursorKnobLineAssigned_FFT = "Y2"

def Cursor_X1_LEChanged_FFT(self):
    text = self.cursorFFT.cursorX1LE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = float(text)
        if value > 100000:
            self.cursorFFT.cursorX1LE.setText("100000.0")
            self.X1ValueFFT = 100000
        elif value >= 10:
            self.X1ValueFFT = value 
            self.cursorFFT.cursorX1LE.setText(f"{value:.1f}")
        else:
            self.cursorFFT.cursorX1LE.setText("10.0")
            self.X1ValueFFT = 10

        self.x_X1_FFT = np.ones_like(self.y_X1_FFT) * self.X1ValueFFT 
        self.FFTScr.removeItem(self.graphicPlottingX1Line_FFT)
        self.graphicPlottingX1Line_FFT = self.FFTScr.plot(self.x_X1_FFT, self.y_X1_FFT, pen=self.X1LineStyle_FFT)
    except ValueError:
        self.cursorFFT.cursorX1LE.setText(f"{self.X1ValueFFT:.1f}")
    self.UpdateCursorDeltaX_FFT()

def Cursor_X2_LEChanged_FFT(self):
    text = self.cursorFFT.cursorX2LE.text()

    try:
        value = float(text)

        if value > 100000:
            self.cursorFFT.cursorX2LE.setText("100000.0")
            self.X2ValueFFT = 100000
        elif value >= 10:
            self.X2ValueFFT = value 
            self.cursorFFT.cursorX2LE.setText(f"{value:.1f}")
        else:
            self.cursorFFT.cursorX2LE.setText("10.0")
            self.X2ValueFFT = 1.00

        self.x_X2_FFT = np.ones_like(self.y_X2_FFT) * self.X2ValueFFT
        self.FFTScr.removeItem(self.graphicPlottingX2Line_FFT)
        self.graphicPlottingX2Line_FFT = self.FFTScr.plot(self.x_X2_FFT, self.y_X2_FFT, pen=self.X2LineStyle_FFT)
    except ValueError:
        self.cursorFFT.cursorX2LE.setText(f"{self.X2ValueFFT:.1f}")
    self.UpdateCursorDeltaX_FFT()

def Cursor_Y1_LEChanged_FFT(self):
    text = self.cursorFFT.cursorY1LE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = float(text)
        if value > 100:
            self.cursorFFT.cursorY1LE.setText("100.0")
            self.Y1ValueFFT = 100
        elif value > -100:
            self.Y1ValueFFT = value
            self.cursorFFT.cursorY1LE.setText(f"{value:.1f}")
        else:
            self.cursorFFT.cursorY1LE.setText("-100.0")
            self.Y1ValueFFT = -100
        
        self.y_Y1_FFT = np.ones_like(self.x_Y1_FFT) * self.Y1ValueFFT 
        
        self.FFTScr.removeItem(self.graphicPlottingY1Line_FFT)
        self.graphicPlottingY1Line_FFT = self.FFTScr.plot(self.x_Y1_FFT, self.y_Y1_FFT, pen=self.Y1LineStyle_FFT)
    except ValueError:
        self.cursorFFT.cursorY1LE.setText(f"{self.Y1ValueFFT:.1f}")
    self.UpdateCursorDeltaY_FFT()

def Cursor_Y2_LEChanged_FFT(self):
    text = self.cursorFFT.cursorY2LE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = float(text)
        if value > 100:
            self.cursorFFT.cursorY2LE.setText("100.0")
            self.Y2ValueFFT = 100
        elif value > -100:
            self.Y2ValueFFT = value
            self.cursorFFT.cursorY2LE.setText(f"{value:.1f}")
        else:
            self.cursorFFT.cursorY2LE.setText("100.0")
            self.Y2ValueFFT = -100

        self.y_Y2_FFT = np.ones_like(self.x_Y2_FFT) * self.Y2ValueFFT
        
        self.FFTScr.removeItem(self.graphicPlottingY2Line_FFT)
        self.graphicPlottingY2Line_FFT = self.FFTScr.plot(self.x_Y2_FFT, self.y_Y2_FFT, pen=self.Y2LineStyle_FFT)
    except ValueError:
        self.cursorFFT.cursorY2LE.setText(f"{self.Y2ValueFFT:.1f}")
    self.UpdateCursorDeltaY_FFT()

def UpdateCursorDeltaX_FFT(self):
    self.cursorFFT.cursorDeltaX_LE.setText(f"{(self.X2ValueFFT - self.X1ValueFFT):.1f}")

def UpdateCursorDeltaY_FFT(self):
    self.cursorFFT.cursorDeltaY_LE.setText(f"{(self.Y2ValueFFT - self.Y1ValueFFT):.1f}")

def CursorKnob_FFT(self):
    if self.screenName == "FFT":
        if self.cursorKnob.buttonIsOn == True:
            if self.cursorKnobLineAssigned_FFT == "X1":
                if self.cursorKnob.levelUp == True:
                    if (self.X1ValueFFT < 100000):
                        self.X1ValueFFT += 10
                    self.cursorFFT.cursorX1LE.setText(f"{(self.X1ValueFFT):.1f}")
                    self.cursorKnob.levelUp = False

                
                if self.cursorKnob.levelDown == True:
                    if (self.X1ValueFFT > 10): self.X1ValueFFT -= 10
                    self.cursorFFT.cursorX1LE.setText(f"{(self.X1ValueFFT):.1f}")
                    self.cursorKnob.levelDown = False
                self.x_X1_FFT = np.ones_like(self.y_X1_FFT) * self.X1ValueFFT
                self.FFTScr.removeItem(self.graphicPlottingX1Line_FFT)
                self.graphicPlottingX1Line_FFT = self.FFTScr.plot(self.x_X1_FFT, self.y_X1_FFT, pen=self.X1LineStyle_FFT)
                self.UpdateCursorDeltaX_FFT()

            elif self.cursorKnobLineAssigned_FFT == "X2":
                if self.cursorKnob.levelUp == True:
                    if (self.X2ValueFFT < 100000): self.X2ValueFFT += 10
                    self.cursorFFT.cursorX2LE.setText(f"{(self.X2ValueFFT):.1f}")
                    self.cursorKnob.levelUp = False
                if self.cursorKnob.levelDown == True:
                    if (self.X2ValueFFT > 10): self.X2ValueFFT -= 10
                    self.cursorFFT.cursorX2LE.setText(f"{(self.X2ValueFFT):.1f}")
                    self.cursorKnob.levelDown = False
                self.x_X2_FFT = np.ones_like(self.y_X2_FFT) * self.X2ValueFFT
                self.FFTScr.removeItem(self.graphicPlottingX2Line_FFT)
                self.graphicPlottingX2Line_FFT = self.FFTScr.plot(self.x_X2_FFT, self.y_X2_FFT, pen=self.X2LineStyle_FFT)
                self.UpdateCursorDeltaX_FFT()

            elif self.cursorKnobLineAssigned_FFT == "Y1":
                if self.cursorKnob.levelUp == True:
                    if (self.Y1ValueFFT < 100): self.Y1ValueFFT += 1
                    self.cursorFFT.cursorY1LE.setText(f"{(self.Y1ValueFFT):.1f}")
                    self.cursorKnob.levelUp = False
                if self.cursorKnob.levelDown == True:
                    if (self.Y1ValueFFT > -100): self.Y1ValueFFT -= 1
                    self.cursorFFT.cursorY1LE.setText(f"{(self.Y1ValueFFT):.1f}")
                    self.cursorKnob.levelDown = False
                self.y_Y1_FFT = np.ones_like(self.x_Y1_FFT) * self.Y1ValueFFT
                self.FFTScr.removeItem(self.graphicPlottingY1Line_FFT)
                self.graphicPlottingY1Line_FFT = self.FFTScr.plot(self.x_Y1_FFT, self.y_Y1_FFT, pen=self.Y1LineStyle_FFT)
                self.UpdateCursorDeltaY_FFT()

            elif self.cursorKnobLineAssigned_FFT == "Y2":
                if self.cursorKnob.levelUp == True:
                    if (self.Y2ValueFFT < 100): self.Y2ValueFFT += 1
                    self.cursorFFT.cursorY2LE.setText(f"{(self.Y2ValueFFT):.1f}")
                    self.cursorKnob.levelUp = False
                if self.cursorKnob.levelDown == True:
                    if (self.Y2ValueFFT > -100): self.Y2ValueFFT -= 1
                    self.cursorFFT.cursorY2LE.setText(f"{(self.Y2ValueFFT):.1f}")
                    self.cursorKnob.levelDown = False
                self.y_Y2_FFT = np.ones_like(self.x_Y2_FFT) * self.Y2ValueFFT
                self.FFTScr.removeItem(self.graphicPlottingY2Line_FFT)
                self.graphicPlottingY2Line_FFT = self.FFTScr.plot(self.x_Y2_FFT, self.y_Y2_FFT, pen=self.Y2LineStyle_FFT)
                self.UpdateCursorDeltaY_FFT()

#Funções para o Cursor de Frequency Response:
#freqRespScr.magnitude
def CursorSelectCBChanged_FreqResp_Magn(self):
    if self.cursorFreqResp_Magn.cursorSelectCB.currentText() == "X1":
        self.cursorKnobLineAssigned_FreqResp_Magn = "X1"
    elif self.cursorFreqResp_Magn.cursorSelectCB.currentText() == "X2":
        self.cursorKnobLineAssigned_FreqResp_Magn = "X2"
    elif self.cursorFreqResp_Magn.cursorSelectCB.currentText() == "Y1":
        self.cursorKnobLineAssigned_FreqResp_Magn = "Y1"
    elif self.cursorFreqResp_Magn.cursorSelectCB.currentText() == "Y2":
        self.cursorKnobLineAssigned_FreqResp_Magn = "Y2"

def Cursor_X1_LEChanged_FreqResp_Magn(self):
    text = self.cursorFreqResp_Magn.cursorX1LE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = float(text)
        if value > 100000:
            self.cursorFreqResp_Magn.cursorX1LE.setText("100000.0")
            self.X1ValueFreqResp_Magn = 100000
        elif value >= 10:
            self.X1ValueFreqResp_Magn = value 
            self.cursorFreqResp_Magn.cursorX1LE.setText(f"{value:.1f}")
        else:
            self.cursorFreqResp_Magn.cursorX1LE.setText("10.0")
            self.X1ValueFreqResp_Magn = 10

        self.x_X1_FreqResp_Magn = np.ones_like(self.y_X1_FreqResp_Magn) * self.X1ValueFreqResp_Magn 
        self.freqRespScr.magnitude.removeItem(self.graphicPlottingX1Line_FreqResp_Magn)
        self.graphicPlottingX1Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_X1_FreqResp_Magn, 
                                                    self.y_X1_FreqResp_Magn, pen=self.X1LineStyle_FreqResp_Magn)
        
        #sincronizando a alteração com o cursor X1 de phase:
        self.X1ValueFreqResp_Phase = self.X1ValueFreqResp_Magn
        self.x_X1_FreqResp_Phase = np.ones_like(self.y_X1_FreqResp_Phase) * self.X1ValueFreqResp_Phase 
        self.freqRespScr.phase.removeItem(self.graphicPlottingX1Line_FreqResp_Phase)
        self.graphicPlottingX1Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_X1_FreqResp_Phase, 
                                                    self.y_X1_FreqResp_Phase, pen=self.X1LineStyle_FreqResp_Phase)
        self.cursorFreqResp_Phase.cursorX1LE.setText(f"{self.cursorFreqResp_Magn.cursorX1LE.text()}")
        self.UpdateCursorDeltaX_FreqResp_Phase()

    except ValueError:
        self.cursorFreqResp_Magn.cursorX1LE.setText(f"{self.X1ValueFreqResp_Magn:.1f}")
    self.UpdateCursorDeltaX_FreqResp_Magn()

    


def Cursor_X2_LEChanged_FreqResp_Magn(self):
    text = self.cursorFreqResp_Magn.cursorX2LE.text()

    try:
        value = float(text)

        if value > 100000:
            self.cursorFreqResp_Magn.cursorX2LE.setText("100000.0")
            self.X2ValueFreqResp_Magn = 100000
        elif value >= 10:
            self.X2ValueFreqResp_Magn = value 
            self.cursorFreqResp_Magn.cursorX2LE.setText(f"{value:.1f}")
        else:
            self.cursorFreqResp_Magn.cursorX2LE.setText("10.0")
            self.X2ValueFreqResp_Magn = 1.00

        self.x_X2_FreqResp_Magn = np.ones_like(self.y_X2_FreqResp_Magn) * self.X2ValueFreqResp_Magn
        self.freqRespScr.magnitude.removeItem(self.graphicPlottingX2Line_FreqResp_Magn)
        self.graphicPlottingX2Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_X2_FreqResp_Magn, 
                                            self.y_X2_FreqResp_Magn, pen=self.X2LineStyle_FreqResp_Magn)
        
        #sincronizando a alteração com o cursor X2 de phase:
        self.X2ValueFreqResp_Phase = self.X2ValueFreqResp_Magn
        self.x_X2_FreqResp_Phase = np.ones_like(self.y_X2_FreqResp_Phase) * self.X2ValueFreqResp_Phase 
        self.freqRespScr.phase.removeItem(self.graphicPlottingX2Line_FreqResp_Phase)
        self.graphicPlottingX2Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_X2_FreqResp_Phase, 
                                                    self.y_X2_FreqResp_Phase, pen=self.X2LineStyle_FreqResp_Phase)
        self.cursorFreqResp_Phase.cursorX2LE.setText(f"{self.cursorFreqResp_Magn.cursorX2LE.text()}")
        self.UpdateCursorDeltaX_FreqResp_Phase()
        
    except ValueError:
        self.cursorFreqResp_Magn.cursorX2LE.setText(f"{self.X2ValueFreqResp_Magn:.1f}")
    self.UpdateCursorDeltaX_FreqResp_Magn()



def Cursor_Y1_LEChanged_FreqResp_Magn(self):
    text = self.cursorFreqResp_Magn.cursorY1LE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = float(text)
        if value > 100:
            self.cursorFreqResp_Magn.cursorY1LE.setText("100.0")
            self.Y1ValueFreqResp_Magn = 100
        elif value > -100:
            self.Y1ValueFreqResp_Magn = value
            self.cursorFreqResp_Magn.cursorY1LE.setText(f"{value:.1f}")
        else:
            self.cursorFreqResp_Magn.cursorY1LE.setText("-100.0")
            self.Y1ValueFreqResp_Magn = -100
        
        self.y_Y1_FreqResp_Magn = np.ones_like(self.x_Y1_FreqResp_Magn) * self.Y1ValueFreqResp_Magn 
        
        self.freqRespScr.magnitude.removeItem(self.graphicPlottingY1Line_FreqResp_Magn)
        self.graphicPlottingY1Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_Y1_FreqResp_Magn, 
                                            self.y_Y1_FreqResp_Magn, pen=self.Y1LineStyle_FreqResp_Magn)
    except ValueError:
        self.cursorFreqResp_Magn.cursorY1LE.setText(f"{self.Y1ValueFreqResp_Magn:.1f}")
    self.UpdateCursorDeltaY_FreqResp_Magn()

def Cursor_Y2_LEChanged_FreqResp_Magn(self):
    text = self.cursorFreqResp_Magn.cursorY2LE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = float(text)
        if value > 100:
            self.cursorFreqResp_Magn.cursorY2LE.setText("100.0")
            self.Y2ValueFreqResp_Magn = 100
        elif value > -100:
            self.Y2ValueFreqResp_Magn = value
            self.cursorFreqResp_Magn.cursorY2LE.setText(f"{value:.1f}")
        else:
            self.cursorFreqResp_Magn.cursorY2LE.setText("100.0")
            self.Y2ValueFreqResp_Magn = -100

        self.y_Y2_FreqResp_Magn = np.ones_like(self.x_Y2_FreqResp_Magn) * self.Y2ValueFreqResp_Magn
        
        self.freqRespScr.magnitude.removeItem(self.graphicPlottingY2Line_FreqResp_Magn)
        self.graphicPlottingY2Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_Y2_FreqResp_Magn, 
                                                self.y_Y2_FreqResp_Magn, pen=self.Y2LineStyle_FreqResp_Magn)
    except ValueError:
        self.cursorFreqResp_Magn.cursorY2LE.setText(f"{self.Y2ValueFreqResp_Magn:.1f}")
    self.UpdateCursorDeltaY_FreqResp_Magn()

def UpdateCursorDeltaX_FreqResp_Magn(self):
    self.cursorFreqResp_Magn.cursorDeltaX_LE.setText(f"{(self.X2ValueFreqResp_Magn - self.X1ValueFreqResp_Magn):.1f}")

def UpdateCursorDeltaY_FreqResp_Magn(self):
    self.cursorFreqResp_Magn.cursorDeltaY_LE.setText(f"{(self.Y2ValueFreqResp_Magn - self.Y1ValueFreqResp_Magn):.1f}")

def CursorKnob_FreqResp_Magn(self):
    if self.screenName == "Freq Resp" and self.freqResp_scr2.freqResp_page2.y_AxisCB.currentText() == "Magnitude":
        if self.cursorKnob.buttonIsOn == True:
            if self.cursorKnobLineAssigned_FreqResp_Magn == "X1":
                if self.cursorKnob.levelUp == True:
                    if (self.X1ValueFreqResp_Magn < 100000):
                        self.X1ValueFreqResp_Magn += 10
                    self.cursorFreqResp_Magn.cursorX1LE.setText(f"{(self.X1ValueFreqResp_Magn):.1f}")
                    self.cursorKnob.levelUp = False

                
                if self.cursorKnob.levelDown == True:
                    if (self.X1ValueFreqResp_Magn > 10): self.X1ValueFreqResp_Magn -= 10
                    self.cursorFreqResp_Magn.cursorX1LE.setText(f"{(self.X1ValueFreqResp_Magn):.1f}")
                    self.cursorKnob.levelDown = False
                self.x_X1_FreqResp_Magn = np.ones_like(self.y_X1_FreqResp_Magn) * self.X1ValueFreqResp_Magn
                self.freqRespScr.magnitude.removeItem(self.graphicPlottingX1Line_FreqResp_Magn)
                self.graphicPlottingX1Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_X1_FreqResp_Magn, 
                                                self.y_X1_FreqResp_Magn, pen=self.X1LineStyle_FreqResp_Magn)
                self.UpdateCursorDeltaX_FreqResp_Magn()

                #sincronizando a alteração com o cursor X1 de phase:
                self.X1ValueFreqResp_Phase = self.X1ValueFreqResp_Magn
                self.x_X1_FreqResp_Phase = np.ones_like(self.y_X1_FreqResp_Phase) * self.X1ValueFreqResp_Phase 
                self.freqRespScr.phase.removeItem(self.graphicPlottingX1Line_FreqResp_Phase)
                self.graphicPlottingX1Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_X1_FreqResp_Phase, 
                                                            self.y_X1_FreqResp_Phase, pen=self.X1LineStyle_FreqResp_Phase)
                self.cursorFreqResp_Phase.cursorX1LE.setText(f"{self.cursorFreqResp_Magn.cursorX1LE.text()}")
                self.UpdateCursorDeltaX_FreqResp_Phase()

            elif self.cursorKnobLineAssigned_FreqResp_Magn == "X2":
                if self.cursorKnob.levelUp == True:
                    if (self.X2ValueFreqResp_Magn < 100000): self.X2ValueFreqResp_Magn += 10
                    self.cursorFreqResp_Magn.cursorX2LE.setText(f"{(self.X2ValueFreqResp_Magn):.1f}")
                    self.cursorKnob.levelUp = False
                if self.cursorKnob.levelDown == True:
                    if (self.X2ValueFreqResp_Magn > 10): self.X2ValueFreqResp_Magn -= 10
                    self.cursorFreqResp_Magn.cursorX2LE.setText(f"{(self.X2ValueFreqResp_Magn):.1f}")
                    self.cursorKnob.levelDown = False
                self.x_X2_FreqResp_Magn = np.ones_like(self.y_X2_FreqResp_Magn) * self.X2ValueFreqResp_Magn
                self.freqRespScr.magnitude.removeItem(self.graphicPlottingX2Line_FreqResp_Magn)
                self.graphicPlottingX2Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_X2_FreqResp_Magn, 
                                        self.y_X2_FreqResp_Magn, pen=self.X2LineStyle_FreqResp_Magn)
                self.UpdateCursorDeltaX_FreqResp_Magn()

                #sincronizando a alteração com o cursor X2 de phase:
                self.X2ValueFreqResp_Phase = self.X2ValueFreqResp_Magn
                self.x_X2_FreqResp_Phase = np.ones_like(self.y_X2_FreqResp_Phase) * self.X2ValueFreqResp_Phase 
                self.freqRespScr.phase.removeItem(self.graphicPlottingX2Line_FreqResp_Phase)
                self.graphicPlottingX2Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_X2_FreqResp_Phase, 
                                                            self.y_X2_FreqResp_Phase, pen=self.X2LineStyle_FreqResp_Phase)
                self.cursorFreqResp_Phase.cursorX2LE.setText(f"{self.cursorFreqResp_Magn.cursorX2LE.text()}")
                self.UpdateCursorDeltaX_FreqResp_Phase()

            elif self.cursorKnobLineAssigned_FreqResp_Magn == "Y1":
                if self.cursorKnob.levelUp == True:
                    if (self.Y1ValueFreqResp_Magn < 100): self.Y1ValueFreqResp_Magn += 1
                    self.cursorFreqResp_Magn.cursorY1LE.setText(f"{(self.Y1ValueFreqResp_Magn):.1f}")
                    self.cursorKnob.levelUp = False
                if self.cursorKnob.levelDown == True:
                    if (self.Y1ValueFreqResp_Magn > -100): self.Y1ValueFreqResp_Magn -= 1
                    self.cursorFreqResp_Magn.cursorY1LE.setText(f"{(self.Y1ValueFreqResp_Magn):.1f}")
                    self.cursorKnob.levelDown = False
                self.y_Y1_FreqResp_Magn = np.ones_like(self.x_Y1_FreqResp_Magn) * self.Y1ValueFreqResp_Magn
                self.freqRespScr.magnitude.removeItem(self.graphicPlottingY1Line_FreqResp_Magn)
                self.graphicPlottingY1Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_Y1_FreqResp_Magn, self.y_Y1_FreqResp_Magn, pen=self.Y1LineStyle_FreqResp_Magn)
                self.UpdateCursorDeltaY_FreqResp_Magn()

            elif self.cursorKnobLineAssigned_FreqResp_Magn == "Y2":
                if self.cursorKnob.levelUp == True:
                    if (self.Y2ValueFreqResp_Magn < 100): self.Y2ValueFreqResp_Magn += 1
                    self.cursorFreqResp_Magn.cursorY2LE.setText(f"{(self.Y2ValueFreqResp_Magn):.1f}")
                    self.cursorKnob.levelUp = False
                if self.cursorKnob.levelDown == True:
                    if (self.Y2ValueFreqResp_Magn > -100): self.Y2ValueFreqResp_Magn -= 1
                    self.cursorFreqResp_Magn.cursorY2LE.setText(f"{(self.Y2ValueFreqResp_Magn):.1f}")
                    self.cursorKnob.levelDown = False
                self.y_Y2_FreqResp_Magn = np.ones_like(self.x_Y2_FreqResp_Magn) * self.Y2ValueFreqResp_Magn
                self.freqRespScr.magnitude.removeItem(self.graphicPlottingY2Line_FreqResp_Magn)
                self.graphicPlottingY2Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_Y2_FreqResp_Magn, 
                                                self.y_Y2_FreqResp_Magn, pen=self.Y2LineStyle_FreqResp_Magn)
                self.UpdateCursorDeltaY_FreqResp_Magn()


#Funções para o Cursor de Frequency Response:
#freqRespScr.phase
def CursorSelectCBChanged_FreqResp_Phase(self):
    if self.cursorFreqResp_Phase.cursorSelectCB.currentText() == "X1":
        self.cursorKnobLineAssigned_FreqResp_Phase = "X1"
    elif self.cursorFreqResp_Phase.cursorSelectCB.currentText() == "X2":
        self.cursorKnobLineAssigned_FreqResp_Phase = "X2"
    elif self.cursorFreqResp_Phase.cursorSelectCB.currentText() == "Y1":
        self.cursorKnobLineAssigned_FreqResp_Phase = "Y1"
    elif self.cursorFreqResp_Phase.cursorSelectCB.currentText() == "Y2":
        self.cursorKnobLineAssigned_FreqResp_Phase = "Y2"

def Cursor_X1_LEChanged_FreqResp_Phase(self):
    text = self.cursorFreqResp_Phase.cursorX1LE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = float(text)
        if value > 100000:
            self.cursorFreqResp_Phase.cursorX1LE.setText("100000.0")
            self.X1ValueFreqResp_Phase = 100000
        elif value >= 10:
            self.X1ValueFreqResp_Phase = value 
            self.cursorFreqResp_Phase.cursorX1LE.setText(f"{value:.1f}")
        else:
            self.cursorFreqResp_Phase.cursorX1LE.setText("10.0")
            self.X1ValueFreqResp_Phase = 10

        self.x_X1_FreqResp_Phase = np.ones_like(self.y_X1_FreqResp_Phase) * self.X1ValueFreqResp_Phase 
        self.freqRespScr.phase.removeItem(self.graphicPlottingX1Line_FreqResp_Phase)
        self.graphicPlottingX1Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_X1_FreqResp_Phase, 
                                                    self.y_X1_FreqResp_Phase, pen=self.X1LineStyle_FreqResp_Phase)
        
        #sincronizando a alteração com o cursor X1 de magnitude:
        self.X1ValueFreqResp_Magn = self.X1ValueFreqResp_Phase
        self.x_X1_FreqResp_Magn = np.ones_like(self.y_X1_FreqResp_Magn) * self.X1ValueFreqResp_Magn 
        self.freqRespScr.magnitude.removeItem(self.graphicPlottingX1Line_FreqResp_Magn)
        self.graphicPlottingX1Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_X1_FreqResp_Magn, 
                                                    self.y_X1_FreqResp_Magn, pen=self.X1LineStyle_FreqResp_Magn)
        self.cursorFreqResp_Magn.cursorX1LE.setText(f"{self.cursorFreqResp_Phase.cursorX1LE.text()}")
        self.UpdateCursorDeltaX_FreqResp_Magn()

    except ValueError:
        self.cursorFreqResp_Phase.cursorX1LE.setText(f"{self.X1ValueFreqResp_Phase:.1f}")
    self.UpdateCursorDeltaX_FreqResp_Phase()

def Cursor_X2_LEChanged_FreqResp_Phase(self):
    text = self.cursorFreqResp_Phase.cursorX2LE.text()

    try:
        value = float(text)

        if value > 100000:
            self.cursorFreqResp_Phase.cursorX2LE.setText("100000.0")
            self.X2ValueFreqResp_Phase = 100000
        elif value >= 10:
            self.X2ValueFreqResp_Phase = value 
            self.cursorFreqResp_Phase.cursorX2LE.setText(f"{value:.1f}")
        else:
            self.cursorFreqResp_Phase.cursorX2LE.setText("10.0")
            self.X2ValueFreqResp_Phase = 1.00

        self.x_X2_FreqResp_Phase = np.ones_like(self.y_X2_FreqResp_Phase) * self.X2ValueFreqResp_Phase
        self.freqRespScr.phase.removeItem(self.graphicPlottingX2Line_FreqResp_Phase)
        self.graphicPlottingX2Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_X2_FreqResp_Phase, 
                                            self.y_X2_FreqResp_Phase, pen=self.X2LineStyle_FreqResp_Phase)
        
        #sincronizando a alteração com o cursor X2 de magnitude:
        self.X2ValueFreqResp_Magn = self.X2ValueFreqResp_Phase
        self.x_X2_FreqResp_Magn = np.ones_like(self.y_X2_FreqResp_Magn) * self.X2ValueFreqResp_Magn 
        self.freqRespScr.magnitude.removeItem(self.graphicPlottingX2Line_FreqResp_Magn)
        self.graphicPlottingX2Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_X2_FreqResp_Magn, 
                                                    self.y_X2_FreqResp_Magn, pen=self.X2LineStyle_FreqResp_Magn)
        self.cursorFreqResp_Magn.cursorX2LE.setText(f"{self.cursorFreqResp_Phase.cursorX2LE.text()}")
        self.UpdateCursorDeltaX_FreqResp_Magn()
        
    except ValueError:
        self.cursorFreqResp_Phase.cursorX2LE.setText(f"{self.X2ValueFreqResp_Phase:.1f}")
    self.UpdateCursorDeltaX_FreqResp_Phase()



def Cursor_Y1_LEChanged_FreqResp_Phase(self):
    text = self.cursorFreqResp_Phase.cursorY1LE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = float(text)
        if value > 180:
            self.cursorFreqResp_Phase.cursorY1LE.setText("180.0")
            self.Y1ValueFreqResp_Phase = 180
        elif value > -180:
            self.Y1ValueFreqResp_Phase = value
            self.cursorFreqResp_Phase.cursorY1LE.setText(f"{value:.1f}")
        else:
            self.cursorFreqResp_Phase.cursorY1LE.setText("-180.0")
            self.Y1ValueFreqResp_Phase = -180
        
        self.y_Y1_FreqResp_Phase = np.ones_like(self.x_Y1_FreqResp_Phase) * self.Y1ValueFreqResp_Phase 
        
        self.freqRespScr.phase.removeItem(self.graphicPlottingY1Line_FreqResp_Phase)
        self.graphicPlottingY1Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_Y1_FreqResp_Phase, 
                                            self.y_Y1_FreqResp_Phase, pen=self.Y1LineStyle_FreqResp_Phase)
    except ValueError:
        self.cursorFreqResp_Phase.cursorY1LE.setText(f"{self.Y1ValueFreqResp_Phase:.1f}")
    self.UpdateCursorDeltaY_FreqResp_Phase()

def Cursor_Y2_LEChanged_FreqResp_Phase(self):
    text = self.cursorFreqResp_Phase.cursorY2LE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = float(text)
        if value > 180:
            self.cursorFreqResp_Phase.cursorY2LE.setText("180.0")
            self.Y2ValueFreqResp_Phase = 180
        elif value > -180:
            self.Y2ValueFreqResp_Phase = value
            self.cursorFreqResp_Phase.cursorY2LE.setText(f"{value:.1f}")
        else:
            self.cursorFreqResp_Phase.cursorY2LE.setText("180.0")
            self.Y2ValueFreqResp_Phase = -180

        self.y_Y2_FreqResp_Phase = np.ones_like(self.x_Y2_FreqResp_Phase) * self.Y2ValueFreqResp_Phase
        
        self.freqRespScr.phase.removeItem(self.graphicPlottingY2Line_FreqResp_Phase)
        self.graphicPlottingY2Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_Y2_FreqResp_Phase, 
                                                self.y_Y2_FreqResp_Phase, pen=self.Y2LineStyle_FreqResp_Phase)
    except ValueError:
        self.cursorFreqResp_Phase.cursorY2LE.setText(f"{self.Y2ValueFreqResp_Phase:.1f}")
    self.UpdateCursorDeltaY_FreqResp_Phase()

def UpdateCursorDeltaX_FreqResp_Phase(self):
    self.cursorFreqResp_Phase.cursorDeltaX_LE.setText(f"{(self.X2ValueFreqResp_Phase - self.X1ValueFreqResp_Phase):.1f}")

def UpdateCursorDeltaY_FreqResp_Phase(self):
    self.cursorFreqResp_Phase.cursorDeltaY_LE.setText(f"{(self.Y2ValueFreqResp_Phase - self.Y1ValueFreqResp_Phase):.1f}")

def CursorKnob_FreqResp_Phase(self):
    if self.screenName == "Freq Resp" and self.freqResp_scr2.freqResp_page2.y_AxisCB.currentText() == "Phase":
        if self.cursorKnob.buttonIsOn == True:
            if self.cursorKnobLineAssigned_FreqResp_Phase == "X1":
                if self.cursorKnob.levelUp == True:
                    if (self.X1ValueFreqResp_Phase < 100000):
                        self.X1ValueFreqResp_Phase += 10
                    self.cursorFreqResp_Phase.cursorX1LE.setText(f"{(self.X1ValueFreqResp_Phase):.1f}")
                    self.cursorKnob.levelUp = False

                
                if self.cursorKnob.levelDown == True:
                    if (self.X1ValueFreqResp_Phase > 10): self.X1ValueFreqResp_Phase -= 10
                    self.cursorFreqResp_Phase.cursorX1LE.setText(f"{(self.X1ValueFreqResp_Phase):.1f}")
                    self.cursorKnob.levelDown = False
                self.x_X1_FreqResp_Phase = np.ones_like(self.y_X1_FreqResp_Phase) * self.X1ValueFreqResp_Phase
                self.freqRespScr.phase.removeItem(self.graphicPlottingX1Line_FreqResp_Phase)
                self.graphicPlottingX1Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_X1_FreqResp_Phase, 
                                                self.y_X1_FreqResp_Phase, pen=self.X1LineStyle_FreqResp_Phase)
                self.UpdateCursorDeltaX_FreqResp_Phase()

                #sincronizando a alteração com o cursor X1 de magnitude:
                self.X1ValueFreqResp_Magn = self.X1ValueFreqResp_Phase
                self.x_X1_FreqResp_Magn = np.ones_like(self.y_X1_FreqResp_Magn) * self.X1ValueFreqResp_Magn 
                self.freqRespScr.magnitude.removeItem(self.graphicPlottingX1Line_FreqResp_Magn)
                self.graphicPlottingX1Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_X1_FreqResp_Magn, 
                                                            self.y_X1_FreqResp_Magn, pen=self.X1LineStyle_FreqResp_Magn)
                self.cursorFreqResp_Magn.cursorX1LE.setText(f"{self.cursorFreqResp_Phase.cursorX1LE.text()}")
                self.UpdateCursorDeltaX_FreqResp_Magn()

            elif self.cursorKnobLineAssigned_FreqResp_Phase == "X2":
                if self.cursorKnob.levelUp == True:
                    if (self.X2ValueFreqResp_Phase < 100000): self.X2ValueFreqResp_Phase += 10
                    self.cursorFreqResp_Phase.cursorX2LE.setText(f"{(self.X2ValueFreqResp_Phase):.1f}")
                    self.cursorKnob.levelUp = False
                if self.cursorKnob.levelDown == True:
                    if (self.X2ValueFreqResp_Phase > 10): self.X2ValueFreqResp_Phase -= 10
                    self.cursorFreqResp_Phase.cursorX2LE.setText(f"{(self.X2ValueFreqResp_Phase):.1f}")
                    self.cursorKnob.levelDown = False
                self.x_X2_FreqResp_Phase = np.ones_like(self.y_X2_FreqResp_Phase) * self.X2ValueFreqResp_Phase
                self.freqRespScr.phase.removeItem(self.graphicPlottingX2Line_FreqResp_Phase)
                self.graphicPlottingX2Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_X2_FreqResp_Phase, 
                                        self.y_X2_FreqResp_Phase, pen=self.X2LineStyle_FreqResp_Phase)
                self.UpdateCursorDeltaX_FreqResp_Phase()

                #sincronizando a alteração com o cursor X2 de magnitude:
                self.X2ValueFreqResp_Magn = self.X2ValueFreqResp_Phase
                self.x_X2_FreqResp_Magn = np.ones_like(self.y_X2_FreqResp_Magn) * self.X2ValueFreqResp_Magn 
                self.freqRespScr.magnitude.removeItem(self.graphicPlottingX2Line_FreqResp_Magn)
                self.graphicPlottingX2Line_FreqResp_Magn = self.freqRespScr.magnitude.plot(self.x_X2_FreqResp_Magn, 
                                                            self.y_X2_FreqResp_Magn, pen=self.X2LineStyle_FreqResp_Magn)
                self.cursorFreqResp_Magn.cursorX2LE.setText(f"{self.cursorFreqResp_Phase.cursorX2LE.text()}")
                self.UpdateCursorDeltaX_FreqResp_Magn()

            elif self.cursorKnobLineAssigned_FreqResp_Phase == "Y1":
                if self.cursorKnob.levelUp == True:
                    if (self.Y1ValueFreqResp_Phase < 180): self.Y1ValueFreqResp_Phase += 1
                    self.cursorFreqResp_Phase.cursorY1LE.setText(f"{(self.Y1ValueFreqResp_Phase):.1f}")
                    self.cursorKnob.levelUp = False
                if self.cursorKnob.levelDown == True:
                    if (self.Y1ValueFreqResp_Phase > -180): self.Y1ValueFreqResp_Phase -= 1
                    self.cursorFreqResp_Phase.cursorY1LE.setText(f"{(self.Y1ValueFreqResp_Phase):.1f}")
                    self.cursorKnob.levelDown = False
                self.y_Y1_FreqResp_Phase = np.ones_like(self.x_Y1_FreqResp_Phase) * self.Y1ValueFreqResp_Phase
                self.freqRespScr.phase.removeItem(self.graphicPlottingY1Line_FreqResp_Phase)
                self.graphicPlottingY1Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_Y1_FreqResp_Phase, self.y_Y1_FreqResp_Phase, pen=self.Y1LineStyle_FreqResp_Phase)
                self.UpdateCursorDeltaY_FreqResp_Phase()

            elif self.cursorKnobLineAssigned_FreqResp_Phase == "Y2":
                if self.cursorKnob.levelUp == True:
                    if (self.Y2ValueFreqResp_Phase < 180): self.Y2ValueFreqResp_Phase += 1
                    self.cursorFreqResp_Phase.cursorY2LE.setText(f"{(self.Y2ValueFreqResp_Phase):.1f}")
                    self.cursorKnob.levelUp = False
                if self.cursorKnob.levelDown == True:
                    if (self.Y2ValueFreqResp_Phase > -180): self.Y2ValueFreqResp_Phase -= 1
                    self.cursorFreqResp_Phase.cursorY2LE.setText(f"{(self.Y2ValueFreqResp_Phase):.1f}")
                    self.cursorKnob.levelDown = False
                self.y_Y2_FreqResp_Phase = np.ones_like(self.x_Y2_FreqResp_Phase) * self.Y2ValueFreqResp_Phase
                self.freqRespScr.phase.removeItem(self.graphicPlottingY2Line_FreqResp_Phase)
                self.graphicPlottingY2Line_FreqResp_Phase = self.freqRespScr.phase.plot(self.x_Y2_FreqResp_Phase, 
                                                self.y_Y2_FreqResp_Phase, pen=self.Y2LineStyle_FreqResp_Phase)
                self.UpdateCursorDeltaY_FreqResp_Phase()

def removeCursorLines(self):
    
    self.cursorLinesOn = False
    self.mainScr.removeItem(self.graphicPlottingX1Line)
    self.mainScr.removeItem(self.graphicPlottingX2Line)
    self.mainScr.removeItem(self.graphicPlottingY1Line)
    self.mainScr.removeItem(self.graphicPlottingY2Line)

    try:
        self.FFTScr.removeItem(self.graphicPlottingX1Line_FFT)
        self.FFTScr.removeItem(self.graphicPlottingX2Line_FFT)
        self.FFTScr.removeItem(self.graphicPlottingY1Line_FFT)
        self.FFTScr.removeItem(self.graphicPlottingY2Line_FFT)

        self.freqRespScr.magnitude.removeItem(self.graphicPlottingX1Line_FreqResp_Magn)
        self.freqRespScr.magnitude.removeItem(self.graphicPlottingX2Line_FreqResp_Magn)
        self.freqRespScr.magnitude.removeItem(self.graphicPlottingY1Line_FreqResp_Magn)
        self.freqRespScr.magnitude.removeItem(self.graphicPlottingY2Line_FreqResp_Magn)

        self.freqRespScr.phase.removeItem(self.graphicPlottingX1Line_FreqResp_Phase)
        self.freqRespScr.phase.removeItem(self.graphicPlottingX2Line_FreqResp_Phase)
        self.freqRespScr.phase.removeItem(self.graphicPlottingY1Line_FreqResp_Phase)
        self.freqRespScr.phase.removeItem(self.graphicPlottingY2Line_FreqResp_Phase)

    except AttributeError: #ocorre quando tenta apagar algo que não existe
        pass




