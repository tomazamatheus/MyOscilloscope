import math
import numpy as np

def updateLissajous(self):
    # y_CH1  = self.mainScr.y_CH1_plot
    # y_CH2  = self.mainScr.y_CH2_plot
    # y_Math = self.mainScr.y_Math_plot

    y_CH1 = np.asarray(self.mainScr.y_CH1_pure, dtype=np.float64)
    y_CH2 = np.asarray(self.mainScr.y_CH2_pure, dtype=np.float64)
    y_Math = np.asarray(self.mainScr.y_Math_pure, dtype=np.float64)

    def resizeScreen(CHx, CHy):
        if CHx.size == 0 or CHy.size == 0:
            return
        
        new_xmin = min(-0.8, 1.2 * np.min(CHx))
        new_xmax = max(0.8, 1.2 * np.max(CHx))
        new_ymin = min(-0.8, 1.2 * np.min(CHy))
        new_ymax = max(0.8, 1.2 * np.max(CHy))

        def different(a, b, tol=1e-6):
            return abs(a - b) > tol

        if (different(new_xmin, self.phasDiag_and_lissajScr.lissaj.xBotLim) or
            different(new_xmax, self.phasDiag_and_lissajScr.lissaj.xTopLim) or
            different(new_ymin, self.phasDiag_and_lissajScr.lissaj.yBotLim) or
            different(new_ymax, self.phasDiag_and_lissajScr.lissaj.yTopLim)):

            self.phasDiag_and_lissajScr.lissaj.xBotLim = new_xmin
            self.phasDiag_and_lissajScr.lissaj.xTopLim = new_xmax
            self.phasDiag_and_lissajScr.lissaj.yBotLim = new_ymin
            self.phasDiag_and_lissajScr.lissaj.yTopLim = new_ymax

            new_min = min(new_xmin, new_ymin)
            new_max = max(new_xmax, new_ymax)

            self.phasDiag_and_lissajScr.lissaj.setRange(
                xRange=(new_min, new_max),
                yRange=(new_min, new_max),
                padding=0
            )

            


        self.phasDiag_and_lissajScr.lissaj.getPlotItem().getAxis('bottom').setTickSpacing(max(1/6, np.max(CHx)/4.0, np.max(CHy)/4.0), 
                                                                                          max(1/6, np.max(CHx)/4.0, np.max(CHy)/4.0))
        self.phasDiag_and_lissajScr.lissaj.getPlotItem().getAxis('left').setTickSpacing(max(1/6, np.max(CHx)/4.0, np.max(CHy)/4.0), 
                                                                                          max(1/6, np.max(CHx)/4.0, np.max(CHy)/4.0))

    if self.phasDiag_and_lissaj_scr2.page2.channelxAxisSelectCB.currentText() == "CH1":
        if self.phasDiag_and_lissaj_scr2.page2.channelyAxisSelectCB.currentText() == "CH1":
            self.phasDiag_and_lissajScr.lissaj.updateGraph(y_CH1, y_CH1)
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='CH1 (V)', color='white', **{'font-size':'8pt'})
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='CH1 (V)', color='white', **{'font-size':'8pt'})
            resizeScreen(y_CH1, y_CH1)

        elif self.phasDiag_and_lissaj_scr2.page2.channelyAxisSelectCB.currentText() == "CH2":
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='CH1 (V)', color='white', **{'font-size':'8pt'})
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='CH2 (V)', color='white', **{'font-size':'8pt'})
            resizeScreen(y_CH1, y_CH2)
            self.phasDiag_and_lissajScr.lissaj.updateGraph(y_CH1, y_CH2)

        else:
            self.phasDiag_and_lissajScr.lissaj.updateGraph(y_CH1, y_Math)
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='CH1 (V)', color='white', **{'font-size':'8pt'})
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='Math (V)', color='white', **{'font-size':'8pt'})
            resizeScreen(y_CH1, y_Math)

    elif self.phasDiag_and_lissaj_scr2.page2.channelxAxisSelectCB.currentText() == "CH2":
        if self.phasDiag_and_lissaj_scr2.page2.channelyAxisSelectCB.currentText() == "CH1":
            self.phasDiag_and_lissajScr.lissaj.updateGraph(y_CH2, y_CH1)
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='CH2 (V)', color='white', **{'font-size':'8pt'})
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='CH1 (V)', color='white', **{'font-size':'8pt'})
            resizeScreen(y_CH2, y_CH1)

        elif self.phasDiag_and_lissaj_scr2.page2.channelyAxisSelectCB.currentText() == "CH2":
            self.phasDiag_and_lissajScr.lissaj.updateGraph(y_CH2, y_CH2)
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='CH2 (V)', color='white', **{'font-size':'8pt'})
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='CH2 (V)', color='white', **{'font-size':'8pt'})
            resizeScreen(y_CH2, y_CH2)

        else:
            self.phasDiag_and_lissajScr.lissaj.updateGraph(y_CH2, y_Math)
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='CH2 (V)', color='white', **{'font-size':'8pt'})
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='Math (V)', color='white', **{'font-size':'8pt'})
            resizeScreen(y_CH2, y_Math)

    else:
        if self.phasDiag_and_lissaj_scr2.page2.channelyAxisSelectCB.currentText() == "CH1":
            self.phasDiag_and_lissajScr.lissaj.updateGraph(y_Math, y_CH1)
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='Math (V)', color='white', **{'font-size':'8pt'})
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='CH1 (V)', color='white', **{'font-size':'8pt'})
            resizeScreen(y_Math, y_CH1)

        elif self.phasDiag_and_lissaj_scr2.page2.channelyAxisSelectCB.currentText() == "CH2":
            self.phasDiag_and_lissajScr.lissaj.updateGraph(y_Math, y_CH2)
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='Math (V)', color='white', **{'font-size':'8pt'})
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='CH2 (V)', color='white', **{'font-size':'8pt'})
            resizeScreen(y_Math, y_CH2)

        else:
            self.phasDiag_and_lissajScr.lissaj.updateGraph(y_Math, y_Math)
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='Math (V)', color='white', **{'font-size':'8pt'})
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='Math (V)', color='white', **{'font-size':'8pt'})
            resizeScreen(y_Math, y_Math)

    

def updatePhasDiag(self):
    #Ajustando um erro estranho no cálculo das fases:
    if self.mainScr.referencePhase == "CH1": 
        self.CH2Phase = self.CH2Phase - self.CH1Phase
        self.mathPhase = self.mathPhase - self.CH1Phase
        self.CH1Phase = 0

    elif self.mainScr.referencePhase == "CH2": 
        self.CH1Phase = self.CH1Phase - self.CH2Phase
        self.mathPhase = self.mathPhase - self.CH2Phase
        self.CH2Phase = 0

    else:
        self.CH1Phase = self.CH1Phase - self.mathPhase
        self.CH2Phase = self.CH2Phase - self.mathPhase
        self.mathPhase = 0

    self.phasDiag_and_lissajScr.phasDiag.CH1_Phase = self.CH1Phase
    self.phasDiag_and_lissajScr.phasDiag.CH2_Phase = self.CH2Phase
    self.phasDiag_and_lissajScr.phasDiag.math_Phase = self.mathPhase

    if self.phasDiagMagnitVoltage == "RMS":
        self.phasDiag_and_lissajScr.phasDiag.CH1_xcoord = self.CH1VRMSValue * math.cos(self.CH1Phase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.CH1_ycoord = self.CH1VRMSValue * math.sin(self.CH1Phase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.CH2_xcoord = self.CH2VRMSValue * math.cos(self.CH2Phase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.CH2_ycoord = self.CH2VRMSValue * math.sin(self.CH2Phase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.math_xcoord = self.mathVRMSValue * math.cos(self.mathPhase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.math_ycoord = self.mathVRMSValue * math.sin(self.mathPhase* math.pi/180)


        self.phasDiag_and_lissaj_scr2.page1.CH1MagnitLE.setText(f"{self.CH1VRMSValue:.2f}")
        self.phasDiag_and_lissaj_scr2.page1.CH2MagnitLE.setText(f"{self.CH2VRMSValue:.2f}")
        self.phasDiag_and_lissaj_scr2.page1.MathMagnitLE.setText(f"{self.mathVRMSValue:.2f}")

    elif self.phasDiagMagnitVoltage == "Pk-to-Pk":
        self.phasDiag_and_lissajScr.phasDiag.CH1_xcoord = self.CH1VppValue * math.cos(self.CH1Phase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.CH1_ycoord = self.CH1VppValue * math.sin(self.CH1Phase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.CH2_xcoord = self.CH2VppValue * math.cos(self.CH2Phase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.CH2_ycoord = self.CH2VppValue * math.sin(self.CH2Phase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.math_xcoord = self.mathVppValue * math.cos(self.mathPhase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.math_ycoord = self.mathVppValue * math.sin(self.mathPhase* math.pi/180)

        self.phasDiag_and_lissaj_scr2.page1.CH1MagnitLE.setText(f"{self.CH1VppValue:.2f}")
        self.phasDiag_and_lissaj_scr2.page1.CH2MagnitLE.setText(f"{self.CH2VppValue:.2f}")
        self.phasDiag_and_lissaj_scr2.page1.MathMagnitLE.setText(f"{self.mathVppValue:.2f}")

    else: #Peak voltage
        self.phasDiag_and_lissajScr.phasDiag.CH1_xcoord = self.CH1VppValue/2 * math.cos(self.CH1Phase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.CH1_ycoord = self.CH1VppValue/2 * math.sin(self.CH1Phase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.CH2_xcoord = self.CH2VppValue/2 * math.cos(self.CH2Phase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.CH2_ycoord = self.CH2VppValue/2 * math.sin(self.CH2Phase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.math_xcoord = self.mathVppValue/2 * math.cos(self.mathPhase* math.pi/180)
        self.phasDiag_and_lissajScr.phasDiag.math_ycoord = self.mathVppValue/2 * math.sin(self.mathPhase* math.pi/180)

        self.phasDiag_and_lissaj_scr2.page1.CH1MagnitLE.setText(f"{self.CH1VppValue/2:.2f}")
        self.phasDiag_and_lissaj_scr2.page1.CH2MagnitLE.setText(f"{self.CH2VppValue/2:.2f}")
        self.phasDiag_and_lissaj_scr2.page1.MathMagnitLE.setText(f"{self.mathVppValue/2:.2f}")

    #ajuste dos limites da tela:
    #obtendo o maior fasor:

    if self.btMath.isOn:
        if self.phasDiagMagnitVoltage == "RMS": greatestAmp = max(self.CH1VRMSValue, self.CH2VRMSValue, self.mathVRMSValue)
        elif self.phasDiagMagnitVoltage == "Pk-to-Pk": greatestAmp = max( self.CH1VppValue,  self.CH2VppValue,  self.mathVppValue)
        else: greatestAmp = max( self.CH1VppValue/2,  self.CH2VppValue/2,  self.mathVppValue/2)
    else:
        if self.phasDiagMagnitVoltage == "RMS": greatestAmp = max(self.CH1VRMSValue, self.CH2VRMSValue)
        elif self.phasDiagMagnitVoltage == "Pk-to-Pk": greatestAmp = max( self.CH1VppValue,  self.CH2VppValue)
        else: greatestAmp = max( self.CH1VppValue/2,  self.CH2VppValue/2)

    self.phasDiag_and_lissajScr.phasDiag.xBotLim = min(-0.5, -1 * greatestAmp)
    self.phasDiag_and_lissajScr.phasDiag.xTopLim = max(0.5, 1 * greatestAmp)
    self.phasDiag_and_lissajScr.phasDiag.yBotLim = min(-0.5, -1 * greatestAmp)
    self.phasDiag_and_lissajScr.phasDiag.yTopLim = max(0.5, 1 * greatestAmp)
    

    self.phasDiag_and_lissajScr.phasDiag.setRange(xRange=(self.phasDiag_and_lissajScr.phasDiag.xBotLim, 
                                                          self.phasDiag_and_lissajScr.phasDiag.xTopLim), 
                                                  yRange=(self.phasDiag_and_lissajScr.phasDiag.yBotLim, 
                                                          self.phasDiag_and_lissajScr.phasDiag.yTopLim))
    

    self.phasDiag_and_lissajScr.phasDiag.updateGraph()

    if self.CH1Phase > 180: self.CH1Phase = -1.0 * (360.0 - self.CH1Phase)
    elif self.CH1Phase < -180: self.CH1Phase = 360.0 + self.CH1Phase
    if self.CH2Phase > 180: self.CH2Phase = -1.0 * (360.0 - self.CH2Phase)
    elif self.CH2Phase < -180: self.CH2Phase = 360.0 + self.CH2Phase
    if self.mathPhase > 180: self.mathPhase = -1.0 * (360.0 - self.mathPhase)
    elif self.mathPhase < -180: self.mathPhase = 360.0 + self.mathPhase
    

    self.phasDiag_and_lissaj_scr2.page1.CH1PhaseLE.setText(f"{self.CH1Phase:.2f}") 
    self.phasDiag_and_lissaj_scr2.page1.CH2PhaseLE.setText(f"{self.CH2Phase:.2f}")
    self.phasDiag_and_lissaj_scr2.page1.MathPhaseLE.setText(f"{self.mathPhase:.2f}")

    if self.btCH1.isOn: self.phasDiag_and_lissajScr.phasDiag.CH1_on = True
    else:               self.phasDiag_and_lissajScr.phasDiag.CH1_on = False
    if self.btCH2.isOn: self.phasDiag_and_lissajScr.phasDiag.CH2_on = True
    else:               self.phasDiag_and_lissajScr.phasDiag.CH2_on = False
    if self.btMath.isOn: self.phasDiag_and_lissajScr.phasDiag.math_on = True
    else:               self.phasDiag_and_lissajScr.phasDiag.math_on = False


def togglePhasDiag(self):
    p = self.width()/1920
    if self.phasDiag_and_lissaj_scr2.page1.isolateScreen.isChecked():
        self.phasDiag_and_lissaj_scr2.page2.isolateScreen.setChecked(False)
        self.phasDiag_and_lissajScr.phasDiag.move(int(p*450), 0)
        self.phasDiag_and_lissajScr.lissaj.move(3000, 3000)
        
    else:
        self.phasDiag_and_lissajScr.phasDiag.move(int(p*610), 0)
        self.phasDiag_and_lissajScr.lissaj.move(int(p*150), 0)

        

def toggleLissaj(self):
    p = self.width()/1920        
    if  self.phasDiag_and_lissaj_scr2.page2.isolateScreen.isChecked():
        self.phasDiag_and_lissaj_scr2.page1.isolateScreen.setChecked(False)
        self.phasDiag_and_lissajScr.lissaj.move(int(p*450), 0)
        self.phasDiag_and_lissajScr.phasDiag.move(3000, 3000)
        
    else:
        self.phasDiag_and_lissajScr.lissaj.move(int(p*150), 0)
        self.phasDiag_and_lissajScr.phasDiag.move(int(p*610), 0)


def phasDiagChangeMagnitVoltage(self):
    if self.phasDiag_and_lissaj_scr2.page1.magnitudeVoltageCB.currentText() == "RMS": self.phasDiagMagnitVoltage = "RMS"
    elif self.phasDiag_and_lissaj_scr2.page1.magnitudeVoltageCB.currentText() == "Peak": self.phasDiagMagnitVoltage = "Peak"
    else:                                                                   self.phasDiagMagnitVoltage = "Pk-to-Pk"