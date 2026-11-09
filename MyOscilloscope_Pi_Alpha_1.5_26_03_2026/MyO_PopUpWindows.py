from PySide6.QtWidgets import QApplication, QDialog, QLabel
import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QFont, QPixmap
from button import Button

class COM_Port_Window(QDialog):
    def __init__(self ):
        super(COM_Port_Window, self).__init__()
        self.setGeometry(350, 350, 550, 130)
        self.setFixedSize(600, 130)
        self.setWindowTitle("Please set COM Port")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.language = "Português"

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())
        
        self.mainLabel = QLabel("", self)
        self.mainLabel.setAlignment(Qt.AlignHCenter)
        self.mainLabel.setGeometry(0, 25, 600, 130)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 11))
        self.mainLabel.setWordWrap(True)
        self.OKButton = Button(self, 240, 90, 410, 30, "",
                                    "images/Bt_OK.png", "images/Bt_OK.png",  False)
        self.OKButton.clicked.connect(self.closeWindow)


    def setLanguage(self):
        if self.language == "English":
            self.setWindowTitle("Please set COM Port")
            self.mainLabel.setText(f"MyOscilloscope needs communication with an available COM Port to work. " +
                                "Please connect the microcontroller in a USB port and press Search button until " + 
                                "MyOscilloscope detects an available COM Port.")
            
        else:
            self.setWindowTitle("Definir Porta COM")
            self.mainLabel.setGeometry(10, 25, 580, 130)
            self.mainLabel.setText(f"MyOscilloscope requer conexão com uma porta COM para funcionar adequadamente.\n" +
                                "Por favor, conecte o microcontrolador a uma entrada USB e pressione o botão Search até que a " + 
                                "interface detecte uma porta COM disponível.")
    def closeWindow(self):
        self.close()

class SavedCalibWindow(QDialog):
    def __init__(self ):
        super(SavedCalibWindow, self).__init__()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowContextHelpButtonHint)
        self.setGeometry(350, 350, 600, 120)
        self.setFixedSize(600, 120)
        self.setWindowTitle("Calibration")
        self.setWindowIcon(QIcon("images/MyOscPi_RedIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.language = "Português"
        self.mainLabel = QLabel("The Calibration Parameters have been saved successfully.", self)
        self.mainLabel.setAlignment(Qt.AlignHCenter)
        self.mainLabel.setGeometry(0, 25, 600, 130)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 11))
        self.OKButton = Button(self, 240, 80, 410, 30, "",
                                    "images/Bt_OK.png", "images/Bt_OK.png",  False)
        self.OKButton.clicked.connect(self.closeWindow)

        #Para deixar a janela no centro da tela:
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

    def setLanguage(self):
        if self.language == "English": self.mainLabel.setText("The Calibration Parameters have been saved successfully.")
        else: self.mainLabel.setText("Os parâmetros de calibração foram salvos com sucesso.")

    def closeWindow(self):
        self.close()

class WFM_SupportWindow(QDialog):
    def __init__(self ):
        super(WFM_SupportWindow, self).__init__()
        self.setGeometry(350, 350, 800, 500)
        self.setFixedSize(800, 500)
        self.language = "Português"
        self.setWindowTitle("Waveform Generator")
        self.setWindowIcon(QIcon("images/MyOscPi_GreenIcon.png"))
        self.setStyleSheet("background-color: rgb(37, 37, 37);")
        self.mainLabel = QLabel("Unlike most waveform generators, the MyOscilloscope Waveform Generator adjusts output\namplitude as a percentage "+
                                "instead of voltage. The maximum achievable level depends on the\ncomputer’s sound card.", self)
        self.mainLabel.setAlignment(Qt.AlignHCenter)
        self.mainLabel.setGeometry(0, 25, 800, 130)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setFont(QFont("Franklin Gothic Medium", 12))
        self.mainLabel.setWordWrap(True)

        self.illustrationLabel = QLabel("illustration", self)
        self.illustrationLabel.setGeometry(50, 100, 680, 160)
        illustrationImage = QPixmap("images/SO_soundVolume.png")
        scaled_illustrationImage = illustrationImage.scaled(
            self.illustrationLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.illustrationLabel.setPixmap(scaled_illustrationImage)

        self.label2 = QLabel("Recommendations:\n\n" + 
                             "• Set the OS volume to 100% and adjust the generated signal amplitude only within\nthe application;" +
                             "\n\n• Disable audio enhancement features and spatial sound by accessing the output device\nproperties " + 
                             "under Sound in the Control Panel (Windows).", self)
        
        self.label2.setGeometry(20, 225, 800, 200)
        self.label2.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label2.setFont(QFont("Franklin Gothic Medium", 12))
        self.label2.setWordWrap(True)

        self.OKButton = Button(self, 300, 445, 200, 30, "OK",
                                    "images/Bt_OK.png", "images/Bt_OK.png",  False)
        self.OKButton.clicked.connect(self.closeWindow)

        #Para deixar a janela no centro da tela:
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())



    def setLanguage(self):
        if self.language == "English":
            self.mainLabel.setText("Unlike most waveform generators, the MyOscilloscope Waveform Generator adjusts output\namplitude as a percentage "+
                                "instead of voltage. The maximum achievable level depends on the\ncomputer’s sound card.")
            self.label2.setText("Recommendations:\n\n" + 
                             "• Set the OS volume to 100% and adjust the generated signal amplitude only within\nthe application;" +
                             "\n• Disable audio enhancement features and spatial sound by accessing the output device\nproperties " + 
                             "under Sound in the Control Panel (Windows).")
            
        else:
            self.mainLabel.setText("Diferente de outros geradores de função, o Waveform Generator tem a amplitude do sinal definida com um "+
                                "valor percentual, ao invés de um valor em escala de tensão. A amplitude máxima varia conforme a placa de áudio do PC do usuário.")
            self.label2.setText("Recomendações:\n\n" + 
                             "• Defina o volume do áudio do seu SO em 100% e altere a amplitude do gerador apenas dentro da interface;" +
                             "\n• Desative os recursos de aprimoramento de áudio e de som espacial ao acessar as propriedades " + 
                             "de Som no Painel de Controle (Windows).")


    def closeWindow(self):
        self.close()

class CreditsWindow(QDialog):
    def __init__(self, version):
        super(CreditsWindow, self).__init__()
        self.setGeometry(350, 350, 800, 700)
        self.setFixedSize(800, 700)
        self.setWindowTitle("Credits")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(37, 37, 37);")
        self.version = version
        self.language = "English"
        

        #Para deixar a janela no centro da tela:
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

        self.logoLabel = QLabel("", self)
        self.logoLabel.setAlignment(Qt.AlignHCenter)
        self.logoLabel.setGeometry(50, 20, 700, 200)
        self.logoLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.logoImage = QPixmap("images/MyOscilloscopeLogo.png")

        scaled_logoImage = self.logoImage.scaled(
            self.logoLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.logoLabel.setPixmap(scaled_logoImage)

        self.versionLabel = QLabel(f"Version {version}", self)
        self.versionLabel.setGeometry(0, 180, 800, 100)
        self.versionLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.versionLabel.setAlignment(Qt.AlignHCenter)
        self.versionLabel.setFont(QFont("Microsoft Sans Serif", 18, QFont.Bold))

        self.authorLabel = QLabel("Author", self)
        self.authorLabel.setGeometry(0, 240, 800, 100)
        self.authorLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.authorLabel.setAlignment(Qt.AlignHCenter)
        self.authorLabel.setFont(QFont("Microsoft Sans Serif", 18, QFont.Bold))

        self.authorNameLabel = QLabel("João Vitor Adami de Medeiros", self)
        self.authorNameLabel.setGeometry(0, 280, 800, 100)
        self.authorNameLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.authorNameLabel.setAlignment(Qt.AlignHCenter)
        self.authorNameLabel.setFont(QFont("Microsoft Sans Serif", 16))

        self.supervisorsLabel = QLabel("Under the supervision of", self)
        self.supervisorsLabel.setGeometry(0, 340, 800, 100)
        self.supervisorsLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.supervisorsLabel.setAlignment(Qt.AlignHCenter)
        self.supervisorsLabel.setFont(QFont("Microsoft Sans Serif", 18, QFont.Bold))

        self.supervisorsNamesLabel = QLabel("Elisabete Galeazzo, Ph.D." +
                                            "\nHenrique Estanislau Maldonado Peres, Ph.D." +
                                            "\nMauricio Oscar Perez Lisboa, M.Sc.", self)
        self.supervisorsNamesLabel.setGeometry(0, 380, 800, 100)
        self.supervisorsNamesLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.supervisorsNamesLabel.setAlignment(Qt.AlignHCenter)
        self.supervisorsNamesLabel.setFont(QFont("Microsoft Sans Serif", 16))


        

        self.contactLabel = QLabel("Contact", self)
        self.contactLabel.setGeometry(0, 480, 800, 100)
        self.contactLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.contactLabel.setAlignment(Qt.AlignHCenter)
        self.contactLabel.setFont(QFont("Microsoft Sans Serif", 18, QFont.Bold))

        self.contactLabel2 = QLabel("Grupo de Sensores Integráveis e Microssistemas do PSI-EPUSP", self)
        self.contactLabel2.setGeometry(0, 510, 800, 100)
        self.contactLabel2.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.contactLabel2.setAlignment(Qt.AlignHCenter)
        self.contactLabel2.setFont(QFont("Microsoft Sans Serif", 16))

        self.contactLabel3 = QLabel("gsim@usp.br", self)
        self.contactLabel3.setGeometry(0, 540, 800, 30)
        self.contactLabel3.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.contactLabel3.setAlignment(Qt.AlignHCenter)
        font = QFont("Microsoft Sans Serif", 16)
        font.setItalic(True)
        self.contactLabel3.setFont(font)

        self.siteLabel = QLabel("Site", self)
        self.siteLabel.setGeometry(0, 580, 800, 100)
        self.siteLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.siteLabel.setAlignment(Qt.AlignHCenter)
        self.siteLabel.setFont(QFont("Microsoft Sans Serif", 18, QFont.Bold))

        self.siteURLLabel = QLabel("myoscilloscope.lme.usp.br", self)
        self.siteURLLabel.setGeometry(0, 610, 800, 30)
        self.siteURLLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.siteURLLabel.setAlignment(Qt.AlignHCenter)
        font = QFont("Microsoft Sans Serif", 16)
        font.setItalic(True)
        self.siteURLLabel.setFont(font)

        self.USP_Logo = QLabel("", self)
        self.Poli_Logo = QLabel("", self)
        self.USP_Logo.setGeometry(20, 570, 170, 100)
        self.Poli_Logo.setGeometry(660, 550, 180, 130)


        USPImage = QPixmap("images/USPLogo")
        scaled_USPImage = USPImage.scaled(
            self.USP_Logo.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.USP_Logo.setPixmap(scaled_USPImage)

        PoliImage = QPixmap("images/PoliLogo")
        scaled_PoliImage = PoliImage.scaled(
            self.Poli_Logo.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.Poli_Logo.setPixmap(scaled_PoliImage)


        self.OKButton = Button(self, 315, 660, 200, 30, "OK",
                                    "images/Bt_OK.png", "images/Bt_OK.png",  False)
        self.OKButton.clicked.connect(self.closeWindow)


        

    def setLanguage(self):
        if self.language == "Português":
            self.setWindowTitle("Créditos")
            self.versionLabel.setText(f"Versão {self.version}")
            self.authorLabel.setText("Autor")
            self.supervisorsLabel.setText("Sob a orientação de")
            self.supervisorsNamesLabel.setText("Profa. Dra. Elisabete Galeazzo" +
                                            "\nDr. Henrique Estanislau Maldonado Peres" +
                                            "\nMs. Mauricio Oscar Perez Lisboa")
            self.contactLabel.setText("Contato")

        else:
            self.setWindowTitle("Credits")
            self.versionLabel.setText(f"Version {self.version}")
            self.authorLabel.setText("Author")
            self.supervisorsLabel.setText("Under the supervision of")
            self.supervisorsNamesLabel.setText("Elisabete Galeazzo, Ph.D." +
                                            "\nHenrique Estanislau Maldonado Peres, Ph.D." +
                                            "\nMauricio Oscar Perez Lisboa, M.Sc.")
            self.contactLabel.setText("Contact")


    def closeWindow(self):
        self.close()

class CaptureScreen(QDialog):
    """ Pendente: ajustar para que a posição da janela seja o centro da tela de qualquer resolução"""

    def __init__(self, language, time, directory, mode):
        super(CaptureScreen, self).__init__()
        self.captureTime = time
        self.captureDirectory = directory
        self.mode = mode
        self.setGeometry(400, 350, 350, 130)
        self.setFixedSize(350, 130)
        self.setWindowTitle("Export")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        #Para deixar a janela no centro da tela:
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())
        
        if self.mode == "Image":
            self.mainLabel = QLabel(f"The Export Image has created a .png archive. \n"
                                    f"Date and Time: {self.captureTime}\nDirectory: {self.captureDirectory}", self)
            if language == "Português":
                self.mainLabel.setText(f"O Export Image criou um arquivo .png. \n"
                                    f"Data e Hora: {self.captureTime}\nDiretório: {self.captureDirectory}")
        else:
            self.mainLabel = QLabel(f"The Export Data has created a .csv archive. \n"
                                    f"Date and Time: {self.captureTime}\nDirectory: {self.captureDirectory}", self)
            if language == "Português":
                self.mainLabel.setText(f"O Export Data criou um arquivo .csv. \n"
                                    f"Data e Hora: {self.captureTime}\nDiretório: {self.captureDirectory}")
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mainLabel.setGeometry(0, 10, 350, 130)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainLabel.setFont(QFont("Microsoft Sans Serif", 11))
        self.mainLabel.setWordWrap(True)
        self.OKButton = Button(self, 100, 90, 410, 30, "",
                                    "images/Bt_OK.png", "images/Bt_OK.png",  False)
        self.OKButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()

if __name__ == '__main__':
    app = QApplication([])
    window = CaptureScreen("English", "aa", "bb", "Image")
    window.show()
    app.exec()