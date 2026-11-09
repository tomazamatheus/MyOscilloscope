import numpy as np
from PySide6.QtCore import Qt


#Métodos de Trigger
#NOTA: Para procurar a seção do código sobre como o trigger é aplicado na interface, ir para classe DataHandler() em MainScreen1.py

def TriggerActivated(self):
    if self.btOnOff.isOn == True and self.screenName == "Main"\
            and self.btTrigger.isOn == True:
        self.secondaryScreenName = "Trigger"
        self.secondaryScreen.setCurrentIndex(1)
        self.triggerKnob.buttonIsOn = True
        self.graphicPlottingTrigger = self.mainScr.plot(self.xTrigger, self.yTrigger, pen=self.graphTriggerLine)
        self.triggerLabel.show()
        self.mainScr.measureTime = True
        self.triggerKnob.changeImage("images/Knob2_OrangeSimple.png")

        if (self.mainScr.triggerMode == "Automatic" and self.mainScr.referencePhase == "CH1"):
            self.yTrigger = (np.ones_like(self.xTrigger) *
                             self.CH1MeanValue + self.mainScr.positionOffset_CH1)
            self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)
            self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")

        elif (self.mainScr.triggerMode == "Automatic" and self.mainScr.referencePhase == "CH2"):
            self.yTrigger = (np.ones_like(self.xTrigger) *
                             self.CH2MeanValue + self.mainScr.positionOffset_CH2)
            self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)
            self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")

        elif (self.mainScr.triggerMode == "Automatic" and self.mainScr.referencePhase == "Math"):
            self.yTrigger = (np.ones_like(self.xTrigger) *
                             self.mathMeanValue + self.mainScr.positionOffset_Math)
            self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)
            self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")
    else:
        self.btTrigger._update_visual()
        
        
        self.triggerKnob.buttonIsOn = False
        self.mainScr.removeItem(self.graphicPlottingTrigger)
        self.triggerLabel.hide()

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

    if self.btTrigger.isOn == True:

        if self.mainScr.referencePhase == "CH1" and not self.mainScr.vdivCH1Scale == 1\
                and self.btCH1.isOn == True:
            self.triggerProportionLabel.show()
            if self.language == "English": self.triggerProportionLabel.setText("Trigger line adjusted \nto CH1 V/div scale")
            else: self.triggerProportionLabel.setText("Linha do trigger sob \nescala de V/div do CH1")
        elif self.mainScr.referencePhase == "CH2" and not self.mainScr.vdivCH2Scale == 1\
                and self.btCH2.isOn == True:
            self.triggerProportionLabel.show()
            if self.language == "English": self.triggerProportionLabel.setText("Trigger line adjusted \nto CH2 V/div scale")
            else: self.triggerProportionLabel.setText("Linha do trigger sob \nescala de V/div do CH2")
        elif self.mainScr.referencePhase == "Math" and not self.mainScr.vdivMathScale == 1\
                and self.btMath.isOn == True:
            self.triggerProportionLabel.show()
            if self.language == "English": self.triggerProportionLabel.setText("Trigger line adjusted \nto Math V/div scale")
            else: self.triggerProportionLabel.setText("Linha do trigger sob \nescala de V/div do Math")
        else:
            self.triggerProportionLabel.hide()
    else:
        self.triggerProportionLabel.hide()
        self.triggerKnob.changeImage("images/Knob2.png")
        self.measureTime = False
    self.UpdateSecondaryButtons()

# Métodos das combo boxes da tela de Trigger (screen 2)


def TrigTypeCBChanged(self):
    if self.trigger.trigTypeCB.currentText() == "Rising Edge":
        self.mainScr.triggerType = "Rising Edge"
    else:
        self.mainScr.triggerType = "Falling Edge"

def TrigModeCBChanged(self):
    if self.trigger.trigModeCB.currentText() == "Manual":
        self.mainScr.triggerMode = "Manual"
    else:
        self.mainScr.triggerMode = "Automatic"

        if (self.mainScr.referencePhase == "CH1"):
            self.mainScr.triggerEdgeValue = self.mainScr.CH1MeanValue + self.mainScr.positionOffset_CH1
            self.mainScr.triggerUsefulEdgeValue = self.mainScr.triggerEdgeValue * self.mainScr.vdivCH1Scale

            self.yTrigger = (np.ones_like(self.xTrigger) *
                             self.mainScr.CH1MeanValue + self.mainScr.positionOffset_CH1)
            self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)

        if (self.mainScr.referencePhase == "CH2"):
            self.mainScr.triggerEdgeValue = self.mainScr.CH2MeanValue + self.mainScr.positionOffset_CH2
            self.mainScr.triggerUsefulEdgeValue = self.mainScr.triggerEdgeValue * self.mainScr.vdivCH2Scale
            self.yTrigger = (np.ones_like(self.xTrigger) *
                             self.mainScr.CH2MeanValue + self.mainScr.positionOffset_CH2)
            self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)
        self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")

def UpdateTriggerLine(self):

    if self.mainScr.triggerMode == "Manual":
        if(self.mainScr.referencePhase == "CH1"):
            self.mainScr.triggerEdgeValue = (self.triggerKnob.usefulValue / 10) / self.mainScr.vdivCH1Scale
            self.mainScr.triggerUsefulEdgeValue = self.mainScr.triggerEdgeValue * self.mainScr.vdivCH1Scale
        elif(self.mainScr.referencePhase == "CH2"):
            self.mainScr.triggerEdgeValue = (self.triggerKnob.usefulValue / 10) / self.mainScr.vdivCH2Scale
            self.mainScr.triggerUsefulEdgeValue = self.mainScr.triggerEdgeValue * self.mainScr.vdivCH2Scale
        elif (self.mainScr.referencePhase == "Math"):
            self.mainScr.triggerEdgeValue = (self.triggerKnob.usefulValue / 10) / self.mainScr.vdivMathScale
            self.mainScr.triggerUsefulEdgeValue = self.mainScr.triggerEdgeValue * self.mainScr.vdivMathScale
        self.yTrigger = np.ones_like(self.xTrigger) * self.mainScr.triggerEdgeValue
        self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")

    else: #referencePhase = "Automatic"
        if(self.mainScr.referencePhase == "CH1"):
            self.mainScr.triggerEdgeValue = self.mainScr.CH1MeanValue + self.mainScr.positionOffset_CH1
            self.mainScr.triggerUsefulEdgeValue = self.mainScr.CH1MeanValue * self.mainScr.vdivCH1Scale + self.mainScr.positionOffset_CH1
            self.yTrigger = np.ones_like(self.xTrigger) * self.mainScr.CH1MeanValue + self.mainScr.positionOffset_CH1
            self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")

        elif (self.mainScr.referencePhase == "CH2"):
            self.mainScr.triggerEdgeValue = self.mainScr.CH2MeanValue + self.mainScr.positionOffset_CH2
            self.mainScr.triggerUsefulEdgeValue = self.mainScr.CH2MeanValue * self.mainScr.vdivCH2Scale + self.mainScr.positionOffset_CH2
            self.yTrigger = np.ones_like(self.xTrigger) * self.mainScr.CH2MeanValue + self.mainScr.positionOffset_CH2
            self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")

        elif (self.mainScr.referencePhase == "Math"):
            self.mainScr.triggerEdgeValue = self.mainScr.mathMeanValue + self.mainScr.positionOffset_Math
            self.mainScr.triggerUsefulEdgeValue = self.mainScr.mathMeanValue * self.mainScr.vdivMathScale + self.mainScr.positionOffset_Math
            self.yTrigger = np.ones_like(self.xTrigger) * self.mainScr.mathMeanValue + self.mainScr.positionOffset_Math
            self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")


    if self.mainScr.referencePhase == "CH1":
        if (self.triggerKnob.usefulValue / 10 < 1.2 * self.mainScr.yTopLim /self.mainScr.vdivCH1Scale
                and self.triggerKnob.usefulValue / 10 > 1.2 * self.mainScr.yBotLim /self.mainScr.vdivCH1Scale
                and self.btTrigger.isOn == True):
            self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)

    elif self.mainScr.referencePhase == "CH2":
        if (self.triggerKnob.usefulValue / 10  * self.mainScr.vdivCH2Scale< 1.2 * self.mainScr.yTopLim
                and self.triggerKnob.usefulValue / 10 * self.mainScr.vdivCH2Scale > 1.2 * self.mainScr.yBotLim
                and self.btTrigger.isOn == True):
            self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)

    elif self.mainScr.referencePhase == "Math":
        if (self.triggerKnob.usefulValue / 10  * self.mainScr.vdivMathScale < 1.2 * self.mainScr.yTopLim
                and self.triggerKnob.usefulValue / 10 * self.mainScr.vdivMathScale > 1.2 * self.mainScr.yBotLim
                and self.btTrigger.isOn == True):
            self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)

    self.mainScr.dataHandler.triggerValue = self.mainScr.triggerUsefulEdgeValue

    if self.mainScr.triggerUsefulEdgeValue < self.yMaxTrig and self.mainScr.triggerUsefulEdgeValue > self.yMinTrig:
        self.mainScr.dataHandler.triggerPossible = True
    else:
        self.mainScr.dataHandler.triggerPossible = False