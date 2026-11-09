import os
from PySide6.QtGui import QPixmap, QPainter, QIcon, QFont, QDesktopServices
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QCheckBox, QComboBox
from PySide6.QtCore import Qt, QRect, QUrl
from PySide6.QtTest import QTest
from pyqtgraph import QtCore
from PySide6 import QtWidgets
from button import Button
from knob import Knob

class WelcomeWindow(QDialog):
    def __init__(self):
        super(WelcomeWindow, self).__init__()
        self.setGeometry(345, 350, 700, 600)
        self.setFixedSize(700, 600)
        self.setWindowTitle("Welcome to MyOscilloscope!")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

        self.language = "Português"

        self.mainLabel = QLabel("", self)
        self.mainLabel.setAlignment(Qt.AlignHCenter)
        self.mainLabel.setGeometry(-10, 30, 719, 271)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        welcomeImage = QPixmap("images/welcomeImage.png")

        scaled_welcomeImage = welcomeImage.scaled(
            self.mainLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.mainLabel.setPixmap(scaled_welcomeImage)

        self.languageSelectLabel = QLabel("Select the language: ", self)
        self.languageSelectLabel.setGeometry(120, 240, 200, 30)
        self.languageSelectLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.languageSelectLabel.setAlignment(Qt.AlignHCenter)
        self.languageSelectLabel.setFont(QFont("Franklin Gothic Medium", 12))

        self.languageSelectLabelCB = QComboBox(self)
        self.languageSelectLabelCB.setGeometry(370, 235, 200, 30)
        self.languageSelectLabelCB.setStyleSheet("""background-color: rgb(56, 56, 56); 
                                                                    color: rgb(240, 240, 240)""")

        self.languageSelectLabelCB.setFont(QFont("Microsoft Sans Serif", 11))
        

        self.languageSelectLabelCBItems = ["Português", "English"]
        self.languageSelectLabelCB.addItems(self.languageSelectLabelCBItems)

        self.sentence1Label = QLabel("Bringing the lab to wherever you are with MyOscilloscope!", self)
        self.sentence1Label.setAlignment(Qt.AlignHCenter)
        self.sentence1Label.setGeometry(-10, 300, 719, 30)
        self.sentence1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentence1Label.setFont(QFont("Franklin Gothic Medium", 16))

        self.sentence2Label = QLabel("For a better experience, consider:" +
        "\n• Consult general guidelines in the User Help tab by clicking on Help.;" +
        "\n• Visiting the project website: myoscilloscope.lme.usp.br*;" +
        "\n• IMPORTANT: Verify microcontroller driver proper installation topics, as detailed on the website.",  self)
        #self.sentence2Label.setAlignment(Qt.AlignHCenter)
        self.sentence2Label.setGeometry(20, 295, 700, 150)
        self.sentence2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentence2Label.setFont(QFont("Franklin Gothic Medium", 12))
        self.sentence2Label.setWordWrap(True)
        
    
        self.OkButton = Button(self, 250, 470, 508, 40, "",
                                    "images/Bt_OK.png", "images/Bt_OK.png",  False)
        
        self.dontShowAgainCheckBox = QCheckBox("Do not show this again", self)
        self.dontShowAgainCheckBox.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.dontShowAgainCheckBox.setFont(QFont("Microsoft Sans Serif", 9))
        self.dontShowAgainCheckBox.setGeometry(275, 520, 200, 80)
        self.dontShowAgainCheckBox.setChecked(False)

        self.sentence3Label = QLabel("*User Guide only available in Portuguese. It requires USP-VPN Connection.", self)
        self.sentence3Label.setAlignment(Qt.AlignHCenter)
        self.sentence3Label.setGeometry(140, 580, 450, 50)
        self.sentence3Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentence3Label.setFont(QFont("Microsoft Sans Serif", 7))

        self.USP_Logo = QLabel("", self)
        self.Poli_Logo = QLabel("", self)
        self.USP_Logo.setGeometry(20, 460, 170, 100)
        self.Poli_Logo.setGeometry(530, 440, 180, 130)


        USPImage = QPixmap("images/USPLogo")
        scaled_USPImage = USPImage.scaled(
            self.USP_Logo.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.USP_Logo.setPixmap(scaled_USPImage)

        PoliImage = QPixmap("images/PoliLogo")
        scaled_PoliImage = PoliImage.scaled(
            self.Poli_Logo.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.Poli_Logo.setPixmap(scaled_PoliImage)

        self.languageSelectLabelCB.currentIndexChanged.connect(self.changeLanguage)
        self.changeLanguage()

    def changeLanguage(self):
        if self.languageSelectLabelCB.currentText() == "Português":
            self.setWindowTitle("Bem-vindo(a) ao MyOscilloscope!")
            self.languageSelectLabel.setText("Selecione o idioma: ")
            self.sentence1Label.setText("Bem-vindo(a) ao MyOscilloscope!")
            self.sentence2Label.setText("Para uma boa experiência, considere:" +
            "\n• Consultar orientações gerais na aba de Apoio ao Usuário, clicando em Help;" +
            "\n• Acessar o site oficial do projeto: myoscilloscope.lme.usp.br*. " + 
            "\n• IMPORTANTE: Verificar questões de instalação adequada do driver do microcontrolador, conforme está presente no site.")
            self.dontShowAgainCheckBox.setText("Não mostrar esta tela novamente.")
            self.dontShowAgainCheckBox.setGeometry(250, 520, 200, 80)
            self.sentence3Label.setText("*Requer conexão com a VPN da USP.")
            self.sentence3Label.setGeometry(125, 580, 450, 50)

        else:
            self.setWindowTitle("Welcome to MyOscilloscope!")
            self.languageSelectLabel.setText("Select the language: ")
            self.sentence1Label.setText("Bringing the lab to wherever you are with MyOscilloscope!")
            self.sentence2Label.setText("For a better experience, consider:" +
            "\n• Consult general guidelines in the User Help tab by clicking on Help.;" +
            "\n• Visit the project official website: myoscilloscope.lme.usp.br*. " + 
            "\n• IMPORTANT: Verify microcontroller driver proper installation topics, as detailed on the website.")
            self.dontShowAgainCheckBox.setText("Do not show this again.")
            self.sentence3Label.setText("*User Guide only available in Portuguese. It requires USP-VPN Connection.")
            self.dontShowAgainCheckBox.setGeometry(275, 520, 200, 80)
            self.sentence3Label.setGeometry(140, 580, 450, 50)



def should_show_welcome(self):
    if not os.path.exists(self.PARAMETERS_FILE):
        return True  

    with open(self.PARAMETERS_FILE, "r") as f:
        for line in f:
            if "show_welcome" in line:
                return line.split("=")[1].strip().lower() == "true"
    return True

def closeWelcomeWindow(self):
    #salvar o novo idioma:
    languageSelected = self.welcomeWindow.languageSelectLabelCB.currentText()
    self.language = languageSelected
    self.saveLanguage(languageSelected)
    if self.welcomeWindow.dontShowAgainCheckBox.isChecked(): self.save_show_welcome(False)
    self.welcomeWindow.close()

def save_show_welcome(self, value: bool):
    filepath = self.PARAMETERS_FILE
    key = "show_welcome"
    val = "true" if value else "false"


    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    key_written = False


    for i, line in enumerate(lines):
        if line.strip().startswith(f"{key} ="):
            lines[i] = f"{key} = {val}\n"
            key_written = True
            break

   
    if not key_written:
        lines.append(f"{key} = {val}\n")

    
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)


if __name__ == '__main__':
    app = QApplication([])
    window = WelcomeWindow()
    window.show()
    app.exec()
