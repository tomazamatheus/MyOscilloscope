import numpy as np
import math

def measurements(self):
        #FFT dos canais:
        self.FFTScr.domainChange(self.mainScr.y_CH1, self.mainScr.y_CH2, self.mainScr.y_Math, self.mainScr.samplingRate)
        if not self.mainScr.freezeTime: self.FFTScr.updateGraph()
        if self.FFT_scr2.page2.channelCB.currentText() == "CH1":
            self.FFT_scr2.page2.freq1LE.setText(f"{self.FFTScr.top3_freqs_CH1[0]:.0f}")
            self.FFT_scr2.page2.freq2LE.setText(f"{self.FFTScr.top3_freqs_CH1[1]:.0f}")
            self.FFT_scr2.page2.freq3LE.setText(f"{self.FFTScr.top3_freqs_CH1[2]:.0f}")

            self.FFT_scr2.page2.ampl1LE.setText(f"{self.FFTScr.top3_amplitudes_CH1[0]:.2f}")
            self.FFT_scr2.page2.ampl2LE.setText(f"{self.FFTScr.top3_amplitudes_CH1[1]:.2f}")
            self.FFT_scr2.page2.ampl3LE.setText(f"{self.FFTScr.top3_amplitudes_CH1[2]:.2f}")

        elif self.FFT_scr2.page2.channelCB.currentText() == "CH2":
            self.FFT_scr2.page2.freq1LE.setText(f"{self.FFTScr.top3_freqs_CH2[0]:.0f}")
            self.FFT_scr2.page2.freq2LE.setText(f"{self.FFTScr.top3_freqs_CH2[1]:.0f}")
            self.FFT_scr2.page2.freq3LE.setText(f"{self.FFTScr.top3_freqs_CH2[2]:.0f}")

            self.FFT_scr2.page2.ampl1LE.setText(f"{self.FFTScr.top3_amplitudes_CH2[0]:.2f}")
            self.FFT_scr2.page2.ampl2LE.setText(f"{self.FFTScr.top3_amplitudes_CH2[1]:.2f}")
            self.FFT_scr2.page2.ampl3LE.setText(f"{self.FFTScr.top3_amplitudes_CH2[2]:.2f}")

        elif self.FFT_scr2.page2.channelCB.currentText() == "Math":
            self.FFT_scr2.page2.freq1LE.setText(f"{self.FFTScr.top3_freqs_Math[0]:.0f}")
            self.FFT_scr2.page2.freq2LE.setText(f"{self.FFTScr.top3_freqs_Math[1]:.0f}")
            self.FFT_scr2.page2.freq3LE.setText(f"{self.FFTScr.top3_freqs_Math[2]:.0f}")

            self.FFT_scr2.page2.ampl1LE.setText(f"{self.FFTScr.top3_amplitudes_Math[0]:.2f}")
            self.FFT_scr2.page2.ampl2LE.setText(f"{self.FFTScr.top3_amplitudes_Math[1]:.2f}")
            self.FFT_scr2.page2.ampl3LE.setText(f"{self.FFTScr.top3_amplitudes_Math[2]:.2f}")

        #cálculo de frequência e período:
        self.greatest_amplit_CH1 = np.argmax(self.FFTScr.FFT_amplits_CH1[1:]) + 1 #retirando o DC
        self.greatest_amplit_CH2 = np.argmax(self.FFTScr.FFT_amplits_CH2[1:]) + 1
        self.greatest_amplit_Math = np.argmax(self.FFTScr.FFT_amplits_Math[1:]) + 1

        #determinação da frequência por interpolação parabólica
        # CH1
        k = self.greatest_amplit_CH1
        A1 = self.FFTScr.FFT_amplits_CH1[k-1]
        A2 = self.FFTScr.FFT_amplits_CH1[k]
        A3 = self.FFTScr.FFT_amplits_CH1[k+1]

        with np.errstate(divide='ignore', invalid='ignore'): #ignorar RuntimeWarning por divisão por zero ao iniciar o programa
            delta = 0.5 * (A1 - A3) / (A1 - 2*A2 + A3)
            self.freqCH1 = self.FFTScr.FFT_freqs_CH1[k] + delta * (self.FFTScr.FFT_freqs_CH1[1] - self.FFTScr.FFT_freqs_CH1[0])

        # CH2
        k = self.greatest_amplit_CH2
        A1 = self.FFTScr.FFT_amplits_CH2[k-1]
        A2 = self.FFTScr.FFT_amplits_CH2[k]
        A3 = self.FFTScr.FFT_amplits_CH2[k+1]

        with np.errstate(divide='ignore', invalid='ignore'):
            delta = 0.5 * (A1 - A3) / (A1 - 2*A2 + A3)
            self.freqCH2 = self.FFTScr.FFT_freqs_CH2[k] + delta * (self.FFTScr.FFT_freqs_CH2[1] - self.FFTScr.FFT_freqs_CH2[0])

        #Math
        k = self.greatest_amplit_Math
        A1 = self.FFTScr.FFT_amplits_Math[k-1]
        A2 = self.FFTScr.FFT_amplits_Math[k]
        A3 = self.FFTScr.FFT_amplits_Math[k+1]

        with np.errstate(divide='ignore', invalid='ignore'):
            delta = 0.5 * (A1 - A3) / (A1 - 2*A2 + A3)
            self.freqMath = self.FFTScr.FFT_freqs_Math[k] + delta * (self.FFTScr.FFT_freqs_Math[1] - self.FFTScr.FFT_freqs_Math[0])

        if not self.freqCH1 == 0:
            self.periodCH1 = 1/self.freqCH1
        else:
            self.periodCH1 = math.inf

        if not self.freqCH2 == 0:
            self.periodCH2 = 1/self.freqCH2
        else:
            self.periodCH2 = math.inf


        if not self.freqMath == 0:
            self.periodMath = 1/self.freqMath
        else:
            self.periodMath = math.inf

        #defasagem:
        self.CH1Phase = np.degrees(np.angle(self.FFTScr.FFT_CH1[self.greatest_amplit_CH1]))
        self.CH2Phase = np.degrees(np.angle(self.FFTScr.FFT_CH2[self.greatest_amplit_CH2]))
        self.mathPhase =np.degrees(np.angle(self.FFTScr.FFT_Math[self.greatest_amplit_Math]))

        #deixando a fase sempre entre -180 e 180 graus:
        if self.CH1Phase > 180: self.CH1Phase = -1.0 * (360.0 - self.CH1Phase)
        elif self.CH1Phase < -180: self.CH1Phase = 360.0 + self.CH1Phase
        if self.CH2Phase > 180: self.CH2Phase = -1.0 * (360.0 - self.CH2Phase)
        elif self.CH2Phase < -180: self.CH2Phase = 360.0 + self.CH2Phase
        if self.mathPhase > 180: self.mathPhase = -1.0 * (360.0 - self.mathPhase)
        elif self.mathPhase < -180: self.mathPhase = 360.0 + self.mathPhase

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


        self.yMaxCH1 = np.max(self.mainScr.y_CH1_pure) 
        self.yMaxCH2 = np.max(self.mainScr.y_CH2_pure) 
        self.yMaxMath = np.max(self.mainScr.y_Math_pure) 

        self.yMinCH1 = np.min(self.mainScr.y_CH1_pure) 
        self.yMinCH2 = np.min(self.mainScr.y_CH2_pure) 
        self.yMinMath = np.min(self.mainScr.y_Math_pure) 
        #valor médio:
        self.CH1MeanValue = np.mean(self.mainScr.y_CH1_pure) 
        self.CH2MeanValue = np.mean(self.mainScr.y_CH2_pure) 
        self.mathMeanValue = np.mean(self.mainScr.y_Math_pure) 

        #Vpp:
        self.CH1VppValue = self.yMaxCH1 - self.yMinCH1
        self.CH2VppValue = self.yMaxCH2 - self.yMinCH2
        self.mathVppValue = self.yMaxMath - self.yMinMath

        # #Vrms:

        y_CH1 = self.mainScr.y_CH1_pure
        y_CH2 = self.mainScr.y_CH2_pure
        y_Math = self.mainScr.y_Math_pure

        N_CH1 = len(y_CH1)
        mean = sum(y_CH1) / N_CH1
        self.CH1VRMSValue = math.sqrt(
            sum((x - mean)**2 for x in y_CH1) / N_CH1
        )

        N_CH2 = len(y_CH2)
        mean = sum(y_CH2) / N_CH2
        self.CH2VRMSValue = math.sqrt(
            sum((x - mean)**2 for x in y_CH2) / N_CH2
        )

        N_math = len(y_Math)
        mean = sum(y_Math) / N_math
        self.mathVRMSValue = math.sqrt(
            sum((x - mean)**2 for x in y_Math) / N_math
        )
    

        #relativo ao trigger - associado ao dataHandler
        
        if (self.mainScr.referencePhase == "CH1"):
            self.yMaxTrig = self.yMaxCH1
            self.yMinTrig = self.yMinCH1

        elif (self.mainScr.referencePhase == "CH2"):
            self.yMaxTrig = self.yMaxCH2
            self.yMinTrig = self.yMinCH2

        elif (self.mainScr.referencePhase == "Math"):
            self.yMaxTrig = self.yMaxMath
            self.yMinTrig = self.yMinMath
    
    

        self.mainScr.dataHandler.triggerValue = self.mainScr.triggerUsefulEdgeValue

        if self.mainScr.triggerUsefulEdgeValue < self.yMaxTrig and self.mainScr.triggerUsefulEdgeValue > self.yMinTrig:
            self.mainScr.dataHandler.triggerPossible = True
        else:
            self.mainScr.dataHandler.triggerPossible = False




        self.mainScr.dataHandler.triggerType = self.mainScr.triggerType
        self.mainScr.dataHandler.triggerMode = self.mainScr.triggerMode
        self.mainScr.dataHandler.triggerChannel = self.mainScr.triggerChannel
        if not self.mainScr.freezeTime: self.updatePhasDiag()
        if not self.mainScr.freezeTime: self.updateLissajous()
        if not self.mainScr.freezeTime: self.UpdateMeasure()