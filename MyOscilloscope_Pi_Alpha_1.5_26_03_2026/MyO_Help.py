from PySide6.QtWidgets import QApplication, QDialog, QLabel, QComboBox, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QSpinBox
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QFont, QPainter, QPolygon, QColor, QPixmap
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QFont
from button import Button

#Botão personalizado com seta de esquerda ou direita
class ArrowButton(QPushButton):
    def __init__(self, direction="left"):
        super().__init__()
        self.direction = direction
        self.setFixedWidth(30)
        self.setMinimumHeight(30)
        self.setCursor(Qt.PointingHandCursor)
        self.setAutoDefault(False)
        self.setDefault(False)

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        color = QColor(0, 255, 120) if self.isDown() else QColor(220, 220, 220)
        painter.setBrush(color)
        painter.setPen(Qt.NoPen)

        w = self.width()
        h = self.height()

        if self.direction == "left":
            points = [
                QPoint(int(w*0.65), int(h*0.25)),
                QPoint(int(w*0.35), int(h*0.5)),
                QPoint(int(w*0.65), int(h*0.75)),
            ]
        else:  # right
            points = [
                QPoint(int(w*0.35), int(h*0.25)),
                QPoint(int(w*0.65), int(h*0.5)),
                QPoint(int(w*0.35), int(h*0.75)),
            ]

        painter.drawPolygon(QPolygon(points))

class ArrowSpinBox(QWidget):
    def __init__(self, label_text=""):
        super().__init__()

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(5)

        self.label = QLabel(label_text)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""color: rgb(220,220,220);
                                    background-color: transparent""")
        self.label.setFont(QFont("Segoe UI", 10))
        main_layout.addWidget(self.label)

        layout = QHBoxLayout()
        layout.setSpacing(0)

        self.minus_btn = ArrowButton("left")
        self.spin = QSpinBox()
        self.spin.setButtonSymbols(QSpinBox.NoButtons)
        self.spin.setRange(1, 33)
        self.spin.setValue(1)
        self.spin.setAlignment(Qt.AlignCenter)

        self.plus_btn = ArrowButton("right")

        layout.addWidget(self.minus_btn)
        layout.addWidget(self.spin)
        layout.addWidget(self.plus_btn)

        main_layout.addLayout(layout)

        self.minus_btn.clicked.connect(self.spin.stepDown)
        self.plus_btn.clicked.connect(self.spin.stepUp)

        self.setStyleSheet("""
            QWidget {
                background-color: rgb(30, 30, 30);
            }

            QSpinBox {
                background-color: rgb(15, 15, 15);
                color: rgb(200, 200, 200);
                border: 2px solid rgb(60, 60, 60);
                font-size: 16px;
                padding: 6px;
            }

            QPushButton {
                background-color: rgb(50, 50, 50);
                border: 2px solid rgb(80, 80, 80);
            }

            QPushButton:pressed {
                background-color: rgb(0, 70, 120);
                border: 2px solid rgb(0, 120, 255);
            }
        """)



class HelpScreen(QDialog):
    def __init__(self ):
        super(HelpScreen, self).__init__()
        self.setGeometry(5, 240, 800, 465)  
        #self.setFixedSize(800, 465)
        self.setWindowTitle("Help")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.language = "English"

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

        self.supportBarLabel = QLabel("", self)
        self.supportBarLabel.setGeometry(0, 405, 800, 60)
        self.supportBarLabel.setStyleSheet("background-color: rgb(30, 30, 30)")

        self.sectionLabel = QLabel("Ir para seção: ", self)
        self.sectionLabel.setGeometry(75, 410, 151, 20)
        self.sectionLabel.setStyleSheet(""" color: rgb(240, 240, 240);
                                            background-color: transparent; """)
        self.sectionLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.sectionLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.sectionCB = QComboBox(self)
        self.sectionCB.setGeometry(75, 430, 151, 25)
        self.sectionCB.setStyleSheet("""background-color: rgb(36, 36, 36); 
                                                                            color: rgb(240, 240, 240)""")

        self.sectionCBItems = ["Tela Inicial", "Introdução", "Acoplamento DC e AC", "Conexão do Circuito", "Fonte de Tensão", "Calibração", "Funcionalidades Principais",
                               "Funcionalidades de Apoio", "Final"]

        self.sectionCB.addItems(self.sectionCBItems)

        self.sectionCB.currentIndexChanged.connect(self.sectionCBChanged)

        self.pageChangerContainer = QWidget(self)
        self.pageChangerContainer.setGeometry(600, 390, 160, 90)
        self.pageChangerContainer.setStyleSheet("background-color: transparent;")

        layout = QVBoxLayout(self.pageChangerContainer)
        layout.addStretch()

        self.instrument_spin = ArrowSpinBox("Página")
        layout.addWidget(self.instrument_spin)
        layout.addStretch()
        self.instrument_spin.spin.valueChanged.connect(self.changePage)


        #inicialização das páginas
        self.page1 = Help_MainScreen()
        self.page2 = Help_Intro_1()
        self.page3 = Help_Intro_2()
        self.page4 = Help_Intro_3()
        self.page5 = Help_Intro_4()
        self.page6 = Help_Intro_5()
        self.page7 = AcoplDCAC_1()
        self.page8 = AcoplDCAC_2()
        self.page9 = ConexProtob_1()
        self.page10 = ConexProtob_2()
        self.page11 = ConexProtob_3()
        self.page12 = Fonte_1()
        self.page13 = Fonte_2()
        self.page14 = Fonte_3()
        self.page15 = Fonte_4()
        self.page16 = Fonte_5()
        self.page17 = Fonte_6()
        self.page18 = Help_Calibration()
        self.page19 = FunctionalitiesI_1()
        self.page20 = FunctionalitiesI_2()
        self.page21 = FunctionalitiesI_3()
        self.page22 = FunctionalitiesI_4()
        self.page23 = FunctionalitiesI_5()
        self.page24 = FunctionalitiesI_6()
        self.page25 = FunctionalitiesI_7()
        self.page26 = FunctionalitiesI_8()
        self.page27 = FunctionalitiesI_9()
        self.page28 = FunctionalitiesI_10()
        self.page29 = FunctionalitiesII_1()
        self.page30 = FunctionalitiesII_2()
        self.page31 = FunctionalitiesII_3()
        self.page32 = Final_1()
        self.page33 = Final_2()




        self.HelpPages = QtWidgets.QWidget(self)
        self.HelpPagesStack = QtWidgets.QStackedWidget()

        self.HelpPagesStack.addWidget(self.page1)
        self.HelpPagesStack.addWidget(self.page2)
        self.HelpPagesStack.addWidget(self.page3)
        self.HelpPagesStack.addWidget(self.page4)
        self.HelpPagesStack.addWidget(self.page5)
        self.HelpPagesStack.addWidget(self.page6)
        self.HelpPagesStack.addWidget(self.page7)
        self.HelpPagesStack.addWidget(self.page8)
        self.HelpPagesStack.addWidget(self.page9)
        self.HelpPagesStack.addWidget(self.page10)
        self.HelpPagesStack.addWidget(self.page11)
        self.HelpPagesStack.addWidget(self.page12)
        self.HelpPagesStack.addWidget(self.page13)
        self.HelpPagesStack.addWidget(self.page14)
        self.HelpPagesStack.addWidget(self.page15)
        self.HelpPagesStack.addWidget(self.page16)
        self.HelpPagesStack.addWidget(self.page17)
        self.HelpPagesStack.addWidget(self.page18)
        self.HelpPagesStack.addWidget(self.page19)
        self.HelpPagesStack.addWidget(self.page20)
        self.HelpPagesStack.addWidget(self.page21)
        self.HelpPagesStack.addWidget(self.page22)
        self.HelpPagesStack.addWidget(self.page23)
        self.HelpPagesStack.addWidget(self.page24)
        self.HelpPagesStack.addWidget(self.page25)
        self.HelpPagesStack.addWidget(self.page26)
        self.HelpPagesStack.addWidget(self.page27)
        self.HelpPagesStack.addWidget(self.page28)
        self.HelpPagesStack.addWidget(self.page29)
        self.HelpPagesStack.addWidget(self.page30)
        self.HelpPagesStack.addWidget(self.page31)
        self.HelpPagesStack.addWidget(self.page32)
        self.HelpPagesStack.addWidget(self.page33)

        helpPages_layout = QVBoxLayout(self.HelpPages)
        helpPages_layout.setContentsMargins(0, 0, 0, 0)
        helpPages_layout.setSpacing(0)
        helpPages_layout.addWidget(self.HelpPagesStack)

        self.HelpPages.setGeometry(0, 0, 800, 405)

    def changePage(self, page):
        self.HelpPagesStack.setCurrentIndex(page - 1) #a página inicial é o índice 0 da stack

        if   page == 1: self.sectionCB.setCurrentIndex(0)
        elif page == 2: self.sectionCB.setCurrentIndex(1)
        elif page == 7: self.sectionCB.setCurrentIndex(2)
        elif page == 9: self.sectionCB.setCurrentIndex(3)
        elif page == 12: self.sectionCB.setCurrentIndex(4)
        elif page == 18: self.sectionCB.setCurrentIndex(5)
        elif page == 19: self.sectionCB.setCurrentIndex(6)
        elif page == 29: self.sectionCB.setCurrentIndex(7)
        elif page == 32: self.sectionCB.setCurrentIndex(8)

    def sectionCBChanged(self):
        section = self.sectionCB.currentIndex()
        if   section == 0: self.instrument_spin.spin.lineEdit().setText("1") 
        elif section == 1: self.instrument_spin.spin.lineEdit().setText("2") 
        elif section == 2: self.instrument_spin.spin.lineEdit().setText("7") 
        elif section == 3: self.instrument_spin.spin.lineEdit().setText("9") 
        elif section == 4: self.instrument_spin.spin.lineEdit().setText("12") 
        elif section == 5: self.instrument_spin.spin.lineEdit().setText("18") 
        elif section == 6: self.instrument_spin.spin.lineEdit().setText("19") 
        elif section == 7: self.instrument_spin.spin.lineEdit().setText("29") 
        elif section == 8: self.instrument_spin.spin.lineEdit().setText("32") 


        

    def closeWindow(self):
        self.close()

class Help_MainScreen(QDialog):
    def __init__(self ):
        super(Help_MainScreen, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Help - Main Screen")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(0, 20, 800, 300)
        self.imageLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
        """)
        self.imagePixmap = QPixmap("images/UserHelp/mainImage.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

        self.label1 = QLabel("Bem-vindo(a) à seção de apoio ao usuário do MyOscilloscope! Navegue pelas páginas a seguir e " + ""
                             "encontre instruções sobre o uso do kit e da interface.", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(5, 330, 790, 100)

class Help_Intro_1(QDialog):
    def __init__(self ):
        super(Help_Intro_1, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Help_Intro_1")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Introdução", self)
        self.titleLabel.setGeometry(280, 10, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 36))


        self.label1 = QLabel("O MyOscilloscope é um projeto pensado para auxiliar os alunos e entusiastas no aprendizado de Circuitos Elétricos. Para isso, há um trabalho em conjunto entre o kit (hardware) e a interface gráfica.", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(5, 330, 790, 100)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(60, 100, 660, 220)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/Help_Intro_1.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)


class Help_Intro_2(QDialog):
    def __init__(self ):
        super(Help_Intro_2, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Help_Intro_2")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Introdução", self)
        self.titleLabel.setGeometry(280, 10, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 36))


        self.label1 = QLabel("O kit MyOscilloscope contém um shield, ou seja, uma placa de circuito impresso com circuitos dedicados ao condicionamento de sinais, projetada para operar em conjunto com um microcontrolador.", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 14))
        self.label1.setGeometry(70, 150, 260, 200)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(380, 100, 370, 280)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)

        self.imagePixmap = QPixmap("images/UserHelp/Help_Intro_2.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

class Help_Intro_3(QDialog):
    def __init__(self ):
        super(Help_Intro_3, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Help_Intro_3")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Introdução", self)
        self.titleLabel.setGeometry(280, 10, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 36))


        self.label1 = QLabel("O kit também inclui jumpers avulsos, uma protoboard e componentes para montagem de circuitos, permitindo a realização de experimentos de forma semelhante à de um laboratório didático.", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 14))
        self.label1.setGeometry(480, 150, 260, 200)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(20, 100, 420, 280)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)

        self.imagePixmap = QPixmap("images/UserHelp/Help_Intro_3.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

class Help_Intro_4(QDialog):
    def __init__(self ):
        super(Help_Intro_4, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Help_Intro_4")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Introdução", self)
        self.titleLabel.setGeometry(280, 10, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 36))


        self.label1 = QLabel("De início, conecte o cabo USB entre o seu PC e o microcontrolador. Caso a interface não reconheça o shield em nenhuma porta COM, clique em Search (tela ‘COM Port’) para realizar uma nova busca.", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 14))
        self.label1.setGeometry(70, 150, 260, 200)

        self.imageLabel1 = QLabel("", self)
        self.imageLabel1.setGeometry(520, 70, 190, 187)
        self.imageLabel1.setStyleSheet("""
            background-color: transparent;
        """)

        self.imageLabel2 = QLabel("", self)
        self.imageLabel2.setGeometry(470, 260, 300, 147)
        self.imageLabel2.setStyleSheet("""
            background-color: rgb(50, 240, 50);
        """)

        self.imagePixmap1 = QPixmap("images/UserHelp/Help_Intro_4_1.png")
        scaled_imagePixmap1 = self.imagePixmap1.scaled(
            self.imageLabel1.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel1.setPixmap(scaled_imagePixmap1)

        self.imagePixmap2 = QPixmap("images/UserHelp/Help_Intro_4_2.png")
        scaled_imagePixmap2 = self.imagePixmap2.scaled(
            self.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel2.setPixmap(scaled_imagePixmap2)

class Help_Intro_5(QDialog):
    def __init__(self ):
        super(Help_Intro_5, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Help_Intro_5")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Introdução", self)
        self.titleLabel.setGeometry(280, 10, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 36))


        self.label1 = QLabel("Monte o circuito na protoboard. Defina um dos nós como referência (GND). Em seguida, escolha o nó a ser observado no canal 1 (CH1) do osciloscópio e o nó a ser observado no canal 2 (CH2).", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(5, 80, 790, 100)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(250, 150, 285, 250)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/Help_Intro_5.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

        self.sourceLabel = QLabel("Fonte: [1]", self)
        self.sourceLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sourceLabel.setAlignment(Qt.AlignHCenter)
        self.sourceLabel.setFont(QFont("Microsoft Sans Serif", 9))
        self.sourceLabel.setGeometry(550, 380, 60, 40)

class AcoplDCAC_1(QDialog):
    def __init__(self ):
        super(AcoplDCAC_1, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("AcoplDCAC_1")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Acoplamento DC e AC", self)
        self.titleLabel.setGeometry(280, 10, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 32))


        self.label1 = QLabel("Conforme será visto mais adiante, um sinal elétrico pode ser separado em duas partes: uma componente DC e uma componente AC. Quando somadas, essas duas partes formam o sinal observado.\n\nVeremos que um sinal pode ser decomposto em várias componentes. A componente de frequência zero (nula) é chamada de componente DC, enquanto todas as outras possuem frequência diferente de zero.", self)

        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(70, 80, 260, 320)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(380, 100, 400, 240)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)

        self.imagePixmap = QPixmap("images/UserHelp/AcoplDCAC_1.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

        self.sourceLabel = QLabel("Fonte: [2]", self)
        self.sourceLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sourceLabel.setAlignment(Qt.AlignHCenter)
        self.sourceLabel.setFont(QFont("Microsoft Sans Serif", 9))
        self.sourceLabel.setGeometry(720, 350, 60, 40)

class AcoplDCAC_2(QDialog):
    def __init__(self ):
        super(AcoplDCAC_2, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("AcoplDCAC_2")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Acoplamento DC e AC", self)
        self.titleLabel.setGeometry(280, 10, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 32))


        self.label1 = QLabel("Os osciloscópios permitem escolher se o componente DC do sinal será exibido ou não. No MyOscilloscope, isso é feito pela forma como a ponta de prova é conectada ao circuito.\nNo canal 1, há duas opções: AC1, que remove o componente DC, e DC1, que mostra o sinal completo (AC + DC). O mesmo vale para o canal 2, com as entradas AC2 e DC2. ", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        #self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(5, 70, 790, 100)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(250, 160, 270, 200)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/AcoplDCAC_2.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

        self.label2 = QLabel("Atenção: é necessário conectar um jumper entre o canal de referência do circuito montado e as entradas GND do shield, indicadas na imagem.", self)
        self.label2.setWordWrap(True)
        self.label2.setStyleSheet(""" color: rgb(240, 240, 240); 
                                      background-color: transparent;""")
        #self.label2.setAlignment(Qt.AlignHCenter)
        self.label2.setFont(QFont("Microsoft Sans Serif", 12))
        self.label2.setGeometry(5, 330, 790, 100)

class ConexProtob_1(QDialog):
    def __init__(self ):
        super(ConexProtob_1, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("ConexProtob_1")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Conexão do circuito em protoboard\ncom o shield", self)
        self.titleLabel.setGeometry(280, 5, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 20))


        self.label1 = QLabel("A imagem mostra um esquema de como realizar a conexão do circuito na protoboard com o shield, utilizando os dois canais em acoplamento DC.", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(5, 80, 790, 100)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(120, 140, 550, 250)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/ConexProtob_1.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)


class ConexProtob_2(QDialog):
    def __init__(self ):
        super(ConexProtob_2, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("ConexProtob_2")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Conexão do circuito em protoboard\ncom o shield", self)
        self.titleLabel.setGeometry(280, 5, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 20))


        self.label1 = QLabel("A imagem mostra um esquema de como realizar a conexão do circuito na protoboard com o shield, utilizando os dois canais em acoplamento AC.", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(5, 80, 790, 100)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(120, 140, 550, 250)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/ConexProtob_2.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

class ConexProtob_3(QDialog):
    def __init__(self ):
        super(ConexProtob_3, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("ConexProtob_3")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Conexão do circuito em protoboard\ncom o shield", self)
        self.titleLabel.setGeometry(280, 5, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 20))


        self.label1 = QLabel("• Não é necessário que ambos os canais estejam no modo AC ou ambos estejam no modo DC. \n\n•A tensão observada é aquela obtida em relação à tensão do nó de referência, que está conectado às entradas GND do shield. Isso significa que alterar o canal de referência pode causar resultados diferentes, pois muda-se a referência de tensão. ", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 16))
        self.label1.setGeometry(5, 150, 790, 300)

class Fonte_1(QDialog):
    def __init__(self ):
        super(Fonte_1, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Fonte_1")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("A fonte de tensão do MyOscilloscope", self)
        self.titleLabel.setGeometry(280, 10, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 20))


        self.label1 = QLabel("Para alimentar o circuito em estudo, o MyOscilloscope dispõe de um cabo especial que trabalha em conjunto com o gerador de forma de onda da interface.", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 14))
        self.label1.setGeometry(70, 80, 650, 100)

        self.imageLabel1 = QLabel("", self)
        self.imageLabel1.setGeometry(60, 180, 225, 187)
        self.imageLabel1.setStyleSheet("""
            background-color: transparent;
        """)

        self.imageLabel2 = QLabel("", self)
        self.imageLabel2.setGeometry(340, 210, 440, 100)
        self.imageLabel2.setStyleSheet("""
            background-color: rgb(50, 240, 50);
        """)

        self.imagePixmap1 = QPixmap("images/UserHelp/Fonte_1_1.png")
        scaled_imagePixmap1 = self.imagePixmap1.scaled(
            self.imageLabel1.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel1.setPixmap(scaled_imagePixmap1)

        self.imagePixmap2 = QPixmap("images/UserHelp/Fonte_1_2.png")
        scaled_imagePixmap2 = self.imagePixmap2.scaled(
            self.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel2.setPixmap(scaled_imagePixmap2)

class Fonte_2(QDialog):
    def __init__(self ):
        super(Fonte_2, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Fonte_2")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("A fonte de tensão do MyOscilloscope", self)
        self.titleLabel.setGeometry(280, 10, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 20))


        self.label1 = QLabel("O tal cabo especial apresenta, em uma de suas extremidades, um conector de áudio P2, para ser conectado à saída de áudio do PC. Na outra extremidade, há três jumpers. Dois deles possuem cores sortidas, e o terceiro apresenta cor preta. ", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 14))
        self.label1.setGeometry(460, 120, 260, 200)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(40, 100, 310, 260)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)

        self.imagePixmap = QPixmap("images/UserHelp/Fonte_1_1.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

class Fonte_3(QDialog):
    def __init__(self ):
        super(Fonte_3, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Fonte_3")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("A fonte de tensão do MyOscilloscope", self)
        self.titleLabel.setGeometry(280, 10, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 20))


        self.label1 = QLabel("Os dois jumpers coloridos representam a parte de maior potencial (geralmente associada à cor vermelha nos laboratórios) da fonte de tensão, enquanto o jumper preto apresenta a de menor potencial (geralmente associada à cor preta).", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 14))
        self.label1.setGeometry(60, 120, 260, 200)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(460, 75, 165, 320)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)

        self.imagePixmap = QPixmap("images/UserHelp/Fonte_3.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

class Fonte_4(QDialog):
    def __init__(self ):
        super(Fonte_4, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Fonte_4")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("A fonte de tensão do MyOscilloscope", self)
        self.titleLabel.setGeometry(280, 10, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 20))


        self.label1 = QLabel("• Algumas aplicações podem usar os dois jumpers de cores sortidas. Não os coloque em curto, " + 
                             "em hipótese nenhuma. Com o gerador de forma de onda ativado, um curto-circuito pode ser causado, " + 
                             "o que pode causar danos ao kit, ao circuito montado e ao PC do usuário. Salvo quando mencionado, " + 
                             "considere usar um dos jumpers de cor sortida e deixar o outro fora do circuito. " +
                             "\n\n• Assim como no laboratório, também não coloque os dois terminais da fonte de tensão em curto. " +
                             "Ou seja, nunca conecte nenhum jumper do cabo da imagem ao lado entre si.", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 14))
        self.label1.setGeometry(300, 90, 450, 400)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(60, 75, 165, 320)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)

        self.imagePixmap = QPixmap("images/UserHelp/Fonte_4.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

class Fonte_5(QDialog):
    def __init__(self ):
        super(Fonte_5, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Fonte_5")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("A fonte de tensão do MyOscilloscope", self)
        self.titleLabel.setGeometry(280, 10, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 20))


        self.label1 = QLabel("O esquema a seguir mostra como conectar os componentes do circuito, incluindo o cabo de alimentação.", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(5, 80, 790, 100)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(130, 130, 510, 270)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/Fonte_5.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

class Fonte_6(QDialog):
    def __init__(self ):
        super(Fonte_6, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Fonte_6")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Waveform Generator", self)
        self.titleLabel.setGeometry(280, 10, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 28))


        self.label1 = QLabel("• O MyOscilloscope apresenta gerador de forma de onda próprio. Nele, pode-se ajustar o tipo de onda gerada, sua frequência e sua amplitude." +
                             "\n\n\n\n\n\n\n\n\n\n" + 
                             "• O botão com um ‘?’ apresenta algumas instruções adicionais sobre como o Waveform Generator funciona. Vale a pena conferir.", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(5, 110, 790, 400)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(130, 170, 510, 115)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/Fonte_1_2.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

class Help_Calibration(QDialog):
    def __init__(self ):
        super(Help_Calibration, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Help_Calibration")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Calibração", self)
        self.titleLabel.setGeometry(280, 10, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 28))


        self.label1 = QLabel("•Antes de realizar medições com o MyOscilloscope, é importante que o kit esteja calibrado em relação ao PC do usuário. Há duas formas de realizar tais ajustes:" +
                             "\n\n1) Calibração Manual, para usuários que apresentam conhecimento sobre o procedimento;" + 
                             "\n\n2) Calibração assistida, com um passo-a-passo para uma boa calibração.", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(5, 110, 790, 400)

        self.imageLabel1 = QLabel("", self)
        self.imageLabel1.setGeometry(200, 240, 423, 110)
        self.imageLabel1.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap1 = QPixmap("images/UserHelp/Calibration_1.png")
        scaled_imagePixmap1 = self.imagePixmap1.scaled(
            self.imageLabel1.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel1.setPixmap(scaled_imagePixmap1)

        self.imageLabel2 = QLabel("", self)
        self.imageLabel2.setGeometry(0, 340, 360, 55)
        self.imageLabel2.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap2 = QPixmap("images/UserHelp/Calibration_2.png")
        scaled_imagePixmap2 = self.imagePixmap2.scaled(
            self.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel2.setPixmap(scaled_imagePixmap2)

        self.imageLabel3 = QLabel("", self)
        self.imageLabel3.setGeometry(500, 320, 510, 115)
        self.imageLabel3.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap3 = QPixmap("images/calibWizard.png")
        scaled_imagePixmap3 = self.imagePixmap3.scaled(
            self.imageLabel3.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel3.setPixmap(scaled_imagePixmap3)

class FunctionalitiesI_1(QDialog):
    def __init__(self ):
        super(FunctionalitiesI_1, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("FunctionalitiesI_1")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Introdução às funcionalidades\ndo MyOscilloscope", self)
        self.titleLabel.setGeometry(280, 5, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 20))


        self.label1 = QLabel("As funcionalidades principais do MyOscilloscope, associadas aos botões do campo superior esquerdo da interface, serão apresentadas a seguir.", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(5, 80, 790, 100)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(0, 200, 800, 135)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/FunctionalitiesI_1.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

class FunctionalitiesI_2(QDialog):
    def __init__(self ):
        super(FunctionalitiesI_2, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("FunctionalitiesI_2")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Main", self)
        self.titleLabel.setGeometry(280, 5, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 40))


        self.label1 = QLabel("Permite a exibição do sinal no domínio do tempo. Com os knobs presentes à direita na interface, " + 
                             "pode-se alterar a escala horizontal (Time), escala vertical (V/div ou A/div) e a posição do ponto " + 
                             "médio (Position) de cada canal." + 
                             "\n\n\n\n\n\n\n\n\n\n\n\n\n" + 
                             "Sua tela auxiliar possui várias aplicações e será mencionada em breve.", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(5, 80, 790, 400)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(210, 150, 345, 200)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/FunctionalitiesI_2.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

class FunctionalitiesI_3(QDialog):
    def __init__(self ):
        super(FunctionalitiesI_3, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("FunctionalitiesI_3")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("FFT", self)
        self.titleLabel.setGeometry(280, 5, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 40))


        self.label1 = QLabel("FFT vem de Fast Fourier Transform,  ou Transformada Rápida de Fourier. Consiste na ideia " + 
                             "de que sinais podem ser representados como somas de senoides de amplitudes e frequências " + 
                             "distintas, inclusive frequência nula (componente DC). Esta seção permite a exibição do sinal " + 
                             "no domínio da frequência. ", self)
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(5, 80, 790, 400)

        self.label2 = QLabel("Sua tela auxiliar apresenta duas páginas: " +
                             "\n\n• Página 1: permite alterar os valores-limite exibidos em cada eixo. " +
                             "\n\n• Página 2: exibe as maiores amplitudes dentre os pares frequência-amplitude de cada canal. ", self)
        self.label2.setWordWrap(True)
        self.label2.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label2.setAlignment(Qt.AlignHCenter)
        self.label2.setFont(QFont("Microsoft Sans Serif", 12))
        self.label2.setGeometry(430, 210, 350, 400)

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(10, 190, 410, 200)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/FunctionalitiesI_3.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

class FunctionalitiesI_4(QDialog):
    def __init__(self ):
        super(FunctionalitiesI_4, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("FunctionalitiesI_4")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Frequency Response", self)
        self.titleLabel.setGeometry(280, 5, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 32))


        self.label1 = QLabel("Permite definir a curva de resposta em frequência do circuito em estudo (sweep).  Nas telas " + 
                             "auxiliares, apresenta:\n"+
"\n• Definição do número de pontos da curva a ser criada e limites de frequência;" + 
"\n• Botões para início, pausa e fim do sweep;"+
"\n• Alteração dos canais associados na função resposta em frequência;"+
"\n• Alteração do gráfico exibido na tela, entre módulo e fase;"+
"\n• Cor da curva a ser criada;"+
"\n• Remoção das curvas criadas na tela;"+
"\n• Ajuste dos limites observados.", self)
        
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(5, 80, 340, 400)



        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(500, 90, 250, 243)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/FunctionalitiesI_4_1.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

        self.imageLabel2 = QLabel("", self)
        self.imageLabel2.setGeometry(520, 340, 220, 55)
        self.imageLabel2.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap2 = QPixmap("images/UserHelp/FunctionalitiesI_4_2.png")
        scaled_imagePixmap2 = self.imagePixmap2.scaled(
            self.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel2.setPixmap(scaled_imagePixmap2)

class FunctionalitiesI_5(QDialog):
    def __init__(self ):
        super(FunctionalitiesI_5, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("FunctionalitiesI_5")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Phasor Diagram & Lissajous", self)
        self.titleLabel.setGeometry(280, 5, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 24))


        self.label1 = QLabel("O Diagrama Fasorial exibe os fasores de cada canal no plano complexo. Sua tela auxiliar exibe " + 
                             "a fase e magnitude de cada fasor. É possível ajustar o tipo de tensão associada às magnitudes " + 
                             "dos fasores.", self)
        
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(250, 120, 340, 400)

        self.label2 = QLabel("A figura de Lissajous exibe uma parametrização baseada em dois canais selecionáveis entre CH1, CH2 " + 
                             "e Math. Sua tela auxiliar permite tal seleção. Ambas as telas auxiliares permitem exibir " + 
                             "suas respectivas funcionalidades de maneira isolada.", self)
        
        self.label2.setWordWrap(True)
        self.label2.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label2.setAlignment(Qt.AlignHCenter)
        self.label2.setFont(QFont("Microsoft Sans Serif", 12))
        self.label2.setGeometry(230, 270, 340, 400)



        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(50, 90, 160, 175)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/FunctionalitiesI_5_1.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

        self.imageLabel2 = QLabel("", self)
        self.imageLabel2.setGeometry(600, 230, 160, 175)
        self.imageLabel2.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap2 = QPixmap("images/UserHelp/FunctionalitiesI_5_2.png")
        scaled_imagePixmap2 = self.imagePixmap2.scaled(
            self.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel2.setPixmap(scaled_imagePixmap2)

class FunctionalitiesI_6(QDialog):
    def __init__(self ):
        super(FunctionalitiesI_6, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("FunctionalitiesI_6")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Funcionalidades da tela auxiliar de Main:\nJumpers de Atenuação", self)
        self.titleLabel.setGeometry(280, 5, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 20))


        self.label1 = QLabel("O Arduino Uno, utilizado no kit, permite medir sinais entre aproximadamente − 3 V e + 3 V quando usado com o shield. O shield possui jumpers de atenuação que, ao serem removidos, permitem medir sinais com até cinco vezes mais amplitude. Nesse caso, é importante ajustar o fator de atenuação do canal correspondente, para que a leitura continue correta.", self)
        
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(5, 90, 800, 400)


        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(50, 200, 220, 175)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/FunctionalitiesI_6_1.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

        self.imageLabel2 = QLabel("", self)
        self.imageLabel2.setGeometry(500, 200, 220, 175)
        self.imageLabel2.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap2 = QPixmap("images/UserHelp/FunctionalitiesI_6_2.png")
        scaled_imagePixmap2 = self.imagePixmap2.scaled(
            self.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel2.setPixmap(scaled_imagePixmap2)

class FunctionalitiesI_7(QDialog):
    def __init__(self ):
        super(FunctionalitiesI_7, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("FunctionalitiesI_7")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Funcionalidades da tela auxiliar de Main:\nAlteração da escala vertical", self)
        self.titleLabel.setGeometry(280, 5, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 20))


        self.label1 = QLabel("Quando a tensão medida em um dos canais corresponde à queda de tensão em um resistor, é possível, pela Lei de Ohm, utilizar esse canal como um amperímetro. Para isso, ative a funcionalidade no canal desejado e informe o valor do resistor (atuará como resistor shunt). Assim, o sinal exibido passará a representar a corrente, e os valores serão mostrados em amperes/div.", self)
        
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(0, 90, 800, 400)


        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(80, 185, 125, 200)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/FunctionalitiesI_7_1.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

        self.imageLabel2 = QLabel("", self)
        self.imageLabel2.setGeometry(500, 185, 280, 120)
        self.imageLabel2.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap2 = QPixmap("images/UserHelp/FunctionalitiesI_7_2.png")
        scaled_imagePixmap2 = self.imagePixmap2.scaled(
            self.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel2.setPixmap(scaled_imagePixmap2)

        self.imageLabel3 = QLabel("", self)
        self.imageLabel3.setGeometry(500, 310, 280, 50)
        self.imageLabel3.setStyleSheet("""
            background-color: rgb(50, 150, 240);
        """)
        self.imagePixmap3 = QPixmap("images/UserHelp/FunctionalitiesI_7_3.png")
        scaled_imagePixmap3 = self.imagePixmap3.scaled(
            self.imageLabel3.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel3.setPixmap(scaled_imagePixmap3)

class FunctionalitiesI_8(QDialog):
    def __init__(self ):
        super(FunctionalitiesI_8, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("FunctionalitiesI_8")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Funcionalidades da tela auxiliar de Main\n", self)
        self.titleLabel.setGeometry(280, 5, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 20))


        self.label1 = QLabel("Escala de tempo personalizada: permite definir um valor qualquer para a escala de tempo (Time) entre 0.1 e 50 ms/div. ", self)
        
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(20, 120, 340, 400)

        self.label2 = QLabel("Canal de Referência: define qual canal representa a fase zero ou de referência. Também afeta " + 
                             "os recursos de Trigger, Cursores, Assistente de Calibração e Diagrama Fasorial.", self)
        
        self.label2.setWordWrap(True)
        self.label2.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label2.setAlignment(Qt.AlignHCenter)
        self.label2.setFont(QFont("Microsoft Sans Serif", 12))
        self.label2.setGeometry(370, 250, 340, 400)



        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(500, 90, 170, 120)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/FunctionalitiesI_8_1.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

        self.imageLabel2 = QLabel("", self)
        self.imageLabel2.setGeometry(80, 250, 170, 80)
        self.imageLabel2.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap2 = QPixmap("images/UserHelp/FunctionalitiesI_8_2.png")
        scaled_imagePixmap2 = self.imagePixmap2.scaled(
            self.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel2.setPixmap(scaled_imagePixmap2)

        self.label3 = QLabel("As próximas páginas contém uma explicação adicional sobre como funcionam as escalas.", self)
        
        self.label3.setWordWrap(True)
        self.label3.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label3.setAlignment(Qt.AlignHCenter)
        self.label3.setFont(QFont("Microsoft Sans Serif", 12))
        self.label3.setGeometry(-5, 370, 790, 100)

class FunctionalitiesI_9(QDialog):
    def __init__(self ):
        super(FunctionalitiesI_9, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("FunctionalitiesI_9")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Escalas horizontal e vertical no domínio do tempo:\nExemplo 1", self)
        self.titleLabel.setGeometry(260, 5, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 18))

        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(80, 90, 625, 270)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/FunctionalitiesI_9.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)


class FunctionalitiesI_10(QDialog):
    def __init__(self ):
        super(FunctionalitiesI_10, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("FunctionalitiesI_10")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Escalas horizontal e vertical no domínio do tempo:\nExemplo 2", self)
        self.titleLabel.setGeometry(260, 5, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 18))


        self.label1 = QLabel("Mesmos sinais em cada canal nas duas imagens, escalas alteradas. " + 
                             "Sempre ajuste as escalas corretamente para uma melhor visualização.", self)
        
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(0, 360, 800, 400)



        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(80, 80, 625, 270)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/FunctionalitiesI_10.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

class FunctionalitiesII_1(QDialog):
    def __init__(self ):
        super(FunctionalitiesII_1, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("FunctionalitiesII_1")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Funcionalidades de apoio do MyOscilloscope", self)
        self.titleLabel.setGeometry(220, 15, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 22))


        self.label1 = QLabel("A seguir, um resumo sobre as funções de apoio do MyOscilloscope que, em sua maioria, " + 
                             "são comuns à maioria dos osciloscópios de bancada.", self)
        
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(0, 90, 800, 400)

        self.label2 = QLabel("• Trigger: Permite a sincronização da aquisição e exibição do sinal, " + 
                             "permitindo adequada visualização.", self)
        
        self.label2.setWordWrap(True)
        self.label2.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label2.setAlignment(Qt.AlignHCenter)
        self.label2.setFont(QFont("Microsoft Sans Serif", 12))
        self.label2.setGeometry(430, 200, 350, 400)



        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(20, 150, 400, 200)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/FunctionalitiesII_1.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

class FunctionalitiesII_2(QDialog):
    def __init__(self ):
        super(FunctionalitiesII_2, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("FunctionalitiesII_2")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Funcionalidades de apoio do MyOscilloscope", self)
        self.titleLabel.setGeometry(220, 15, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 22))


        self.label1 = QLabel("• Measure: Exibe medidas importantes dos sinais de cada canal, tais como frequência, período, " + 
                             "valor médio, valores mínimo e máximo, entre outras informações.", self)
        
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(160, 120, 660, 400)

        self.label2 = QLabel("• Cursor: Exibe os cursores, que auxiliam na obtenção de informações do sinal no gráfico ao ajustá-los.", self)
        
        self.label2.setWordWrap(True)
        self.label2.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label2.setAlignment(Qt.AlignHCenter)
        self.label2.setFont(QFont("Microsoft Sans Serif", 12))
        self.label2.setGeometry(190, 215, 350, 400)

        self.label3 = QLabel("• Freeze: Paralisa a atualização dos dados na tela do osciloscópio. ", self)
        
        self.label3.setWordWrap(True)
        self.label3.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label3.setAlignment(Qt.AlignHCenter)
        self.label3.setFont(QFont("Microsoft Sans Serif", 12))
        self.label3.setGeometry(190, 340, 350, 400)



        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(20, 90, 100, 300)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/FunctionalitiesII_2_1.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)


        self.imageLabel2 = QLabel("", self)
        self.imageLabel2.setGeometry(550, 170, 240, 140)
        self.imageLabel2.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap2 = QPixmap("images/UserHelp/FunctionalitiesII_2_2.png")
        scaled_imagePixmap2 = self.imagePixmap2.scaled(
            self.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel2.setPixmap(scaled_imagePixmap2)

        self.imageLabel3 = QLabel("", self)
        self.imageLabel3.setGeometry(550, 320, 220, 70)
        self.imageLabel3.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap3 = QPixmap("images/Bt_Freeze_Chosen.png")
        scaled_imagePixmap3 = self.imagePixmap3.scaled(
            self.imageLabel3.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel3.setPixmap(scaled_imagePixmap3)

class FunctionalitiesII_3(QDialog):
    def __init__(self ):
        super(FunctionalitiesII_3, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("FunctionalitiesII_3")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Funcionalidades de apoio do MyOscilloscope", self)
        self.titleLabel.setGeometry(220, 15, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 22))


        self.label1 = QLabel("• Export: Permite a criação de uma planilha .csv com os dados dos gráficos da interface " + 
                             "(Export Data) ou a criação de um arquivo .png que exibe uma cópia das informações presentes na " + 
                             "tela, bem como a tela principal aberta no momento da captura (Export Image).", self)
        
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(390, 110, 400, 400)

        self.label2 = QLabel("• Math: Permite ajustar a operação associada ao canal Math, para todas as funcionalidades desta " + 
                             "interface, com escolha de operações binárias entre CH1 e CH2.", self)
        
        self.label2.setWordWrap(True)
        self.label2.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label2.setAlignment(Qt.AlignHCenter)
        self.label2.setFont(QFont("Microsoft Sans Serif", 12))
        self.label2.setGeometry(0, 290, 390, 400)



        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(0, 110, 370, 85)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/FunctionalitiesII_3_1.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

        self.imageLabel2 = QLabel("", self)
        self.imageLabel2.setGeometry(430, 290, 370, 85)
        self.imageLabel2.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap2 = QPixmap("images/UserHelp/FunctionalitiesII_3_2.png")
        scaled_imagePixmap2 = self.imagePixmap2.scaled(
            self.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel2.setPixmap(scaled_imagePixmap2)


class Final_1(QDialog):
    def __init__(self ):
        super(Final_1, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Final_1")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.logoLabel = QLabel("", self)
        self.logoLabel.setGeometry(0, 0, 200, 70)
        self.logoLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: transparent;
        """)
        self.logoPixmap = QPixmap("images/UserHelp/UserHelpLogo.png")
        scaled_logoPixmap = self.logoPixmap.scaled(
            self.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.logoLabel.setPixmap(scaled_logoPixmap)

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 10, 800, 60)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("", self)
        self.titleLabel.setGeometry(220, 15, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 22))


        self.label1 = QLabel("Para mais informações, consulte o site oficial do MyOscilloscope. " + 
                             "Isso pode ser feito ao clicar no botão da imagem ao lado.", self)
        
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(240, 110, 400, 400)

        self.label2 = QLabel("A tela de Créditos pode ser acessada ao clicar no ícone da Escola Politécnica da USP, a Minerva.", self)
        
        self.label2.setWordWrap(True)
        self.label2.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.label2.setAlignment(Qt.AlignHCenter)
        self.label2.setFont(QFont("Microsoft Sans Serif", 12))
        self.label2.setGeometry(120, 290, 390, 400)



        self.imageLabel = QLabel("", self)
        self.imageLabel.setGeometry(80, 80, 150, 150)
        self.imageLabel.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap = QPixmap("images/UserHelp/Final_1_1.png")
        scaled_imagePixmap = self.imagePixmap.scaled(
            self.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel.setPixmap(scaled_imagePixmap)

        self.imageLabel2 = QLabel("", self)
        self.imageLabel2.setGeometry(520, 210, 170, 190)
        self.imageLabel2.setStyleSheet("""
            background-color: transparent;
        """)
        self.imagePixmap2 = QPixmap("images/UserHelp/Final_1_2.png")
        scaled_imagePixmap2 = self.imagePixmap2.scaled(
            self.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.imageLabel2.setPixmap(scaled_imagePixmap2)

class Final_2(QDialog):
    def __init__(self ):
        super(Final_2, self).__init__()
        self.setGeometry(5, 240, 800, 405)  
        # self.setFixedSize(800, 405)
        self.setWindowTitle("Final_2")
        self.setWindowIcon(QIcon("images/MyOscPi_BlackIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.backgroundLabel.setGeometry(0, 100, 800, 230)
        self.backgroundLabel.lower()

        self.titleLabel = QLabel("Referências", self)
        self.titleLabel.setGeometry(0, 15, 800, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240); 
                                          background-color: transparent;""")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 22))


        self.label1 = QLabel("• As informações presentes nessa seção de Apoio ao Usuário foram baseadas no Guia do Usuário " + 
                             "para o MyOscilloscope, disponível em: myoscilloscope.lme.usp.br. Acesso em 17 fev 2026. " + 
                             "\n\n\n\n[1] Retirado e adaptado do material de aula da Professora Dra. Elisabete Galeazzo, da Escola " + 
                             "Politécnica da USP. " +
                            "\n\n\n[2] https://www.facom.ufu.br/~jamil/eletronica/sinais_eletricos/sinais_eletricos.htm (Adaptado)." + 
                            " Acesso em 17 fev 2026.", self)
        
        self.label1.setWordWrap(True)
        self.label1.setStyleSheet(""" color: rgb(240, 240, 240);
                                      background-color: transparent """)
        self.label1.setAlignment(Qt.AlignHCenter)
        self.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.label1.setGeometry(10, 110, 780, 400)

       


if __name__ == '__main__':
    app = QApplication([])
    window = HelpScreen()
    window.show()
    app.exec()