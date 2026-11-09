import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
import os
os.environ["PYQTGRAPH_QT_LIB"] = "PySide6" #necessário para pyqtgraph com PySide6
import pyqtgraph as pg
import numpy as np
from PhasDiag import PhasDiag
from Lissajous import Lissajous


#Essa classe reúne as classes de PhasDiag.py e de Lissajous.py, que estão em conjunto na tela PhasDiag/Lissajous
class PhasDiag_and_Lissajous(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(10, 260, 1120, 360)
        self.setStyleSheet('''background-color: "black" ''')
        self.phasDiag = PhasDiag(self)
        self.lissaj = Lissajous(self)

        self.phasDiag.setGeometry(610, 0, 430, 430)
        self.lissaj.setGeometry(150, 0, 410, 410)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = PhasDiag_and_Lissajous()
    win.show()
    sys.exit(app.exec())