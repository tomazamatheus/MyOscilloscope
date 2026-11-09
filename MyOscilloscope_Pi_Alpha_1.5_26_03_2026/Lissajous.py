import sys
from PySide6.QtWidgets import QApplication, QDialog, QLabel
import os
os.environ["PYQTGRAPH_QT_LIB"] = "PySide6" #necessário para pyqtgraph com PySide6
from pyqtgraph import PlotWidget, mkPen
from PySide6.QtGui import QPixmap
import numpy as np

class Lissajous(PlotWidget):
    def __init__(self, parent=None):
        super(Lissajous, self).__init__(parent)
        self.setGeometry(10, 260, 360, 360)
        self.xBotLim = -2
        self.xTopLim = 2
        self.yBotLim = -2
        self.yTopLim = 2
        self.getPlotItem().getViewBox().setMouseEnabled(x=False, y=False)
        self.getPlotItem().hideButtons()
        self.setRange(xRange=(self.xBotLim, self.xTopLim), yRange=(self.yBotLim, self.yTopLim))
        self.setBackground((18, 18, 0))
        self.showGrid(x=True, y=True, alpha=0.4)
        self.getPlotItem().getAxis('bottom').setTickSpacing(0.5, 0.5)
        self.getPlotItem().getAxis('left').setTickSpacing(0.5, 0.5)
        self.getAxis('left').enableAutoSIPrefix(False) #Não divide por 1000 quando os valores são pequenos se False
        self.getAxis('bottom').enableAutoSIPrefix(False)
        self.getPlotItem().setLabel(axis='bottom', text='CH1 (V)', color='white', **{'font-size':'8pt'})
        self.getPlotItem().setLabel(axis='left', text='CH2 (V)', color='white', **{'font-size':'8pt'})
        #self.getAxis('left').setStyle(showValues=False)  # Esconde os números do eixo vertical
        #self.getAxis('bottom').setStyle(showValues=False)  # idem, horizontal
        self.firstUpdate = True
        #self.getPlotItem().getViewBox().setAspectLocked(True)

    def updateGraph(self, xAxis, yAxis):
        self.xAxis = xAxis
        self.yAxis = yAxis
        if self.firstUpdate:
            #self.graphStyle = mkPen(color = "yellow", width = 2.6)
            self.graphicPlotting = self.plot(self.xAxis, self.yAxis, pen = None, symbol='o', symbolSize=5, symbolBrush='skyblue')
            self.firstUpdate = False

        else:
            self.graphicPlotting.setData(xAxis, yAxis)
            

        # self.xMax= np.max(xAxis)
        # self.xMin= np.min(xAxis)
        # self.yMax= np.max(yAxis)
        # self.yMin= np.min(yAxis)
    
if __name__ == '__main__':
    app = QApplication([])
    window = Lissajous()
    window.show()
    app.exec()