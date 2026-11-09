import numpy as np


def changeMainSecondScr_1_to_2(self):
    self.currentMainScr2_Scr = 2
    if self.screenName == "Main": self.secondaryScreen.setCurrentIndex(8)

def changeMainSecondScr_2_to_1(self):
    self.currentMainScr2_Scr = 1
    if self.screenName == "Main": self.secondaryScreen.setCurrentIndex(7)


def SubmitTimeValue(self):
    insertedText = self.mainScr2_1.customTimeScaleLE.text()
    try:
        value = float(insertedText)
        self.mainScr.timeScale = value
        if self.microcontroller == "Arduino":
            if value < 0.1:
                value = 0.1
                self.mainScr2_1.customTimeScaleLE.setText("0.1")
            elif value > 50:
                value = 50
                self.mainScr2_1.customTimeScaleLE.setText("50")
        else:
            if value < 0.001:
                value = 0.001
                self.mainScr2_1.customTimeScaleLE.setText("0.001")
            elif value > 50:
                value = 50
                self.mainScr2_1.customTimeScaleLE.setText("50")

        if self.mainScr.timeScale < 0.2:
            self.timeKnob.usefulValue = -3
        elif self.mainScr.timeScale < 0.5:
            self.timeKnob.usefulValue = -2
        elif self.mainScr.timeScale < 1:
            self.timeKnob.usefulValue = -1
        elif self.mainScr.timeScale < 2:
            self.timeKnob.usefulValue = 0
        elif self.mainScr.timeScale < 5:
            self.timeKnob.usefulValue = 1
        elif self.mainScr.timeScale < 10:
            self.timeKnob.usefulValue = 2
        elif self.mainScr.timeScale < 20:
            self.timeKnob.usefulValue = 3
        elif self.mainScr.timeScale < 50:
            self.timeKnob.usefulValue = 4
        else:
            self.timeKnob.usefulValue = 5

        if (self.timeKnob.usefulValue >= 0):
            if self.mainScr.timeScale < 50:
                self.timeLabel.setText(
                    f"Time: {self.mainScr.timeScale:.0f} ms/div*")
            else:
                self.timeLabel.setText(f"Time: 50 ms/div*")
        else:
            if self.microcontroller == "Arduino":
                if self.mainScr.timeScale > 0.1:
                    self.timeLabel.setText(
                        f"Time: {self.mainScr.timeScale:.1f} ms/div*")
                else:
                    self.timeLabel.setText(f"Time: 0.1 ms/div*")
            else:
                if self.mainScr.timeScale > 0.001:
                    if self.mainScr.timeScale >= 0.2:
                        self.timeLabel.setText(
                            f"Time: {self.mainScr.timeScale:.1f} ms/div*")
                    else:
                        self.timeLabel.setText(
                            f"Time: {(self.mainScr.timeScale * 1000):.1f} µs/div*")
                else:
                    self.timeLabel.setText(f"Time: 1 µs/div*")
        self.mainScr.setRange(
            xRange=(0, 0.01 * value), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
        self.mainScr.getPlotItem().getAxis(
            'bottom').setTickSpacing(0.001 * value, 0.002 * value)
        #self.setTimeWindow.close()
    except ValueError:
        self.mainScr2_1.customTimeScaleLE.setText("1")

def ChangeRefChannel(self):
    if   self.mainScr2_1.refChannelCB.currentText() == "CH1": self.mainScr.referencePhase = "CH1"
    elif self.mainScr2_1.refChannelCB.currentText() == "CH2": self.mainScr.referencePhase = "CH2"
    else:                                                     self.mainScr.referencePhase = "Math"
    self.trigger.trigChannelLE.setText(f"{self.mainScr.referencePhase}")
    self.adjustCursorYAxisLabels()


def ChangeAttnFactorCH1(self):
    if self.mainScr2_1.attnFactorCB_CH1.currentText() == "x1": self.mainScr.dataHandler.attnFactor_CH1 = "x1"
    else:                                           self.mainScr.dataHandler.attnFactor_CH1 = "x5"
    self.mainScr.dataHandler.setDataEnable = True

def ChangeAttnFactorCH2(self):
    if self.mainScr2_1.attnFactorCB_CH2.currentText() == "x1": self.mainScr.dataHandler.attnFactor_CH2 = "x1"
    else:                                           self.mainScr.dataHandler.attnFactor_CH2 = "x5"
    self.mainScr.dataHandler.setDataEnable = True
    
def currentInVerticalScale(self):

    # ---------- CH1 ---------------
    if self.mainScr2_2.currentInVerticalScaleCheckBox_CH1.isChecked():

        if self.mainScr.vdivCH1Scale/self.shuntRes_CH1 >= 0.5:
            self.CH1Label.setText(f"CH1:\n{(self.mainScr.vdivCH1Scale/self.shuntRes_CH1):.2f} A/div")
            
        elif self.mainScr.vdivCH1Scale/self.shuntRes_CH1  >= 0.5 * 1e-3:
            self.CH1Label.setText(f"CH1:\n{(self.mainScr.vdivCH1Scale/self.shuntRes_CH1 * 1000):.2f} mA/div")

        else:
            self.CH1Label.setText(f"CH1:\n{(self.mainScr.vdivCH1Scale/self.shuntRes_CH1 * 1e6):.2f} µA/div")
        self.currentForCH1Scale = True

        self.mainScr2_2.resistorValueLE_CH1.setStyleSheet(
        """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.mainScr2_2.resistorValueLE_CH1.setReadOnly(False)
        self.vdivLabel1.setText("A/div")
        self.mainScr2_2.resistorValueLE_CH1.setText(f"{(self.shuntRes_CH1):.1f}")
        self.adjustCursorYAxisLabels()


    else:
        if self.mainScr.vdivCH1Scale >= 0.5: self.CH1Label.setText(f"CH1: {self.mainScr.vdivCH1Scale} V/div")
        else: self.CH1Label.setText(f"CH1: {(self.mainScr.vdivCH1Scale * 1000):.0f} mV/div")
        self.currentForCH1Scale = False

        self.mainScr2_2.resistorValueLE_CH1.setStyleSheet(
        """color: rgb(240, 240, 240); background-color: rgb(150, 150, 150)""")
        self.mainScr2_2.resistorValueLE_CH1.setText("")
        self.mainScr2_2.resistorValueLE_CH1.setReadOnly(True)
        self.shuntRes_CH1 = 1
        self.mainScr2_2.resistorValueLE_CH1.setText("")
        self.vdivLabel1.setText("V/div")
        self.adjustCursorYAxisLabels()
        
        

    # ----------------- CH2 --------------------
    if self.mainScr2_2.currentInVerticalScaleCheckBox_CH2.isChecked():
        if self.mainScr.vdivCH2Scale/self.shuntRes_CH2 >= 0.5:
            self.CH2Label.setText(f"CH2:\n{(self.mainScr.vdivCH2Scale/self.shuntRes_CH2):.2f} A/div")

        elif self.mainScr.vdivCH2Scale/self.shuntRes_CH2  >= 0.5 * 1e-3:
            self.CH2Label.setText(f"CH2:\n{(self.mainScr.vdivCH2Scale/self.shuntRes_CH2 * 1000):.2f} mA/div")
        
        else:
            self.CH2Label.setText(f"CH2:\n{(self.mainScr.vdivCH2Scale/self.shuntRes_CH2 * 1e6):.2f} µA/div")
        self.currentForCH2Scale = True

        self.mainScr2_2.resistorValueLE_CH2.setStyleSheet(
        """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.mainScr2_2.resistorValueLE_CH2.setReadOnly(False)
        self.vdivLabel2.setText("A/div")
        self.mainScr2_2.resistorValueLE_CH2.setText(f"{(self.shuntRes_CH2):.1f}")

        self.adjustCursorYAxisLabels()
        

    else:
        if self.mainScr.vdivCH2Scale >= 0.5: self.CH2Label.setText(f"CH2: {self.mainScr.vdivCH2Scale} V/div")
        else: self.CH2Label.setText(f"CH2: {(self.mainScr.vdivCH2Scale * 1000):.0f} mV/div")
        self.currentForCH2Scale = False

        self.mainScr2_2.resistorValueLE_CH2.setStyleSheet(
        """color: rgb(240, 240, 240); background-color: rgb(150, 150, 150)""")
        self.mainScr2_2.resistorValueLE_CH2.setText("")
        self.mainScr2_2.resistorValueLE_CH2.setReadOnly(True)
        self.shuntRes_CH2 = 1
        self.mainScr2_2.resistorValueLE_CH2.setText("")
        self.vdivLabel2.setText("V/div")

        self.adjustCursorYAxisLabels()
        

    # ----------- Math -----------------
    if self.mainScr2_2.currentInVerticalScaleCheckBox_Math.isChecked():
        if self.mainScr.vdivMathScale/self.shuntRes_Math >= 0.5:
            self.mathvDivLabel.setText(f"Math:\n{(self.mainScr.vdivMathScale/self.shuntRes_Math):.2f} A/div")

        elif self.mainScr.vdivMathScale/self.shuntRes_Math  >= 0.5 * 1e-3:
            self.mathvDivLabel.setText(f"Math:\n{(self.mainScr.vdivMathScale/self.shuntRes_Math * 1000):.2f} mA/div")
        
        else:
            self.mathvDivLabel.setText(f"Math:\n{(self.mainScr.vdivMathScale/self.shuntRes_Math * 1e6):.2f} µA/div")
        self.currentForMathScale = True

        self.mainScr2_2.resistorValueLE_Math.setStyleSheet(
        """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.mainScr2_2.resistorValueLE_Math.setReadOnly(False)
        self.vdivLabel3.setText("A/div")
        self.mainScr2_2.resistorValueLE_Math.setText(f"{(self.shuntRes_Math):.1f}")

        self.adjustCursorYAxisLabels()

    else:
        if self.mainScr.vdivMathScale >= 0.5: self.mathvDivLabel.setText(f"Math: {self.mainScr.vdivMathScale} V/div")
        else: self.mathvDivLabel.setText(f"Math: {(self.mainScr.vdivMathScale * 1000):.0f} mV/div")
        self.currentForMathScale = False

        self.mainScr2_2.resistorValueLE_Math.setStyleSheet(
        """color: rgb(240, 240, 240); background-color: rgb(150, 150, 150)""")
        self.mainScr2_2.resistorValueLE_Math.setText("")
        self.mainScr2_2.resistorValueLE_Math.setReadOnly(True)
        self.shuntRes_Math = 1
        self.mainScr2_2.resistorValueLE_Math.setText("")
        self.vdivLabel3.setText("V/div")

        self.adjustCursorYAxisLabels()

def adjustCursorYAxisLabels(self):
    #mudando o cursor de Main para se ajustar à mudança de escala vertical:
    if self.mainScr.referencePhase == "CH1":
        if not self.currentForCH1Scale:
            self.cursor.cursorY1Label.setText("Y1 (V): ")
            self.cursor.cursorY2Label.setText("Y2 (V): ")
            self.cursor.cursorDeltaYLabel.setText("Y2 - Y1 (V): ")
        else:
            self.cursor.cursorY1Label.setText("Y1 (mA): ")
            self.cursor.cursorY2Label.setText("Y2 (mA): ")
            self.cursor.cursorDeltaYLabel.setText("Y2 - Y1 (mA): ")

    elif self.mainScr.referencePhase == "CH2":
        if not self.currentForCH2Scale:
            self.cursor.cursorY1Label.setText("Y1 (V): ")
            self.cursor.cursorY2Label.setText("Y2 (V): ")
            self.cursor.cursorDeltaYLabel.setText("Y2 - Y1 (V): ")
        else:
            self.cursor.cursorY1Label.setText("Y1 (mA): ")
            self.cursor.cursorY2Label.setText("Y2 (mA): ")
            self.cursor.cursorDeltaYLabel.setText("Y2 - Y1 (mA): ")

    else:
        if not self.currentForMathScale:
            self.cursor.cursorY1Label.setText("Y1 (V): ")
            self.cursor.cursorY2Label.setText("Y2 (V): ")
            self.cursor.cursorDeltaYLabel.setText("Y2 - Y1 (V): ")
        else:
            self.cursor.cursorY1Label.setText("Y1 (mA): ")
            self.cursor.cursorY2Label.setText("Y2 (mA): ")
            self.cursor.cursorDeltaYLabel.setText("Y2 - Y1 (mA): ")

    """ NOTA: os valores exibidos nos lineEdits podem ficam errados logo após acionada essa função... As linhas abaixo tentam
    resolver isso, mas causa outros problemas... Pensar melhor nisso..."""
    # #"replotando":
    # self.removeCursorLines()
    # self.y_X1 = np.arange(-6, 6)
    # self.x_X1 = np.ones_like(self.y_X1) * self.X1Value
    # self.X1LineStyle = mkPen(color="white", width=1.7)
    # self.graphicPlottingX1Line = self.mainScr.plot(self.x_X1, self.y_X1, pen=self.X1LineStyle)

    # self.y_X2 = np.arange(-6, 6)
    # self.x_X2 = np.ones_like(self.y_X2) * self.X2Value
    # self.X2LineStyle = mkPen(color="white", width=1.7)
    # self.graphicPlottingX2Line = self.mainScr.plot(self.x_X2, self.y_X2, pen=self.X2LineStyle)

    # self.cursor.cursorY1LE.returnPressed.emit()
    # self.cursor.cursorY2LE.returnPressed.emit()
    
        

def shuntResLineEdit_CH1(self):
    insertedText = self.mainScr2_2.resistorValueLE_CH1.text()
    try:
        resValue = float(insertedText)
        if resValue < 0.001:
            resValue = 0.001
        elif resValue > 1e6:
            resValue = 1e6

        self.shuntRes_CH1 = resValue
        self.currentInVerticalScale()
    
    except(ValueError):
        self.mainScr2_2.resistorValueLE_CH1.setText("1.0")
        self.shuntResLineEdit_CH1()

def shuntResLineEdit_CH2(self):
    insertedText = self.mainScr2_2.resistorValueLE_CH2.text()
    try:
        resValue = float(insertedText)
        if resValue < 0.001:
            resValue = 0.001
        elif resValue > 1e6:
            resValue = 1e6

        self.shuntRes_CH2 = resValue
        self.currentInVerticalScale()
    
    except(ValueError):
        self.mainScr2_2.resistorValueLE_CH2.setText("1.0")
        self.shuntResLineEdit_CH2()

def shuntResLineEdit_Math(self):
    insertedText = self.mainScr2_2.resistorValueLE_Math.text()
    try:
        resValue = float(insertedText)
        if resValue < 0.001:
            resValue = 0.001
        elif resValue > 1e6:
            resValue = 1e6

        self.shuntRes_Math = resValue
        self.currentInVerticalScale()
    
    except(ValueError):
        self.mainScr2_2.resistorValueLE_Math.setText("1.0")
        self.shuntResLineEdit_Math()