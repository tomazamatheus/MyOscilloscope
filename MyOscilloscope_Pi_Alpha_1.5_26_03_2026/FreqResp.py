import sys
import numpy as np
from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QApplication, QDialog, QLabel
import os
os.environ["PYQTGRAPH_QT_LIB"] = "PySide6" #necessário para pyqtgraph com PySide6
from pyqtgraph import PlotWidget, mkPen, InfiniteLine
from PySide6.QtGui import QPixmap
import math

class FreqResp(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.stacked = QStackedWidget(self)

    
        self.magnitude = FreqResp_Magnitude()
        self.phase = FreqResp_Phase()

        self.stacked.addWidget(self.magnitude)  # index 0
        self.stacked.addWidget(self.phase)      # index 1


        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.stacked)

        self.stacked.setCurrentIndex(0)


class FreqResp_Magnitude(PlotWidget):
    def __init__(self, parent=None):
        super(FreqResp_Magnitude, self).__init__(parent)
        self.xBotLim = 10
        self.xTopLim = 10000
        self.yBotLim = -65
        self.yTopLim = 15
        self.getPlotItem().getViewBox().setMouseEnabled(x=False, y=False)
        self.getPlotItem().hideButtons()


        self.setBackground((5, 16, 5))
        self.showGrid(x=True, y=True, alpha=0.5)
        self.getPlotItem().setLogMode(x=True, y=False)

        self.setXRange(1, 4)
        
        major_ticks = [
            (1, "10"),
            (2, "100"),
            (3, "1000"),
            (4, "10000"),
        ]


        minor_ticks = []

        for decade in range(1, 6):  
            for k in range(2, 10):
                pos = decade + math.log10(k)
                minor_ticks.append((pos, "")) 

        self.getPlotItem().getAxis('bottom').setTicks([major_ticks, minor_ticks])
        

        self.setYRange(-65, 15)
        self.getPlotItem().getAxis('left').setTickSpacing(10, 5)

        #Ativar eixos da direita e do topo apenas como bordas
        self.getPlotItem().showAxis('right')
        self.getPlotItem().showAxis('top')
        self.getPlotItem().getAxis('right').setTicks([])  
        self.getPlotItem().getAxis('right').setStyle(showValues=True) 
        self.getPlotItem().getAxis('top').setTicks([])
        self.getPlotItem().getAxis('top').setStyle(showValues=False)

        self.getPlotItem().setLabel(axis='bottom', text='Frequency (Hz)', color='white', **{'font-size':'8pt'})
        self.getPlotItem().setLabel(axis='left', text='Magnitude (dB)', color='white', **{'font-size':'8pt'})

        self.minus3dBLine = InfiniteLine(
            pos=-3,
            angle=0,
            pen=mkPen(color="green", width=0.7)
        )
        self.addItem(self.minus3dBLine)

class FreqResp_Phase(PlotWidget):
    def __init__(self, parent=None):
        super(FreqResp_Phase, self).__init__(parent)
        self.xBotLim = 10
        self.xTopLim = 10000
        self.yBotLim = -180
        self.yTopLim = 180
        self.getPlotItem().getViewBox().setMouseEnabled(x=False, y=False)
        self.getPlotItem().hideButtons()


        self.setBackground((5, 12, 5))
        self.showGrid(x=True, y=True, alpha=0.5)
        self.getPlotItem().setLogMode(x=True, y=False)

        self.setXRange(1, 4)
        
        major_ticks = [
            (1, "10"),
            (2, "100"),
            (3, "1000"),
            (4, "10000"),
        ]


        minor_ticks = []

        for decade in range(1, 6):  
            for k in range(2, 10):
                pos = decade + math.log10(k)
                minor_ticks.append((pos, "")) 

        self.getPlotItem().getAxis('bottom').setTicks([major_ticks, minor_ticks])
        

        self.setYRange(-180, 180)
        self.getPlotItem().getAxis('left').setTickSpacing(20, 10)

        #Ativar eixos da direita e do topo apenas como bordas
        self.getPlotItem().showAxis('right')
        self.getPlotItem().showAxis('top')
        self.getPlotItem().getAxis('right').setTicks([])  
        self.getPlotItem().getAxis('right').setStyle(showValues=True) 
        self.getPlotItem().getAxis('top').setTicks([])
        self.getPlotItem().getAxis('top').setStyle(showValues=False)

        self.getPlotItem().setLabel(axis='bottom', text='Frequency (Hz)', color='white', **{'font-size':'8pt'})
        self.getPlotItem().setLabel(axis='left', text='Phase (degrees)', color='white', **{'font-size':'8pt'})

        self.deg45Line = InfiniteLine(
            pos=45,
            angle=0,
            pen=mkPen(color="green", width=0.6)
        )

        self.degMinus45Line = InfiniteLine(
            pos=-45,
            angle=0,
            pen=mkPen(color="green", width=0.6)
        )
        self.addItem(self.deg45Line)
        self.addItem(self.degMinus45Line)

        self.deg90Line = InfiniteLine(
            pos=90,
            angle=0,
            pen=mkPen(color="blue", width=0.4)
        )
        self.addItem(self.deg90Line)

        self.degMinus90Line = InfiniteLine(
            pos=-90,
            angle=0,
            pen=mkPen(color="blue", width=0.4)
        )
        self.addItem(self.degMinus90Line)

        self.degZeroLine = InfiniteLine(
            pos=0,
            angle=0,
            pen=mkPen(color="blue", width=0.4)
        )
        self.addItem(self.degZeroLine)



if __name__ == '__main__':
    app = QApplication([])
    window = FreqResp_Phase()
    window.show()
    app.exec()
