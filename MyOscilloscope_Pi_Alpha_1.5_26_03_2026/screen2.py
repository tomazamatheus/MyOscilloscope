from PySide6.QtWidgets import QDialog, QLabel, QComboBox, QLineEdit, QApplication, QPushButton, QCheckBox, QScrollArea, QWidget, QVBoxLayout, QStackedWidget
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtCore import Qt, QRect
import os
os.environ["PYQTGRAPH_QT_LIB"] = "PySide6" #necessário para pyqtgraph com PySide6
from pyqtgraph import QtCore
from button import Button
import sys


class Standby_Screen2(QDialog):
    def __init__(self):
        super(Standby_Screen2, self).__init__()
        self.screenOn = True
        self.mainLabel = QLabel("", self)

    def changeStandbyScreen(self):

        if self.screenOn == True:
            self.mainLabel.setText("")
            self.setGeometry(890, 260, 151, 371)
            self.setStyleSheet("background-color: rgb(40, 40, 40);")
            self.mainLabel.setGeometry(0, 150, 151, 52)
            self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
            self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.mainLabel.setFont(QFont("Microsoft Sans Serif", 9))
        else:
            self.mainLabel.setText("")
            self.mainLabel.setStyleSheet(""" color: rgb(240, 50, 240) """)
            self.setStyleSheet("background-color: rgb(256, 256, 256);")


class Trigger(QDialog):
    def __init__(self):
        super(Trigger, self).__init__()
        self.setGeometry(890, 260, 151, 371)
        self.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.mainLabel = QLabel("Trigger", self)
        self.mainLabel.setGeometry(0, 20, 151, 52)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 25))

        self.trigChannelLabel = QLabel("Trigger Channel:", self)
        self.trigChannelLabel.setGeometry(5, 190, 151, 22)
        self.trigChannelLabel.setStyleSheet(
            """ color: rgb(240, 240, 240) """)
        self.trigChannelLE = QLineEdit(self)
        self.trigChannelLE.setText("CH1")
        self.trigChannelLE.setReadOnly(True)
        self.trigChannelLE.setGeometry(0, 210, 151, 22)
        self.trigChannelLE.setStyleSheet("""background-color: rgb(56, 56, 56); 
                                            color: rgb(240, 240, 240)""")
        
        self.trigChannelLabel2 = QLabel("To change the trigger channel, change the reference channel in the Main section.", self)
        self.trigChannelLabel2.setWordWrap(True)
        self.trigChannelLabel2.setGeometry(0, 255, 151, 30)
        self.trigChannelLabel2.setStyleSheet("color: rgb(240, 240, 240)")
        self.trigChannelLabel2.setFont(QFont("Microsoft Sans Serif", 7))
        

        self.trigTypeCBLabel = QLabel("Trigger Type:", self)
        self.trigTypeCBLabel.setGeometry(5, 310, 151, 22)
        self.trigTypeCBLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.trigTypeCB = QComboBox(self)
        self.trigTypeCB.setGeometry(0, 330, 151, 22)
        self.trigTypeCB.setStyleSheet("""background-color: rgb(56, 56, 56); 
                                                    color: rgb(240, 240, 240)""")
        
        

        self.trigModeCBLabel = QLabel("Trigger Mode:", self)
        self.trigModeCBLabel.setGeometry(5, 70, 151, 22)
        self.trigModeCBLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.trigModeCB = QComboBox(self)
        self.trigModeCB.setGeometry(0, 90, 151, 22)
        self.trigModeCB.setStyleSheet("""background-color: rgb(56, 56, 56); 
                                                            color: rgb(240, 240, 240)""")

        
        
        self.trigTypeCBItens = ["Rising Edge", "Falling Edge"]
        self.trigModeCBItens = ["Manual", "Automatic"]
        
        self.trigTypeCB.addItems(self.trigTypeCBItens)
        self.trigModeCB.addItems(self.trigModeCBItens)

    def resizeEvent(self, event):

        p = self.width()/151
        self.trigModeCB.setGeometry(0, int(p * 95), int(p * 151), int(p * 30))
        self.trigTypeCB.setGeometry(0, int(p * 335), int(p * 151), int(p * 30))
        self.trigChannelLE.setGeometry(
            0, int(p * 255), int(p * 151), int(p * 30))
        self.trigModeCBLabel.setGeometry(
            int(p * 5), int(p * 70), int(p * 151), int(p * 27))
        self.trigTypeCBLabel.setGeometry(
            int(p * 5), int(p * 310), int(p * 151), int(p * 27))
        self.trigChannelLabel.setGeometry(
            int(p * 5), int(p * 190), int(p * 151), int(p * 27))
        self.trigChannelLabel2.setGeometry(0, int(p * 215), int(p * 151), int(p * 38))
        self.mainLabel.setGeometry(0, int(p * 20), int(p * 151), int(p * 52))

        if (self.width() <= 109):
            font = QFont("Lucida Sans Unicode", 8)
            self.trigModeCB.setFont(font)
            self.trigTypeCB.setFont(font)
            self.trigChannelLE.setFont(font)

        if (self.width() <= 75):
            font = QFont("Lucida Sans Unicode", 6)
            self.trigModeCB.setFont(font)
            self.trigTypeCB.setFont(font)
            self.trigChannelLE.setFont(font)
            self.trigModeCB.setGeometry(
                0, int(p * 90), int(p * 151), int(p * 32))
            self.trigTypeCB.setGeometry(
                0, int(p * 330), int(p * 151), int(p * 32))
            self.trigChannelLE.setGeometry(
                0, int(p * 210), int(p * 151), int(p * 32))
            self.trigModeCBLabel.setFont(QFont("Lucida Sans Unicode", 6))
            self.trigTypeCBLabel.setFont(QFont("Lucida Sans Unicode", 6))
            self.trigChannelLabel.setFont(QFont("Lucida Sans Unicode", 6))

        if (self.width() <= 54):
            self.trigModeCBLabel.setFont(QFont("Lucida Sans Unicode", 5))
            self.trigTypeCBLabel.setFont(QFont("Lucida Sans Unicode", 5))
            self.trigChannelLabel.setFont(QFont("Lucida Sans Unicode", 5))
            self.mainLabel.setFont(QFont("Microsoft Sans Serif", 10))
            self.trigModeCB.setGeometry(
                0, int(p * 90), int(p * 151), int(p * 42))
            self.trigTypeCB.setGeometry(
                0, int(p * 330), int(p * 151), int(p * 42))
            self.trigChannelLE.setGeometry(
                0, int(p * 210), int(p * 151), int(p * 42))


class Measure(QDialog):
    def __init__(self):
        super(Measure, self).__init__()
        self.setGeometry(890, 260, 151, 371)
        self.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.mainLabel = QLabel("Measure", self)
        self.mainLabel.setGeometry(0, 0, 151, 52)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 16))

        self.channelSelectLabel = QLabel("Channel: ", self)
        self.channelSelectLabel.setGeometry(5, 30, 151, 22)
        self.channelSelectLabel.setStyleSheet(
            """ color: rgb(240, 240, 240) """)
        # self.channelSelectLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.channelSelectCB = QComboBox(self)
        self.channelSelectCB.setGeometry(0, 50, 151, 22)
        self.channelSelectCB.setStyleSheet("""background-color: rgb(56, 56, 56); 
                                                                    color: rgb(240, 240, 240)""")

        self.channelSelectCBItems = ["CH1", "CH2", "Math"]
        self.channelSelectCB.addItems(self.channelSelectCBItems)

        self.frequencyLabel = QLabel("Frequency ", self)
        self.frequencyLabel.setGeometry(5, 80, 141, 22)
        self.frequencyLabel.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.frequencyLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.frequencyLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freqLE = QLineEdit(self)
        self.freqLE.setGeometry(5, 100, 141, 20)
        self.freqLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.freqLE.setText("500 Hz")
        self.freqLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freqLE.setReadOnly(True)

        self.periodLabel = QLabel("Period ", self)
        self.periodLabel.setGeometry(5, 130, 141, 22)
        self.periodLabel.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.periodLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.periodLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.periodLE = QLineEdit(self)
        self.periodLE.setGeometry(5, 150, 141, 20)
        self.periodLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.periodLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.periodLE.setText("9000 s")
        self.periodLE.setReadOnly(True)

        self.meanLabel = QLabel("DC - Mean ", self)
        self.meanLabel.setGeometry(5, 180, 141, 22)
        self.meanLabel.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.meanLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.meanLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.meanLE = QLineEdit(self)
        self.meanLE.setGeometry(5, 200, 141, 20)
        self.meanLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.meanLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.meanLE.setText("1.2 V")
        self.meanLE.setReadOnly(True)

        self.vppLabel = QLabel("Peak-to-Peak", self)
        self.vppLabel.setGeometry(5, 230, 141, 22)
        self.vppLabel.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.vppLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.vppLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.vppLE = QLineEdit(self)
        self.vppLE.setGeometry(5, 250, 141, 20)
        self.vppLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.vppLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.vppLE.setText("9.5 V")
        self.vppLE.setReadOnly(True)

        self.vrmsLabel = QLabel("RMS", self)
        self.vrmsLabel.setGeometry(5, 280, 141, 22)
        self.vrmsLabel.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.vrmsLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.vrmsLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.vrmsLE = QLineEdit(self)
        self.vrmsLE.setGeometry(5, 300, 141, 20)
        self.vrmsLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.vrmsLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.vrmsLE.setText("344.6 V")
        self.vrmsLE.setReadOnly(True)

        self.maxLabel = QLabel("Max", self)
        self.maxLabel.setGeometry(80, 330, 70, 22)
        self.maxLabel.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.maxLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.maxLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.maxLE = QLineEdit(self)
        self.maxLE.setGeometry(75, 350, 70, 20)
        self.maxLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.maxLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.maxLE.setText("1399.8 V")
        self.maxLE.setReadOnly(True)

        self.minLabel = QLabel("Min", self)
        self.minLabel.setGeometry(5, 330, 70, 22)
        self.minLabel.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.minLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.minLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.minLE = QLineEdit(self)
        self.minLE.setGeometry(5, 350, 70, 20)
        self.minLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.minLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.minLE.setText("-1399.8 V")
        self.minLE.setReadOnly(True)

        self.phaseLabel = QLabel("Phase Shift", self)
        self.phaseLabel.setGeometry(5, 380, 141, 22)
        self.phaseLabel.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.phaseLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.phaseLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.phaseLE = QLineEdit(self)
        self.phaseLE.setGeometry(5, 400, 141, 20)
        self.phaseLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.phaseLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.phaseLE.setText("")
        self.phaseLE.setReadOnly(True)

    def resizeEvent(self, event):

        p = self.width()/151
        self.mainLabel.setGeometry(0, 0, int(p * 151), int(p * 52))
        self.channelSelectLabel.setGeometry(
            int(p * 5), int(p * 30), int(p * 151), int(p * 22))
        self.channelSelectCB.setGeometry(
            0, int(p * 50), int(p * 151), int(p * 27))
        self.frequencyLabel.setGeometry(
            int(p * 5), int(p * 80), int(p * 141), int(p * 22))
        self.freqLE.setGeometry(int(p * 5), int(p * 100),
                                int(p * 141), int(p * 27))
        self.periodLabel.setGeometry(
            int(p * 5), int(p * 130), int(p * 141), int(p * 22))
        self.periodLE.setGeometry(
            int(p * 5), int(p * 150), int(p * 141), int(p * 25))
        self.meanLabel.setGeometry(
            int(p * 5), int(p * 180), int(p * 141), int(p * 22))
        self.meanLE.setGeometry(int(p * 5), int(p * 200),
                                int(p * 141), int(p * 25))
        self.vppLabel.setGeometry(
            int(p * 5), int(p * 230), int(p * 141), int(p * 22))
        self.vppLE.setGeometry(int(p * 5), int(p * 250),
                               int(p * 141), int(p * 25))
        self.vrmsLabel.setGeometry(
            int(p * 5), int(p * 280), int(p * 141), int(p * 22))
        self.vrmsLE.setGeometry(int(p * 5), int(p * 300),
                                int(p * 141), int(p * 25))
        self.minLabel.setGeometry(
            int(p * 5), int(p * 330), int(p * 70), int(p * 22))
        self.minLE.setGeometry(int(p * 5), int(p * 350),
                               int(p * 70), int(p * 25))
        self.maxLabel.setGeometry(
            int(p * 80), int(p * 330), int(p * 70), int(p * 22))
        self.maxLE.setGeometry(int(p * 75), int(p * 350),
                               int(p * 70), int(p * 25))
        self.phaseLabel.setGeometry(
            int(p * 5), int(p * 380), int(p * 141), int(p * 22))
        self.phaseLE.setGeometry(
            int(p * 5), int(p * 400), int(p * 141), int(p * 25))

        if (self.width() <= 106):
            self.mainLabel.setFont(QFont("Microsoft Sans Serif", 12))
            self.channelSelectLabel.setFont(QFont("Nirmala UI", 8))
            self.channelSelectCB.setFont(QFont("Nirmala UI", 8))
            self.freqLE.setFont(QFont("Nirmala UI", 8))
            self.periodLE.setFont(QFont("Nirmala UI", 8))
            self.meanLE.setFont(QFont("Nirmala UI", 8))
            self.vppLE.setFont(QFont("Nirmala UI", 8))
            self.vrmsLE.setFont(QFont("Nirmala UI", 8))
            self.maxLE.setFont(QFont("Nirmala UI", 7))
            self.minLE.setFont(QFont("Nirmala UI", 7))
            self.phaseLE.setFont(QFont("Nirmala UI", 8))

            self.frequencyLabel.setFont(QFont("Nirmala UI", 8))
            self.periodLabel.setFont(QFont("Nirmala UI", 8))
            self.meanLabel.setFont(QFont("Nirmala UI", 8))
            self.vppLabel.setFont(QFont("Nirmala UI", 8))
            self.vrmsLabel.setFont(QFont("Nirmala UI", 8))
            self.maxLabel.setFont(QFont("Nirmala UI", 8))
            self.minLabel.setFont(QFont("Nirmala UI", 8))
            self.phaseLabel.setFont(QFont("Nirmala UI", 8))

            # self.channelSelectLabel.setGeometry(
            #     int(p * 5), int(p * 40), int(p * 151), int(p * 22))
            # self.channelSelectCB.setGeometry(
            #     0, int(p * 60), int(p * 151), int(p * 27))
            # self.frequencyLabel.setGeometry(
            #     int(p * 5), int(p * 90), int(p * 141), int(p * 22))
            # self.freqLE.setGeometry(
            #     int(p * 5), int(p * 112), int(p * 141), int(p * 27))
            # self.periodLabel.setGeometry(
            #     int(p * 5), int(p * 140), int(p * 141), int(p * 22))
            # self.periodLE.setGeometry(
            #     int(p * 5), int(p * 162), int(p * 141), int(p * 25))
            # self.meanLabel.setGeometry(
            #     int(p * 5), int(p * 190), int(p * 141), int(p * 22))
            # self.meanLE.setGeometry(
            #     int(p * 5), int(p * 212), int(p * 141), int(p * 25))
            # self.vppLabel.setGeometry(
            #     int(p * 5), int(p * 240), int(p * 141), int(p * 22))
            # self.vppLE.setGeometry(
            #     int(p * 5), int(p * 262), int(p * 141), int(p * 25))
            # self.vrmsLabel.setGeometry(
            #     int(p * 5), int(p * 290), int(p * 141), int(p * 22))
            # self.vrmsLE.setGeometry(
            #     int(p * 5), int(p * 312), int(p * 141), int(p * 25))
            # self.maxLabel.setGeometry(
            #     int(p * 5), int(p * 340), int(p * 70), int(p * 22))
            # self.maxLE.setGeometry(
            #     int(p * 5), int(p * 362), int(p * 70), int(p * 25))
            # self.minLabel.setGeometry(
            #     int(p * 80), int(p * 340), int(p * 70), int(p * 22))
            # self.minLE.setGeometry(
            #     int(p * 75), int(p * 362), int(p * 70), int(p * 25))
            # self.phaseLabel.setGeometry(
            #     int(p * 5), int(p * 390), int(p * 141), int(p * 22))
            # self.phaseLE.setGeometry(
            #     int(p * 5), int(p * 412), int(p * 141), int(p * 25))


class Cursor(QDialog):
    def __init__(self):
        super(Cursor, self).__init__()
        self.setGeometry(890, 260, 151, 371)
        self.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.mainLabel = QLabel("Cursor", self)
        self.mainLabel.setGeometry(0, 0, 151, 52)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 16))

        self.cursorSelectLabel = QLabel("You can assign the cursor \nknob to a line or"
                                        " edit each \none manually. \nKnob is assigned to: ", self)
        self.cursorSelectLabel.setGeometry(0, 35, 151, 70)
        self.cursorSelectLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorSelectLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorSelectCB = QComboBox(self)
        self.cursorSelectCB.setGeometry(0, 120, 151, 22)
        self.cursorSelectCB.setStyleSheet("""background-color: rgb(36, 36, 36); 
                                                                            color: rgb(240, 240, 240)""")

        self.cursorSelectCBItems = ["X1", "X2", "Y1", "Y2"]

        self.cursorSelectCB.addItems(self.cursorSelectCBItems)

        self.cursorX1Label = QLabel("X1 (ms): ", self)
        self.cursorX1Label.setGeometry(5, 140, 151, 20)
        self.cursorX1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorX1Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX1LE = QLineEdit(self)
        self.cursorX1LE.setGeometry(5, 160, 141, 25)
        self.cursorX1LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX1LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorX1LE.setText("")

        self.cursorX2Label = QLabel("X2 (ms): ", self)
        self.cursorX2Label.setGeometry(5, 180, 151, 20)
        self.cursorX2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorX2Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX2LE = QLineEdit(self)
        self.cursorX2LE.setGeometry(5, 200, 141, 20)
        self.cursorX2LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX2LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorX2LE.setText("")

        self.cursorY1Label = QLabel("Y1 (V): ", self)
        self.cursorY1Label.setGeometry(5, 220, 151, 20)
        self.cursorY1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorY1Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY1LE = QLineEdit(self)
        self.cursorY1LE.setGeometry(5, 240, 141, 20)
        self.cursorY1LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY1LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorY1LE.setText("")

        self.cursorY2Label = QLabel("Y2 (V): ", self)
        self.cursorY2Label.setGeometry(5, 260, 151, 20)
        self.cursorY2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorY2Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY2LE = QLineEdit(self)
        self.cursorY2LE.setGeometry(5, 280, 141, 20)
        self.cursorY2LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY2LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorY2LE.setText("")

        self.cursorDeltaXLabel = QLabel("X2 - X1 (ms): ", self)
        self.cursorDeltaXLabel.setGeometry(5, 300, 151, 20)
        self.cursorDeltaXLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorDeltaXLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaX_LE = QLineEdit(self)
        self.cursorDeltaX_LE.setGeometry(5, 320, 141, 20)
        self.cursorDeltaX_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaX_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorDeltaX_LE.setText("")
        self.cursorDeltaX_LE.setReadOnly(True)

        self.cursorDeltaYLabel = QLabel("Y2 - Y1 (V): ", self)
        self.cursorDeltaYLabel.setGeometry(5, 340, 151, 20)
        self.cursorDeltaYLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorDeltaYLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaY_LE = QLineEdit(self)
        self.cursorDeltaY_LE.setGeometry(5, 360, 141, 20)
        self.cursorDeltaY_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaY_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorDeltaY_LE.setText("")
        self.cursorDeltaY_LE.setReadOnly(True)

    def resizeEvent(self, event):
        p = self.width()/151
        self.mainLabel.setGeometry(0, 0, int(p * 151), int(p * 52))
        self.cursorSelectLabel.setGeometry(
            0, int(p * 35), int(p * 151), int(p * 75))
        self.cursorSelectCB.setGeometry(
            0, int(p * 120), int(p * 151), int(p * 22))
        self.cursorX1Label.setGeometry(
            int(p * 5), int(p * 140), int(p * 151), int(p * 20))
        self.cursorX1LE.setGeometry(
            int(p * 5), int(p * 160), int(p * 141), int(p * 25))
        self.cursorX2Label.setGeometry(
            int(p * 5), int(p * 185), int(p * 151), int(p * 20))
        self.cursorX2LE.setGeometry(
            int(p * 5), int(p * 205), int(p * 141), int(p * 25))
        self.cursorY1Label.setGeometry(
            int(p * 5), int(p * 230), int(p * 151), int(p * 20))
        self.cursorY1LE.setGeometry(
            int(p * 5), int(p * 250), int(p * 141), int(p * 25))
        self.cursorY2Label.setGeometry(
            int(p * 5), int(p * 275), int(p * 151), int(p * 20))
        self.cursorY2LE.setGeometry(
            int(p * 5), int(p * 295), int(p * 141), int(p * 25))
        self.cursorDeltaXLabel.setGeometry(
            int(p * 5), int(p * 320), int(p * 151), int(p * 20))
        self.cursorDeltaX_LE.setGeometry(
            int(p * 5), int(p * 340), int(p * 141), int(p * 25))
        self.cursorDeltaYLabel.setGeometry(
            int(p * 5), int(p * 365), int(p * 151), int(p * 20))
        self.cursorDeltaY_LE.setGeometry(
            int(p * 5), int(p * 385), int(p * 141), int(p * 25))


        if self.width() <= 106:
            self.cursorSelectLabel.setFont(QFont("Lucida Sans Unicode", 6))
            self.cursorSelectLabel.setText("You can assign the cursor \nknob to a line or"
                                        " edit each \none manually. \nKnob is assigned to: ")
            
            
            self.cursorSelectCB.setFont(QFont("Nirmala UI", 8))
            self.cursorX1Label.setFont(QFont("Nirmala UI", 8))
            self.cursorX1LE.setFont(QFont("Nirmala UI", 8))
            self.cursorX2Label.setFont(QFont("Nirmala UI", 8))
            self.cursorX2LE.setFont(QFont("Nirmala UI", 8))
            self.cursorY1Label.setFont(QFont("Nirmala UI", 8))
            self.cursorY1LE.setFont(QFont("Nirmala UI", 8))
            self.cursorY2Label.setFont(QFont("Nirmala UI", 8))
            self.cursorY2LE.setFont(QFont("Nirmala UI", 8))
            self.cursorDeltaXLabel.setFont(QFont("Nirmala UI", 8))
            self.cursorDeltaX_LE.setFont(QFont("Nirmala UI", 8))
            self.cursorDeltaYLabel.setFont(QFont("Nirmala UI", 8))
            self.cursorDeltaY_LE.setFont(QFont("Nirmala UI", 8))

class FFT_screen2(QDialog):
    def __init__(self):
        super(FFT_screen2, self).__init__()
        
        self.setGeometry(890, 260, 175, 450)
        self.language = "English"
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(40, 40, 40);
            }
            
                           
            QScrollArea {
                background: rgb(40,40,40);
            }

            QScrollArea > QWidget > QWidget {
                background: rgb(40,40,40);
            }

            QScrollBar:vertical {
                background: rgb(60,60,60);
                width: 12px;
            }

            QScrollBar::handle:vertical {
                background: rgb(220,220,220);
                min-height: 25px;
                border-radius: 6px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: rgb(60,60,60);
            }
                           
            """)
        self.mainLabel = QLabel("FFT", self)
        self.mainLabel.setGeometry(0, 0, 151, 52)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 20))



        self.secondaryLabel = QLabel(
            "Screen 1: adjust\nthe visible limits\n", self)
        self.secondaryLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.secondaryLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.secondaryLabel.setFont(QFont("Lucida Sans Unicode", 7))
        self.secondaryLabel.setGeometry(15, 40, 110, 40)
        self.secondaryLabel.setWordWrap(True)


        self.page1Button = QPushButton("1", self)
        self.page1Button.setGeometry(115, 10, 30, 30)
        self.page1Button.setFlat(True)  # sem bordas
        self.page1Button.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.page1Button.setFont(QFont("Microsoft Sans Serif", 14))

        self.page2Button = QPushButton("2", self)
        self.page2Button.setGeometry(115, 40, 30, 30)
        self.page2Button.setFlat(True)  # sem bordas
        self.page2Button.setStyleSheet(""" color: rgb(100, 100, 100) """)
        self.page2Button.setFont(QFont("Microsoft Sans Serif", 14))

        self.stack = QStackedWidget(self)
        self.page1 = FFT_page1()
        self.page2 = FFT_page2()

        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)

        self.stack.setGeometry(0, 80, 141, 360)
        self.stack.setCurrentIndex(0)
        self.page1Button.clicked.connect(self.goToPage1)
        self.page2Button.clicked.connect(self.goToPage2)

    def goToPage1(self):
        self.stack.setCurrentIndex(0)
        self.page1Button.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.page2Button.setStyleSheet(""" color: rgb(100, 100, 100) """)
        if self.language == "English": self.secondaryLabel.setText("Screen 1: adjust\nthe visible limits\n")
        else: self.secondaryLabel.setText("Pág. 1: Ajuste dos limites visíveis")
        

    def goToPage2(self):
        self.stack.setCurrentIndex(1)
        self.page1Button.setStyleSheet(""" color: rgb(100, 100, 100) """)
        self.page2Button.setStyleSheet(""" color: rgb(240, 240, 240) """)
        if self.language == "English": self.secondaryLabel.setText("Screen 2:\nBiggest frequencies")
        else: self.secondaryLabel.setText("Pág. 2: Maiores frequências")

    def resizeEvent(self, event):
        if self.width() >= 175:
            self.stack.setGeometry(0, 80, 180, 500)
            self.page1Button.setGeometry(145, 10, 30, 30)
            self.page2Button.setGeometry(145, 40, 30, 30)
        
        elif self.width() >= 140:
            self.stack.setGeometry(0, 80, 140, 400)
            self.page1Button.setGeometry(110, 10, 30, 30)
            self.page2Button.setGeometry(110, 40, 30, 30)

        elif self.width() >= 123:
            self.mainLabel.setGeometry(-10, 0, 151, 52)
            self.secondaryLabel.setGeometry(0, 40, 110, 40)
            self.stack.setGeometry(0, 80, 120, 340)
            self.page1Button.setGeometry(95, 10, 30, 30)
            self.page2Button.setGeometry(95, 40, 30, 30)


class FFT_page1(QDialog):
    def __init__(self):
        super(FFT_page1, self).__init__()
        
        self.setGeometry(890, 260, 175, 310)
        
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(40, 40, 40);
            }
            
                           
            QScrollArea {
                background: rgb(40,40,40);
            }

            QScrollArea > QWidget > QWidget {
                background: rgb(40,40,40);
            }

            QScrollBar:vertical {
                background: rgb(60,60,60);
                width: 12px;
            }

            QScrollBar::handle:vertical {
                background: rgb(220,220,220);
                min-height: 25px;
                border-radius: 6px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: rgb(60,60,60);
            }
                           
            """)
        self.x_botLim_Label = QLabel("Bot. limit (Freq.) \n(Hz): ", self)
        self.x_botLim_Label.setGeometry(0, 175, 151, 20)
        self.x_botLim_Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.x_botLim_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.x_botLim_LE = QLineEdit(self)
        self.x_botLim_LE.setGeometry(5, 95, 141, 20)
        self.x_botLim_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.x_botLim_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.x_botLim_LE.setText("10")
        

        self.x_topLim_Label = QLabel("Top limit (Freq.) \n(Hz): ", self)
        self.x_topLim_Label.setGeometry(5, 160, 151, 20)
        self.x_topLim_Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.x_topLim_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.x_topLim_LE = QLineEdit(self)
        self.x_topLim_LE.setGeometry(5, 180, 141, 20)
        self.x_topLim_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.x_topLim_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.x_topLim_LE.setText("10000")

        self.y_botLim_Label = QLabel("Bot. limit (Ampl.) \n(dB): ", self)
        self.y_botLim_Label.setGeometry(5, 245, 151, 20)
        self.y_botLim_Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.y_botLim_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.y_botLim_LE = QLineEdit(self)
        self.y_botLim_LE.setGeometry(5, 265, 141, 20)
        self.y_botLim_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.y_botLim_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.y_botLim_LE.setText("-65")

        self.y_topLim_Label = QLabel("Top limit (Ampl.) \n(dB): ", self)
        self.y_topLim_Label.setGeometry(5, 330, 151, 20)
        self.y_topLim_Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.y_topLim_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.y_topLim_LE = QLineEdit(self)
        self.y_topLim_LE.setGeometry(5, 350, 141, 20)
        self.y_topLim_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.y_topLim_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.y_topLim_LE.setText("15")

        #Há um problema de interação entre o Pixmap da classe criada Button e o QVBoxLayout...
        self.btRestoreDefault = Button(self, 5, 380, 151, 20, "Restore\nDefault",
                                    "", "",  False)
    
        self.x_botLim_LE.setFixedWidth(95)
        self.x_topLim_LE.setFixedWidth(95)
        self.y_botLim_LE.setFixedWidth(95)
        self.y_topLim_LE.setFixedWidth(95)
        self.x_botLim_Label.setFixedWidth(95)
        self.x_topLim_Label.setFixedWidth(95)
        self.y_botLim_Label.setFixedWidth(95)
        self.y_topLim_Label.setFixedWidth(95)
        self.btRestoreDefault.setFixedWidth(95)
        self.btRestoreDefault.setFixedHeight(40)

        self.scroll = QScrollArea(self)
        self.scroll.setWidgetResizable(True)

        content = QWidget()
        layout = QVBoxLayout(content)

        layout.addWidget(self.x_botLim_Label)
        layout.addWidget(self.x_botLim_LE)
        layout.addWidget(self.x_topLim_Label)
        layout.addWidget(self.x_topLim_LE)
        layout.addWidget(self.y_botLim_Label)
        layout.addWidget(self.y_botLim_LE)
        layout.addWidget(self.y_topLim_Label)
        layout.addWidget(self.y_topLim_LE)
        layout.addWidget(self.btRestoreDefault)
        
        self.btRestoreDefault.setStyleSheet("""
            QPushButton {
                background-color: rgb(196, 196, 196);
                border: 1px solid #9a9a9a;
                padding: 4px 8px;
                border-radius: 4px;
                font-family: "Nirmala UI";
                font-size: 8pt;
            }
            QPushButton:pressed {
                background-color: rgb(170, 170, 170);
            }
            """)
        
        self.scroll.setWidget(content)
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.scroll)
        self.setLayout(mainLayout)
        
        

    def resizeEvent(self, event):
        #p = self.width()/151
        #self.setGeometry(int(p * 1130), int(p * 230), int(p * 175), int(p * 450))
        if self.width() >= 175:
            self.x_botLim_LE.setFixedWidth(135)
            self.x_topLim_LE.setFixedWidth(135)
            self.y_botLim_LE.setFixedWidth(135)
            self.y_topLim_LE.setFixedWidth(135)
            self.x_botLim_Label.setFixedWidth(135)
            self.x_topLim_Label.setFixedWidth(135)
            self.y_botLim_Label.setFixedWidth(135)
            self.y_topLim_Label.setFixedWidth(135)
            self.btRestoreDefault.setFixedWidth(135)
            self.btRestoreDefault.setFixedHeight(40)

        elif self.width() >= 140:
            self.x_botLim_LE.setFixedWidth(95)
            self.x_topLim_LE.setFixedWidth(95)
            self.y_botLim_LE.setFixedWidth(95)
            self.y_topLim_LE.setFixedWidth(95)
            self.x_botLim_Label.setFixedWidth(95)
            self.x_topLim_Label.setFixedWidth(95)
            self.y_botLim_Label.setFixedWidth(95)
            self.y_topLim_Label.setFixedWidth(95)
            self.btRestoreDefault.setFixedWidth(95)
            self.btRestoreDefault.setFixedHeight(40)

        elif self.width() >= 120:
            self.x_botLim_LE.setFixedWidth(70)
            self.x_topLim_LE.setFixedWidth(70)
            self.y_botLim_LE.setFixedWidth(70)
            self.y_topLim_LE.setFixedWidth(70)
            self.x_botLim_Label.setFixedWidth(70)
            self.x_topLim_Label.setFixedWidth(70)
            self.y_botLim_Label.setFixedWidth(70)
            self.y_topLim_Label.setFixedWidth(70)
            self.btRestoreDefault.setFixedWidth(70)
            self.btRestoreDefault.setFixedHeight(40)
            self.x_botLim_Label.setFont(QFont("Nirmala UI", 8))
            self.x_topLim_Label.setFont(QFont("Nirmala UI", 8))
            self.y_botLim_Label.setFont(QFont("Nirmala UI", 7))
            self.y_topLim_Label.setFont(QFont("Nirmala UI", 7))
            self.x_botLim_Label.setText("Bot. limit\n(Freq.)(Hz): ")
            self.x_topLim_Label.setText("Top. limit\n(Freq.)(Hz): ")
            self.y_botLim_Label.setText("Bot. limit\n(Ampl.)(dB): ")
            self.y_topLim_Label.setText("Top. limit\n(Ampl.)(dB): ")
            self.x_botLim_LE.setFont(QFont("Nirmala UI", 8))
            self.x_topLim_LE.setFont(QFont("Nirmala UI", 8))
            self.y_botLim_LE.setFont(QFont("Nirmala UI", 8))
            self.y_topLim_LE.setFont(QFont("Nirmala UI", 8))

        elif self.width() <= 106:
            self.x_botLim_LE.setFixedWidth(55)
            self.x_topLim_LE.setFixedWidth(55)
            self.y_botLim_LE.setFixedWidth(55)
            self.y_topLim_LE.setFixedWidth(55)
            self.x_botLim_Label.setFixedWidth(55)
            self.x_topLim_Label.setFixedWidth(55)
            self.y_botLim_Label.setFixedWidth(55)
            self.y_topLim_Label.setFixedWidth(55)
            self.btRestoreDefault.setFixedWidth(55)
            self.btRestoreDefault.setFixedHeight(40)

            self.x_botLim_Label.setFont(QFont("Nirmala UI", 8))
            self.x_topLim_Label.setFont(QFont("Nirmala UI", 8))
            self.y_botLim_Label.setFont(QFont("Nirmala UI", 7))
            self.y_topLim_Label.setFont(QFont("Nirmala UI", 7))
            self.x_botLim_Label.setText("Bot. limit\n(Freq.)(Hz): ")
            self.x_topLim_Label.setText("Top. limit\n(Freq.)(Hz): ")
            self.y_botLim_Label.setText("Bot. limit\n(Ampl.)(dB): ")
            self.y_topLim_Label.setText("Top. limit\n(Ampl.)(dB): ")
            self.x_botLim_LE.setFont(QFont("Nirmala UI", 8))
            self.x_topLim_LE.setFont(QFont("Nirmala UI", 8))
            self.y_botLim_LE.setFont(QFont("Nirmala UI", 8))
            self.y_topLim_LE.setFont(QFont("Nirmala UI", 8))

class NoWheelComboBox(QComboBox):
    def wheelEvent(self, event):
        event.ignore()

class FFT_page2(QDialog):
    def __init__(self):
        super(FFT_page2, self).__init__()
        
        self.setGeometry(890, 260, 175, 310)
        
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(40, 40, 40);
            }
            
                           
            QScrollArea {
                background: rgb(40,40,40);
            }

            QScrollArea > QWidget > QWidget {
                background: rgb(40,40,40);
            }

            QScrollBar:vertical {
                background: rgb(60,60,60);
                width: 12px;
            }

            QScrollBar::handle:vertical {
                background: rgb(220,220,220);
                min-height: 25px;
                border-radius: 6px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: rgb(60,60,60);
            }
                           
            """)
        self.tertiaryLabel = QLabel("Freq (Hz),\nAmpl (dB):", self)
        self.tertiaryLabel.setGeometry(0, 90, 151, 60)
        self.tertiaryLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.tertiaryLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.tertiaryLabel.setFont(QFont("Lucida Sans Unicode", 7))

        self.channelLabel = QLabel("Channel:", self)
        self.channelLabel.setGeometry(0, 110, 151, 60)
        self.channelLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.channelLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.channelLabel.setFont(QFont("Microsoft Sans Serif", 6))

        self.channelCB = NoWheelComboBox(self)
        self.channelCB.setGeometry(0, 130, 151, 25)
        self.channelCB.setStyleSheet("""background-color: rgb(56, 56, 56); 
                                                                    color: rgb(240, 240, 240)""")

        self.channelCBItems = ["CH1", "CH2", "Math"]
        self.channelCB.addItems(self.channelCBItems)

        self.freq1Label = QLabel("Freq 1: ", self)
        self.freq1Label.setGeometry(0, 170, 75, 20)
        self.freq1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.freq1Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freq1Label.setFont(QFont("Microsoft Sans Serif", 8))
        self.freq1LE = QLineEdit(self)
        self.freq1LE.setGeometry(65, 170, 85, 20)
        self.freq1LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freq1LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.freq1LE.setText("")
        self.freq1LE.setReadOnly(True)

        self.ampl1Label = QLabel("Ampl 1: ", self)
        self.ampl1Label.setGeometry(0, 200, 75, 20)
        self.ampl1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.ampl1Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ampl1Label.setFont(QFont("Microsoft Sans Serif", 8))
        self.ampl1LE = QLineEdit(self)
        self.ampl1LE.setGeometry(65, 200, 85, 20)
        self.ampl1LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ampl1LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.ampl1LE.setText("")
        self.ampl1LE.setReadOnly(True)

        self.freq2Label = QLabel("Freq 2: ", self)
        self.freq2Label.setGeometry(0, 270, 75, 20)
        self.freq2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.freq2Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freq2Label.setFont(QFont("Microsoft Sans Serif", 8))
        self.freq2LE = QLineEdit(self)
        self.freq2LE.setGeometry(65, 270, 85, 20)
        self.freq2LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freq2LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.freq2LE.setText("")
        self.freq2LE.setReadOnly(True)

        self.ampl2Label = QLabel("Ampl 2: ", self)
        self.ampl2Label.setGeometry(0, 300, 75, 20)
        self.ampl2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.ampl2Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ampl2Label.setFont(QFont("Microsoft Sans Serif", 8))
        self.ampl2LE = QLineEdit(self)
        self.ampl2LE.setGeometry(65, 300, 85, 20)
        self.ampl2LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ampl2LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.ampl2LE.setText("")
        self.ampl2LE.setReadOnly(True)

        self.freq3Label = QLabel("Freq 3: ", self)
        self.freq3Label.setGeometry(0, 360, 75, 20)
        self.freq3Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.freq3Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freq3Label.setFont(QFont("Microsoft Sans Serif", 8))
        self.freq3LE = QLineEdit(self)
        self.freq3LE.setGeometry(65, 360, 85, 20)
        self.freq3LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freq3LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.freq3LE.setText("")
        self.freq3LE.setReadOnly(True)

        self.ampl3Label = QLabel("Ampl 3: ", self)
        self.ampl3Label.setGeometry(0, 390, 75, 20)
        self.ampl3Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.ampl3Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ampl3Label.setFont(QFont("Microsoft Sans Serif", 8))
        self.ampl3LE = QLineEdit(self)
        self.ampl3LE.setGeometry(65, 390, 85, 20)
        self.ampl3LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ampl3LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.ampl3LE.setText("")
        self.ampl3LE.setReadOnly(True)

        self.scroll = QScrollArea(self)
        self.scroll.setWidgetResizable(True)

        content = QWidget()
        layout = QVBoxLayout(content)

        layout.addWidget(self.tertiaryLabel)
        layout.addWidget(self.channelLabel)
        layout.addWidget(self.channelCB)
        layout.addWidget(self.freq1Label)
        layout.addWidget(self.freq1LE)
        layout.addWidget(self.ampl1Label)
        layout.addWidget(self.ampl1LE)
        layout.addWidget(self.freq2Label)
        layout.addWidget(self.freq2LE)
        layout.addWidget(self.ampl2Label)
        layout.addWidget(self.ampl2LE)
        layout.addWidget(self.freq3Label)
        layout.addWidget(self.freq3LE)
        layout.addWidget(self.ampl3Label)
        layout.addWidget(self.ampl3LE)

        self.scroll.setWidget(content)
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.scroll)
        

    def resizeEvent(self, event):
        if self.width() >= 175:
            self.tertiaryLabel.setFixedWidth(135)
            self.channelLabel.setFixedWidth(135)
            self.channelCB.setFixedWidth(135)
            self.freq1Label.setFixedWidth(135)
            self.freq1LE.setFixedWidth(135)
            self.ampl1Label.setFixedWidth(135)
            self.ampl1LE.setFixedWidth(135)
            self.freq2Label.setFixedWidth(135)
            self.freq2LE.setFixedWidth(135)
            self.ampl2Label.setFixedWidth(135)
            self.ampl2LE.setFixedWidth(135)
            self.freq3Label.setFixedWidth(135)
            self.freq3LE.setFixedWidth(135)
            self.ampl3Label.setFixedWidth(135)
            self.ampl3LE.setFixedWidth(135)

        elif self.width() >= 140:
            self.tertiaryLabel.setFixedWidth(95)
            self.channelLabel.setFixedWidth(95)
            self.channelCB.setFixedWidth(95)
            self.freq1Label.setFixedWidth(95)
            self.freq1LE.setFixedWidth(95)
            self.ampl1Label.setFixedWidth(95)
            self.ampl1LE.setFixedWidth(95)
            self.freq2Label.setFixedWidth(95)
            self.freq2LE.setFixedWidth(95)
            self.ampl2Label.setFixedWidth(95)
            self.ampl2LE.setFixedWidth(95)
            self.freq3Label.setFixedWidth(95)
            self.freq3LE.setFixedWidth(95)
            self.ampl3Label.setFixedWidth(95)
            self.ampl3LE.setFixedWidth(95)

        elif self.width() >= 120:
            self.tertiaryLabel.setFixedWidth(70)
            self.channelLabel.setFixedWidth(70)
            self.channelCB.setFixedWidth(70)
            self.freq1Label.setFixedWidth(70)
            self.freq1LE.setFixedWidth(70)
            self.ampl1Label.setFixedWidth(70)
            self.ampl1LE.setFixedWidth(70)
            self.freq2Label.setFixedWidth(70)
            self.freq2LE.setFixedWidth(70)
            self.ampl2Label.setFixedWidth(70)
            self.ampl2LE.setFixedWidth(70)
            self.freq3Label.setFixedWidth(70)
            self.freq3LE.setFixedWidth(70)
            self.ampl3Label.setFixedWidth(70)
            self.ampl3LE.setFixedWidth(70)

        else:
            self.freq1Label.setFont(QFont("Nirmala UI", 8))
            self.freq1LE.setFont(QFont("Nirmala UI", 8))
            self.ampl1Label.setFont(QFont("Nirmala UI", 8))
            self.ampl1LE.setFont(QFont("Nirmala UI", 8))
            self.freq2Label.setFont(QFont("Nirmala UI", 8))
            self.freq2LE.setFont(QFont("Nirmala UI", 8))
            self.ampl2Label.setFont(QFont("Nirmala UI", 8))
            self.ampl2LE.setFont(QFont("Nirmala UI", 8))
            self.freq3Label.setFont(QFont("Nirmala UI", 8))
            self.freq3LE.setFont(QFont("Nirmala UI", 8))
            self.ampl3Label.setFont(QFont("Nirmala UI", 8))
            self.ampl3LE.setFont(QFont("Nirmala UI", 8))

            self.tertiaryLabel.setFixedWidth(55)
            self.channelLabel.setFixedWidth(55)
            self.channelCB.setFixedWidth(55)
            self.freq1Label.setFixedWidth(55)
            self.freq1LE.setFixedWidth(55)
            self.ampl1Label.setFixedWidth(55)
            self.ampl1LE.setFixedWidth(55)
            self.freq2Label.setFixedWidth(55)
            self.freq2LE.setFixedWidth(55)
            self.ampl2Label.setFixedWidth(55)
            self.ampl2LE.setFixedWidth(55)
            self.freq3Label.setFixedWidth(55)
            self.freq3LE.setFixedWidth(55)
            self.ampl3Label.setFixedWidth(55)
            self.ampl3LE.setFixedWidth(55)

        
       
class CursorFFT(QDialog):
    def __init__(self):
        super(CursorFFT, self).__init__()
        self.setGeometry(890, 260, 151, 371)
        self.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.mainLabel = QLabel("Cursor", self)
        self.mainLabel.setGeometry(0, 0, 151, 52)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 16))

        self.cursorSelectLabel = QLabel("You can assign the cursor \nknob to a line or"
                                        " edit each \none manually. \nKnob is assigned to: ", self)
        self.cursorSelectLabel.setGeometry(0, 35, 151, 70)
        self.cursorSelectLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorSelectLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorSelectCB = QComboBox(self)
        self.cursorSelectCB.setGeometry(0, 120, 151, 22)
        self.cursorSelectCB.setStyleSheet("""background-color: rgb(36, 36, 36); 
                                                                            color: rgb(240, 240, 240)""")

        self.cursorSelectCBItems = ["X1", "X2", "Y1", "Y2"]

        self.cursorSelectCB.addItems(self.cursorSelectCBItems)

        self.cursorX1Label = QLabel("X1 (Hz): ", self)
        self.cursorX1Label.setGeometry(5, 140, 151, 20)
        self.cursorX1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorX1Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX1LE = QLineEdit(self)
        self.cursorX1LE.setGeometry(5, 160, 141, 20)
        self.cursorX1LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX1LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorX1LE.setText("")

        self.cursorX2Label = QLabel("X2 (Hz): ", self)
        self.cursorX2Label.setGeometry(5, 180, 151, 20)
        self.cursorX2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorX2Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX2LE = QLineEdit(self)
        self.cursorX2LE.setGeometry(5, 200, 141, 20)
        self.cursorX2LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX2LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorX2LE.setText("")

        self.cursorY1Label = QLabel("Y1 (dB): ", self)
        self.cursorY1Label.setGeometry(5, 220, 151, 20)
        self.cursorY1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorY1Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY1LE = QLineEdit(self)
        self.cursorY1LE.setGeometry(5, 240, 141, 20)
        self.cursorY1LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY1LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorY1LE.setText("")

        self.cursorY2Label = QLabel("Y2 (dB): ", self)
        self.cursorY2Label.setGeometry(5, 260, 151, 20)
        self.cursorY2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorY2Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY2LE = QLineEdit(self)
        self.cursorY2LE.setGeometry(5, 280, 141, 20)
        self.cursorY2LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY2LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorY2LE.setText("")

        self.cursorDeltaXLabel = QLabel("X2 - X1 (Hz): ", self)
        self.cursorDeltaXLabel.setGeometry(5, 300, 151, 20)
        self.cursorDeltaXLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorDeltaXLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaX_LE = QLineEdit(self)
        self.cursorDeltaX_LE.setGeometry(5, 320, 141, 20)
        self.cursorDeltaX_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaX_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorDeltaX_LE.setText("")
        self.cursorDeltaX_LE.setReadOnly(True)

        self.cursorDeltaYLabel = QLabel("Y2 - Y1 (dB): ", self)
        self.cursorDeltaYLabel.setGeometry(5, 340, 151, 20)
        self.cursorDeltaYLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorDeltaYLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaY_LE = QLineEdit(self)
        self.cursorDeltaY_LE.setGeometry(5, 360, 141, 20)
        self.cursorDeltaY_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaY_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorDeltaY_LE.setText("")
        self.cursorDeltaY_LE.setReadOnly(True)

    def resizeEvent(self, event):
        p = self.width()/151
        self.mainLabel.setGeometry(0, 0, int(p * 151), int(p * 52))
        self.cursorSelectLabel.setGeometry(
            0, int(p * 35), int(p * 151), int(p * 70))
        self.cursorSelectCB.setGeometry(
            0, int(p * 120), int(p * 151), int(p * 22))
        self.cursorX1Label.setGeometry(
            int(p * 5), int(p * 140), int(p * 151), int(p * 20))
        self.cursorX1LE.setGeometry(
            int(p * 5), int(p * 160), int(p * 141), int(p * 25))
        self.cursorX2Label.setGeometry(
            int(p * 5), int(p * 185), int(p * 151), int(p * 20))
        self.cursorX2LE.setGeometry(
            int(p * 5), int(p * 205), int(p * 141), int(p * 25))
        self.cursorY1Label.setGeometry(
            int(p * 5), int(p * 230), int(p * 151), int(p * 20))
        self.cursorY1LE.setGeometry(
            int(p * 5), int(p * 250), int(p * 141), int(p * 25))
        self.cursorY2Label.setGeometry(
            int(p * 5), int(p * 275), int(p * 151), int(p * 20))
        self.cursorY2LE.setGeometry(
            int(p * 5), int(p * 295), int(p * 141), int(p * 25))
        self.cursorDeltaXLabel.setGeometry(
            int(p * 5), int(p * 320), int(p * 151), int(p * 20))
        self.cursorDeltaX_LE.setGeometry(
            int(p * 5), int(p * 340), int(p * 141), int(p * 25))
        self.cursorDeltaYLabel.setGeometry(
            int(p * 5), int(p * 365), int(p * 151), int(p * 20))
        self.cursorDeltaY_LE.setGeometry(
            int(p * 5), int(p * 385), int(p * 141), int(p * 25))

        if self.width() <= 127:
            self.cursorSelectLabel.setFont(QFont("Lucida Sans Unicode", 7))
            self.cursorSelectLabel.setGeometry(
                0, int(p * 35), int(p * 151), int(p * 160))

        if self.width() <= 106:
            self.cursorSelectLabel.setFont(QFont("Lucida Sans Unicode", 6))
            self.cursorSelectLabel.setText("You can assign the cursor \nknob to a line or"
                                        " edit each \none manually. \nKnob is assigned to: ")

            self.cursorSelectCB.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorX1Label.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorX1LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorX2Label.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorX2LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorY1Label.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorY1LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorY2Label.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorY2LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorDeltaXLabel.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorDeltaX_LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorDeltaYLabel.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorDeltaY_LE.setFont(QFont("Lucida Sans Unicode", 8))

class PhasDiag_and_Lissajous_scr2(QDialog):
    def __init__(self):
        super(PhasDiag_and_Lissajous_scr2, self).__init__()
        self.setGeometry(890, 260, 175, 450)
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(40, 40, 40);
            }
            
                           
            QScrollArea {
                background: rgb(40,40,40);
            }

            QScrollArea > QWidget > QWidget {
                background: rgb(40,40,40);
            }

            QScrollBar:vertical {
                background: rgb(60,60,60);
                width: 12px;
            }

            QScrollBar::handle:vertical {
                background: rgb(220,220,220);
                min-height: 25px;
                border-radius: 6px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: rgb(60,60,60);
            }
                           
            """)
        self.mainLabel = QLabel("Phasor Diagram", self)
        self.mainLabel.setGeometry(0, 20, 175, 72)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 14))

        # self.isolateScreen = QCheckBox("Isolate", self)
        # self.isolateScreen.setStyleSheet(""" color: rgb(240, 240, 240) """)
        # self.isolateScreen.setFont(QFont("Microsoft Sans Serif", 9))
        # self.isolateScreen.setGeometry(0, 70, 130, 30)
        # self.isolateScreen.setChecked(False)

        self.page1Button = QPushButton("1", self)
        self.page1Button.setGeometry(45, 50, 30, 30)
        self.page1Button.setFlat(True)  # sem bordas
        self.page1Button.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.page1Button.setFont(QFont("Microsoft Sans Serif", 16))

        self.page2Button = QPushButton("2", self)
        self.page2Button.setGeometry(75, 50, 30, 30)
        self.page2Button.setFlat(True)  # sem bordas
        self.page2Button.setStyleSheet(""" color: rgb(100, 100, 100) """)
        self.page2Button.setFont(QFont("Microsoft Sans Serif", 16))

        self.stack = QStackedWidget(self)
        self.page1 = PhasDiag_and_Lissajous_page1()
        self.page2 = PhasDiag_and_Lissajous_page2()

        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)

        self.stack.setGeometry(0, 80, 145, 370)
        self.stack.setCurrentIndex(0)
        self.page1Button.clicked.connect(self.goToPage1)
        self.page2Button.clicked.connect(self.goToPage2)

    def goToPage1(self):
        self.stack.setCurrentIndex(0)
        self.page1Button.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.page2Button.setStyleSheet(""" color: rgb(100, 100, 100) """)
        self.mainLabel.setText("Phasor Diagram")
        

    def goToPage2(self):
        self.stack.setCurrentIndex(1)
        self.page1Button.setStyleSheet(""" color: rgb(100, 100, 100) """)
        self.page2Button.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setText("Lissajous")

    def resizeEvent(self, event):
        
        p = self.width()/175
        
        self.mainLabel.setGeometry(0, int(p * 20), int(p * 175), int(p * 72))

        if self.width() >= 175:
            self.stack.setGeometry(0, int(80), int(175), int(500))
        elif self.width() >= 140:
            self.stack.setGeometry(0, int(80), int(140), int(400))
        elif self.width() >= 123:
            self.stack.setGeometry(0, int(80), int(120), int(340))
            self.mainLabel.setFont(QFont("Microsoft Sans Serif", 12))

class PhasDiag_and_Lissajous_page1(QDialog): #Phasor Diagram
    def __init__(self):
        super(PhasDiag_and_Lissajous_page1, self).__init__()
        self.setGeometry(890, 260, 175, 370)
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(40, 40, 40);
            }
            
                           
            QScrollArea {
                background: rgb(40,40,40);
            }

            QScrollArea > QWidget > QWidget {
                background: rgb(40,40,40);
            }

            QScrollBar:vertical {
                background: rgb(60,60,60);
                width: 12px;
            }

            QScrollBar::handle:vertical {
                background: rgb(220,220,220);
                min-height: 25px;
                border-radius: 6px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: rgb(60,60,60);
            }
                           
            """)

        self.isolateScreen = QCheckBox("Isolate", self)
        self.isolateScreen.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.isolateScreen.setFont(QFont("Microsoft Sans Serif", 9))
        self.isolateScreen.setGeometry(0, 70, 130, 30)
        self.isolateScreen.setChecked(False)

        self.CH1Label = QLabel("CH1", self)
        self.CH1Label.setGeometry(0, 100, 151, 22)
        self.CH1Label.setStyleSheet(""" color: blue """)
        self.CH1Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.CH1Label.setFont(QFont("Microsoft Sans Serif", 11))

        self.CH1MagnitLabel = QLabel("Magnitude\n(V):", self)
        self.CH1MagnitLabel.setGeometry(0, 120, 151, 22)
        self.CH1MagnitLabel.setStyleSheet(""" color: white """)
        self.CH1MagnitLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.CH1MagnitLabel.setFont(QFont("Microsoft Sans Serif", 8))

        self.CH1MagnitLE = QLineEdit(self)
        self.CH1MagnitLE.setGeometry(5, 140, 141, 20)
        self.CH1MagnitLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.CH1MagnitLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.CH1MagnitLE.setReadOnly(True)

        self.CH1PhaseLabel = QLabel("Phase\n(deg.):", self)
        self.CH1PhaseLabel.setGeometry(0, 160, 151, 22)
        self.CH1PhaseLabel.setStyleSheet(""" color: white """)
        self.CH1PhaseLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.CH1PhaseLabel.setFont(QFont("Microsoft Sans Serif", 8))

        self.CH1PhaseLE = QLineEdit(self)
        self.CH1PhaseLE.setGeometry(5, 180, 141, 20)
        self.CH1PhaseLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.CH1PhaseLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.CH1PhaseLE.setReadOnly(True)

        self.CH2Label = QLabel("CH2", self)
        self.CH2Label.setGeometry(0, 210, 151, 22)
        self.CH2Label.setStyleSheet(""" color: red """)
        self.CH2Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.CH2Label.setFont(QFont("Microsoft Sans Serif", 11))

        self.CH2MagnitLabel = QLabel("Magnitude\n(V):", self)
        self.CH2MagnitLabel.setGeometry(0, 230, 151, 22)
        self.CH2MagnitLabel.setStyleSheet(""" color: white """)
        self.CH2MagnitLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.CH2MagnitLabel.setFont(QFont("Microsoft Sans Serif", 8))

        self.CH2MagnitLE = QLineEdit(self)
        self.CH2MagnitLE.setGeometry(5, 250, 141, 20)
        self.CH2MagnitLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.CH2MagnitLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.CH2MagnitLE.setReadOnly(True)

        self.CH2PhaseLabel = QLabel("Phase\n(deg.):", self)
        self.CH2PhaseLabel.setGeometry(0, 270, 151, 22)
        self.CH2PhaseLabel.setStyleSheet(""" color: white """)
        self.CH2PhaseLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.CH2PhaseLabel.setFont(QFont("Microsoft Sans Serif", 8))

        self.CH2PhaseLE = QLineEdit(self)
        self.CH2PhaseLE.setGeometry(5, 290, 141, 20)
        self.CH2PhaseLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.CH2PhaseLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.CH2PhaseLE.setReadOnly(True)

        self.MathLabel = QLabel("Math", self)
        self.MathLabel.setGeometry(0, 320, 151, 22)
        self.MathLabel.setStyleSheet(""" color: cyan """)
        self.MathLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MathLabel.setFont(QFont("Microsoft Sans Serif", 11))

        self.MathMagnitLabel = QLabel("Magnitude\n(V):", self)
        self.MathMagnitLabel.setGeometry(0, 340, 151, 22)
        self.MathMagnitLabel.setStyleSheet(""" color: white """)
        self.MathMagnitLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MathMagnitLabel.setFont(QFont("Microsoft Sans Serif", 8))

        self.MathMagnitLE = QLineEdit(self)
        self.MathMagnitLE.setGeometry(5, 360, 141, 20)
        self.MathMagnitLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MathMagnitLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.MathMagnitLE.setReadOnly(True)

        self.MathPhaseLabel = QLabel("Phase\n(deg.):", self)
        self.MathPhaseLabel.setGeometry(0, 380, 151, 22)
        self.MathPhaseLabel.setStyleSheet(""" color: white """)
        self.MathPhaseLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MathPhaseLabel.setFont(QFont("Microsoft Sans Serif", 8))

        self.MathPhaseLE = QLineEdit(self)
        self.MathPhaseLE.setGeometry(5, 400, 141, 20)
        self.MathPhaseLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MathPhaseLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.MathPhaseLE.setReadOnly(True)

        self.magnitudeVoltageLabel = QLabel("Magnitude\nVoltage:", self)
        self.magnitudeVoltageLabel.setGeometry(0, 450, 151, 22)
        self.magnitudeVoltageLabel.setStyleSheet(""" color: white """)
        self.magnitudeVoltageLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.magnitudeVoltageLabel.setFont(QFont("Microsoft Sans Serif", 8))

        self.magnitudeVoltageCB = QComboBox(self)
        self.magnitudeVoltageCB.setGeometry(0, 480, 151, 22)
        self.magnitudeVoltageCB.setStyleSheet("""background-color: rgb(56, 56, 56); 
                                                                    color: rgb(240, 240, 240)""")

        self.magnitudeVoltageCBItems = ["RMS", "Peak", "Pk-to-Pk"]
        self.magnitudeVoltageCB.addItems(self.magnitudeVoltageCBItems)

        self.scroll = QScrollArea(self)
        self.scroll.setWidgetResizable(True)

        content = QWidget()
        layout = QVBoxLayout(content)


        layout.addWidget(self.isolateScreen)
        layout.addWidget(self.CH1Label)
        layout.addWidget(self.CH1MagnitLabel)
        layout.addWidget(self.CH1MagnitLE)
        layout.addWidget(self.CH1PhaseLabel)
        layout.addWidget(self.CH1PhaseLE)
        layout.addWidget(self.CH2Label)
        layout.addWidget(self.CH2MagnitLabel)
        layout.addWidget(self.CH2MagnitLE)
        layout.addWidget(self.CH2PhaseLabel)
        layout.addWidget(self.CH2PhaseLE)
        layout.addWidget(self.MathLabel)
        layout.addWidget(self.MathMagnitLabel)
        layout.addWidget(self.MathMagnitLE)
        layout.addWidget(self.MathPhaseLabel)
        layout.addWidget(self.MathPhaseLE)
        layout.addWidget(self.magnitudeVoltageLabel)
        layout.addWidget(self.magnitudeVoltageCB)
        
        
        self.scroll.setWidget(content)
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.scroll)



    def resizeEvent(self, event):
        if self.width() >= 175:
            self.isolateScreen.setFixedWidth(110)
            self.CH1Label.setFixedWidth(110)
            self.CH1MagnitLabel.setFixedWidth(110)
            self.CH1MagnitLE.setFixedWidth(110)
            self.CH1PhaseLabel.setFixedWidth(110)
            self.CH1PhaseLE.setFixedWidth(110)
            self.CH2Label.setFixedWidth(110)
            self.CH2MagnitLabel.setFixedWidth(110)
            self.CH2MagnitLE.setFixedWidth(110)
            self.CH2PhaseLabel.setFixedWidth(110)
            self.CH2PhaseLE.setFixedWidth(110)
            self.MathLabel.setFixedWidth(110)
            self.MathMagnitLabel.setFixedWidth(110)
            self.MathMagnitLE.setFixedWidth(110)
            self.MathPhaseLabel.setFixedWidth(110)
            self.MathPhaseLE.setFixedWidth(110)
            self.magnitudeVoltageLabel.setFixedWidth(110)
            self.magnitudeVoltageCB.setFixedWidth(110)

        elif self.width() >= 140:
            self.isolateScreen.setFixedWidth(90)
            self.CH1Label.setFixedWidth(90)
            self.CH1MagnitLabel.setFixedWidth(90)
            self.CH1MagnitLE.setFixedWidth(90)
            self.CH1PhaseLabel.setFixedWidth(90)
            self.CH1PhaseLE.setFixedWidth(90)
            self.CH2Label.setFixedWidth(90)
            self.CH2MagnitLabel.setFixedWidth(90)
            self.CH2MagnitLE.setFixedWidth(90)
            self.CH2PhaseLabel.setFixedWidth(90)
            self.CH2PhaseLE.setFixedWidth(90)
            self.MathLabel.setFixedWidth(90)
            self.MathMagnitLabel.setFixedWidth(90)
            self.MathMagnitLE.setFixedWidth(90)
            self.MathPhaseLabel.setFixedWidth(90)
            self.MathPhaseLE.setFixedWidth(90)
            self.magnitudeVoltageLabel.setFixedWidth(90)
            self.magnitudeVoltageCB.setFixedWidth(90)

        elif self.width() >= 120:
            self.isolateScreen.setFixedWidth(70)
            self.CH1Label.setFixedWidth(70)
            self.CH1MagnitLabel.setFixedWidth(70)
            self.CH1MagnitLE.setFixedWidth(70)
            self.CH1PhaseLabel.setFixedWidth(70)
            self.CH1PhaseLE.setFixedWidth(70)
            self.CH2Label.setFixedWidth(70)
            self.CH2MagnitLabel.setFixedWidth(70)
            self.CH2MagnitLE.setFixedWidth(70)
            self.CH2PhaseLabel.setFixedWidth(70)
            self.CH2PhaseLE.setFixedWidth(70)
            self.MathLabel.setFixedWidth(70)
            self.MathMagnitLabel.setFixedWidth(70)
            self.MathMagnitLE.setFixedWidth(70)
            self.MathPhaseLabel.setFixedWidth(70)
            self.MathPhaseLE.setFixedWidth(70)
            self.magnitudeVoltageLabel.setFixedWidth(70)
            self.magnitudeVoltageCB.setFixedWidth(70)


        elif self.width() <= 106: #Resolução menor ou igual a 1366x768
            self.isolateScreen.setFixedWidth(55)
            self.CH1Label.setFixedWidth(55)
            self.CH1MagnitLabel.setFixedWidth(55)
            self.CH1MagnitLE.setFixedWidth(55)
            self.CH1PhaseLabel.setFixedWidth(55)
            self.CH1PhaseLE.setFixedWidth(55)
            self.CH2Label.setFixedWidth(55)
            self.CH2MagnitLabel.setFixedWidth(55)
            self.CH2MagnitLE.setFixedWidth(55)
            self.CH2PhaseLabel.setFixedWidth(55)
            self.CH2PhaseLE.setFixedWidth(55)
            self.MathLabel.setFixedWidth(55)
            self.MathMagnitLabel.setFixedWidth(55)
            self.MathMagnitLE.setFixedWidth(55)
            self.MathPhaseLabel.setFixedWidth(55)
            self.MathPhaseLE.setFixedWidth(55)
            self.magnitudeVoltageLabel.setFixedWidth(55)
            self.magnitudeVoltageCB.setFixedWidth(55)
            self.isolateScreen.setFont(QFont("Calibri", 8))
            self.CH1Label.setFont(QFont("Lucida Sans Unicode", 10))
            self.CH1MagnitLabel.setFont(QFont("Lucida Sans Unicode", 7))
            self.CH1MagnitLE.setFont(QFont("Lucida Sans Unicode", 7))
            self.CH1PhaseLabel.setFont(QFont("Lucida Sans Unicode", 7))
            self.CH1PhaseLE.setFont(QFont("Lucida Sans Unicode", 7))
            self.CH2Label.setFont(QFont("Lucida Sans Unicode", 10))
            self.CH2MagnitLabel.setFont(QFont("Lucida Sans Unicode", 7))
            self.CH2MagnitLE.setFont(QFont("Lucida Sans Unicode", 7))
            self.CH2PhaseLabel.setFont(QFont("Lucida Sans Unicode", 7))
            self.CH2PhaseLE.setFont(QFont("Lucida Sans Unicode", 7))
            self.MathLabel.setFont(QFont("Lucida Sans Unicode", 10))
            self.MathMagnitLabel.setFont(QFont("Lucida Sans Unicode", 7))
            self.MathMagnitLE.setFont(QFont("Lucida Sans Unicode", 7))
            self.MathPhaseLabel.setFont(QFont("Lucida Sans Unicode", 7))
            self.MathPhaseLE.setFont(QFont("Lucida Sans Unicode", 7))
            self.magnitudeVoltageLabel.setFont(QFont("Lucida Sans Unicode", 7))

class PhasDiag_and_Lissajous_page2(QDialog): #Lissajous
    def __init__(self):
        super(PhasDiag_and_Lissajous_page2, self).__init__()
        self.setGeometry(890, 260, 151, 370)
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(40, 40, 40);
            }
            
                           
            QScrollArea {
                background: rgb(40,40,40);
            }

            QScrollArea > QWidget > QWidget {
                background: rgb(40,40,40);
            }

            QScrollBar:vertical {
                background: rgb(60,60,60);
                width: 12px;
            }

            QScrollBar::handle:vertical {
                background: rgb(220,220,220);
                min-height: 25px;
                border-radius: 6px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: rgb(60,60,60);
            }
                           
            """)

        self.isolateScreen = QCheckBox("Isolate", self)
        self.isolateScreen.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.isolateScreen.setFont(QFont("Microsoft Sans Serif", 9))
        self.isolateScreen.setGeometry(0, 70, 130, 30)
        self.isolateScreen.setChecked(False)

        self.choosexAxisChannelLabel = QLabel("x-Axis\nChannel:", self)
        self.choosexAxisChannelLabel.setGeometry(0, 130, 151, 20)
        self.choosexAxisChannelLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.choosexAxisChannelLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.choosexAxisChannelLabel.setFont(QFont("Microsoft Sans Serif", 9))

        self.channelxAxisSelectCB = QComboBox(self)
        self.channelxAxisSelectCB.setGeometry(0, 160, 151, 22)
        self.channelxAxisSelectCB.setStyleSheet("""background-color: rgb(36, 36, 36); 
                                                                            color: rgb(240, 240, 240)""")
        self.channelxAxisSelectCBItems = ["CH1", "CH2", "Math"]
        self.channelxAxisSelectCB.addItems(self.channelxAxisSelectCBItems)

        self.chooseyAxisChannelLabel = QLabel("y-Axis\nChannel:", self)
        self.chooseyAxisChannelLabel.setGeometry(0, 220, 151, 20)
        self.chooseyAxisChannelLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.chooseyAxisChannelLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.chooseyAxisChannelLabel.setFont(QFont("Microsoft Sans Serif", 9))

        self.channelyAxisSelectCB = QComboBox(self)
        self.channelyAxisSelectCB.setGeometry(0, 250, 151, 22)
        self.channelyAxisSelectCB.setStyleSheet("""background-color: rgb(36, 36, 36); 
                                                                            color: rgb(240, 240, 240)""")
        self.channelyAxisSelectCBItems = ["CH1", "CH2", "Math"]
        self.channelyAxisSelectCB.addItems(self.channelyAxisSelectCBItems)
        self.channelyAxisSelectCB.setCurrentIndex(1)

        self.scroll = QScrollArea(self)
        self.scroll.setWidgetResizable(True)

        content = QWidget()
        layout = QVBoxLayout(content)

        layout.addWidget(self.isolateScreen)
        layout.addWidget(self.choosexAxisChannelLabel)
        layout.addWidget(self.channelxAxisSelectCB)
        layout.addWidget(self.chooseyAxisChannelLabel)
        layout.addWidget(self.channelyAxisSelectCB)

        

        self.scroll.setWidget(content)
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.scroll)

    def resizeEvent(self, event):
        
        if self.width() >= 175:
            self.isolateScreen.setFixedWidth(130)
            self.choosexAxisChannelLabel.setFixedWidth(130)
            self.channelxAxisSelectCB.setFixedWidth(130)
            self.chooseyAxisChannelLabel.setFixedWidth(130)
            self.channelyAxisSelectCB.setFixedWidth(130)

        # if self.width() >= 151:
        #     self.isolateScreen.setFixedWidth(95)
        #     self.choosexAxisChannelLabel.setFixedWidth(95)
        #     self.channelxAxisSelectCB.setFixedWidth(95)
        #     self.chooseyAxisChannelLabel.setFixedWidth(95)
        #     self.channelyAxisSelectCB.setFixedWidth(95)

        # else:
        #     self.isolateScreen.setFixedWidth(55)
        #     self.choosexAxisChannelLabel.setFixedWidth(55)
        #     self.channelxAxisSelectCB.setFixedWidth(55)
        #     self.chooseyAxisChannelLabel.setFixedWidth(55)
        #     self.channelyAxisSelectCB.setFixedWidth(55)
        #     self.isolateScreen.setFont(QFont("Calibri", 8))
        #     self.choosexAxisChannelLabel.setFont(QFont("Nirmala UI", 7))
        #     self.chooseyAxisChannelLabel.setFont(QFont("Nirmala UI", 7))

        self.choosexAxisChannelLabel.setFixedHeight(40)
        self.chooseyAxisChannelLabel.setFixedHeight(40)
        

class Main_for_Screen2_1(QDialog):
    def __init__(self):
        super(Main_for_Screen2_1, self).__init__()
        self.setGeometry(890, 260, 151, 371)
        self.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.mainLabel = QLabel("Main", self)
        self.mainLabel.setGeometry(0, 0, 151, 52)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 16))

        self.page1Button = QPushButton("1", self)
        self.page1Button.setGeometry(125, 10, 30, 30)
        self.page1Button.setFlat(True)  # sem bordas
        self.page1Button.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.page1Button.setFont(QFont("Microsoft Sans Serif", 14))

        self.page2Button = QPushButton("2", self)
        self.page2Button.setGeometry(125, 40, 30, 30)
        self.page2Button.setFlat(True)  # sem bordas
        self.page2Button.setStyleSheet(""" color: rgb(100, 100, 100) """)
        self.page2Button.setFont(QFont("Microsoft Sans Serif", 14))

        self.refChannelLabel = QLabel("Reference Channel: ", self)
        self.refChannelLabel.setGeometry(0, 70, 151, 72)
        self.refChannelLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.refChannelLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.refChannelLabel.setFont(QFont("Microsoft Sans Serif", 10))

        self.refChannelCB = QComboBox(self)
        self.refChannelCB.setGeometry(0, 90, 151, 22)
        self.refChannelCB.setStyleSheet("""background-color: rgb(36, 36, 36); 
                                     color: rgb(240, 240, 240)""")

        self.refChannelCBItems = ["CH1", "CH2", "Math"]

        self.refChannelCB.addItems(self.refChannelCBItems)

        self.attnFactorLabel_CH1 = QLabel("Attn. Factor (CH1):", self)
        self.attnFactorLabel_CH1.setGeometry(0, 150, 151, 72)
        self.attnFactorLabel_CH1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.attnFactorLabel_CH1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.attnFactorLabel_CH1.setFont(QFont("Microsoft Sans Serif", 10))

        self.attnFactorCB_CH1 = QComboBox(self)
        self.attnFactorCB_CH1.setGeometry(0, 170, 151, 22)
        self.attnFactorCB_CH1.setStyleSheet("""background-color: rgb(36, 36, 36); 
                                     color: rgb(240, 240, 240)""")

        self.attnFactorCBItems_CH1 = ["x1", "x5"]
        self.attnFactorCB_CH1.addItems(self.attnFactorCBItems_CH1)

        self.attnFactorLabel_CH2 = QLabel("Attn. Factor (CH2):", self)
        self.attnFactorLabel_CH2.setGeometry(0, 190, 151, 72)
        self.attnFactorLabel_CH2.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.attnFactorLabel_CH2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.attnFactorLabel_CH2.setFont(QFont("Microsoft Sans Serif", 10))

        self.attnFactorCB_CH2 = QComboBox(self)
        self.attnFactorCB_CH2.setGeometry(0, 210, 151, 22)
        self.attnFactorCB_CH2.setStyleSheet("""background-color: rgb(36, 36, 36); 
                                     color: rgb(240, 240, 240)""")

        self.attnFactorCBItems_CH2 = ["x1", "x5"]
        self.attnFactorCB_CH2.addItems(self.attnFactorCBItems_CH2)
        

        self.customTimeScaleLabel = QLabel("Enter Custom\nTime Scale (ms):", self)
        self.customTimeScaleLabel.setGeometry(0, 250, 151, 72)
        self.customTimeScaleLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.customTimeScaleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.customTimeScaleLabel.setFont(QFont("Microsoft Sans Serif", 10))

        self.customTimeScaleLE = QLineEdit(self)
        self.customTimeScaleLE.setGeometry(5, 290, 140, 20)
        self.customTimeScaleLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.customTimeScaleLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.customTimeScaleLE.setText("")

    def resizeEvent(self, event):
        p = self.width() / 151
        
        self.mainLabel.setGeometry(
            int(p * 0), int(p * 0),
            int(p * 151), int(p * 52)
        )

        self.page1Button.setGeometry(
            int(p * 125), int(p * 10),
            int(p * 30), int(p * 30)
        )

        self.page2Button.setGeometry(
            int(p * 125), int(p * 40),
            int(p * 30), int(p * 30)
        )

        self.refChannelLabel.setGeometry(
            int(p * 0), int(p * 70),
            int(p * 151), int(p * 72)
        )

        self.refChannelCB.setGeometry(
            int(p * 0), int(p * 90),
            int(p * 151), int(p * 28)
        )

        self.attnFactorLabel_CH1.setGeometry(
            int(p * 0), int(p * 150),
            int(p * 151), int(p * 72)
        )

        self.attnFactorCB_CH1.setGeometry(
            int(p * 0), int(p * 175),
            int(p * 151), int(p * 28)
        )

        self.attnFactorLabel_CH2.setGeometry(
            int(p * 0), int(p * 200),
            int(p * 151), int(p * 72)
        )

        self.attnFactorCB_CH2.setGeometry(
            int(p * 0), int(p * 225),
            int(p * 151), int(p * 28)
        )

        self.customTimeScaleLabel.setGeometry(
            int(p * 0), int(p * 250),
            int(p * 151), int(p * 72)
        )

        self.customTimeScaleLE.setGeometry(
            int(p * 5), int(p * 310),
            int(p * 140), int(p * 28)
        )

        if self.width() <= 106: #1366x768
            self.mainLabel.setFont(QFont("Microsoft Sans Serif", 14))
            self.refChannelLabel.setFont(QFont("Nirmala UI", 9))
            self.attnFactorLabel_CH1.setFont(QFont("Nirmala UI", 10))
            self.attnFactorLabel_CH2.setFont(QFont("Nirmala UI", 10))
            self.customTimeScaleLabel.setFont(QFont("Nirmala UI", 10))
    




class Main_for_Screen2_2(QDialog):
    def __init__(self):
        super(Main_for_Screen2_2, self).__init__()
        self.setGeometry(890, 260, 151, 371)
        self.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.mainLabel = QLabel("Main", self)
        self.mainLabel.setGeometry(0, 0, 151, 52)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 16))

        self.page1Button = QPushButton("1", self)
        self.page1Button.setGeometry(125, 10, 30, 30)
        self.page1Button.setFlat(True)  # sem bordas
        self.page1Button.setStyleSheet(""" color: rgb(100, 100, 100) """)
        self.page1Button.setFont(QFont("Microsoft Sans Serif", 14))

        self.page2Button = QPushButton("2", self)
        self.page2Button.setGeometry(125, 40, 30, 30)
        self.page2Button.setFlat(True)  # sem bordas
        self.page2Button.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.page2Button.setFont(QFont("Microsoft Sans Serif", 14))

        self.currentInVerticalScaleLabel = QLabel("Replace V/div with A/div \non vertical scale:", self) 
        self.currentInVerticalScaleLabel.setGeometry(0, 90, 151, 60)
        self.currentInVerticalScaleLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.currentInVerticalScaleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.currentInVerticalScaleLabel.setFont(QFont("Microsoft Sans Serif", 8))

        self.resistorLabel = QLabel("Shunt \nResistor (Ω):", self) 
        self.resistorLabel.setGeometry(60, 140, 90, 72)
        self.resistorLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.resistorLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.resistorLabel.setFont(QFont("Arial", 8))

        self.currentInVerticalScaleCheckBox_CH1 = QCheckBox("CH1", self)
        self.currentInVerticalScaleCheckBox_CH1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.currentInVerticalScaleCheckBox_CH1.setFont(QFont("Microsoft Sans Serif", 9))
        self.currentInVerticalScaleCheckBox_CH1.setGeometry(0, 180, 60, 20)
        self.currentInVerticalScaleCheckBox_CH1.setChecked(False)

        self.resistorValueLE_CH1 = QLineEdit(self)
        self.resistorValueLE_CH1.setGeometry(65, 180, 70, 20)
        self.resistorValueLE_CH1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # self.resistorValueLE_CH1.setStyleSheet(
        #     """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.resistorValueLE_CH1.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(150, 150, 150)""")
        self.resistorValueLE_CH1.setText("")
        self.resistorValueLE_CH1.setReadOnly(True) #Se torna false com o checkbox ativado

        self.currentInVerticalScaleCheckBox_CH2 = QCheckBox("CH2", self)
        self.currentInVerticalScaleCheckBox_CH2.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.currentInVerticalScaleCheckBox_CH2.setFont(QFont("Microsoft Sans Serif", 9))
        self.currentInVerticalScaleCheckBox_CH2.setGeometry(0, 220, 60, 20)
        self.currentInVerticalScaleCheckBox_CH2.setChecked(False)

        self.resistorValueLE_CH2 = QLineEdit(self)
        self.resistorValueLE_CH2.setGeometry(65, 220, 70, 20)
        self.resistorValueLE_CH2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.resistorValueLE_CH2.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(150, 150, 150)""")
        self.resistorValueLE_CH2.setText("")
        self.resistorValueLE_CH2.setReadOnly(True) #Se torna false com o checkbox ativado

        self.currentInVerticalScaleCheckBox_Math = QCheckBox("Math", self)
        self.currentInVerticalScaleCheckBox_Math.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.currentInVerticalScaleCheckBox_Math.setFont(QFont("Microsoft Sans Serif", 9))
        self.currentInVerticalScaleCheckBox_Math.setGeometry(0, 260, 60, 20)
        self.currentInVerticalScaleCheckBox_Math.setChecked(False)

        self.resistorValueLE_Math = QLineEdit(self)
        self.resistorValueLE_Math.setGeometry(65, 260, 70, 20)
        self.resistorValueLE_Math.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.resistorValueLE_Math.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(150, 150, 150)""")
        self.resistorValueLE_Math.setText("")
        self.resistorValueLE_Math.setReadOnly(True) #Se torna false com o checkbox ativado

    def resizeEvent(self, event):
        p = self.width() / 151

        self.mainLabel.setGeometry(
            int(p * 0), int(p * 0),
            int(p * 151), int(p * 52)
        )

        self.page1Button.setGeometry(
            int(p * 125), int(p * 10),
            int(p * 30), int(p * 30)
        )

        self.page2Button.setGeometry(
            int(p * 125), int(p * 40),
            int(p * 30), int(p * 30)
        )

        self.currentInVerticalScaleLabel.setGeometry(
            int(p * 0), int(p * 90),
            int(p * 151), int(p * 60)
        )

        self.resistorLabel.setGeometry(
            int(p * 60), int(p * 140),
            int(p * 90), int(p * 72)
        )

        self.currentInVerticalScaleCheckBox_CH1.setGeometry(
            int(p * 0), int(p * 180),
            int(p * 60), int(p * 20)
        )

        self.resistorValueLE_CH1.setGeometry(
            int(p * 65), int(p * 180),
            int(p * 70), int(p * 30)
        )

        self.currentInVerticalScaleCheckBox_CH2.setGeometry(
            int(p * 0), int(p * 220),
            int(p * 60), int(p * 20)
        )

        self.resistorValueLE_CH2.setGeometry(
            int(p * 65), int(p * 220),
            int(p * 70), int(p * 30)
        )

        self.currentInVerticalScaleCheckBox_Math.setGeometry(
            int(p * 0), int(p * 260),
            int(p * 60), int(p * 20)
        )

        self.resistorValueLE_Math.setGeometry(
            int(p * 65), int(p * 260),
            int(p * 70), int(p * 30)
        )

        if self.width() <= 106:
            self.resistorValueLE_CH1.setGeometry(
            int(p * 75), int(p * 180),
            int(p * 70), int(p * 25)
            )

            self.resistorValueLE_CH2.setGeometry(
            int(p * 75), int(p * 220),
            int(p * 70), int(p * 25)
            )

            self.resistorValueLE_Math.setGeometry(
            int(p * 75), int(p * 260),
            int(p * 70), int(p * 25)
            )

            self.currentInVerticalScaleCheckBox_CH1.setGeometry(
            int(p * 0), int(p * 180),
            int(p * 70), int(p * 20)
            )

            self.currentInVerticalScaleCheckBox_CH2.setGeometry(
            int(p * 0), int(p * 220),
            int(p * 70), int(p * 20)
            )
            
            self.currentInVerticalScaleCheckBox_Math.setGeometry(
            int(p * 0), int(p * 260),
            int(p * 70), int(p * 20)
            )

            
            self.currentInVerticalScaleLabel.setFont(QFont("Nirmala UI", 7))

class FreqResp_forScr2(QDialog):
    def __init__(self):
        super(FreqResp_forScr2, self).__init__()
        self.setGeometry(890, 260, 151, 451)
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(40, 40, 40);
            }
            
                           
            QScrollArea {
                background: rgb(40,40,40);
            }

            QScrollArea > QWidget > QWidget {
                background: rgb(40,40,40);
            }

            QScrollBar:vertical {
                background: rgb(60,60,60);
                width: 12px;
            }

            QScrollBar::handle:vertical {
                background: rgb(220,220,220);
                min-height: 25px;
                border-radius: 6px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: rgb(60,60,60);
            }
                           
        """)
        self.mainLabel = QLabel("Frequency\nResponse", self)
        self.mainLabel.setGeometry(0, 0, 151, 65)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 14))

        self.page1Button = QPushButton("1", self)
        self.page1Button.setGeometry(0, 60, 50, 50)
        self.page1Button.setFlat(True)  # sem bordas
        self.page1Button.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.page1Button.setFont(QFont("Microsoft Sans Serif", 14))

        self.page2Button = QPushButton("2", self)
        self.page2Button.setGeometry(50, 60, 50, 50)
        self.page2Button.setFlat(True)  # sem bordas
        self.page2Button.setStyleSheet(""" color: rgb(100, 100, 100) """)
        self.page2Button.setFont(QFont("Microsoft Sans Serif", 14))

        self.page3Button = QPushButton("3", self)
        self.page3Button.setGeometry(100, 60, 50, 50)
        self.page3Button.setFlat(True)  # sem bordas
        self.page3Button.setStyleSheet(""" color: rgb(100, 100, 100) """)
        self.page3Button.setFont(QFont("Microsoft Sans Serif", 14))

        self.stack = QStackedWidget(self)
        self.freqResp_page1 = FreqResp_forScr2_Page1()
        self.freqResp_page2 = FreqResp_forScr2_Page2()
        self.freqResp_page3 = FreqResp_forScr2_Page3()
        self.stack.addWidget(self.freqResp_page1)
        self.stack.addWidget(self.freqResp_page2)
        self.stack.addWidget(self.freqResp_page3)
        self.stack.setGeometry(0, 110, 151, 341)
        self.stack.setCurrentIndex(0)
        self.page1Button.clicked.connect(self.goToPage1)
        self.page2Button.clicked.connect(self.goToPage2)
        self.page3Button.clicked.connect(self.goToPage3)

    def goToPage1(self):
        self.stack.setCurrentIndex(0)
        self.page1Button.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.page2Button.setStyleSheet(""" color: rgb(100, 100, 100) """)
        self.page3Button.setStyleSheet(""" color: rgb(100, 100, 100) """)

    def goToPage2(self):
        self.stack.setCurrentIndex(1)
        self.page1Button.setStyleSheet(""" color: rgb(100, 100, 100) """)
        self.page2Button.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.page3Button.setStyleSheet(""" color: rgb(100, 100, 100) """)

    def goToPage3(self):
        self.stack.setCurrentIndex(2)
        self.page1Button.setStyleSheet(""" color: rgb(100, 100, 100) """)
        self.page2Button.setStyleSheet(""" color: rgb(100, 100, 100) """)
        self.page3Button.setStyleSheet(""" color: rgb(240, 240, 240) """)

    def resizeEvent(self, event):
        p = self.width() / 151

        self.mainLabel.setGeometry(
            int(p*0), int(p*0), int(p*151), int(p*65)
        )

        self.page1Button.setGeometry(
            int(p*0), int(p*60), int(p*50), int(p*50)
        )
        self.page2Button.setGeometry(
            int(p*50), int(p*60), int(p*50), int(p*50)
        )
        self.page3Button.setGeometry(
            int(p*100), int(p*60), int(p*50), int(p*50)
        )

        self.stack.setGeometry(
            int(p*0), int(p*110), int(p*151), int(p*341)
        )

        # =======================
        # page1
        # =======================

        self.freqResp_page1.numberPointsLabel.setGeometry(
            int(p*5), int(p*0), int(p*151), int(p*20)
        )
        self.freqResp_page1.numberPointsLE.setGeometry(
            int(p*5), int(p*20), int(p*141), int(p*28)
        )

        self.freqResp_page1.initialFreqLabel.setGeometry(
            int(p*5), int(p*80), int(p*151), int(p*20)
        )
        self.freqResp_page1.initialFreqLE.setGeometry(
            int(p*5), int(p*100), int(p*141), int(p*28)
        )

        self.freqResp_page1.finalFreqLabel.setGeometry(
            int(p*5), int(p*160), int(p*151), int(p*20)
        )
        self.freqResp_page1.finalFreqLE.setGeometry(
            int(p*5), int(p*180), int(p*141), int(p*28)
        )

        self.freqResp_page1.btSweep_Play.setGeometry(
            int(p*5), int(p*240), int(p*75), int(p*55)
        )
        self.freqResp_page1.btSweep_Play_ImageLabel.setGeometry(
            int(p*5), int(p*240), int(p*75), int(p*55)
        )
        self.freqResp_page1.btSweep_Play_ImageLabel.setPixmap(
            self.freqResp_page1.btSweep_Play_Available_Pixmap.scaled(
            self.freqResp_page1.btSweep_Play_ImageLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))

        self.freqResp_page1.btSweep_Stop.setGeometry(
            int(p*90), int(p*240), int(p*75), int(p*55)
        )
        self.freqResp_page1.btSweep_Stop_ImageLabel.setGeometry(
            int(p*90), int(p*240), int(p*75), int(p*55)
        )
        self.freqResp_page1.btSweep_Stop_ImageLabel.setPixmap(
            self.freqResp_page1.btSweep_Stop_Pixmap_Unavailable.scaled(
            self.freqResp_page1.btSweep_Stop_ImageLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))

        self.freqResp_page1.btSweepLabel.setGeometry(
            int(p*5), int(p*220), int(p*151), int(p*22)
        )

        # =======================
        # page2
        # =======================

        self.freqResp_page2.functionTypeLabel.setGeometry(
            int(p*5), int(p*0), int(p*151), int(p*22)
        )
        self.freqResp_page2.functionTypeCB.setGeometry(
            int(p*0), int(p*20), int(p*151), int(p*28)
        )

        self.freqResp_page2.y_AxisLabel.setGeometry(
            int(p*5), int(p*80), int(p*151), int(p*22)
        )
        self.freqResp_page2.y_AxisCB.setGeometry(
            int(p*0), int(p*100), int(p*151), int(p*28)
        )

        self.freqResp_page2.plotColorLabel.setGeometry(
            int(p*5), int(p*160), int(p*151), int(p*22)
        )
        self.freqResp_page2.plotColorCB.setGeometry(
            int(p*0), int(p*180), int(p*151), int(p*28)
        )

        self.freqResp_page2.btclearScreen.setGeometry(
            int(p*30), int(p*220), int(p*75), int(p*45)
        )
        self.freqResp_page2.clearScreenPartialCheckBox.setGeometry(
            int(p*12), int(p*270), int(p*130), int(p*50)
        )


        #page3

        
        if self.width() >= 151:
            self.freqResp_page3.x_botLim_LE.setFixedWidth(95)
            self.freqResp_page3.x_topLim_LE.setFixedWidth(95)
            self.freqResp_page3.y_botLim_LE.setFixedWidth(95)
            self.freqResp_page3.y_topLim_LE.setFixedWidth(95)
            self.freqResp_page3.y_botLim_LE_phase.setFixedWidth(95)
            self.freqResp_page3.y_topLim_LE_phase.setFixedWidth(95)
            self.freqResp_page3.x_botLim_Label.setFixedWidth(95)
            self.freqResp_page3.x_topLim_Label.setFixedWidth(95)
            self.freqResp_page3.y_botLim_Label.setFixedWidth(95)
            self.freqResp_page3.y_topLim_Label.setFixedWidth(95)
            self.freqResp_page3.y_botLim_Label_phase.setFixedWidth(95)
            self.freqResp_page3.y_topLim_Label_phase.setFixedWidth(95)
            self.freqResp_page3.btRestoreDefault.setFixedWidth(95)
            self.freqResp_page3.btRestoreDefault.setFixedHeight(40)

        elif self.width() >= 135:
            self.freqResp_page3.x_botLim_LE.setFixedWidth(85)
            self.freqResp_page3.x_topLim_LE.setFixedWidth(85)
            self.freqResp_page3.y_botLim_LE.setFixedWidth(85)
            self.freqResp_page3.y_topLim_LE.setFixedWidth(85)
            self.freqResp_page3.y_botLim_LE_phase.setFixedWidth(85)
            self.freqResp_page3.y_topLim_LE_phase.setFixedWidth(85)
            self.freqResp_page3.x_botLim_Label.setFixedWidth(85)
            self.freqResp_page3.x_topLim_Label.setFixedWidth(85)
            self.freqResp_page3.y_botLim_Label.setFixedWidth(85)
            self.freqResp_page3.y_topLim_Label.setFixedWidth(85)
            self.freqResp_page3.y_botLim_Label_phase.setFixedWidth(85)
            self.freqResp_page3.y_topLim_Label_phase.setFixedWidth(85)
            self.freqResp_page3.btRestoreDefault.setFixedWidth(85)
            self.freqResp_page3.btRestoreDefault.setFixedHeight(40)
        
        elif self.width() >= 110:
            self.freqResp_page3.x_botLim_LE.setFixedWidth(70)
            self.freqResp_page3.x_topLim_LE.setFixedWidth(70)
            self.freqResp_page3.y_botLim_LE.setFixedWidth(70)
            self.freqResp_page3.y_topLim_LE.setFixedWidth(70)
            self.freqResp_page3.y_botLim_LE_phase.setFixedWidth(70)
            self.freqResp_page3.y_topLim_LE_phase.setFixedWidth(70)
            self.freqResp_page3.x_botLim_Label.setFixedWidth(70)
            self.freqResp_page3.x_topLim_Label.setFixedWidth(70)
            self.freqResp_page3.y_botLim_Label.setFixedWidth(70)
            self.freqResp_page3.y_topLim_Label.setFixedWidth(70)
            self.freqResp_page3.y_botLim_Label_phase.setFixedWidth(70)
            self.freqResp_page3.y_topLim_Label_phase.setFixedWidth(70)
            self.freqResp_page3.btRestoreDefault.setFixedWidth(70)
            self.freqResp_page3.btRestoreDefault.setFixedHeight(40)

            self.freqResp_page3.x_botLim_Label.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page3.x_topLim_Label.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page3.y_botLim_Label.setFont(QFont("Nirmala UI", 7))
            self.freqResp_page3.y_topLim_Label.setFont(QFont("Nirmala UI", 7))
            self.freqResp_page3.y_botLim_Label_phase.setFont(QFont("Nirmala UI", 7))
            self.freqResp_page3.y_topLim_Label_phase.setFont(QFont("Nirmala UI", 7))
            self.freqResp_page3.x_botLim_Label.setText("Bot. limit\n(Freq.)(Hz): ")
            self.freqResp_page3.x_topLim_Label.setText("Top. limit\n(Freq.)(Hz): ")
            self.freqResp_page3.y_botLim_Label.setText("Bot. limit\n(Magn.)(dB): ")
            self.freqResp_page3.y_topLim_Label.setText("Top. limit\n(Magn.)(dB): ")
            self.freqResp_page3.y_botLim_Label_phase.setText("Bot. limit\n(Phase)(deg.): ")
            self.freqResp_page3.y_topLim_Label_phase.setText("Top. limit\n(Phase)(deg.): ")
            self.freqResp_page3.x_botLim_LE.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page3.x_topLim_LE.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page3.y_botLim_LE.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page3.y_topLim_LE.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page3.y_botLim_LE_phase.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page3.y_topLim_LE_phase.setFont(QFont("Nirmala UI", 8))

        elif self.width() <= 106:
            self.freqResp_page3.x_botLim_LE.setFixedWidth(55)
            self.freqResp_page3.x_topLim_LE.setFixedWidth(55)
            self.freqResp_page3.y_botLim_LE.setFixedWidth(55)
            self.freqResp_page3.y_topLim_LE.setFixedWidth(55)
            self.freqResp_page3.y_botLim_LE_phase.setFixedWidth(55)
            self.freqResp_page3.y_topLim_LE_phase.setFixedWidth(55)
            self.freqResp_page3.y_topLim_LE.setFixedWidth(55)
            self.freqResp_page3.x_botLim_Label.setFixedWidth(55)
            self.freqResp_page3.x_topLim_Label.setFixedWidth(55)
            self.freqResp_page3.y_botLim_Label.setFixedWidth(55)
            self.freqResp_page3.y_botLim_Label_phase.setFixedWidth(55)
            self.freqResp_page3.y_topLim_Label_phase.setFixedWidth(55)
            self.freqResp_page3.y_topLim_Label.setFixedWidth(55)
            self.freqResp_page3.btRestoreDefault.setFixedWidth(55)
            self.freqResp_page3.btRestoreDefault.setFixedHeight(40)

            self.freqResp_page3.x_botLim_Label.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page3.x_topLim_Label.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page3.y_botLim_Label.setFont(QFont("Nirmala UI", 7))
            self.freqResp_page3.y_topLim_Label.setFont(QFont("Nirmala UI", 7))
            self.freqResp_page3.y_botLim_Label_phase.setFont(QFont("Nirmala UI", 7))
            self.freqResp_page3.y_topLim_Label_phase.setFont(QFont("Nirmala UI", 7))
            self.freqResp_page3.x_botLim_Label.setText("Bot. limit\n(Freq.)(Hz): ")
            self.freqResp_page3.x_topLim_Label.setText("Top. limit\n(Freq.)(Hz): ")
            self.freqResp_page3.y_botLim_Label.setText("Bot. limit\n(Magn.)(dB): ")
            self.freqResp_page3.y_topLim_Label.setText("Top. limit\n(Magn.)(dB): ")
            self.freqResp_page3.y_botLim_Label_phase.setText("Bot. limit\n(Phase)(deg.): ")
            self.freqResp_page3.y_topLim_Label_phase.setText("Top. limit\n(Phase)(deg.): ")
            self.freqResp_page3.x_botLim_LE.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page3.x_topLim_LE.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page3.y_botLim_LE.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page3.y_topLim_LE.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page3.y_botLim_LE_phase.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page3.y_topLim_LE_phase.setFont(QFont("Nirmala UI", 8))

            self.freqResp_page1.numberPointsLabel.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page1.numberPointsLE.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page1.initialFreqLabel.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page1.initialFreqLE.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page1.finalFreqLabel.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page1.finalFreqLE.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page1.btSweepLabel.setFont(QFont("Nirmala UI", 8))

            self.freqResp_page2.functionTypeLabel.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page2.functionTypeCB.setFont(QFont("Nirmala UI", 8))

            self.freqResp_page2.y_AxisLabel.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page2.y_AxisCB.setFont(QFont("Nirmala UI", 8))

            self.freqResp_page2.plotColorLabel.setFont(QFont("Nirmala UI", 8))
            self.freqResp_page2.plotColorCB.setFont(QFont("Nirmala UI", 8))

            self.freqResp_page2.btclearScreen.setStyleSheet("""
                background-color: rgb(110, 110, 110);
                color: rgb(225, 225, 225);
                border: 1px solid #9a9a9a;
                padding: 4px 8px;
                border-radius: 4px;
                font-family: "Nirmala UI";
                font-size: 7pt;

            """)
            self.freqResp_page2.clearScreenPartialCheckBox.setFont(QFont("Nirmala UI", 7))




class FreqResp_forScr2_Page1(QDialog):
    def __init__(self):
        super(FreqResp_forScr2_Page1, self).__init__()
        self.setGeometry(890, 260, 175, 341)
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(40, 40, 40);
            }
            
                           
            QScrollArea {
                background: rgb(40,40,40);
            }

            QScrollArea > QWidget > QWidget {
                background: rgb(40,40,40);
            }

            QScrollBar:vertical {
                background: rgb(60,60,60);
                width: 12px;
            }

            QScrollBar::handle:vertical {
                background: rgb(220,220,220);
                min-height: 25px;
                border-radius: 6px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: rgb(60,60,60);
            }
                           
        """)

        self.numberPointsLabel = QLabel("Number of points: ", self)
        self.numberPointsLabel.setGeometry(5, 0, 151, 20)
        self.numberPointsLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.numberPointsLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.numberPointsLE = QLineEdit(self)
        self.numberPointsLE.setGeometry(5, 20, 141, 28)
        self.numberPointsLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.numberPointsLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.numberPointsLE.setText("60")

        self.initialFreqLabel = QLabel("Initial Freq. (Hz): ", self)
        self.initialFreqLabel.setGeometry(5, 80, 151, 20)
        self.initialFreqLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.initialFreqLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.initialFreqLE = QLineEdit(self)
        self.initialFreqLE.setGeometry(5, 100, 141, 28)
        self.initialFreqLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.initialFreqLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.initialFreqLE.setText("20")

        self.finalFreqLabel = QLabel("Final Freq. (Hz): ", self)
        self.finalFreqLabel.setGeometry(5, 160, 151, 20)
        self.finalFreqLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.finalFreqLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.finalFreqLE = QLineEdit(self)
        self.finalFreqLE.setGeometry(5, 180, 141, 28)
        self.finalFreqLE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.finalFreqLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.finalFreqLE.setText("9000")

        

        #O botão do Sweep tem o mesmo design do WFM Generator, como no LabVIEW:
        self.btSweep_Play = QPushButton("", self)
        self.sweepOn = False
        self.btSweep_Play_Mode = "Paused"
        self.btSweep_Play.setGeometry(5, 240, 75, 55)
        self.btSweep_Play.setAutoDefault(False)
        self.btSweep_Play.setDefault(False)
        self.btSweep_Play_ImageLabel = QLabel("", self)
        self.btSweep_Play_ImageLabel.setGeometry(5, 240, 75, 55)
        self.btSweep_Play_ImageLabel.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.btSweep_Play_Available_Pixmap = QPixmap("images/Bt_Sweep_Play.png")
        self.btSweep_Play_Unavailable_Pixmap = QPixmap("images/Bt_Sweep_Play_Unavailable.png")
        self.btSweep_Play_Resume_Pixmap = QPixmap("images/Bt_Sweep_Play_Resume.png")
        self.btSweep_Play_Pause_Pixmap = QPixmap("images/Bt_Sweep_Pause.png")
        self.btSweep_Play_ImageLabel.setPixmap(self.btSweep_Play_Available_Pixmap.scaled
                                               (self.btSweep_Play_ImageLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
        
        self.btSweep_Play_ImageLabel.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.btSweep_Play.clicked.connect(self.bt_sweepPlayClicked)

        self.btSweep_Stop = QPushButton("", self)
        self.btSweep_Stop.setGeometry(90, 240, 75, 55)
        self.btSweep_Stop.setAutoDefault(False)
        self.btSweep_Stop.setDefault(False)
        self.btSweep_Stop_ImageLabel = QLabel("", self)
        self.btSweep_Stop_ImageLabel.setGeometry(90, 240, 75, 55)
        self.btSweep_Stop_ImageLabel.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.btSweep_Stop_Pixmap_Unavailable = QPixmap("images/Bt_Sweep_Stop_Unavailable.png")
        self.btSweep_Stop_Pixmap_Available = QPixmap("images/Bt_Sweep_Stop_Available.png")
        
        self.btSweep_Stop_ImageLabel.setPixmap(self.btSweep_Stop_Pixmap_Unavailable.scaled(self.btSweep_Stop_ImageLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
        self.btSweep_Stop_ImageLabel.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.btSweep_Stop.setEnabled(False)
        self.btSweep_Stop.clicked.connect(self.bt_sweepStopClicked)

        self.btSweepLabel = QLabel("Sweep Control:", self)
        self.btSweepLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.btSweepLabel.setGeometry(5, 220, 151, 22)
        self.btSweepLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)


    def bt_sweepPlayClicked(self):
        if not self.sweepOn: 
            self.sweepOn = True
            self.btSweep_Stop.setEnabled(True)
            self.btSweep_Stop_ImageLabel.setPixmap(self.btSweep_Stop_Pixmap_Available.scaled(self.btSweep_Stop_ImageLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))

        if self.btSweep_Play_Mode == "Paused":
            self.btSweep_Play_Mode = "Running"
            self.btSweep_Play_ImageLabel.setPixmap(self.btSweep_Play_Pause_Pixmap.scaled
                                               (self.btSweep_Play_ImageLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
            
        elif self.btSweep_Play_Mode == "Running":
            self.btSweep_Play_Mode = "Paused" 
            self.btSweep_Play_ImageLabel.setPixmap(self.btSweep_Play_Resume_Pixmap.scaled
                                               (self.btSweep_Play_ImageLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
            
    def bt_sweepStopClicked(self):
        self.btSweep_Stop_ImageLabel.setPixmap(self.btSweep_Stop_Pixmap_Unavailable.scaled(self.btSweep_Stop_ImageLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
        self.btSweep_Stop.setEnabled(False)
        self.btSweep_Play_Mode = "Paused" 
        self.btSweep_Play_ImageLabel.setPixmap(self.btSweep_Play_Available_Pixmap.scaled
                                               (self.btSweep_Play_ImageLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))
        self.sweepOn = False



class FreqResp_forScr2_Page2(QDialog):
    def __init__(self):
        super(FreqResp_forScr2_Page2, self).__init__()
        self.setGeometry(890, 260, 175, 341)
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(40, 40, 40);
            }
            
                           
            QScrollArea {
                background: rgb(40,40,40);
            }

            QScrollArea > QWidget > QWidget {
                background: rgb(40,40,40);
            }

            QScrollBar:vertical {
                background: rgb(60,60,60);
                width: 12px;
            }

            QScrollBar::handle:vertical {
                background: rgb(220,220,220);
                min-height: 25px;
                border-radius: 6px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: rgb(60,60,60);
            }
                           
        """)

        self.functionTypeLabel = QLabel("Sweep Function: ", self)
        self.functionTypeLabel.setGeometry(5, 0, 151, 22)
        self.functionTypeLabel.setStyleSheet(
            """ color: rgb(240, 240, 240) """)
        # self.functionTypeLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.functionTypeCB = QComboBox(self)
        self.functionTypeCB.setGeometry(0, 20, 151, 22)
        self.functionTypeCB.setStyleSheet("""background-color: rgb(56, 56, 56); 
                                                                    color: rgb(240, 240, 240)""")

        self.functionTypeCBItems = ["CH2/CH1", "CH1/CH2", "Math/CH1", "CH1/Math", "Math/CH2", "CH2/Math", "CH1", "CH2", "Math"]
        self.functionTypeCB.addItems(self.functionTypeCBItems)

        self.y_AxisLabel = QLabel("y-Axis: ", self)
        self.y_AxisLabel.setGeometry(5, 80, 151, 22)
        self.y_AxisLabel.setStyleSheet(
            """ color: rgb(240, 240, 240) """)
        # self.y_AxisLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.y_AxisCB = QComboBox(self)
        self.y_AxisCB.setGeometry(0, 100, 151, 22)
        self.y_AxisCB.setStyleSheet("""background-color: rgb(56, 56, 56); 
                                                                    color: rgb(240, 240, 240)""")

        self.y_AxisCBItems = ["Magnitude", "Phase"]
        self.y_AxisCB.addItems(self.y_AxisCBItems)

        self.plotColorLabel = QLabel("Plot Color:", self)
        self.plotColorLabel.setGeometry(5, 160, 151, 22)
        self.plotColorLabel.setStyleSheet(
            """ color: rgb(240, 240, 240) """)
        # self.plotColorLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.plotColorCB = QComboBox(self)
        self.plotColorCB.setGeometry(0, 180, 151, 22)
        self.plotColorCB.setStyleSheet("""background-color: rgb(56, 56, 56); 
                                                                    color: rgb(240, 240, 240)""")

        self.plotColorCBItems = ["White", "Blue", "Red", "Green", "Yellow", "Purple", "Orange", "Cyan"]
        self.plotColorCB.addItems(self.plotColorCBItems)

        self.btclearScreen = Button(self, 30, 220, 75, 40, "Clear\nScreen",
                                    "", "",  False)
        
        
        self.btclearScreen.setStyleSheet("""
                background-color: rgb(110, 110, 110);
                color: rgb(225, 225, 225);
                border: 1px solid #9a9a9a;
                padding: 4px 8px;
                border-radius: 4px;
                font-family: "Nirmala UI";
                font-size: 8pt;

            """)
        
        self.clearScreenPartialCheckBox = QCheckBox("Keep last plot\nwhen cleaning", self)
        self.clearScreenPartialCheckBox.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.clearScreenPartialCheckBox.setFont(QFont("Microsoft Sans Serif", 8))
        self.clearScreenPartialCheckBox.setGeometry(12, 270, 130, 50)
        self.clearScreenPartialCheckBox.setChecked(False)
        

class FreqResp_forScr2_Page3(QDialog):
    #Página 1 da tela secundária do FFT, versão Freq Resp...
    def __init__(self):
        super(FreqResp_forScr2_Page3, self).__init__()
        self.setGeometry(890, 260, 175, 341)
        self.setStyleSheet("""
            QDialog {
                background-color: rgb(40, 40, 40);
            }
            
                           
            QScrollArea {
                background: rgb(40,40,40);
            }

            QScrollArea > QWidget > QWidget {
                background: rgb(40,40,40);
            }

            QScrollBar:vertical {
                background: rgb(60,60,60);
                width: 12px;
            }

            QScrollBar::handle:vertical {
                background: rgb(220,220,220);
                min-height: 25px;
                border-radius: 6px;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: rgb(60,60,60);
            }
                           
        """)

        self.x_botLim_Label = QLabel("Bot. limit (Freq.) \n(Hz): ", self)
        self.x_botLim_Label.setGeometry(0, 175, 151, 20)
        self.x_botLim_Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.x_botLim_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.x_botLim_LE = QLineEdit(self)
        self.x_botLim_LE.setGeometry(5, 95, 141, 20)
        self.x_botLim_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.x_botLim_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.x_botLim_LE.setText("10")
        

        self.x_topLim_Label = QLabel("Top limit (Freq.) \n(Hz): ", self)
        self.x_topLim_Label.setGeometry(5, 160, 151, 20)
        self.x_topLim_Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.x_topLim_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.x_topLim_LE = QLineEdit(self)
        self.x_topLim_LE.setGeometry(5, 180, 141, 20)
        self.x_topLim_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.x_topLim_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.x_topLim_LE.setText("10000")

        #magnitude:
        self.y_botLim_Label = QLabel("Bot. limit\n(Magn.) (dB): ", self)
        self.y_botLim_Label.setGeometry(5, 245, 151, 20)
        self.y_botLim_Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.y_botLim_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.y_botLim_LE = QLineEdit(self)
        self.y_botLim_LE.setGeometry(5, 265, 141, 20)
        self.y_botLim_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.y_botLim_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.y_botLim_LE.setText("-65")

        self.y_topLim_Label = QLabel("Top limit\n(Magn.) (dB): ", self)
        self.y_topLim_Label.setGeometry(5, 330, 151, 20)
        self.y_topLim_Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.y_topLim_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.y_topLim_LE = QLineEdit(self)
        self.y_topLim_LE.setGeometry(5, 350, 141, 20)
        self.y_topLim_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.y_topLim_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.y_topLim_LE.setText("15")


        #phase:
        self.y_botLim_Label_phase = QLabel("Bot. limit\n(Phase) (deg.): ", self)
        self.y_botLim_Label_phase.setGeometry(5, 245, 151, 20)
        self.y_botLim_Label_phase.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.y_botLim_Label_phase.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.y_botLim_LE_phase = QLineEdit(self)
        self.y_botLim_LE_phase.setGeometry(5, 265, 141, 20)
        self.y_botLim_LE_phase.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.y_botLim_LE_phase.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.y_botLim_LE_phase.setText("-180")

        self.y_topLim_Label_phase = QLabel("Top limit\n(Phase) (deg.): ", self)
        self.y_topLim_Label_phase.setGeometry(5, 330, 151, 20)
        self.y_topLim_Label_phase.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.y_topLim_Label_phase.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.y_topLim_LE_phase = QLineEdit(self)
        self.y_topLim_LE_phase.setGeometry(5, 350, 141, 20)
        self.y_topLim_LE_phase.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.y_topLim_LE_phase.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.y_topLim_LE_phase.setText("180")

        #Há um problema de interação entre o Pixmap da classe criada Button e o QVBoxLayout...
        self.btRestoreDefault = Button(self, 5, 380, 151, 20, "Restore\nDefault",
                                    "", "",  False)
        
        self.x_botLim_LE.setFixedWidth(92)
        self.x_topLim_LE.setFixedWidth(92)
        self.y_botLim_LE.setFixedWidth(92)
        self.y_topLim_LE.setFixedWidth(92)
        self.y_botLim_LE_phase.setFixedWidth(92)
        self.y_topLim_LE_phase.setFixedWidth(92)
        self.x_botLim_Label.setFixedWidth(92)
        self.x_topLim_Label.setFixedWidth(92)
        self.y_botLim_Label.setFixedWidth(92)
        self.y_topLim_Label.setFixedWidth(92)
        self.y_botLim_Label_phase.setFixedWidth(92)
        self.y_topLim_Label_phase.setFixedWidth(92)
        self.btRestoreDefault.setFixedWidth(92)
        self.btRestoreDefault.setFixedHeight(40)

        self.scroll = QScrollArea(self)
        self.scroll.setWidgetResizable(True)

        content = QWidget()
        layout = QVBoxLayout(content)

        layout.addWidget(self.x_botLim_Label)
        layout.addWidget(self.x_botLim_LE)
        layout.addWidget(self.x_topLim_Label)
        layout.addWidget(self.x_topLim_LE)
        layout.addWidget(self.y_botLim_Label)
        layout.addWidget(self.y_botLim_LE)
        layout.addWidget(self.y_topLim_Label)
        layout.addWidget(self.y_topLim_LE)
        layout.addWidget(self.y_botLim_Label_phase)
        layout.addWidget(self.y_botLim_LE_phase)
        layout.addWidget(self.y_topLim_Label_phase)
        layout.addWidget(self.y_topLim_LE_phase)
        layout.addWidget(self.btRestoreDefault)
        
        self.btRestoreDefault.setStyleSheet("""
            QPushButton {
                background-color: rgb(196, 196, 196);
                border: 1px solid #9a9a9a;
                padding: 4px 8px;
                border-radius: 4px;
                font-family: "Nirmala UI";
                font-size: 8pt;
            }
            QPushButton:pressed {
                background-color: rgb(170, 170, 170);
            }
            """)
        
        self.scroll.setWidget(content)
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.scroll)
        self.setLayout(mainLayout)

class CursorFreqResp_Magnitude(QDialog):
    def __init__(self):
        super(CursorFreqResp_Magnitude, self).__init__()
        self.setGeometry(890, 260, 151, 371)
        self.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.mainLabel = QLabel("Cursor", self)
        self.mainLabel.setGeometry(0, 0, 151, 52)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 16))

        self.cursorSelectLabel = QLabel("You can assign the cursor \nknob to a line or"
                                        " edit each \none manually. \nKnob is assigned to: ", self)
        self.cursorSelectLabel.setGeometry(0, 35, 151, 70)
        self.cursorSelectLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorSelectLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorSelectCB = QComboBox(self)
        self.cursorSelectCB.setGeometry(0, 120, 151, 22)
        self.cursorSelectCB.setStyleSheet("""background-color: rgb(36, 36, 36); 
                                                                            color: rgb(240, 240, 240)""")

        self.cursorSelectCBItems = ["X1", "X2", "Y1", "Y2"]

        self.cursorSelectCB.addItems(self.cursorSelectCBItems)

        self.cursorX1Label = QLabel("X1 (Hz): ", self)
        self.cursorX1Label.setGeometry(5, 140, 151, 20)
        self.cursorX1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorX1Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX1LE = QLineEdit(self)
        self.cursorX1LE.setGeometry(5, 160, 141, 20)
        self.cursorX1LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX1LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorX1LE.setText("")

        self.cursorX2Label = QLabel("X2 (Hz): ", self)
        self.cursorX2Label.setGeometry(5, 180, 151, 20)
        self.cursorX2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorX2Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX2LE = QLineEdit(self)
        self.cursorX2LE.setGeometry(5, 200, 141, 20)
        self.cursorX2LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX2LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorX2LE.setText("")

        self.cursorY1Label = QLabel("Y1 (dB): ", self)
        self.cursorY1Label.setGeometry(5, 220, 151, 20)
        self.cursorY1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorY1Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY1LE = QLineEdit(self)
        self.cursorY1LE.setGeometry(5, 240, 141, 20)
        self.cursorY1LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY1LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorY1LE.setText("")

        self.cursorY2Label = QLabel("Y2 (dB): ", self)
        self.cursorY2Label.setGeometry(5, 260, 151, 20)
        self.cursorY2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorY2Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY2LE = QLineEdit(self)
        self.cursorY2LE.setGeometry(5, 280, 141, 20)
        self.cursorY2LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY2LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorY2LE.setText("")

        self.cursorDeltaXLabel = QLabel("X2 - X1 (Hz): ", self)
        self.cursorDeltaXLabel.setGeometry(5, 300, 151, 20)
        self.cursorDeltaXLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorDeltaXLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaX_LE = QLineEdit(self)
        self.cursorDeltaX_LE.setGeometry(5, 320, 141, 20)
        self.cursorDeltaX_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaX_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorDeltaX_LE.setText("")
        self.cursorDeltaX_LE.setReadOnly(True)

        self.cursorDeltaYLabel = QLabel("Y2 - Y1 (dB): ", self)
        self.cursorDeltaYLabel.setGeometry(5, 340, 151, 20)
        self.cursorDeltaYLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorDeltaYLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaY_LE = QLineEdit(self)
        self.cursorDeltaY_LE.setGeometry(5, 360, 141, 20)
        self.cursorDeltaY_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaY_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorDeltaY_LE.setText("")
        self.cursorDeltaY_LE.setReadOnly(True)

    def resizeEvent(self, event):
        p = self.width()/151
        self.mainLabel.setGeometry(0, 0, int(p * 151), int(p * 52))
        self.cursorSelectLabel.setGeometry(
            0, int(p * 35), int(p * 151), int(p * 70))
        self.cursorSelectCB.setGeometry(
            0, int(p * 120), int(p * 151), int(p * 22))
        self.cursorX1Label.setGeometry(
            int(p * 5), int(p * 140), int(p * 151), int(p * 20))
        self.cursorX1LE.setGeometry(
            int(p * 5), int(p * 160), int(p * 141), int(p * 25))
        self.cursorX2Label.setGeometry(
            int(p * 5), int(p * 185), int(p * 151), int(p * 20))
        self.cursorX2LE.setGeometry(
            int(p * 5), int(p * 205), int(p * 141), int(p * 25))
        self.cursorY1Label.setGeometry(
            int(p * 5), int(p * 230), int(p * 151), int(p * 20))
        self.cursorY1LE.setGeometry(
            int(p * 5), int(p * 250), int(p * 141), int(p * 25))
        self.cursorY2Label.setGeometry(
            int(p * 5), int(p * 275), int(p * 151), int(p * 20))
        self.cursorY2LE.setGeometry(
            int(p * 5), int(p * 295), int(p * 141), int(p * 25))
        self.cursorDeltaXLabel.setGeometry(
            int(p * 5), int(p * 320), int(p * 151), int(p * 20))
        self.cursorDeltaX_LE.setGeometry(
            int(p * 5), int(p * 340), int(p * 141), int(p * 25))
        self.cursorDeltaYLabel.setGeometry(
            int(p * 5), int(p * 365), int(p * 151), int(p * 20))
        self.cursorDeltaY_LE.setGeometry(
            int(p * 5), int(p * 385), int(p * 141), int(p * 25))

        if self.width() <= 127:
            self.cursorSelectLabel.setFont(QFont("Lucida Sans Unicode", 7))
            self.cursorSelectLabel.setGeometry(
                0, int(p * 35), int(p * 151), int(p * 160))

        if self.width() <= 106:
            self.cursorSelectLabel.setFont(QFont("Lucida Sans Unicode", 6))
            self.cursorSelectLabel.setText("You can assign the cursor \nknob to a line or"
                                        " edit each \none manually. \nKnob is assigned to: ")

            self.cursorSelectCB.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorX1Label.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorX1LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorX2Label.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorX2LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorY1Label.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorY1LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorY2Label.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorY2LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorDeltaXLabel.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorDeltaX_LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorDeltaYLabel.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorDeltaY_LE.setFont(QFont("Lucida Sans Unicode", 8))

class CursorFreqResp_Phase(QDialog):
    def __init__(self):
        super(CursorFreqResp_Phase, self).__init__()
        self.setGeometry(890, 260, 151, 371)
        self.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.mainLabel = QLabel("Cursor", self)
        self.mainLabel.setGeometry(0, 0, 151, 52)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 16))

        self.cursorSelectLabel = QLabel("You can assign the cursor \nknob to a line or"
                                        " edit each \none manually. \nKnob is assigned to: ", self)
        self.cursorSelectLabel.setGeometry(0, 35, 151, 70)
        self.cursorSelectLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorSelectLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorSelectCB = QComboBox(self)
        self.cursorSelectCB.setGeometry(0, 120, 151, 22)
        self.cursorSelectCB.setStyleSheet("""background-color: rgb(36, 36, 36); 
                                                                            color: rgb(240, 240, 240)""")

        self.cursorSelectCBItems = ["X1", "X2", "Y1", "Y2"]

        self.cursorSelectCB.addItems(self.cursorSelectCBItems)

        self.cursorX1Label = QLabel("X1 (Hz): ", self)
        self.cursorX1Label.setGeometry(5, 140, 151, 20)
        self.cursorX1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorX1Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX1LE = QLineEdit(self)
        self.cursorX1LE.setGeometry(5, 160, 141, 20)
        self.cursorX1LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX1LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorX1LE.setText("")

        self.cursorX2Label = QLabel("X2 (Hz): ", self)
        self.cursorX2Label.setGeometry(5, 180, 151, 20)
        self.cursorX2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorX2Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX2LE = QLineEdit(self)
        self.cursorX2LE.setGeometry(5, 200, 141, 20)
        self.cursorX2LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorX2LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorX2LE.setText("")

        self.cursorY1Label = QLabel("Y1 (deg.): ", self)
        self.cursorY1Label.setGeometry(5, 220, 151, 20)
        self.cursorY1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorY1Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY1LE = QLineEdit(self)
        self.cursorY1LE.setGeometry(5, 240, 141, 20)
        self.cursorY1LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY1LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorY1LE.setText("")

        self.cursorY2Label = QLabel("Y2 (deg.): ", self)
        self.cursorY2Label.setGeometry(5, 260, 151, 20)
        self.cursorY2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorY2Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY2LE = QLineEdit(self)
        self.cursorY2LE.setGeometry(5, 280, 141, 20)
        self.cursorY2LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorY2LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorY2LE.setText("")

        self.cursorDeltaXLabel = QLabel("X2 - X1 (Hz): ", self)
        self.cursorDeltaXLabel.setGeometry(5, 300, 151, 20)
        self.cursorDeltaXLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorDeltaXLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaX_LE = QLineEdit(self)
        self.cursorDeltaX_LE.setGeometry(5, 320, 141, 20)
        self.cursorDeltaX_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaX_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorDeltaX_LE.setText("")
        self.cursorDeltaX_LE.setReadOnly(True)

        self.cursorDeltaYLabel = QLabel("Y2 - Y1 (deg.): ", self)
        self.cursorDeltaYLabel.setGeometry(5, 340, 151, 20)
        self.cursorDeltaYLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.cursorDeltaYLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaY_LE = QLineEdit(self)
        self.cursorDeltaY_LE.setGeometry(5, 360, 141, 20)
        self.cursorDeltaY_LE.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorDeltaY_LE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.cursorDeltaY_LE.setText("")
        self.cursorDeltaY_LE.setReadOnly(True)

    def resizeEvent(self, event):
        p = self.width()/151
        self.mainLabel.setGeometry(0, 0, int(p * 151), int(p * 52))
        self.cursorSelectLabel.setGeometry(
            0, int(p * 35), int(p * 151), int(p * 70))
        self.cursorSelectCB.setGeometry(
            0, int(p * 120), int(p * 151), int(p * 22))
        self.cursorX1Label.setGeometry(
            int(p * 5), int(p * 140), int(p * 151), int(p * 20))
        self.cursorX1LE.setGeometry(
            int(p * 5), int(p * 160), int(p * 141), int(p * 25))
        self.cursorX2Label.setGeometry(
            int(p * 5), int(p * 185), int(p * 151), int(p * 20))
        self.cursorX2LE.setGeometry(
            int(p * 5), int(p * 205), int(p * 141), int(p * 25))
        self.cursorY1Label.setGeometry(
            int(p * 5), int(p * 230), int(p * 151), int(p * 20))
        self.cursorY1LE.setGeometry(
            int(p * 5), int(p * 250), int(p * 141), int(p * 25))
        self.cursorY2Label.setGeometry(
            int(p * 5), int(p * 275), int(p * 151), int(p * 20))
        self.cursorY2LE.setGeometry(
            int(p * 5), int(p * 295), int(p * 141), int(p * 25))
        self.cursorDeltaXLabel.setGeometry(
            int(p * 5), int(p * 320), int(p * 151), int(p * 20))
        self.cursorDeltaX_LE.setGeometry(
            int(p * 5), int(p * 340), int(p * 141), int(p * 25))
        self.cursorDeltaYLabel.setGeometry(
            int(p * 5), int(p * 365), int(p * 151), int(p * 20))
        self.cursorDeltaY_LE.setGeometry(
            int(p * 5), int(p * 385), int(p * 141), int(p * 25))

        if self.width() <= 127:
            self.cursorSelectLabel.setFont(QFont("Lucida Sans Unicode", 7))
            self.cursorSelectLabel.setGeometry(
                0, int(p * 35), int(p * 151), int(p * 160))

        if self.width() <= 106:
            self.cursorSelectLabel.setFont(QFont("Lucida Sans Unicode", 6))
            self.cursorSelectLabel.setText("You can assign the cursor \nknob to a line or"
                                        " edit each \none manually. \nKnob is assigned to: ")

            self.cursorSelectCB.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorX1Label.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorX1LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorX2Label.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorX2LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorY1Label.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorY1LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorY2Label.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorY2LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorDeltaXLabel.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorDeltaX_LE.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorDeltaYLabel.setFont(QFont("Lucida Sans Unicode", 8))
            self.cursorDeltaY_LE.setFont(QFont("Lucida Sans Unicode", 8))

class Calibration_scr2(QDialog):
    def __init__(self):
        super(Calibration_scr2, self).__init__()
        self.setGeometry(890, 260, 151, 371)
        self.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.mainLabel = QLabel("Calibration", self)
        self.mainLabel.setGeometry(0, 20, 175, 52)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 20))

        self.LPF_CheckBox = QCheckBox("Enable Low-Pass Filter (DSP)", self)
        self.LPF_CheckBox.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.LPF_CheckBox.setFont(QFont("Microsoft Sans Serif", 9))
        self.LPF_CheckBox.setGeometry(0, 60, 175, 30)
        self.LPF_CheckBox.setChecked(False)
        self.LPF_CheckBox.checkStateChanged.connect(self.LPF_Checkbox_coverLabel)

        self.LPF_label = QLabel("LPF Cutoff Freq. (Hz):", self)
        self.LPF_label.setGeometry(5, 110, 175, 22)
        self.LPF_label.setStyleSheet(
            """ color: rgb(240, 240, 240) """)
        self.LPF_LE = QLineEdit(self)
        self.LPF_LE.setText("10000")
        self.LPF_LE.setGeometry(0, 130, 175, 22)
        self.LPF_LE.setStyleSheet("""background-color: rgb(56, 56, 56); 
                                            color: rgb(240, 240, 240)""")
        
        self.LPF_coverLabel = QLabel("", self)
        self.LPF_coverLabel.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.LPF_coverLabel.setGeometry(0, 110, 175, 45)
        self.LPF_coverLabel.show()
        
        self.phaseCorr_CheckBox = QCheckBox("Enable Phase\nCorrection Adjust", self)
        self.phaseCorr_CheckBox.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.phaseCorr_CheckBox.setFont(QFont("Microsoft Sans Serif", 9))
        self.phaseCorr_CheckBox.setGeometry(0, 160, 175, 60)
        self.phaseCorr_CheckBox.setChecked(True)


        self.phaseCorr_label = QLabel("The Phase Correction adjust and the LPF may cause a slight distortion in the channels.", self)
        self.phaseCorr_label.setWordWrap(True)
        self.phaseCorr_label.setGeometry(0, 220, 175, 70)
        self.phaseCorr_label.setStyleSheet("color: rgb(240, 240, 240)")
        self.phaseCorr_label.setFont(QFont("Microsoft Sans Serif", 8))

    def LPF_Checkbox_coverLabel(self):
        if self.LPF_CheckBox.isChecked():
            self.LPF_coverLabel.hide()
        else:
            self.LPF_coverLabel.show()

    def resizeEvent(self, event):
        p = self.width()/175
        self.mainLabel.setGeometry(0, int(p * 20), int(p * 175), int(p * 52))
        self.LPF_LE.setGeometry(0, int(130), int(p * 175), int(22))
        self.phaseCorr_label.setGeometry(0, int(220), int(p * 175), int(70))

        if self.width() <= 128:
            self.mainLabel.setFont(QFont("Microsoft Sans Serif", 18))



if __name__ == '__main__':
    app = QApplication([])
    window = Calibration_scr2()
    window.show()
    app.exec()
