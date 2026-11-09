import numpy as np

#Ajuste da escala de Tempo:
def UpdateTimeScale(self, dialValue):

    if self.timeKnob.usefulValue == 0: #1 ms/div
        self.mainScr.setRange(xRange=(0, 0.01), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
        self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.001, 0.002)
    elif self.timeKnob.usefulValue == 1: #2 ms/div
        self.mainScr.setRange(xRange=(0, 0.02), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
        self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.002, 0.004)
    elif self.timeKnob.usefulValue == 2: #5 ms/div
        self.mainScr.setRange(xRange=(0, 0.05), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
        self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.005, 0.010)
    elif self.timeKnob.usefulValue == 3: #10 ms/div
        self.mainScr.setRange(xRange=(0, 0.1), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
        self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.010, 0.020)
    elif self.timeKnob.usefulValue == 4: #20 ms/div
        self.mainScr.setRange(xRange=(0, 0.2), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
        self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.020, 0.040)
    elif self.timeKnob.usefulValue == 5: #50 ms/div
        self.mainScr.setRange(xRange=(0, 0.5), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
        self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.050, 0.100)

    elif self.timeKnob.usefulValue == -1: #0.5 ms/div
        self.mainScr.setRange(xRange=(0, 0.005), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
        self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.0005, 0.001)
    elif self.timeKnob.usefulValue == -2: #200 us/div
        self.mainScr.setRange(xRange=(0, 0.002), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
        self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.0002, 0.0004)
    elif self.timeKnob.usefulValue == -3: #100 us/div
        self.mainScr.setRange(xRange=(0, 0.001), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
        self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.0001, 0.0002)
    
    else: 
        if self.microcontroller == "Raspberry":
            if self.timeKnob.usefulValue == -4: #50 us/div
                self.mainScr.setRange(xRange=(0, 0.0005), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
                self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.00005, 0.0001)
            elif self.timeKnob.usefulValue == -5: #20 us/div
                self.mainScr.setRange(xRange=(0, 0.0002), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
                self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.00002, 0.00004)
            elif self.timeKnob.usefulValue == -6: #10 us/div
                self.mainScr.setRange(xRange=(0, 0.0001), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
                self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.00001, 0.00002)
            elif self.timeKnob.usefulValue == -7: #5 us/div
                self.mainScr.setRange(xRange=(0, 0.00005), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
                self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.000005, 0.00001)
            elif self.timeKnob.usefulValue == -8: #2 us/div
                self.mainScr.setRange(xRange=(0, 0.00002), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
                self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.000002, 0.000004)
            elif self.timeKnob.usefulValue == -9: #1 us/div
                self.mainScr.setRange(xRange=(0, 0.00001), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
                self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.000001, 0.000002)
    
        else: #"Arduino" - escala mínima de 100 us/div
            self.timeKnob.usefulValue = -3
            self.timeKnob.scaleValue = 0.1
            self.mainScr.setRange(xRange=(0, 0.001), yRange=(self.mainScr.yBotLim, self.mainScr.yTopLim))
            self.mainScr.getPlotItem().getAxis('bottom').setTickSpacing(0.0001, 0.0002)


    self.mainScr.timeScale = self.timeKnob.scaleValue
    self.plotUpdate()
    if (self.timeKnob.usefulValue >= 0):
        self.timeLabel.setText(f"Time: {self.mainScr.timeScale:.0f} ms/div")
    elif self.timeKnob.usefulValue > -3:
        self.timeLabel.setText(f"Time: {self.mainScr.timeScale:.1f} ms/div")
    else:
        self.timeLabel.setText(f"Time: {((self.mainScr.timeScale) * 1000):.0f} µs/div")


    if self.btCursor.isOn == True:
        self.x_X1 = np.ones_like(self.y_X1) * self.X1Value
        self.mainScr.removeItem(self.graphicPlottingX1Line)
        self.graphicPlottingX1Line = self.mainScr.plot(self.x_X1, self.y_X1, pen=self.X1LineStyle)

        self.x_X2 = np.ones_like(self.y_X2) * self.X2Value
        self.mainScr.removeItem(self.graphicPlottingX2Line)
        self.graphicPlottingX2Line = self.mainScr.plot(self.x_X2, self.y_X2, pen=self.X2LineStyle)



#Ajustes das escalas de tensão
def UpdateVDivCH1(self, dialValue):
    self.mainScr.vdivCH1Scale = self.vdivCH1Knob.scaleValue
    
    if not self.currentForCH1Scale:
        if self.mainScr.vdivCH1Scale >= 0.5: self.CH1Label.setText(f"CH1: {self.mainScr.vdivCH1Scale} V/div")
        else: self.CH1Label.setText(f"CH1: {(self.mainScr.vdivCH1Scale * 1000):.0f} mV/div")
    else:
        if self.mainScr.vdivCH1Scale/self.shuntRes_CH1 >= 0.5:
            self.CH1Label.setText(f"CH1:\n{(self.mainScr.vdivCH1Scale/self.shuntRes_CH1):.2f} A/div")
        elif self.mainScr.vdivCH1Scale/self.shuntRes_CH1  >= 0.5 * 1e-3:
            self.CH1Label.setText(f"CH1:\n{(self.mainScr.vdivCH1Scale/self.shuntRes_CH1 * 1000):.2f} mA/div")
        else:
            self.CH1Label.setText(f"CH1:\n{(self.mainScr.vdivCH1Scale/self.shuntRes_CH1 * 1e6):.2f} µA/div")
        

    # Atualização da reta do trigger ao alterar a escala vertical do CH1:
    if (self.btTrigger.isOn == True and self.mainScr.referencePhase == "CH1"
            and not self.mainScr.vdivCH1Scale == 1):
        if(self.mainScr.triggerMode == "Manual"):
            self.mainScr.triggerEdgeValue = ((self.triggerKnob.usefulValue / 10) *
                                             self.mainScr.vdivCH1Scale)
        elif self.mainScr.triggerMode == "Automatic":
            self.mainScr.triggerEdgeValue = self.mainScr.CH1MeanValue + self.mainScr.positionOffset_CH1
            self.mainScr.triggerUsefulEdgeValue = self.mainScr.triggerEdgeValue * self.mainScr.vdivCH1Scale
        self.yTrigger = np.ones_like(self.xTrigger) * self.mainScr.triggerEdgeValue
        self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)

        self.triggerProportionLabel.show()
        self.triggerProportionLabel.setText("Trigger line adjusted \nto CH1 V/div scale")
        if self.btTrigger.isOn == True:
            self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")
        self.yTrigger = np.ones_like(self.xTrigger) * self.mainScr.triggerEdgeValue
        self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)
        self.triggerProportionLabel.show()


        if self.btCH1.isOn == True:
            self.triggerProportionLabel.setText("Trigger line adjusted \nto CH1 V/div scale")
    elif self.mainScr.referencePhase == "CH1":
        self.triggerProportionLabel.hide()

    if(self.btCursor.isOn == True and self.mainScr.referencePhase == "CH1"):
        self.y_Y1 = np.ones_like(self.x_Y1) * self.Y1Value / self.mainScr.vdivCH1Scale
        self.mainScr.removeItem(self.graphicPlottingY1Line)
        self.graphicPlottingY1Line = self.mainScr.plot(self.x_Y1, self.y_Y1, pen=self.Y1LineStyle)
        self.y_Y2 = np.ones_like(self.x_Y2) * self.Y2Value / self.mainScr.vdivCH1Scale
        self.mainScr.removeItem(self.graphicPlottingY2Line)
        self.graphicPlottingY2Line = self.mainScr.plot(self.x_Y2, self.y_Y2, pen=self.Y2LineStyle)
    self.plotUpdate()
        
def UpdateVDivCH2(self, dialValue):
    
    self.mainScr.vdivCH2Scale = self.vdivCH2Knob.scaleValue


    if not self.currentForCH2Scale:
        if self.mainScr.vdivCH2Scale >= 0.5: self.CH2Label.setText(f"CH2: {self.mainScr.vdivCH2Scale} V/div")
        else: self.CH2Label.setText(f"CH2: {(self.mainScr.vdivCH2Scale * 1000):.0f} mV/div")
    else:
        if self.mainScr.vdivCH2Scale/self.shuntRes_CH2 >= 0.5:
            self.CH2Label.setText(f"CH2:\n{(self.mainScr.vdivCH2Scale/self.shuntRes_CH2):.2f} A/div")

        elif self.mainScr.vdivCH2Scale/self.shuntRes_CH2  >= 0.5 * 1e-3:
            self.CH2Label.setText(f"CH2:\n{(self.mainScr.vdivCH2Scale/self.shuntRes_CH2 * 1000):.2f} mA/div")
        
        else:
            self.CH2Label.setText(f"CH2:\n{(self.mainScr.vdivCH2Scale/self.shuntRes_CH2 * 1e6):.2f} µA/div")
        

    # Atualização da reta do trigger ao alterar a escala vertical do CH2:
    if (self.btTrigger.isOn == True and self.mainScr.referencePhase == "CH2"
        and not self.mainScr.vdivCH2Scale == 1):
        if (self.mainScr.triggerMode == "Manual"):
            self.mainScr.triggerEdgeValue = ((self.triggerKnob.usefulValue / 10) *
                                             self.mainScr.vdivCH2Scale)
        elif self.mainScr.triggerMode == "Automatic":
            self.mainScr.triggerEdgeValue = self.mainScr.CH2MeanValue + self.mainScr.offset_CH2
            self.mainScr.triggerUsefulEdgeValue = self.mainScr.triggerEdgeValue * self.mainScr.vdivCH2Scale
        self.yTrigger = np.ones_like(self.xTrigger) * self.mainScr.triggerEdgeValue
        self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)
        self.triggerProportionLabel.show()
        self.triggerProportionLabel.setText("Trigger line is adjusted \nto CH2 V/div scale")
        if self.btTrigger.isOn == True:
            self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")
    elif self.mainScr.referencePhase == "CH2":
        self.triggerProportionLabel.hide()

    if (self.btCursor.isOn == True and self.mainScr.referencePhase == "CH2"):
        self.y_Y1 = np.ones_like(self.x_Y1) * self.Y1Value / self.mainScr.vdivCH2Scale
        self.mainScr.removeItem(self.graphicPlottingY1Line)
        self.graphicPlottingY1Line = self.mainScr.plot(self.x_Y1, self.y_Y1, pen=self.Y1LineStyle)
        self.y_Y2 = np.ones_like(self.x_Y2) * self.Y2Value / self.mainScr.vdivCH2Scale
        self.mainScr.removeItem(self.graphicPlottingY2Line)
        self.graphicPlottingY2Line = self.mainScr.plot(self.x_Y2, self.y_Y2, pen=self.Y2LineStyle)
    self.plotUpdate()

def UpdateVDivMath(self, dialValue):
    
    self.mainScr.vdivMathScale = self.vdivMathKnob.scaleValue
    #self.mainScr.notFreeze = True

    if self.mainScr.vdivMathScale >= 0.5: self.mathvDivLabel.setText(f"Math: {self.mainScr.vdivMathScale} V/div")
    else: self.mathvDivLabel.setText(f"Math: {(self.mainScr.vdivMathScale * 1000):.0f} mV/div")

    if not self.currentForMathScale:
        if self.mainScr.vdivMathScale >= 0.5: self.mathvDivLabel.setText(f"Math: {self.mainScr.vdivMathScale} V/div")
        else: self.mathvDivLabel.setText(f"Math: {(self.mainScr.vdivMathScale * 1000):.0f} mV/div")
    else:
        if self.mainScr.vdivMathScale/self.shuntRes_Math >= 0.5:
            self.mathvDivLabel.setText(f"Math:\n{(self.mainScr.vdivMathScale/self.shuntRes_Math):.2f} A/div")

        elif self.mainScr.vdivMathScale/self.shuntRes_Math  >= 0.5 * 1e-3:
            self.mathvDivLabel.setText(f"Math:\n{(self.mainScr.vdivMathScale/self.shuntRes_Math * 1000):.2f} mA/div")
        
        else:
            self.mathvDivLabel.setText(f"Math:\n{(self.mainScr.vdivMathScale/self.shuntRes_Math * 1e6):.2f} µA/div")

    # Atualização da reta do trigger ao alterar a escala vertical do Math:
    if (self.btTrigger.isOn == True and self.mainScr.referencePhase == "Math"
        and not self.mainScr.vdivMathScale == 1):
        if (self.mainScr.triggerMode == "Manual"):
            self.mainScr.triggerEdgeValue = ((self.triggerKnob.usefulValue / 10) *
                                             self.mainScr.vdivMathScale)
        elif self.mainScr.triggerMode == "Automatic":
            self.mainScr.triggerEdgeValue = self.mainScr.mathMeanValue + self.mainScr.positionOffset_Math
            self.mainScr.triggerUsefulEdgeValue = self.mainScr.triggerEdgeValue * self.mainScr.vdivMathScale
        self.yTrigger = np.ones_like(self.xTrigger) * self.mainScr.triggerEdgeValue
        self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)
        self.triggerProportionLabel.show()
        self.triggerProportionLabel.setText("Trigger line adjusted \nto Math V/div scale")
        if self.btTrigger.isOn == True:
            self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")
    elif self.mainScr.referencePhase == "Math":
        self.triggerProportionLabel.hide()

    if (self.btCursor.isOn == True and self.mainScr.referencePhase == "Math"):
        self.y_Y1 = np.ones_like(self.x_Y1) * self.Y1Value / self.mainScr.vdivMathScale
        self.mainScr.removeItem(self.graphicPlottingY1Line)
        self.graphicPlottingY1Line = self.mainScr.plot(self.x_Y1, self.y_Y1, pen=self.Y1LineStyle)
        self.y_Y2 = np.ones_like(self.x_Y2) * self.Y2Value / self.mainScr.vdivMathScale
        self.mainScr.removeItem(self.graphicPlottingY2Line)
        self.graphicPlottingY2Line = self.mainScr.plot(self.x_Y2, self.y_Y2, pen=self.Y2LineStyle)
    self.plotUpdate()

#Ajustes da Posição do sinal exibido
def UpdatePositionCH1(self):
    self.mainScr.positionOffset_CH1 = self.posCH1Knob.usefulValue * (4/40)


    if (self.mainScr.referencePhase == "CH1" and self.mainScr.triggerMode == "Automatic"):
        self.mainScr.triggerEdgeValue = self.mainScr.CH1MeanValue + self.mainScr.positionOffset_CH1
        self.mainScr.triggerUsefulEdgeValue = self.mainScr.triggerEdgeValue * self.mainScr.vdivCH1Scale

        self.yTrigger = np.ones_like(self.xTrigger) * self.mainScr.CH1MeanValue + self.mainScr.positionOffset_CH1
        self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)
        if self.btTrigger.isOn == True:
            self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")

    


    if self.btCH1.isOn and self.btMain.isOn:
        self.posCH1Label.show()

    if(self.posCH1Knob.usefulValue > 0):
        self.posCH1Label.setText(f"CH1 Position \n + {self.posCH1Knob.usefulValue * (4/40) * 
                                                                  self.mainScr.vdivCH1Scale:.2f} V")
    elif(self.posCH1Knob.usefulValue < 0):
        self.posCH1Label.setText(f"CH1 Position \n {self.posCH1Knob.usefulValue * (4/40) * 
                                                                  self.mainScr.vdivCH1Scale:.2f} V")
    else:
        self.posCH1Label.hide()
    self.plotUpdate()




def UpdatePositionCH2(self):

    self.mainScr.positionOffset_CH2 = self.posCH2Knob.usefulValue * (4/40)


    if (self.mainScr.referencePhase == "CH2" and self.mainScr.triggerMode == "Automatic"):
        self.mainScr.triggerEdgeValue = self.mainScr.CH2MeanValue + self.mainScr.positionOffset_CH2
        self.mainScr.triggerUsefulEdgeValue = self.mainScr.triggerEdgeValue * self.mainScr.vdivCH2Scale

        self.yTrigger = np.ones_like(self.xTrigger) * self.mainScr.CH2MeanValue + self.mainScr.positionOffset_CH2
        self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)
        if self.btTrigger.isOn == True:
            self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")

    

    if self.btCH2.isOn and self.btMain.isOn:
        self.posCH2Label.show()

    if (self.posCH2Knob.usefulValue > 0):
        self.posCH2Label.setText(f"CH2 Position \n + "
                                 f"{self.posCH2Knob.usefulValue  * (4/40) *
                                    self.mainScr.vdivCH2Scale:.2f} V")
    elif(self.posCH2Knob.usefulValue < 0):
        self.posCH2Label.setText(f"CH2 Position \n {self.posCH2Knob.usefulValue * (4/40) *
                                                    self.mainScr.vdivCH2Scale:.2f} V")
    else:
        self.posCH2Label.hide()
    self.plotUpdate()

def UpdatePositionMath(self):
    self.mainScr.positionOffset_Math = self.posMathKnob.usefulValue * (4/40)

    if (self.mainScr.referencePhase == "Math" and self.mainScr.triggerMode == "Automatic"):
        self.mainScr.triggerEdgeValue = self.mainScr.mathMeanValue + self.mainScr.positionOffset_Math
        self.mainScr.triggerUsefulEdgeValue = self.mainScr.triggerEdgeValue * self.mainScr.vdivMathScale

        self.yTrigger = np.ones_like(self.xTrigger) * self.mainScr.mathMeanValue + self.mainScr.positionOffset_Math
        self.graphicPlottingTrigger.setData(self.xTrigger, self.yTrigger)
        if self.btTrigger.isOn == True:
            self.triggerLabel.setText(f"Trigger \n{self.mainScr.triggerUsefulEdgeValue:.1f} V")



    if self.btMath.isOn and self.btMain.isOn:
        self.mathPosLabel.show()

    if(self.posMathKnob.usefulValue > 0):
        self.mathPosLabel.setText(f"Math Position \n + {self.posMathKnob.usefulValue * (4/40) * 
                                                                  self.mainScr.vdivMathScale:.2f} V")
    elif(self.posMathKnob.usefulValue < 0):
        self.mathPosLabel.setText(f"Math Position \n {self.posMathKnob.usefulValue * (4/40) * 
                                                                  self.mainScr.vdivMathScale:.2f} V")
    else:
        self.mathPosLabel.hide()
    self.plotUpdate()

def plotUpdate(self):
    self.mainScr.visibleWindow = int(10 * (self.mainScr.timeScale/1000)/self.mainScr.samplingPeriod)
    self.mainScr.decimation = max(1, int(self.mainScr.visibleWindow/self.mainScr.max_visible_points))
    self.mainScr.x_plot = self.mainScr.x[: self.mainScr.visibleWindow]
    y_temp_CH1 = (self.mainScr.y_CH1_copy[: self.mainScr.visibleWindow] / self.mainScr.vdivCH1Scale) + self.mainScr.positionOffset_CH1
    y_temp_CH2 = (self.mainScr.y_CH2_copy[: self.mainScr.visibleWindow] / self.mainScr.vdivCH2Scale) + self.mainScr.positionOffset_CH2
    y_temp_Math = (self.mainScr.y_Math_copy[: self.mainScr.visibleWindow] / self.mainScr.vdivMathScale) + self.mainScr.positionOffset_Math


    self.mainScr.graphicPlotting_CH1.setData(self.mainScr.x_plot[::self.mainScr.decimation], y_temp_CH1[::self.mainScr.decimation])
    self.mainScr.graphicPlotting_CH2.setData(self.mainScr.x_plot[::self.mainScr.decimation], y_temp_CH2[::self.mainScr.decimation])
    self.mainScr.graphicPlotting_Math.setData(self.mainScr.x_plot[::self.mainScr.decimation], y_temp_Math[::self.mainScr.decimation])



