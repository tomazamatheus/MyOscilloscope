from PySide6.QtWidgets import QDialog, QApplication, QLabel, QComboBox, QLineEdit, QPushButton
from PySide6.QtCore import Qt
from button import Button
from PySide6.QtGui import QPixmap
from PySide6.QtSvgWidgets import QSvgWidget
import sys



class COM_Port(QDialog):
    def __init__(self):
        super(COM_Port, self).__init__()
        self.setGeometry(50, 677, 345, 80)
        self.p = self.width()/345
        self.backgroundSvg = QSvgWidget("images_svg/screen_COMPort.svg", self)
        self.backgroundSvg.setGeometry(0, 0, int(self.p * 410), int(self.p * 82))
        self.backgroundSvg.lower()


        self.COM_PortLE = QLineEdit(self)
        self.COM_PortLE.setGeometry(int(self.p * 6), int(self.p * 38), int(self.p * 138), int(self.p * 32))
        self.COM_PortLE.setStyleSheet("""background-color: rgb(140, 140, 140); 
                                                            color: rgb(255, 255, 255)""")
        #self.COM_PortLE.addItems(self.CB_Items)
        self.COM_PortLE.setText("No Port.")

        #Refresh (LabVIEW) = Search (Python)
        self.btSearch = Button(self, int(self.p * 163), int(self.p * 38), int(self.p * 157), int(self.p * 32), "Search",
                            "images_svg/bt_Search.svg", "images_svg/bt_Search.svg", False)

        
        self.signalIconRed = QSvgWidget("images_svg/COMPort_OFF.svg", self)
        self.signalIconRed.setGeometry(int(self.p * 350), int(self.p * 32), int(self.p * 38), int(self.p * 38))
        self.signalIconRed.setStyleSheet("background-color: transparent")

        self.signalIconGreen = QSvgWidget("images_svg/COMPort_ON.svg", self)
        self.signalIconGreen.setGeometry(-400, -400, -400, -400)
        self.signalIconGreen.setStyleSheet("background-color: transparent")

    def ChangeCurrentCOM_Port(self):
        self.currentCOM_Port = self.COM_PortCB.currentText()

class BlackScreen_Scr4(QDialog):
    def __init__(self):
        super(BlackScreen_Scr4, self).__init__()
        self.setGeometry(60, 685, 325, 65)
        self.setStyleSheet("background-color: rgb(40, 40, 40)")

# app = QApplication(sys.argv)
# window = COM_Port()
# window.show()
# app.exec()
