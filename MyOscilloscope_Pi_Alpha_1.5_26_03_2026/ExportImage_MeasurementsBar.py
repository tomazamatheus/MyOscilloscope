from PySide6.QtWidgets import QDialog, QLabel, QComboBox, QLineEdit, QApplication, QPushButton, QCheckBox, QScrollArea, QWidget, QVBoxLayout, QStackedWidget
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtCore import Qt, QRect
import os, datetime
from button import Button
import sys

class ExpImage_MeasureBar(QDialog):
    def __init__(self):
        super(ExpImage_MeasureBar, self).__init__()
        self.setGeometry(0, 0, 842, 200)
        self.setStyleSheet("background-color: rgb(224, 240, 255);")

        

        self.mainLabel1 = QLabel("CH1", self)
        self.mainLabel1.setGeometry(100, 5, 85, 20)
        self.mainLabel1.setStyleSheet(""" color: rgb(0, 70, 134) """)
        self.mainLabel1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel1.setFont(QFont("Microsoft Sans Serif", 14))

        self.mainLabel2 = QLabel("CH2", self)
        self.mainLabel2.setGeometry(375, 5, 85, 20)
        self.mainLabel2.setStyleSheet(""" color: red """)
        self.mainLabel2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel2.setFont(QFont("Microsoft Sans Serif", 14))

        self.mainLabel3 = QLabel("Math", self)
        self.mainLabel3.setGeometry(660, 5, 85, 20)
        self.mainLabel3.setStyleSheet(""" color: rgb(2, 135, 255) """)
        self.mainLabel3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel3.setFont(QFont("Microsoft Sans Serif", 14))

        

        self.freqLabel_1 = QLabel("Frequency:", self)
        self.freqLabel_1.setGeometry(50, 30, 85, 20)
        self.freqLabel_1.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.freqLabel_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freqLE_1 = QLineEdit(self)
        self.freqLE_1.setGeometry(50, 50, 85, 20)
        self.freqLE_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freqLE_1.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.freqLE_1.setText("")

        self.periodLabel_1 = QLabel("Period:", self)
        self.periodLabel_1.setGeometry(140, 30, 85, 20)
        self.periodLabel_1.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.periodLabel_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.periodLE_1 = QLineEdit(self)
        self.periodLE_1.setGeometry(140, 50, 85, 20)
        self.periodLE_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.periodLE_1.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.periodLE_1.setText("")

        self.freqLabel_2 = QLabel("Frequency:", self)
        self.freqLabel_2.setGeometry(330, 30, 85, 20)
        self.freqLabel_2.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.freqLabel_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freqLE_2 = QLineEdit(self)
        self.freqLE_2.setGeometry(330, 50, 85, 20)
        self.freqLE_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freqLE_2.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.freqLE_2.setText("")

        self.periodLabel_2 = QLabel("Period:", self)
        self.periodLabel_2.setGeometry(420, 30, 85, 20)
        self.periodLabel_2.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.periodLabel_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.periodLE_2 = QLineEdit(self)
        self.periodLE_2.setGeometry(420, 50, 85, 20)
        self.periodLE_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.periodLE_2.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.periodLE_2.setText("")

        self.freqLabel_3 = QLabel("Frequency:", self)
        self.freqLabel_3.setGeometry(615, 30, 85, 20)
        self.freqLabel_3.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.freqLabel_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freqLE_3 = QLineEdit(self)
        self.freqLE_3.setGeometry(615, 50, 85, 20)
        self.freqLE_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.freqLE_3.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.freqLE_3.setText("")

        self.periodLabel_3 = QLabel("Period:", self)
        self.periodLabel_3.setGeometry(705, 30, 85, 20)
        self.periodLabel_3.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.periodLabel_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.periodLE_3 = QLineEdit(self)
        self.periodLE_3.setGeometry(705, 50, 85, 20)
        self.periodLE_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.periodLE_3.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.periodLE_3.setText("")


        self.DCLabel_1 = QLabel("DC - Mean:", self)
        self.DCLabel_1.setGeometry(5, 80, 90, 20)
        self.DCLabel_1.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.DCLabel_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.DCLE_1 = QLineEdit(self)
        self.DCLE_1.setGeometry(5, 100, 85, 20)
        self.DCLE_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.DCLE_1.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.DCLE_1.setText("")

        self.Pk_to_PkLabel_1 = QLabel("Peak-to-Peak:", self)
        self.Pk_to_PkLabel_1.setGeometry(95, 80, 85, 20)
        self.Pk_to_PkLabel_1.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.Pk_to_PkLabel_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Pk_to_PkLE_1 = QLineEdit(self)
        self.Pk_to_PkLE_1.setGeometry(95, 100, 85, 20)
        self.Pk_to_PkLE_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Pk_to_PkLE_1.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.Pk_to_PkLE_1.setText("")

        self.RMSLabel_1 = QLabel("RMS:", self)
        self.RMSLabel_1.setGeometry(185, 80, 85, 20)
        self.RMSLabel_1.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.RMSLabel_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.RMSLE_1 = QLineEdit(self)
        self.RMSLE_1.setGeometry(185, 100, 85, 20)
        self.RMSLE_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.RMSLE_1.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.RMSLE_1.setText("")

        self.DCLabel_2 = QLabel("DC - Mean:", self)
        self.DCLabel_2.setGeometry(285, 80, 90, 20)
        self.DCLabel_2.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.DCLabel_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.DCLE_2 = QLineEdit(self)
        self.DCLE_2.setGeometry(285, 100, 85, 20)
        self.DCLE_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.DCLE_2.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.DCLE_2.setText("")

        self.Pk_to_PkLabel_2 = QLabel("Peak-to-Peak:", self)
        self.Pk_to_PkLabel_2.setGeometry(375, 80, 85, 20)
        self.Pk_to_PkLabel_2.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.Pk_to_PkLabel_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Pk_to_PkLE_2 = QLineEdit(self)
        self.Pk_to_PkLE_2.setGeometry(375, 100, 85, 20)
        self.Pk_to_PkLE_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Pk_to_PkLE_2.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.Pk_to_PkLE_2.setText("")

        self.RMSLabel_2 = QLabel("RMS:", self)
        self.RMSLabel_2.setGeometry(465, 80, 85, 20)
        self.RMSLabel_2.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.RMSLabel_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.RMSLE_2 = QLineEdit(self)
        self.RMSLE_2.setGeometry(465, 100, 85, 20)
        self.RMSLE_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.RMSLE_2.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.RMSLE_2.setText("")

        self.DCLabel_3 = QLabel("DC - Mean:", self)
        self.DCLabel_3.setGeometry(570, 80, 90, 20)
        self.DCLabel_3.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.DCLabel_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.DCLE_3 = QLineEdit(self)
        self.DCLE_3.setGeometry(570, 100, 85, 20)
        self.DCLE_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.DCLE_3.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.DCLE_3.setText("")

        self.Pk_to_PkLabel_3 = QLabel("Peak-to-Peak:", self)
        self.Pk_to_PkLabel_3.setGeometry(660, 80, 85, 20)
        self.Pk_to_PkLabel_3.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.Pk_to_PkLabel_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Pk_to_PkLE_3 = QLineEdit(self)
        self.Pk_to_PkLE_3.setGeometry(660, 100, 85, 20)
        self.Pk_to_PkLE_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Pk_to_PkLE_3.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.Pk_to_PkLE_3.setText("")

        self.RMSLabel_3 = QLabel("RMS:", self)
        self.RMSLabel_3.setGeometry(750, 80, 85, 20)
        self.RMSLabel_3.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.RMSLabel_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.RMSLE_3 = QLineEdit(self)
        self.RMSLE_3.setGeometry(750, 100, 85, 20)
        self.RMSLE_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.RMSLE_3.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.RMSLE_3.setText("")

        self.MinLabel_1 = QLabel("Min Value:", self)
        self.MinLabel_1.setGeometry(5, 130, 85, 20)
        self.MinLabel_1.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.MinLabel_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MinLE_1 = QLineEdit(self)
        self.MinLE_1.setGeometry(5, 150, 85, 20)
        self.MinLE_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MinLE_1.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.MinLE_1.setText("")

        self.MaxLabel_1 = QLabel("Max Value:", self)
        self.MaxLabel_1.setGeometry(95, 130, 85, 20)
        self.MaxLabel_1.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.MaxLabel_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MaxLE_1 = QLineEdit(self)
        self.MaxLE_1.setGeometry(95, 150, 85, 20)
        self.MaxLE_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MaxLE_1.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.MaxLE_1.setText("")

        self.phaseShiftLabel_1 = QLabel("Phase Shift:", self)
        self.phaseShiftLabel_1.setGeometry(185, 130, 85, 20)
        self.phaseShiftLabel_1.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.phaseShiftLabel_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.phaseShiftLE_1 = QLineEdit(self)
        self.phaseShiftLE_1.setGeometry(185, 150, 85, 20)
        self.phaseShiftLE_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.phaseShiftLE_1.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.phaseShiftLE_1.setText("")

        self.MinLabel_2 = QLabel("Min Value:", self)
        self.MinLabel_2.setGeometry(285, 130, 85, 20)
        self.MinLabel_2.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.MinLabel_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MinLE_2 = QLineEdit(self)
        self.MinLE_2.setGeometry(285, 150, 85, 20)
        self.MinLE_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MinLE_2.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.MinLE_2.setText("")

        self.MaxLabel_2 = QLabel("Max Value:", self)
        self.MaxLabel_2.setGeometry(375, 130, 85, 20)
        self.MaxLabel_2.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.MaxLabel_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MaxLE_2 = QLineEdit(self)
        self.MaxLE_2.setGeometry(375, 150, 85, 20)
        self.MaxLE_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MaxLE_2.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.MaxLE_2.setText("")

        self.phaseShiftLabel_2 = QLabel("Phase Shift:", self)
        self.phaseShiftLabel_2.setGeometry(465, 130, 85, 20)
        self.phaseShiftLabel_2.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.phaseShiftLabel_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.phaseShiftLE_2 = QLineEdit(self)
        self.phaseShiftLE_2.setGeometry(465, 150, 85, 20)
        self.phaseShiftLE_2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.phaseShiftLE_2.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.phaseShiftLE_2.setText("")

        self.MinLabel_3 = QLabel("Min Value:", self)
        self.MinLabel_3.setGeometry(570, 130, 85, 20)
        self.MinLabel_3.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.MinLabel_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MinLE_3 = QLineEdit(self)
        self.MinLE_3.setGeometry(570, 150, 85, 20)
        self.MinLE_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MinLE_3.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.MinLE_3.setText("")

        self.MaxLabel_3 = QLabel("Max Value:", self)
        self.MaxLabel_3.setGeometry(660, 130, 85, 20)
        self.MaxLabel_3.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.MaxLabel_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MaxLE_3 = QLineEdit(self)
        self.MaxLE_3.setGeometry(660, 150, 85, 20)
        self.MaxLE_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.MaxLE_3.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.MaxLE_3.setText("")

        self.phaseShiftLabel_3 = QLabel("Phase Shift:", self)
        self.phaseShiftLabel_3.setGeometry(750, 130, 85, 20)
        self.phaseShiftLabel_3.setStyleSheet(""" color: rgb(20, 20, 20) """)
        self.phaseShiftLabel_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.phaseShiftLE_3 = QLineEdit(self)
        self.phaseShiftLE_3.setGeometry(750, 150, 85, 20)
        self.phaseShiftLE_3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.phaseShiftLE_3.setStyleSheet(
            """color: rgb(56, 56, 56); 
            background-color: rgb(240, 240, 240)""")
        self.phaseShiftLE_3.setText("")



        self.hideLabel1 = QLabel("", self)
        self.hideLabel1.setStyleSheet("background-color: rgb(224, 240, 255)")
        self.hideLabel1.setGeometry(0, 0, 270, 200)
        self.hideLabel1.raise_()
        self.hideLabel1.hide()

        self.hideLabel2 = QLabel("", self)
        self.hideLabel2.setStyleSheet("background-color: rgb(224, 240, 255)")
        self.hideLabel2.setGeometry(280, 0, 270, 200)
        self.hideLabel2.raise_()
        self.hideLabel2.hide()

        self.hideLabel3 = QLabel("", self)
        self.hideLabel3.setStyleSheet("background-color: rgb(224, 240, 255)")
        self.hideLabel3.setGeometry(570, 0, 270, 200)
        self.hideLabel3.raise_()
        self.hideLabel3.hide()

        self.supportLabel1 = QLabel("Reference Channel: CH1", self)
        self.supportLabel1.setGeometry(150, 175, 845, 25)
        self.supportLabel1.setStyleSheet("""background-color: transparent; 
                                            font-weight: bold; """)
        self.supportLabel1.setFont(QFont("Nirmala UI", 11))

        self.supportLabel2 = QLabel("Captured at: " + f"{datetime.date.today()} {datetime.datetime.now().time()}.", self)
        self.supportLabel2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.supportLabel2.setGeometry(400, 175, 400, 80)
        self.supportLabel2.setStyleSheet("""background-color: transparent; 
                                            font-weight: bold; """)
        self.supportLabel2.setFont(QFont("Nirmala UI", 11))
        

        


if __name__ == '__main__':
    app = QApplication([])
    window = ExpImage_MeasureBar()
    window.show()
    app.exec()