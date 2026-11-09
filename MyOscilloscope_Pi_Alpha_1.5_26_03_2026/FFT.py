import sys, math
import os
os.environ["PYQTGRAPH_QT_LIB"] = "PySide6" #necessário para pyqtgraph com PySide6
import pyqtgraph as pg
import pyqtgraph as pg
import numpy as np
from PySide6.QtWidgets import QApplication, QDialog, QLabel
from pyqtgraph import PlotWidget, mkPen
from PySide6.QtGui import QPixmap

    

class FFT(PlotWidget):
    def __init__(self, parent=None):
        super(FFT, self).__init__(parent)
       
        self.xBotLim = 10
        self.xTopLim = 10000
        self.yBotLim = -65
        self.yTopLim = 15
        self.getPlotItem().getViewBox().setMouseEnabled(x=False, y=False)
        self.getPlotItem().hideButtons()
        

        self.CH1_Active = True
        self.CH2_Active = True
        self.Math_Active = False


        self.setBackground((16, 5, 5))
        self.showGrid(x=True, y=True, alpha=0.5)
        self.getPlotItem().setLogMode(x=True, y=False)


        self.setXRange(1, math.log10(250000))
        major_ticks = [
            (1, "10"),
            (2, "100"),
            (3, "1000"),
            (4, "10000"),
            (math.log10(250000), "250000")
        ]


        minor_ticks = []

        for decade in range(1, 6):  
            for k in range(2, 10):
                pos = decade + math.log10(k)
                minor_ticks.append((pos, "")) 

        self.getPlotItem().getAxis('bottom').setTicks([major_ticks, minor_ticks])
        

        self.setYRange(-65, 15)
        self.getPlotItem().getAxis('left').setTickSpacing(10, 10)

        #Ativar eixos da direita e do topo apenas como bordas
        self.getPlotItem().showAxis('right')
        self.getPlotItem().showAxis('top')
        self.getPlotItem().getAxis('right').setTicks([])  
        self.getPlotItem().getAxis('right').setStyle(showValues=True) 
        self.getPlotItem().getAxis('top').setTicks([])
        self.getPlotItem().getAxis('top').setStyle(showValues=False)

        self.getPlotItem().setLabel(axis='bottom', text='Frequency (Hz)', color='white', **{'font-size':'8pt'})
        self.getPlotItem().setLabel(axis='left', text='Amplitude (dB)', color='white', **{'font-size':'8pt'})

        self.FFT_CH1 = None
        self.FFT_freqs_CH1 = None
        self.FFT_amplits_CH1 = None

        self.FFT_CH2 = None
        self.FFT_freqs_CH2 = None
        self.FFT_amplits_CH2 = None

        self.FFT_Math = None
        self.FFT_freqs_Math = None
        self.FFT_amplits_Math = None

        self.firstUpdate = True
        self.allowUpdateGraph = True

        #para efeito de inicialização:
        self.graphStyleCH1 = mkPen(color = "blue", width = 2)
        self.graphStyleCH2 = mkPen(color = "red", width = 2)
        self.graphStyleMath = mkPen(color = "cyan", width = 2)






        
    
    def domainChange(self, CH1, CH2, Math, samplingRate):
        self.N1 = len(CH1)
        CH1 = CH1 - np.mean(CH1) 
        CH1_w = CH1 * np.hanning(len(CH1)) #janela de Hanning para melhor FFT
        self.FFT_CH1 = np.fft.rfft(CH1_w) #rfft considera apenas a parte positiva no dom. da frequência
        self.FFT_freqs_CH1 = np.fft.rfftfreq(len(CH1), d=1/samplingRate)  #Todas as frequências
        self.FFT_amplits_CH1 = np.abs(self.FFT_CH1) / self.N1
        self.FFT_amplits_CH1[1:-1] *= 2 #ajuste por haver apenas parte positiva no nosso FFT - por padrão não é assim na biblioteca

        self.N2 = len(CH2)
        CH2 = CH2 - np.mean(CH2) 
        CH2_w = CH2 * np.hanning(len(CH2)) #janela de Hanning para melhor FFT
        self.FFT_CH2 = np.fft.rfft(CH2_w) #rfft considera apenas a parte positiva no dom. da frequência
        self.FFT_freqs_CH2 = np.fft.rfftfreq(len(CH2), d=1/samplingRate)  #Todas as frequências
        self.FFT_amplits_CH2 = np.abs(self.FFT_CH2) / self.N2
        self.FFT_amplits_CH2[1:-1] *= 2

        self.N_Math = len(Math)
        Math = Math - np.mean(Math) 
        Math_w = Math * np.hanning(len(Math)) #janela de Hanning para melhor FFT
        self.FFT_Math= np.fft.rfft(Math_w) #rfft considera apenas a parte positiva no dom. da frequência
        self.FFT_freqs_Math = np.fft.rfftfreq(len(Math), d=1/samplingRate)  #Todas as frequências
        self.FFT_amplits_Math = np.abs(self.FFT_Math) / self.N_Math
        self.FFT_amplits_Math[1:-1] *= 2

        self.amplitRef = 1 #1 V ou 3.3 V?
        eps = 1e-12 #eps evita valores nulos para o logaritmo
        self.FFT_amplits_CH1_dB = 20 * np.log10(np.maximum(self.FFT_amplits_CH1, eps) / self.amplitRef) 
        self.FFT_amplits_CH2_dB = 20 * np.log10(np.maximum(self.FFT_amplits_CH2, eps) / self.amplitRef) 
        self.FFT_amplits_Math_dB = 20 * np.log10(np.maximum(self.FFT_amplits_Math, eps) / self.amplitRef)

        
        

    def updateGraph(self):
        if self.firstUpdate:
            self.graphStyleCH1 = mkPen(color = "blue", width = 2)
            self.graphicPlotting_CH1 = self.plot(self.FFT_freqs_CH1, self.FFT_amplits_CH1_dB, pen = self.graphStyleCH1)

            self.graphStyleCH2 = mkPen(color = "red", width = 2)
            self.graphicPlotting_CH2 = self.plot(self.FFT_freqs_CH2, self.FFT_amplits_CH2_dB, pen = self.graphStyleCH2)

            self.graphStyleMath = mkPen(color = "cyan", width = 2)
            self.graphicPlotting_Math = self.plot(self.FFT_freqs_Math, self.FFT_amplits_Math_dB, pen= self.graphStyleMath)
            
            self.firstUpdate = False

        if self.allowUpdateGraph:
            if self.CH1_Active: self.graphicPlotting_CH1.setData(self.FFT_freqs_CH1, self.FFT_amplits_CH1_dB)
            else: self.removeItem(self.graphicPlotting_CH1)
            if self.CH2_Active: self.graphicPlotting_CH2.setData(self.FFT_freqs_CH2, self.FFT_amplits_CH2_dB)
            else: self.removeItem(self.graphicPlotting_CH2)
            if self.Math_Active: self.graphicPlotting_Math.setData(self.FFT_freqs_Math, self.FFT_amplits_Math_dB)
            else: self.removeItem(self.graphicPlotting_Math)
                
                
        self.top3_components_CH1 = np.argsort(self.FFT_amplits_CH1)[-3:][::-1]
        self.top3_amplitudes_CH1 = self.FFT_amplits_CH1_dB[self.top3_components_CH1]
        self.top3_freqs_CH1 = self.FFT_freqs_CH1[self.top3_components_CH1]

        self.top3_components_CH2 = np.argsort(self.FFT_amplits_CH2)[-3:][::-1]
        self.top3_amplitudes_CH2 = self.FFT_amplits_CH2_dB[self.top3_components_CH2]
        self.top3_freqs_CH2 = self.FFT_freqs_CH2[self.top3_components_CH2]

        self.top3_components_Math = np.argsort(self.FFT_amplits_Math)[-3:][::-1]
        self.top3_amplitudes_Math = self.FFT_amplits_Math_dB[self.top3_components_Math]
        self.top3_freqs_Math = self.FFT_freqs_Math[self.top3_components_Math]

if __name__ == '__main__':
    app = QApplication([])
    window = FFT()
    window.show()
    app.exec()
            

    
        
        
