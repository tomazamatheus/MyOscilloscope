import sys
from PySide6.QtWidgets import QApplication, QDialog, QLabel
import os
os.environ["PYQTGRAPH_QT_LIB"] = "PySide6" #necessário para pyqtgraph com PySide6
import pyqtgraph as pg
from pyqtgraph import PlotWidget, mkPen
from PySide6.QtGui import QPixmap
import numpy as np

class PhasDiag(PlotWidget):
    def __init__(self, parent=None):
        super(PhasDiag, self).__init__(parent)
        self.setGeometry(345, 300, 400, 400)
        self.xBotLim = -2
        self.xTopLim = 2
        self.yBotLim = -2
        self.yTopLim = 2
        self.getPlotItem().getViewBox().setMouseEnabled(x=False, y=False)
        self.getPlotItem().hideButtons()
        self.setRange(xRange=(self.xBotLim, self.xTopLim), yRange=(self.yBotLim, self.yTopLim))
        self.setBackground((18, 18, 0))
        self.showGrid(x=True, y=True, alpha=0.4)
        self.getPlotItem().getAxis('bottom').setTickSpacing(0.25, 0.25)
        self.getPlotItem().getAxis('left').setTickSpacing(0.25, 0.25)
        self.getAxis('left').setStyle(showValues=False)  # Esconde os números do eixo vertical
        self.getAxis('bottom').setStyle(showValues=False)  # idem, horizontal

        #plot da abcissa:
        self.x_xAxis = np.arange(-40, 40)
        self.y_xAxis = np.zeros_like(self.x_xAxis) 
        self.xAxisLineStyle = mkPen(color="white", width=1.0)
        self.graphicPlottingY1Line = self.plot(self.x_xAxis, self.y_xAxis, pen=self.xAxisLineStyle)

        #plot da ordenada:
        self.y_yAxis = np.arange(-40, 40)
        self.x_yAxis = np.zeros_like(self.y_xAxis) 
        self.yAxisLineStyle = mkPen(color="white", width=1.0)
        self.graphicPlottingY1Line = self.plot(self.x_yAxis, self.y_yAxis, pen=self.yAxisLineStyle)

        self.CH1_xcoord = 0
        self.CH1_ycoord = 0
        self.CH2_xcoord = 0
        self.CH2_ycoord = 0
        self.math_xcoord = 0
        self.math_ycoord = 0
        self.CH1_Phase = 0
        self.CH2_Phase = 0
        self.math_Phase = 0

        self.CH1_on = True
        self.CH2_on = True
        self.math_on = False

        self.CH1_Phasor = self.plot([0, self.CH1_xcoord], [0, self.CH1_ycoord], pen= mkPen('b', width=2))
        self.CH2_Phasor = self.plot([0, self.CH2_xcoord], [0, self.CH2_ycoord], pen= mkPen('r', width=2))
        self.math_Phasor = self.plot([0, self.math_xcoord], [0, self.math_ycoord], pen= mkPen('c', width=2))

        self.arrow_CH1 = pg.ArrowItem(
            pos=(self.CH1_xcoord, self.CH1_ycoord),                   
            angle= 180 - np.degrees(np.arctan2(self.CH1_ycoord, self.CH1_xcoord)),     
            headLen=15,                             
            brush='b'                               
        )
        self.addItem(self.arrow_CH1)

        self.arrow_CH2 = pg.ArrowItem(
            pos=(self.CH2_xcoord, self.CH2_ycoord),                   
            angle= 180 - np.degrees(np.arctan2(self.CH2_ycoord, self.CH2_xcoord)),     
            headLen=15,                             
            brush='r'                               
        )
        self.addItem(self.arrow_CH2)

        self.arrow_Math = pg.ArrowItem(
            pos=(self.math_xcoord, self.math_ycoord),                   
            angle= 180 - np.degrees(np.arctan2(self.math_ycoord, self.math_xcoord)),     
            headLen=15,                             
            brush='c'                               
        )
        self.addItem(self.arrow_Math)

       

    def updateGraph(self):
        self.removeItem(self.CH1_Phasor)
        self.removeItem(self.CH2_Phasor)
        self.removeItem(self.math_Phasor)
        self.removeItem(self.arrow_CH1)
        self.removeItem(self.arrow_CH2)
        self.removeItem(self.arrow_Math)

        if self.CH1_on:
            self.CH1_Phasor = self.plot([0, self.CH1_xcoord], [0, self.CH1_ycoord], pen= mkPen('b', width=2))
            self.arrow_CH1 = pg.ArrowItem(
                pos=(self.CH1_xcoord, self.CH1_ycoord),                   
                angle= 180 - np.degrees(np.arctan2(self.CH1_ycoord, self.CH1_xcoord)),     
                headLen=15,                             
                brush='b'                               
            )
            self.addItem(self.arrow_CH1)

        if self.CH2_on:
            self.CH2_Phasor = self.plot([0, self.CH2_xcoord], [0, self.CH2_ycoord], pen= mkPen('r', width=2))
            self.arrow_CH2 = pg.ArrowItem(
                pos=(self.CH2_xcoord, self.CH2_ycoord),                   
                angle= 180 - np.degrees(np.arctan2(self.CH2_ycoord, self.CH2_xcoord)),     
                headLen=15,                             
                brush='r'                               
            )
            self.addItem(self.arrow_CH2)
        
        if self.math_on:
            self.math_Phasor = self.plot([0, self.math_xcoord], [0, self.math_ycoord], pen= mkPen('c', width=2))
            self.arrow_Math = pg.ArrowItem(
                pos=(self.math_xcoord, self.math_ycoord),                   
                angle= 180 - np.degrees(np.arctan2(self.math_ycoord, self.math_xcoord)),
                headLen=15,                             
                brush='c'                               
            )
            self.addItem(self.arrow_Math)




if __name__ == '__main__':
    app = QApplication([])
    window = PhasDiag()
    window.show()
    app.exec()