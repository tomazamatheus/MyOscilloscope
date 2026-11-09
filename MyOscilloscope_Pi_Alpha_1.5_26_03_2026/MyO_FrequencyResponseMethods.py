
import math
from pyqtgraph import mkPen, QtCore, mkBrush
from PySide6.QtCore import QTimer, Qt
import numpy as np

def playPauseSweep(self):
    if not self.sweepRunning and not self.sweepPaused:
        self.start_sweep()
        return

    else:
        self.pauseOrResumeSweep()
        return

def start_sweep(self):
    if self.sweepHaveNotStarted:
        if self.sweepRunning:
            return

        self.sweepRunning = True
        self.sweepPaused = False
        self.pendingCapture = False

        self.samplingIndex = 0

        
        self.currentSamples = []
        self.currentSamples_phase = []
        
        pen = mkPen(self.nextSweepColor, width=2.2)

        curve = self.freqRespScr.magnitude.plot(
            pen=pen,
            symbol='o',
            symbolSize=6,
            symbolBrush=mkBrush(self.nextSweepColor),
            symbolPen=mkPen(self.nextSweepColor)
        )
        curve.curveColor = self.nextSweepColor

        curve_phase = self.freqRespScr.phase.plot(
            pen=pen,
            symbol='o',
            symbolSize=6,
            symbolBrush=mkBrush(self.nextSweepColor),
            symbolPen=mkPen(self.nextSweepColor)
        )

        self.currentCurve = curve
        self.freqRespCurves.append(curve)

        self.currentCurve_phase = curve_phase
        self.freqRespCurves_phase.append(curve_phase)

        self.sweepTimer.start()

        if not self.WFMgeneratorScr.btOnOff_isOn:
            self.WFMgeneratorScr.WFMBtOnOff()

        self.WFMgeneratorScr.generator.set_freq(self.freqResp_initFreq)
        self.sweepHaveNotStarted = False
        self.freqResp_scr2.freqResp_page2.functionTypeCB.setEnabled(False)

        self.freqResp_scr2.freqResp_page1.numberPointsLE.setEnabled(False)
        self.freqResp_scr2.freqResp_page1.initialFreqLE.setEnabled(False) 
        self.freqResp_scr2.freqResp_page1.finalFreqLE.setEnabled(False)   


        self.freqResp_freqsLogInterp = np.logspace(np.log10(self.freqResp_initFreq), 
                                                    np.log10(self.freqResp_finalFreq), self.freqResp_nPoints)
        
    self.freqSweepScr.progressBar.setStyleSheet(f"""
            QProgressBar {{
                border: 1px solid #555;
                border-radius: 4px;
                text-align: center;
            }}
            QProgressBar::chunk {{
                background-color: rgb(70, 160, 80);
            }}
            """)
    

def advanceSweep(self):
    self.timeKnob.usefulValue = self.timeKnob.maxUsefulValue  
    self.timeKnob.scaleValue = 50
    self.UpdateTimeScale(None)
    self.mainScr.timeScale = self.timeKnob.scaleValue
    self.timeLabel.setText(f"Time: {self.mainScr.timeScale:.0f} ms/div")

    if not self.sweepRunning or self.sweepPaused:
        return

    if self.samplingIndex >= len(self.freqResp_freqsLogInterp):
        self.stopSweep()
        return

    self.currentFrequency = self.freqResp_freqsLogInterp[self.samplingIndex]
    self.WFMgeneratorScr.generator.set_freq(self.currentFrequency)

    self.pendingCapture = True
    QTimer.singleShot(500, self.captureSamples)


def captureSamples(self):
    if not self.sweepRunning or self.sweepPaused or not self.pendingCapture:
        return

    self.pendingCapture = False

    
    if self.functionType == "CH2/CH1":
        #magnitude
        try:
            sample = 20 * np.log10(
                self.CH2VRMSValue / self.CH1VRMSValue
            )
        except ZeroDivisionError:
            sample = math.inf
        #phase
        sample_phase = self.CH2Phase - self.CH1Phase
        

    elif self.functionType == "CH1/CH2":
        try:
            sample = 20 * np.log10(
                self.CH1VRMSValue / self.CH2VRMSValue
            )
        except ZeroDivisionError:
            sample = math.inf
        #phase
        sample_phase = self.CH1Phase - self.CH2Phase
        

    elif self.functionType == "CH1/Math":
        try:
            sample = 20 * np.log10(
                self.CH1VRMSValue / self.mathVRMSValue
            )
        except ZeroDivisionError:
            sample = math.inf
        #phase
        sample_phase = self.CH1Phase - self.mathPhase
        

    elif self.functionType == "Math/CH1":
        try:
            sample = 20 * np.log10(
                self.mathVRMSValue / self.CH1VRMSValue
            )
        except ZeroDivisionError:
            sample = math.inf
        #phase
        sample_phase = self.mathPhase - self.CH1Phase
        

    elif self.functionType == "CH2/Math":
        try:
            sample = 20 * np.log10(
                self.CH2VRMSValue / self.mathVRMSValue
            )
        except ZeroDivisionError:
            sample = math.inf
        #phase
        sample_phase = self.CH2Phase - self.mathPhase
        

    elif self.functionType == "Math/CH2":
        try:
            sample = 20 * np.log10(
                self.mathVRMSValue / self.CH2VRMSValue
            )
        except ZeroDivisionError:
            sample = math.inf
        #phase
        sample_phase = self.mathPhase - self.CH2Phase
        

    elif self.functionType == "CH1":
        sample = 20 * np.log10(
            self.CH1VRMSValue
        )

        #phase
        sample_phase = self.CH1Phase
        

    elif self.functionType == "CH2":
        sample = 20 * np.log10(
            self.CH2VRMSValue
        )
        #phase
        sample_phase = self.CH2Phase
        

    else:
        sample = 20 * np.log10(
            self.mathVRMSValue
        )
        #phase
        sample_phase = self.mathPhase
        

    self.currentSamples.append(sample)
    if sample_phase > 180: sample_phase = -1.0 * (360.0 - sample_phase)
    elif sample_phase < -180: sample_phase = 360.0 + sample_phase
    self.currentSamples_phase.append(sample_phase)

    freqs_plot = self.freqResp_freqsLogInterp[:len(self.currentSamples)]
    self.currentCurve.setData(freqs_plot, self.currentSamples)
    self.currentCurve_phase.setData(freqs_plot, self.currentSamples_phase)

    self.samplingIndex += 1
    self.freqSweepScr.updateProgressBar(int(self.samplingIndex/self.freqResp_nPoints * 100))

def pauseOrResumeSweep(self):
    if self.freqResp_scr2.freqResp_page1.btSweep_Play_Mode == "Running": #Ou seja, se acabou de despausar (Resume)
        if not self.sweepRunning or not self.sweepPaused:
            return

        self.sweepPaused = False
        self.sweepTimer.start()

        self.freqSweepScr.progressBar.setStyleSheet(f"""
            QProgressBar {{
                border: 1px solid #555;
                border-radius: 4px;
                text-align: center;
            }}
            QProgressBar::chunk {{
                background-color: rgb(70, 160, 80);
            }}
            """)
        

    else: #Pause
        if not self.sweepRunning or self.sweepPaused:
            return

        self.sweepPaused = True
        self.sweepTimer.stop()

        self.freqSweepScr.progressBar.setStyleSheet(f"""
            QProgressBar {{
                border: 1px solid #555;
                border-radius: 4px;
                text-align: center;
            }}
            QProgressBar::chunk {{
                background-color: rgb(80, 110, 210);
            }}
            """)

def stopSweep(self):
    self.sweepRunning = False
    self.sweepPaused = False
    self.pendingCapture = False
    self.sweepHaveNotStarted = True
    self.sweepTimer.stop()
    self.WFMgeneratorScr.freq_SpinBox.setValue(500)
    self.WFMgeneratorScr.generator.set_freq(500)
    self.freqResp_scr2.freqResp_page2.functionTypeCB.setEnabled(True)
    self.freqResp_scr2.freqResp_page1.numberPointsLE.setEnabled(True)
    self.freqResp_scr2.freqResp_page1.initialFreqLE.setEnabled(True) 
    self.freqResp_scr2.freqResp_page1.finalFreqLE.setEnabled(True)
    self.timeKnob.usefulValue = 0
    self.timeKnob.scaleValue = 1
    self.UpdateTimeScale(0)
    self.mainScr.timeScale = self.timeKnob.scaleValue
    self.timeLabel.setText(f"Time: {self.mainScr.timeScale:.0f} ms/div")

def clearSweeps(self):
    if not self.freqResp_scr2.freqResp_page2.clearScreenPartialCheckBox.isChecked():
        # Magnitude
        for curve in self.freqRespCurves:
            self.freqRespScr.magnitude.removeItem(curve)
        self.freqRespCurves.clear()

        # Phase
        for curve in self.freqRespCurves_phase:
            self.freqRespScr.phase.removeItem(curve)
        self.freqRespCurves_phase.clear()

        self.currentCurve = None
        self.currentCurve_phase = None

    else:
        # Magnitude
        while len(self.freqRespCurves) > 1:
            curve = self.freqRespCurves.pop(0)
            self.freqRespScr.magnitude.removeItem(curve)

        # Phase
        while len(self.freqRespCurves_phase) > 1:
            curve = self.freqRespCurves_phase.pop(0)
            self.freqRespScr.phase.removeItem(curve)


def changePlotColor(self):
    if self.freqResp_scr2.freqResp_page2.plotColorCB.currentText() == "White": self.nextSweepColor = "w"
    elif self.freqResp_scr2.freqResp_page2.plotColorCB.currentText() == "Yellow": self.nextSweepColor = "y"
    elif self.freqResp_scr2.freqResp_page2.plotColorCB.currentText() == "Blue": self.nextSweepColor = "b"
    elif self.freqResp_scr2.freqResp_page2.plotColorCB.currentText() == "Red": self.nextSweepColor = "r"
    elif self.freqResp_scr2.freqResp_page2.plotColorCB.currentText() == "Green": self.nextSweepColor = "g"
    elif self.freqResp_scr2.freqResp_page2.plotColorCB.currentText() == "Purple": self.nextSweepColor = "purple"
    elif self.freqResp_scr2.freqResp_page2.plotColorCB.currentText() == "Orange": self.nextSweepColor = "orange"
    elif self.freqResp_scr2.freqResp_page2.plotColorCB.currentText() == "Cyan": self.nextSweepColor = "c"

def changeFunctionType(self):
    if self.freqResp_scr2.freqResp_page2.functionTypeCB.currentText() == "CH2/CH1": self.functionType = "CH2/CH1"
    elif self.freqResp_scr2.freqResp_page2.functionTypeCB.currentText() == "CH1/CH2": self.functionType = "CH1/CH2"
    elif self.freqResp_scr2.freqResp_page2.functionTypeCB.currentText() == "CH1/Math": self.functionType = "CH1/Math"
    elif self.freqResp_scr2.freqResp_page2.functionTypeCB.currentText() == "Math/CH1": self.functionType = "Math/CH1"
    elif self.freqResp_scr2.freqResp_page2.functionTypeCB.currentText() == "CH2/Math": self.functionType = "CH2/Math"
    elif self.freqResp_scr2.freqResp_page2.functionTypeCB.currentText() == "Math/CH2": self.functionType = "Math/CH2"
    elif self.freqResp_scr2.freqResp_page2.functionTypeCB.currentText() == "CH1": self.functionType = "CH1"
    elif self.freqResp_scr2.freqResp_page2.functionTypeCB.currentText() == "CH2": self.functionType = "CH2"
    elif self.freqResp_scr2.freqResp_page2.functionTypeCB.currentText() == "Math": self.functionType = "Math"

def change_numPoints_LE_FreqResp(self):
    text = self.freqResp_scr2.freqResp_page1.numberPointsLE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = int(text)
        if value > 300:
            self.freqResp_scr2.freqResp_page1.numberPointsLE.setText("300")
            self.freqResp_nPoints = 300
        elif value >= 2:
            self.freqResp_nPoints = value
            self.freqResp_scr2.freqResp_page1.numberPointsLE.setText(f"{value:.0f}")
        else:
            self.freqResp_nPoints = 2
            self.freqResp_scr2.freqResp_page1.numberPointsLE.setText("2")
        
    except ValueError:
        self.freqResp_scr2.freqResp_page1.numberPointsLE.setText("60")
        self.freqResp_nPoints = 60

def change_initFreq_LE_FreqResp(self):
    text = self.freqResp_scr2.freqResp_page1.initialFreqLE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = float(text)
        if value > 20000:
            self.freqResp_scr2.freqResp_page1.initialFreqLE.setText("20000")
            self.freqResp_initFreq = 20000
        elif value >= 20:
            self.freqResp_initFreq = value
            self.freqResp_scr2.freqResp_page1.initialFreqLE.setText(f"{value:.0f}")
        else:
            self.freqResp_initFreq = 20
            self.freqResp_scr2.freqResp_page1.initialFreqLE.setText("20")
        
    except ValueError:
        self.freqResp_scr2.freqResp_page1.initialFreqLE.setText("50")
        self.freqResp_initFreq = 50

def change_finalFreq_LE_FreqResp(self):
    text = self.freqResp_scr2.freqResp_page1.finalFreqLE.text()
    # verifica que a entrada é de fato numérica
    try:
        value = float(text)
        if value > 20000:
            self.freqResp_scr2.freqResp_page1.finalFreqLE.setText("20000")
            self.freqResp_finalFreq = 20000
        elif value >= 20:
            self.freqResp_finalFreq = value
            self.freqResp_scr2.freqResp_page1.finalFreqLE.setText(f"{value:.0f}")
        else:
            self.freqResp_finalFreq = 20
            self.freqResp_scr2.freqResp_page1.finalFreqLE.setText("20")
        
    except ValueError:
        self.freqResp_scr2.freqResp_page1.finalFreqLE.setText("1000")
        self.freqResp_finalFreq = 1000

def syncXAxis(self, sourcePlot, targetPlot): #sincronizar ajustes de limites entre fase e magnitude - freq resp
    srcItem = sourcePlot.getPlotItem()
    tgtItem = targetPlot.getPlotItem()

    # Copiar range
    xMin, xMax = srcItem.vb.viewRange()[0]
    tgtItem.vb.setXRange(xMin, xMax, padding=0)

    # Copiar ticks
    srcAxis = srcItem.getAxis('bottom')
    tgtAxis = tgtItem.getAxis('bottom')

    if srcAxis._tickLevels is not None:
        tgtAxis.setTicks(srcAxis._tickLevels)



def FreqResp_xBotLimLE_Changed(self):
    
    text = self.freqResp_scr2.freqResp_page3.x_botLim_LE.text()

    try:
        minor_ticks = []
        for decade in range(1, 6):  
            for k in range(2, 10):
                pos = decade + math.log10(k)
                minor_ticks.append((pos, "")) 

        self.freqRespScr.magnitude.xBotLim = float(text) 
        if self.freqRespScr.magnitude.xBotLim >= self.freqRespScr.magnitude.xTopLim:
            self.freqRespScr.magnitude.xBotLim = self.freqRespScr.magnitude.xTopLim
            self.freqResp_scr2.freqResp_page3.x_botLim_LE.setText(f"{self.freqRespScr.magnitude.xBotLim:.0f}")
            self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}")]
            self.freqRespScr.magnitude.setXRange(self.freqRespScr.magnitude.xBotLim, self.freqRespScr.magnitude.xBotLim)

        else:
            if self.freqRespScr.magnitude.xBotLim < 10:
                self.freqResp_scr2.freqResp_page3.x_botLim_LE.setText("10")
                if self.freqRespScr.magnitude.xTopLim < 100: 
                    self.freqRespScr.magnitude.ticksX = [(1, "10"), (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                elif self.freqRespScr.magnitude.xTopLim < 1000: 
                    self.freqRespScr.magnitude.ticksX = [(1, "10"), (2, "100"), (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                elif self.freqRespScr.magnitude.xTopLim < 10000:
                    self.freqRespScr.magnitude.ticksX = [(1, "10"), (2, "100"), (3, "1000"), (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                elif self.freqRespScr.magnitude.xTopLim < 100000:
                    self.freqRespScr.magnitude.ticksX = [(1, "10"), (2, "100"), (3, "1000"), (4, "10000"), (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                
                self.freqRespScr.magnitude.setXRange(1, math.log10(self.freqRespScr.magnitude.xTopLim))
                self.freqRespScr.magnitude.getPlotItem().getAxis('bottom').setTicks([self.freqRespScr.magnitude.ticksX, minor_ticks])
                
            elif self.freqRespScr.magnitude.xBotLim >= 100000:
                self.freqResp_scr2.freqResp_page3.x_botLim_LE.setText("100000")
                self.freqRespScr.magnitude.ticksX = [(5, "100000")]
                self.freqRespScr.magnitude.setXRange(4, 6)
                self.freqRespScr.magnitude.getPlotItem().getAxis('bottom').setTicks([self.freqRespScr.magnitude.ticksX, minor_ticks])

            else:
                self.freqResp_scr2.freqResp_page3.x_botLim_LE.setText(f"{self.freqRespScr.magnitude.xBotLim:.0f}")
                if self.freqRespScr.magnitude.xBotLim < 100:
                    if self.freqRespScr.magnitude.xTopLim < 100:     
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                        
                    elif self.freqRespScr.magnitude.xTopLim < 1000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"),
                                            (2, "100"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))

                    elif self.freqRespScr.magnitude.xTopLim < 10000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"),
                                            (2, "100"),
                                            (3, "1000"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                        
                    elif self.freqRespScr.magnitude.xTopLim < 100000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"),
                                            (2, "100"),
                                            (3, "1000"),
                                            (4, "10000"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                    
                    else:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"),
                                            (2, "100"),
                                            (3, "1000"),
                                            (4, "10000"), 
                                            (5, "100000")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(100000))

                        
                elif self.freqRespScr.magnitude.xBotLim < 1000:
                    if self.freqRespScr.magnitude.xTopLim < 1000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                        
                    elif self.freqRespScr.magnitude.xTopLim < 10000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"),
                                            (3, "1000"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                        
                    elif self.freqRespScr.magnitude.xTopLim < 100000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"),
                                            (3, "1000"),
                                            (4, "10000"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                    
                    else:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"),
                                            (3, "1000"),
                                            (4, "10000"), 
                                            (5, "100000")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(100000))
                        
                elif self.freqRespScr.magnitude.xBotLim < 10000:
                    if self.freqRespScr.magnitude.xTopLim < 10000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                        
                        
                    elif self.freqRespScr.magnitude.xTopLim < 100000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"),
                                            (4, "10000"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                    
                    else:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"),
                                            (4, "10000"), 
                                            (5, "100000")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(10000))
                    
                
                elif self.freqRespScr.magnitude.xBotLim < 100000: 
                    if self.freqRespScr.magnitude.xTopLim < 100000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"),
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                    
                    else:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"),
                                            (5, "100000")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(10000))

                self.freqRespScr.magnitude.getPlotItem().getAxis('bottom').setTicks([self.freqRespScr.magnitude.ticksX, minor_ticks])

    

    except ValueError:
        self.freqResp_scr2.freqResp_page3.x_botLim_LE.setText("10")
        if self.freqRespScr.magnitude.xTopLim < 100: 
            self.freqRespScr.magnitude.ticksX = [(1, "10"), (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
        elif self.freqRespScr.magnitude.xTopLim < 1000: 
            self.freqRespScr.magnitude.ticksX = [(1, "10"), (2, "100"), (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
        elif self.freqRespScr.magnitude.xTopLim < 10000:
            self.freqRespScr.magnitude.ticksX = [(1, "10"), (2, "100"), (3, "1000"), (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
        elif self.freqRespScr.magnitude.xTopLim < 100000:
            self.freqRespScr.magnitude.ticksX = [(1, "10"), (2, "100"), (3, "1000"), (4, "10000"), (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
        
        self.freqRespScr.magnitude.setXRange(1, math.log10(self.freqRespScr.magnitude.xTopLim))
        self.freqRespScr.magnitude.getPlotItem().getAxis('bottom').setTicks([self.freqRespScr.magnitude.ticksX, minor_ticks])


    


    

def FreqResp_xTopLimLE_Changed(self):
    text = self.freqResp_scr2.freqResp_page3.x_topLim_LE.text()

    try:
        minor_ticks = []
        for decade in range(1, 6):  
            for k in range(2, 10):
                pos = decade + math.log10(k)
                minor_ticks.append((pos, "")) 

        self.freqRespScr.magnitude.xTopLim = float(text) 
        if self.freqRespScr.magnitude.xTopLim <= self.freqRespScr.magnitude.xBotLim:
            self.freqRespScr.magnitude.xTopLim = self.freqRespScr.magnitude.xBotLim
            self.freqResp_scr2.freqResp_page3.x_topLim_LE.setText(f"{self.freqRespScr.magnitude.xTopLim:.0f}")
            self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
            self.freqRespScr.magnitude.setXRange(self.freqRespScr.magnitude.xTopLim, self.freqRespScr.magnitude.xTopLim)

        else:
            if self.freqRespScr.magnitude.xTopLim >= 100000:
                self.freqRespScr.magnitude.xTopLim = 100000
                self.freqResp_scr2.freqResp_page3.x_topLim_LE.setText("100000")

                if self.freqRespScr.magnitude.xBotLim < 100:
                    self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), (2, "100"), (3, "1000"), (4, "10000"), 
                                            (5, "100000")]
                    self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                    
                elif self.freqRespScr.magnitude.xBotLim < 1000:
                    self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), (3, "1000"), (4, "10000"), 
                                            (5, "100000")]
                    self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                    
                elif self.freqRespScr.magnitude.xBotLim < 10000:
                    self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), (4, "10000"), 
                                            (5, "100000")]
                    self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                    
                elif self.freqRespScr.magnitude.xBotLim < 100000:
                    self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), 
                                            (5, "100000")]
                    self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                    
                else:
                    self.freqRespScr.magnitude.ticksX = [(5, "100000")]
                    self.freqRespScr.magnitude.setXRange(4.9, 5.1)
            
            elif self.freqRespScr.magnitude.xTopLim < 10:
                self.freqRespScr.magnitude.xTopLim = 10
                self.freqResp_scr2.freqResp_page3.x_topLim_LE.setText("10")
                self.freqRespScr.magnitude.ticksX = [(1, "10")]
                self.freqRespScr.magnitude.setXRange(0.8, 1.2)
                self.freqRespScr.magnitude.getPlotItem().getAxis('bottom').setTicks([self.freqRespScr.magnitude.ticksX, minor_ticks])

            else:
                self.freqResp_scr2.freqResp_page3.x_topLim_LE.setText(f"{self.freqRespScr.magnitude.xTopLim:.0f}")

                if self.freqRespScr.magnitude.xTopLim > 10000:
                    if self.freqRespScr.magnitude.xBotLim < 100:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), (2, "100"), (3, "1000"), (4, "10000"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))

                    elif self.freqRespScr.magnitude.xBotLim < 1000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), (3, "1000"), (4, "10000"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))

                    elif self.freqRespScr.magnitude.xBotLim < 10000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), (4, "10000"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))

                    elif self.freqRespScr.magnitude.xBotLim < 10000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), (4, "10000"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))

                    elif self.freqRespScr.magnitude.xBotLim < 100000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"),
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                
                elif self.freqRespScr.magnitude.xTopLim > 1000:
                    if self.freqRespScr.magnitude.xBotLim < 100:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), (2, "100"), (3, "1000"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))

                    elif self.freqRespScr.magnitude.xBotLim < 1000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), (3, "1000"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))

                    elif self.freqRespScr.magnitude.xBotLim < 10000:
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                
                elif self.freqRespScr.magnitude.xTopLim > 100:
                    if self.freqRespScr.magnitude.xBotLim < 100:
                        
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), (2, "100"),  
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))

                    elif self.freqRespScr.magnitude.xBotLim < 1000:
                        
                        self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                        self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
                        

                else:
                    self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), 
                                            (math.log10(self.freqRespScr.magnitude.xTopLim), f"{self.freqRespScr.magnitude.xTopLim:.0f}")]
                    self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))

                self.freqRespScr.magnitude.getPlotItem().getAxis('bottom').setTicks([self.freqRespScr.magnitude.ticksX, minor_ticks])
                

    except ValueError:
        self.freqRespScr.magnitude.xTopLim = 100000
        self.freqResp_scr2.freqResp_page3.x_topLim_LE.setText("100000")

        if self.freqRespScr.magnitude.xBotLim < 100:
            self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), (2, "100"), (3, "1000"), (4, "10000"), 
                                    (5, "100000")]
            self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
            
        elif self.freqRespScr.magnitude.xBotLim < 1000:
            self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), (3, "1000"), (4, "10000"), 
                                    (5, "100000")]
            self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
            
        elif self.freqRespScr.magnitude.xBotLim < 10000:
            self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), (4, "10000"), 
                                    (5, "100000")]
            self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
            
        elif self.freqRespScr.magnitude.xBotLim < 100000:
            self.freqRespScr.magnitude.ticksX = [(math.log10(self.freqRespScr.magnitude.xBotLim), f"{self.freqRespScr.magnitude.xBotLim:.0f}"), 
                                    (5, "100000")]
            self.freqRespScr.magnitude.setXRange(math.log10(self.freqRespScr.magnitude.xBotLim), math.log10(self.freqRespScr.magnitude.xTopLim))
            
        else:
            self.freqRespScr.magnitude.ticksX = [(5, "100000")]
            self.freqRespScr.magnitude.setXRange(4.9, 5.1)

    self.syncXAxis(
        self.freqRespScr.magnitude,
        self.freqRespScr.phase
    )

    

def FreqResp_yBotLimLE_Changed(self):
    try:
        text = self.freqResp_scr2.freqResp_page3.y_botLim_LE.text()
        self.freqRespScr.magnitude.yBotLim = float(text)

        if self.freqRespScr.magnitude.yBotLim < -1000:
            self.freqRespScr.magnitude.yBotLim = -1000
        
        elif self.freqRespScr.magnitude.yBotLim > 1000:
            self.freqRespScr.magnitude.yBotLim = 1000

        self.freqRespScr.magnitude.setYRange(self.freqRespScr.magnitude.yBotLim, self.freqRespScr.magnitude.yTopLim)

    except ValueError:
        self.freqRespScr.magnitude.yBotLim = -60
        self.freqRespScr.magnitude.setYRange(self.freqRespScr.magnitude.yBotLim, self.freqRespScr.magnitude.yTopLim)
    
    
    
    

def FreqResp_yTopLimLE_Changed(self):
    try:
        text = self.freqResp_scr2.freqResp_page3.y_topLim_LE.text()
        self.freqRespScr.magnitude.yTopLim = float(text)

        if self.freqRespScr.magnitude.yTopLim < -1000:
            self.freqRespScr.magnitude.yTopLim = -1000
        
        elif self.freqRespScr.magnitude.yTopLim > 1000:
            self.freqRespScr.magnitude.yTopLim = 1000

        self.freqRespScr.magnitude.setYRange(self.freqRespScr.magnitude.yBotLim, self.freqRespScr.magnitude.yTopLim)

    except ValueError:
        self.freqRespScr.magnitude.yTopLim = 30
        self.freqRespScr.magnitude.setYRange(self.freqRespScr.magnitude.yBotLim, self.freqRespScr.magnitude.yTopLim)
    


def FreqResp_yBotLimLE_phase_Changed(self):
    try:
        text = self.freqResp_scr2.freqResp_page3.y_botLim_LE_phase.text()
        self.freqRespScr.phase.yBotLim = float(text)

        if self.freqRespScr.phase.yBotLim < -180:
            self.freqRespScr.phase.yBotLim = -180
        
        elif self.freqRespScr.phase.yBotLim > 180:
            self.freqRespScr.phase.yBotLim = 180

        self.freqRespScr.phase.setYRange(self.freqRespScr.phase.yBotLim, self.freqRespScr.phase.yTopLim)

    except ValueError:
        self.freqRespScr.phase.yBotLim = -180
        self.freqRespScr.phase.setYRange(self.freqRespScr.phase.yBotLim, self.freqRespScr.phase.yTopLim)

def FreqResp_yTopLimLE_phase_Changed(self):
    try:
        text = self.freqResp_scr2.freqResp_page3.y_topLim_LE_phase.text()
        self.freqRespScr.phase.yTopLim = float(text)

        if self.freqRespScr.phase.yTopLim < -180:
            self.freqRespScr.phase.yTopLim = -180
        
        elif self.freqRespScr.phase.yTopLim > 180:
            self.freqRespScr.phase.yTopLim = 180

        self.freqRespScr.phase.setYRange(self.freqRespScr.phase.yBotLim, self.freqRespScr.phase.yTopLim)

    except ValueError:
        self.freqRespScr.phase.yTopLim = -180
        self.freqRespScr.phase.setYRange(self.freqRespScr.phase.yBotLim, self.freqRespScr.phase.yTopLim)

def FreqResp_restoreDefault(self):
    self.freqResp_scr2.freqResp_page3.x_botLim_LE.setText("10")
    self.freqRespScr.magnitude.xBotLim = float(self.freqResp_scr2.freqResp_page3.x_botLim_LE.text())
    self.freqResp_scr2.freqResp_page3.x_topLim_LE.setText("10000")
    self.freqRespScr.magnitude.xTopLim = float(self.freqResp_scr2.freqResp_page3.x_topLim_LE.text())
    self.freqResp_scr2.freqResp_page3.y_botLim_LE.setText("-65")
    self.freqRespScr.magnitude.yBotLim = float(self.freqResp_scr2.freqResp_page3.y_botLim_LE.text())
    self.freqResp_scr2.freqResp_page3.y_topLim_LE.setText("15")
    self.freqRespScr.magnitude.yTopLim = float(self.freqResp_scr2.freqResp_page3.y_topLim_LE.text())
    self.freqResp_scr2.freqResp_page3.y_botLim_LE_phase.setText("-180")
    self.freqRespScr.phase.yBotLim = float(self.freqResp_scr2.freqResp_page3.y_botLim_LE.text())
    self.freqResp_scr2.freqResp_page3.y_topLim_LE_phase.setText("180")
    self.freqRespScr.phase.yTopLim = float(self.freqResp_scr2.freqResp_page3.y_topLim_LE.text())

    self.freqResp_scr2.freqResp_page3.x_botLim_LE.returnPressed.emit()
    self.freqResp_scr2.freqResp_page3.x_topLim_LE.returnPressed.emit()
    self.freqResp_scr2.freqResp_page3.y_botLim_LE.returnPressed.emit()
    self.freqResp_scr2.freqResp_page3.y_topLim_LE.returnPressed.emit()
    self.freqResp_scr2.freqResp_page3.y_botLim_LE_phase.returnPressed.emit()
    self.freqResp_scr2.freqResp_page3.y_topLim_LE_phase.returnPressed.emit()

    
def changeFreqRespAxis(self):
    if self.freqResp_scr2.freqResp_page2.y_AxisCB.currentIndex() == 0: self.freqRespScr.stacked.setCurrentIndex(0)
    else: self.freqRespScr.stacked.setCurrentIndex(1)

def sweepControl_Play(self):
    if self.freqResp_scr2.freqResp_page1.sweepOn:
        if self.notStartedProgressBar:
            self.tertiaryScreen.setCurrentIndex(5)
            self.freqSweepScr.updateProgressBar(0)
            self.notStartedProgressBar = False

            #tirando os botões de screen3 da tela:
            self.bt_Wfm.moveButton(-100, -100)
            self.bt_Calibration.moveButton(-100, -100)
            self.bt_Exp.moveButton(-100, -100)
            self.bt_MathPlus.moveButton(-100, -100)



    if self.freqResp_scr2.freqResp_page1.btSweep_Play_Mode == "Running":
        self.freqSweepScr.sweepRunning = True
        if self.language == "English": 
            self.freqSweepScr.label1.setText("Sweep is running! \nProgress:")
            self.freqSweepScr.label2.setText("Sweep complete! Please press Stop Sweep button.")
        else: 
            self.freqSweepScr.label1.setText("O Sweep se encontra em andamento! \nProgresso:")
            self.freqSweepScr.label2.setText("Sweep completo! Por favor, pressione o botão Stop Sweep.")
    else: #Pausa
        self.freqSweepScr.sweepRunning = False
        if self.language == "English": self.freqSweepScr.label1.setText("Sweep is paused. \nProgress:")
        else: self.freqSweepScr.label1.setText("O Sweep se encontra pausado. \nProgresso:")


def sweepControl_Stop(self):
    self.freqSweepScr.sweepRunning = False
    self.notStartedProgressBar = True

    if self.freqSweepScr.progressBar.value() < 100:
        if self.language == "English": self.freqSweepScr.label1.setText("Sweep has been stopped.")
        else: self.freqSweepScr.label1.setText("Encerrando o Sweep...") 
        self.freqResp_scr2.freqResp_page1.btSweep_Play.setEnabled(False)
        QTimer.singleShot(800, self.finish_stop)
    else:
        self.finish_stop()

def finish_stop(self):
    self.freqSweepScr.progressBar.setValue(0)
    self.freqResp_scr2.freqResp_page1.btSweep_Play.setEnabled(True)

    p = self.width() / 1920
    if self.btOnOff.isOn:
        self.bt_Wfm.moveButton(int(p * 1600), int(p * 105))
        self.bt_Calibration.moveButton(int(p * 1675), int(p * 105))
        self.bt_Exp.moveButton(int(p * 1750), int(p * 105))
        self.bt_MathPlus.moveButton(int(p * 1825), int(p * 105))

    self.tertiaryScreen.setCurrentIndex(1)
    self.freqSweepScr.stopBlinkingLabel(self.freqSweepScr.label2)


def sweepProgressBar_valueChanged(self, value):
    if value >= 100:
        self.freqResp_scr2.freqResp_page1.btSweep_Play.setEnabled(False)
        self.freqResp_scr2.freqResp_page1.btSweep_Play_ImageLabel.setPixmap(self.freqResp_scr2.freqResp_page1.
                                                                            btSweep_Play_Unavailable_Pixmap.scaled
                                            (self.freqResp_scr2.freqResp_page1.btSweep_Play_ImageLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))