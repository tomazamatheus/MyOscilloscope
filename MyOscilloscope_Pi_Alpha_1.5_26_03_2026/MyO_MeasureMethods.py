from PySide6.QtCore import Qt

#Métodos de Measure

def MeasureActivated(self):
    if self.btOnOff.isOn == True and self.btMeas.isOn == True and not self.screenName == "":
        self.secondaryScreenName = "Measure"
        self.secondaryScreen.setCurrentIndex(2)
        if not self.calibManual_isOn:
            if(self.btCH1.isOn and self.mainScr.triggerChannel == "CH1"
                or self.btCH2.isOn and self.mainScr.triggerChannel == "CH2"
                or self.btMath.isOn and self.mainScr.triggerChannel == "Math"):
                self.phaseLabel.show()
                self.phaseLabel.raise_()
            if self.language == "English":
                if self.mainScr.referencePhase == "CH1":
                    self.phaseLabel.setText("Reference Channel: \nCH1")
                elif self.mainScr.referencePhase == "CH2":
                    self.phaseLabel.setText("Reference Channel: \nCH2")
                elif self.mainScr.referencePhase == "Math":
                    self.phaseLabel.setText("Reference Channel: \nMath")
            else:
                if self.mainScr.referencePhase == "CH1":
                    self.phaseLabel.setText("Canal de Ref.: \nCH1")
                elif self.mainScr.referencePhase == "CH2":
                    self.phaseLabel.setText("Canal de Ref.: \nCH2")
                elif self.mainScr.referencePhase == "Math":
                    self.phaseLabel.setText("Canal de Ref.: \nMath")

    else:
        self.btMeas._update_visual()
        
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


        if not self.screenName == "Phas Diag": self.phaseLabel.hide()

    self.UpdateSecondaryButtons()
    if(self.btCH1.isOn == False and self.mainScr.triggerChannel == "CH1"
        or self.btCH2.isOn == False and self.mainScr.triggerChannel == "CH2"
        or self.btMath.isOn == False and self.mainScr.triggerChannel == "Math"): self.phaseLabel.lower()

def MeasChannelSelectCBChanged(self):
    if self.measure.channelSelectCB.currentText() == "CH1":
        self.measChannelSelected = "CH1"
    elif self.measure.channelSelectCB.currentText() == "CH2":
        self.measChannelSelected = "CH2"
    elif self.measure.channelSelectCB.currentText() == "Math":
        self.measChannelSelected = "Math"

def UpdateMeasure(self):
    if self.measChannelSelected == "CH1":

        if self.freqCH1 < 1000:
            self.measure.freqLE.setText(f"{self.freqCH1:.3f} Hz")
        else:
            self.measure.freqLE.setText(f"{(self.freqCH1/1000):.3f} kHz")

        if self.periodCH1 > 0.001:
            self.measure.periodLE.setText(f"{(self.periodCH1 * 1000):.3f} ms")
        elif self.periodCH1 > 0.000001:
            self.measure.periodLE.setText(f"{(self.periodCH1 * 1000000):.3f} us")
        else:
            self.measure.periodLE.setText(f"< 1 us")

        if not self.currentForCH1Scale:
            if self.CH1MeanValue > 0.9 or self.CH1MeanValue < -0.9:
                self.measure.meanLE.setText(f"{self.CH1MeanValue:.3f} V")
            elif self.CH1MeanValue > 0.001 or self.CH1MeanValue < -0.001:
                self.measure.meanLE.setText(f"{(self.CH1MeanValue * 1000):.2f} mV")
            elif self.CH1MeanValue > 0.000001 or self.CH1MeanValue < -0.000001:
                self.measure.meanLE.setText(f"{(self.CH1MeanValue * 1000000):.1f} µV")

            if self.CH1VppValue > 0.9 or self.CH1VppValue < -0.9:
                self.measure.vppLE.setText(f"{self.CH1VppValue:.2f} V")
            elif self.CH1VppValue > 0.001 or self.CH1VppValue < -0.001:
                self.measure.vppLE.setText(f"{(self.CH1VppValue * 1000):.2f} mV")
            elif self.CH1VppValue > 0.000001 or self.CH1VppValue < -0.000001:
                self.measure.vppLE.setText(f"{(self.CH1VppValue * 1000000):.2f} µV")

            if self.CH1VRMSValue > 0.9 or self.CH1VRMSValue < -0.9:
                self.measure.vrmsLE.setText(f"{self.CH1VRMSValue:.2f} V")
            elif self.CH1VRMSValue > 0.001 or self.CH1VRMSValue < -0.001:
                self.measure.vrmsLE.setText(f"{(self.CH1VRMSValue * 1000):.2f} mV")
            elif self.CH1VRMSValue > 0.000001 or self.CH1VRMSValue < -0.000001:
                self.measure.vrmsLE.setText(f"{(self.CH1VRMSValue * 1000000):.2f} µV")

            if self.yMaxCH1 > 0.9 or self.yMaxCH1 < -0.9:
                self.measure.maxLE.setText(f"{self.yMaxCH1:.2f} V")
            elif self.yMaxCH1 > 0.001 or self.yMaxCH1 < -0.001:
                self.measure.maxLE.setText(f"{(self.yMaxCH1 * 1000):.2f} mV")
            elif self.yMaxCH1 > 0.000001 or self.yMaxCH1 < -0.000001:
                self.measure.maxLE.setText(f"{(self.yMaxCH1 * 1000000):.2f} µV")

            if self.yMinCH1 > 0.9 or self.yMinCH1 < -0.9:
                self.measure.minLE.setText(f"{self.yMinCH1:.2f} V")
            elif self.yMinCH1 > 0.001 or self.yMinCH1 < -0.001:
                self.measure.minLE.setText(f"{(self.yMinCH1 * 1000):.2f} mV")
            elif self.yMinCH1 > 0.000001 or self.yMinCH1 < -0.000001:
                self.measure.minLE.setText(f"{(self.yMinCH1 * 1000000):.2f} µV")

        else:
            if self.CH1MeanValue/self.shuntRes_CH1 > 0.9 or self.CH1MeanValue/self.shuntRes_CH1 < -0.9:
                self.measure.meanLE.setText(f"{self.CH1MeanValue/self.shuntRes_CH1:.3f} A")
            elif self.CH1MeanValue/self.shuntRes_CH1 > 0.001 or self.CH1MeanValue/self.shuntRes_CH1 < -0.001:
                self.measure.meanLE.setText(f"{(self.CH1MeanValue/self.shuntRes_CH1 * 1000):.2f} mA")
            elif self.CH1MeanValue/self.shuntRes_CH1 > 0.000001 or self.CH1MeanValue/self.shuntRes_CH1 < -0.000001:
                self.measure.meanLE.setText(f"{(self.CH1MeanValue/self.shuntRes_CH1 * 1000000):.1f} µA")

            if self.CH1VppValue/self.shuntRes_CH1 > 0.9 or self.CH1VppValue/self.shuntRes_CH1 < -0.9:
                self.measure.vppLE.setText(f"{self.CH1VppValue/self.shuntRes_CH1:.2f} A")
            elif self.CH1VppValue/self.shuntRes_CH1 > 0.001 or self.CH1VppValue/self.shuntRes_CH1 < -0.001:
                self.measure.vppLE.setText(f"{(self.CH1VppValue/self.shuntRes_CH1 * 1000):.2f} mA")
            elif self.CH1VppValue/self.shuntRes_CH1 > 0.000001 or self.CH1VppValue/self.shuntRes_CH1 < -0.000001:
                self.measure.vppLE.setText(f"{(self.CH1VppValue/self.shuntRes_CH1 * 1000000):.2f} µA")

            if self.CH1VRMSValue/self.shuntRes_CH1 > 0.9 or self.CH1VRMSValue/self.shuntRes_CH1 < -0.9:
                self.measure.vrmsLE.setText(f"{self.CH1VRMSValue/self.shuntRes_CH1:.2f} A")
            elif self.CH1VRMSValue/self.shuntRes_CH1 > 0.001 or self.CH1VRMSValue/self.shuntRes_CH1 < -0.001:
                self.measure.vrmsLE.setText(f"{(self.CH1VRMSValue/self.shuntRes_CH1 * 1000):.2f} mA")
            elif self.CH1VRMSValue/self.shuntRes_CH1 > 0.000001 or self.CH1VRMSValue/self.shuntRes_CH1 < -0.000001:
                self.measure.vrmsLE.setText(f"{(self.CH1VRMSValue/self.shuntRes_CH1 * 1000000):.2f} µA")

            if self.yMaxCH1/self.shuntRes_CH1 > 0.9 or self.yMaxCH1/self.shuntRes_CH1 < -0.9:
                self.measure.maxLE.setText(f"{self.yMaxCH1/self.shuntRes_CH1:.2f} A")
            elif self.yMaxCH1/self.shuntRes_CH1 > 0.001 or self.yMaxCH1/self.shuntRes_CH1 < -0.001:
                self.measure.maxLE.setText(f"{(self.yMaxCH1/self.shuntRes_CH1 * 1000):.2f} mA")
            elif self.yMaxCH1/self.shuntRes_CH1 > 0.000001 or self.yMaxCH1/self.shuntRes_CH1 < -0.000001:
                self.measure.maxLE.setText(f"{(self.yMaxCH1/self.shuntRes_CH1 * 1000000):.2f} µA")

            if self.yMinCH1/self.shuntRes_CH1 > 0.9 or self.yMinCH1/self.shuntRes_CH1 < -0.9:
                self.measure.minLE.setText(f"{self.yMinCH1/self.shuntRes_CH1:.2f} A")
            elif self.yMinCH1/self.shuntRes_CH1 > 0.001 or self.yMinCH1/self.shuntRes_CH1 < -0.001:
                self.measure.minLE.setText(f"{(self.yMinCH1/self.shuntRes_CH1 * 1000):.2f} mA")
            elif self.yMinCH1/self.shuntRes_CH1 > 0.000001 or self.yMinCH1/self.shuntRes_CH1 < -0.000001:
                self.measure.minLE.setText(f"{(self.yMinCH1/self.shuntRes_CH1 * 1000000):.2f} µA")


        self.measure.phaseLE.setText(f"{self.CH1Phase:.1f}°")
        


    elif self.measChannelSelected == "CH2":

        if self.freqCH2 < 1000:
            self.measure.freqLE.setText(f"{self.freqCH2:.3f} Hz")
        else:
            self.measure.freqLE.setText(f"{(self.freqCH2 / 1000):.3f} kHz")

        if self.periodCH2 > 0.001:
            self.measure.periodLE.setText(f"{(self.periodCH2 * 1000):.3f} ms")
        elif self.periodCH2 > 0.000001:
            self.measure.periodLE.setText(f"{(self.periodCH2 * 1000000):.3f} us")
        else:
            self.measure.periodLE.setText(f"< 1 us")

        if not self.currentForCH2Scale:
            if self.CH2MeanValue > 0.9 or self.CH2MeanValue < -0.9:
                self.measure.meanLE.setText(f"{self.CH2MeanValue:.3f} V")
            elif self.CH2MeanValue > 0.001 or self.CH2MeanValue < -0.001:
                self.measure.meanLE.setText(f"{(self.CH2MeanValue * 1000):.2f} mV")
            elif self.CH2MeanValue > 0.000001 or self.CH2MeanValue < -0.000001:
                self.measure.meanLE.setText(f"{(self.CH2MeanValue * 1000000):.1f} µV")

            if self.CH2VppValue > 0.9 or self.CH2VppValue < -0.9:
                self.measure.vppLE.setText(f"{self.CH2VppValue:.2f} V")
            elif self.CH2VppValue > 0.001 or self.CH2VppValue < -0.001:
                self.measure.vppLE.setText(f"{(self.CH2VppValue * 1000):.2f} mV")
            elif self.CH2VppValue > 0.000001 or self.CH2VppValue < -0.000001:
                self.measure.vppLE.setText(f"{(self.CH2VppValue * 1000000):.2f} µV")

            if self.CH2VRMSValue > 0.9 or self.CH2VRMSValue < -0.9:
                self.measure.vrmsLE.setText(f"{self.CH2VRMSValue:.2f} V")
            elif self.CH2VRMSValue > 0.001 or self.CH2VRMSValue < -0.001:
                self.measure.vrmsLE.setText(f"{(self.CH2VRMSValue * 1000):.2f} mV")
            elif self.CH2VRMSValue > 0.000001 or self.CH2VRMSValue < -0.000001:
                self.measure.vrmsLE.setText(f"{(self.CH2VRMSValue * 1000000):.2f} µV")

            if self.yMaxCH2 > 0.9 or self.yMaxCH2 < -0.9:
                self.measure.maxLE.setText(f"{self.yMaxCH2:.2f} V")
            elif self.yMaxCH2 > 0.001 or self.yMaxCH2 < -0.001:
                self.measure.maxLE.setText(f"{(self.yMaxCH2 * 1000):.2f} mV")
            elif self.yMaxCH2 > 0.000001 or self.yMaxCH2 < -0.000001:
                self.measure.maxLE.setText(f"{(self.yMaxCH2 * 1000000):.2f} µV")

            if self.yMinCH2 > 0.9 or self.yMinCH2 < -0.9:
                self.measure.minLE.setText(f"{self.yMinCH2:.2f} V")
            elif self.yMinCH2 > 0.001 or self.yMinCH2 < -0.001:
                self.measure.minLE.setText(f"{(self.yMinCH2 * 1000):.2f} mV")
            elif self.yMinCH2 > 0.000001 or self.yMinCH2 < -0.000001:
                self.measure.minLE.setText(f"{(self.yMinCH2 * 1000000):.2f} µV")

        else:
            if self.CH2MeanValue/self.shuntRes_CH2 > 0.9 or self.CH2MeanValue/self.shuntRes_CH2 < -0.9:
                self.measure.meanLE.setText(f"{self.CH2MeanValue/self.shuntRes_CH2:.3f} A")
            elif self.CH2MeanValue/self.shuntRes_CH2 > 0.001 or self.CH2MeanValue/self.shuntRes_CH2 < -0.001:
                self.measure.meanLE.setText(f"{(self.CH2MeanValue/self.shuntRes_CH2 * 1000):.2f} mA")
            elif self.CH2MeanValue/self.shuntRes_CH2 > 0.000001 or self.CH2MeanValue/self.shuntRes_CH2 < -0.000001:
                self.measure.meanLE.setText(f"{(self.CH2MeanValue/self.shuntRes_CH2 * 1000000):.1f} µA")

            if self.CH2VppValue/self.shuntRes_CH2 > 0.9 or self.CH2VppValue/self.shuntRes_CH2 < -0.9:
                self.measure.vppLE.setText(f"{self.CH2VppValue/self.shuntRes_CH2:.2f} A")
            elif self.CH2VppValue/self.shuntRes_CH2 > 0.001 or self.CH2VppValue/self.shuntRes_CH2 < -0.001:
                self.measure.vppLE.setText(f"{(self.CH2VppValue/self.shuntRes_CH2 * 1000):.2f} mA")
            elif self.CH2VppValue/self.shuntRes_CH2 > 0.000001 or self.CH2VppValue/self.shuntRes_CH2 < -0.000001:
                self.measure.vppLE.setText(f"{(self.CH2VppValue/self.shuntRes_CH2 * 1000000):.2f} µA")

            if self.CH2VRMSValue/self.shuntRes_CH2 > 0.9 or self.CH2VRMSValue/self.shuntRes_CH2 < -0.9:
                self.measure.vrmsLE.setText(f"{self.CH2VRMSValue/self.shuntRes_CH2:.2f} A")
            elif self.CH2VRMSValue/self.shuntRes_CH2 > 0.001 or self.CH2VRMSValue/self.shuntRes_CH2 < -0.001:
                self.measure.vrmsLE.setText(f"{(self.CH2VRMSValue/self.shuntRes_CH2 * 1000):.2f} mA")
            elif self.CH2VRMSValue/self.shuntRes_CH2 > 0.000001 or self.CH2VRMSValue/self.shuntRes_CH2 < -0.000001:
                self.measure.vrmsLE.setText(f"{(self.CH2VRMSValue/self.shuntRes_CH2 * 1000000):.2f} µA")

            if self.yMaxCH2/self.shuntRes_CH2 > 0.9 or self.yMaxCH2/self.shuntRes_CH2 < -0.9:
                self.measure.maxLE.setText(f"{self.yMaxCH2/self.shuntRes_CH2:.2f} A")
            elif self.yMaxCH2/self.shuntRes_CH2 > 0.001 or self.yMaxCH2/self.shuntRes_CH2 < -0.001:
                self.measure.maxLE.setText(f"{(self.yMaxCH2/self.shuntRes_CH2 * 1000):.2f} mA")
            elif self.yMaxCH2/self.shuntRes_CH2 > 0.000001 or self.yMaxCH2/self.shuntRes_CH2 < -0.000001:
                self.measure.maxLE.setText(f"{(self.yMaxCH2/self.shuntRes_CH2 * 1000000):.2f} µA")

            if self.yMinCH2/self.shuntRes_CH2 > 0.9 or self.yMinCH2/self.shuntRes_CH2 < -0.9:
                self.measure.minLE.setText(f"{self.yMinCH2/self.shuntRes_CH2:.2f} A")
            elif self.yMinCH2/self.shuntRes_CH2 > 0.001 or self.yMinCH2/self.shuntRes_CH2 < -0.001:
                self.measure.minLE.setText(f"{(self.yMinCH2/self.shuntRes_CH2 * 1000):.2f} mA")
            elif self.yMinCH2/self.shuntRes_CH2 > 0.000001 or self.yMinCH2/self.shuntRes_CH2 < -0.000001:
                self.measure.minLE.setText(f"{(self.yMinCH2/self.shuntRes_CH2 * 1000000):.2f} µA")

        self.measure.phaseLE.setText(f"{self.CH2Phase:.1f}°")
        

    elif self.measChannelSelected == "Math":

        if self.freqMath < 1000:
            self.measure.freqLE.setText(f"{self.freqMath:.3f} Hz")
        else:
            self.measure.freqLE.setText(f"{(self.freqMath / 1000):.3f} kHz")

        if self.periodMath > 0.001:
            self.measure.periodLE.setText(f"{(self.periodMath * 1000):.3f} ms")
        elif self.periodMath > 0.000001:
            self.measure.periodLE.setText(f"{(self.periodMath * 1000000):.3f} us")
        else:
            self.measure.periodLE.setText(f"< 1 us")

        if not self.currentForMathScale:
            if self.mathMeanValue > 0.9 or self.mathMeanValue < -0.9:
                self.measure.meanLE.setText(f"{self.mathMeanValue:.3f} V")
            elif self.mathMeanValue > 0.001 or self.mathMeanValue < -0.001:
                self.measure.meanLE.setText(f"{(self.mathMeanValue * 1000):.2f} mV")
            elif self.mathMeanValue > 0.000001 or self.mathMeanValue < -0.000001:
                self.measure.meanLE.setText(f"{(self.mathMeanValue * 1000000):.1f} µV")

            if self.mathVppValue > 0.9 or self.mathVppValue < -0.9:
                self.measure.vppLE.setText(f"{self.mathVppValue:.2f} V")
            elif self.mathVppValue > 0.001 or self.mathVppValue < -0.001:
                self.measure.vppLE.setText(f"{(self.mathVppValue * 1000):.2f} mV")
            elif self.mathVppValue > 0.000001 or self.mathVppValue < -0.000001:
                self.measure.vppLE.setText(f"{(self.mathVppValue * 1000000):.2f} µV")

            if self.mathVRMSValue > 0.9 or self.mathVRMSValue < -0.9:
                self.measure.vrmsLE.setText(f"{self.mathVRMSValue:.2f} V")
            elif self.mathVRMSValue > 0.001 or self.mathVRMSValue < -0.001:
                self.measure.vrmsLE.setText(f"{(self.mathVRMSValue * 1000):.2f} mV")
            elif self.mathVRMSValue > 0.000001 or self.mathVRMSValue < -0.000001:
                self.measure.vrmsLE.setText(f"{(self.mathVRMSValue * 1000000):.2f} µV")

            if self.yMaxMath > 0.9 or self.yMaxMath < -0.9:
                self.measure.maxLE.setText(f"{self.yMaxMath:.2f} V")
            elif self.yMaxMath > 0.001 or self.yMaxMath < -0.001:
                self.measure.maxLE.setText(f"{(self.yMaxMath * 1000):.2f} mV")
            elif self.yMaxMath > 0.000001 or self.yMaxMath < -0.000001:
                self.measure.maxLE.setText(f"{(self.yMaxMath * 1000000):.2f} µV")

            if self.yMinMath > 0.9 or self.yMinMath < -0.9:
                self.measure.minLE.setText(f"{self.yMinMath:.2f} V")
            elif self.yMinMath > 0.001 or self.yMinMath < -0.001:
                self.measure.minLE.setText(f"{(self.yMinMath * 1000):.2f} mV")
            elif self.yMinMath > 0.000001 or self.yMinMath < -0.000001:
                self.measure.minLE.setText(f"{(self.yMinMath * 1000000):.2f} µV")
        
        else:
            if self.mathMeanValue/self.shuntRes_Math > 0.9 or self.mathMeanValue/self.shuntRes_Math < -0.9:
                self.measure.meanLE.setText(f"{self.mathMeanValue/self.shuntRes_Math:.3f} A")
            elif self.mathMeanValue/self.shuntRes_Math > 0.001 or self.mathMeanValue/self.shuntRes_Math < -0.001:
                self.measure.meanLE.setText(f"{(self.mathMeanValue/self.shuntRes_Math * 1000):.2f} mA")
            elif self.mathMeanValue/self.shuntRes_Math > 0.000001 or self.mathMeanValue/self.shuntRes_Math < -0.000001:
                self.measure.meanLE.setText(f"{(self.mathMeanValue/self.shuntRes_Math * 1000000):.1f} µA")

            if self.mathVppValue/self.shuntRes_Math > 0.9 or self.mathVppValue/self.shuntRes_Math < -0.9:
                self.measure.vppLE.setText(f"{self.mathVppValue/self.shuntRes_Math:.2f} A")
            elif self.mathVppValue/self.shuntRes_Math > 0.001 or self.mathVppValue/self.shuntRes_Math < -0.001:
                self.measure.vppLE.setText(f"{(self.mathVppValue/self.shuntRes_Math * 1000):.2f} mA")
            elif self.mathVppValue/self.shuntRes_Math > 0.000001 or self.mathVppValue/self.shuntRes_Math < -0.000001:
                self.measure.vppLE.setText(f"{(self.mathVppValue/self.shuntRes_Math * 1000000):.2f} µA")

            if self.mathVRMSValue/self.shuntRes_Math > 0.9 or self.mathVRMSValue/self.shuntRes_Math < -0.9:
                self.measure.vrmsLE.setText(f"{self.mathVRMSValue/self.shuntRes_Math:.2f} A")
            elif self.mathVRMSValue/self.shuntRes_Math > 0.001 or self.mathVRMSValue/self.shuntRes_Math < -0.001:
                self.measure.vrmsLE.setText(f"{(self.mathVRMSValue/self.shuntRes_Math * 1000):.2f} mA")
            elif self.mathVRMSValue/self.shuntRes_Math > 0.000001 or self.mathVRMSValue/self.shuntRes_Math < -0.000001:
                self.measure.vrmsLE.setText(f"{(self.mathVRMSValue/self.shuntRes_Math * 1000000):.2f} µA")

            if self.yMaxMath/self.shuntRes_Math > 0.9 or self.yMaxMath/self.shuntRes_Math < -0.9:
                self.measure.maxLE.setText(f"{self.yMaxMath/self.shuntRes_Math:.2f} A")
            elif self.yMaxMath/self.shuntRes_Math > 0.001 or self.yMaxMath/self.shuntRes_Math < -0.001:
                self.measure.maxLE.setText(f"{(self.yMaxMath/self.shuntRes_Math * 1000):.2f} mA")
            elif self.yMaxMath/self.shuntRes_Math > 0.000001 or self.yMaxMath/self.shuntRes_Math < -0.000001:
                self.measure.maxLE.setText(f"{(self.yMaxMath/self.shuntRes_Math * 1000000):.2f} µA")

            if self.yMinMath/self.shuntRes_Math > 0.9 or self.yMinMath/self.shuntRes_Math < -0.9:
                self.measure.minLE.setText(f"{self.yMinMath/self.shuntRes_Math:.2f} A")
            elif self.yMinMath/self.shuntRes_Math > 0.001 or self.yMinMath/self.shuntRes_Math < -0.001:
                self.measure.minLE.setText(f"{(self.yMinMath/self.shuntRes_Math * 1000):.2f} mA")
            elif self.yMinMath/self.shuntRes_Math > 0.000001 or self.yMinMath/self.shuntRes_Math < -0.000001:
                self.measure.minLE.setText(f"{(self.yMinMath/self.shuntRes_Math * 1000000):.2f} µA")

        self.measure.phaseLE.setText(f"{self.mathPhase:.1f}°")
            

