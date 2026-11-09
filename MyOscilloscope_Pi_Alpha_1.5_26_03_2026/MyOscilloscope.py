"""
   MyOscilloscope Pi - versão Alpha 1.5.3
          por João Vitor Adami
         joaovitor.adami@usp.br
               15 Abr 2026

            Orientação por:
      Profa. Dra. Elisabete Galeazzo
        Dr. Henrique E. M. Peres
        Ms. Mauricio O. P. Lisboa


Escola Politécnica da Universidade de São Paulo
              
"""


import numpy as np
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6 import QtWidgets
from button import *
from knob import *
from screen2 import *
from screen3 import *
from screen4 import *
from Main_Screen1 import *
from FFT import *
from FreqResp import *
from PhasDiag import *
from Lissajous import *
from PhasDiag_and_LissajousScreen import *
from StandbyScreen import *
from MyO_Screen1_Methods import *
from MyO_ONOFFandCH_Bt_Methods import *
from MyO_Updates_for_Buttons_and_Labels import *
from MyO_MeasureMethods import *
from MyO_CursorMethods import *
from MyO_TriggerMethods import *
from MyO_Time_Volt_andPositionUpdates import *
from MyO_Freeze import * 
from MyO_MathComboBoxMethod import *
from MyO_ResizeEvents import *
from MyO_FFT_Methods import *
from MyO_PhasDiag_and_Lissaj_Methods import *
from MyO_FadeIn_and_Out_Methods import *
from MyO_ExportData import *
from MyO_WelcomeScreenMethods import *
from MyO_Main_for_secondaryScreenMethods import *
from MyO_CalibManual_Methods import *
from MyO_CalibWizClasses import *
from MyO_CalibWizMethods import *
from MyO_FrequencyResponseMethods import *
from MyO_Measurements import *
from MyO_Help import *
from MyO_PopUpWindows import *
from MyO_ExportImage import *
from MyO_Language import *

class MyOscPiWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.version = "Alpha 1.5.3 - 15/Apr/26"
        self.setWindowTitle(f"MyOscilloscope ({self.version})")
        self.setWindowIcon(QIcon("images/MyOscPi_BlueIcon.png"))
        self.setStyleSheet("background-color: rgb(230, 230, 230);")
        screen = QApplication.primaryScreen()
        available = screen.availableGeometry()
        self.setGeometry(0, 0, available.width(), available.height())
        self.p = self.width()/1920 #constante de (p)roporção


        """Definir o microcontrolador usado entre Arduino e Raspberry:"""
        self.microcontroller = "Raspberry"
        
        self.screenName = ""
        self.secondaryScreenName = ""
        # Tela 1
        self.screen1 = QtWidgets.QWidget(self)
        self.primaryScreen = QtWidgets.QStackedWidget()
        self.screen1.setGeometry(int(self.p * 20), int(self.p * 285), int(self.p * 1120), int(self.p * 360))
        QVBoxLayout(self.screen1).addWidget(self.primaryScreen)
        self.primaryScreen.setCurrentIndex(0)

        #Labels e SVGs de fundo:
        # Labels e SVGs de fundo:
        self.backgroundLabel0 = QLabel("", self)
        self.backgroundLabel0.setGeometry(int(self.p * 0), int(self.p * 0), int(self.p * 1920), int(self.p * 1030))
        self.backgroundLabel0.setStyleSheet("background-color: rgb(207, 207, 207);")

        self.background_svg1 = QSvgWidget("images_svg/backgroundLabel1.svg", self)
        self.background_svg1.setGeometry(int(self.p * 0), int(self.p * 100), int(self.p * 635), int(self.p * 160))
        self.background_svg1.setStyleSheet("background-color: transparent;")

        self.background_svg2 = QSvgWidget("images_svg/backgroundLabel2.svg", self)
        self.background_svg2.setGeometry(int(self.p * (-31)), int(self.p * (-25)), int(self.p * 1985), int(self.p * 188))
        self.background_svg2.setStyleSheet("background-color: transparent;")

        self.background_svg3 = QSvgWidget("images_svg/backgroundLabel3.svg", self)
        self.background_svg3.setGeometry(int(self.p * (-35)), int(self.p * 855), int(self.p * 1985), int(self.p * 188))
        self.background_svg3.setStyleSheet("background-color: transparent;")

        self.backgroundLabel4 = QLabel("", self)
        self.backgroundLabel4.setGeometry(int(self.p * -5), int(self.p * 75), int(self.p * 1931), int(self.p * 263))
        self.backgroundLabel4.setStyleSheet("""
            background-color: rgb(58, 58, 58);
            border-radius: 38px;
        """)

        self.backgroundLabel4_aux = QLabel("", self)
        self.backgroundLabel4_aux.setGeometry(int(self.p * 1656), int(self.p * 250), int(self.p * 275), int(self.p * 125))
        self.backgroundLabel4_aux.setStyleSheet("""
            background-color: rgb(58, 58, 58);
            border-radius: 38px;
        """)

        self.backgroundLabel4_aux_2 = QLabel("", self)
        self.backgroundLabel4_aux_2.setGeometry(int(self.p * -5), int(self.p * 300), int(self.p * 20), int(self.p * 583))
        self.backgroundLabel4_aux_2.setStyleSheet("""
            background-color: rgb(58, 58, 58);
            border-radius: 38px;
        """)

        self.backgroundLabel5 = QLabel("", self)
        self.backgroundLabel5.setGeometry(int(self.p * 5), int(self.p * 300), int(self.p * 1190), int(self.p * 583))
        self.backgroundLabel5.setStyleSheet("""
            background-color: rgb(30, 30, 30);
            border-radius: 10px;
        """)

        self.backgroundLabel6 = QLabel("", self)
        self.backgroundLabel6.setGeometry(int(self.p * 1125), int(self.p * 88), int(self.p * 775), int(self.p * 200))
        self.backgroundLabel6.setStyleSheet("""
            background-color: rgb(40, 40, 40);
            border-radius: 25px;
        """)

        self.backgroundLabel7 = QLabel("", self)
        self.backgroundLabel7.setGeometry(int(self.p * 88), int(self.p * 885), int(self.p * 456), int(self.p * 113))
        self.backgroundLabel7.setStyleSheet("""
            background-color: rgb(40, 40, 40);
            border-radius: 25px;
        """)

        self.background_svg1.raise_()


        # está em Main.py (o .py principal ainda é esse aqui aberto!)
       #Tela primária: a principal
        self.standbyScr1 = Standby()
        self.mainScr = Main()
        self.phasDiag_and_lissajScr = PhasDiag_and_Lissajous()
        self.freqRespScr = FreqResp()
        self.FFTScr = FFT()  
        self.helpScr = HelpScreen()
        self.standbyScr1.label.clear()
        
        self.screen1 = QtWidgets.QWidget(self)
        self.primaryScreen = QtWidgets.QStackedWidget()

        self.primaryScreen.addWidget(self.standbyScr1)
        self.primaryScreen.addWidget(self.mainScr)
        self.primaryScreen.addWidget(self.phasDiag_and_lissajScr)
        self.primaryScreen.addWidget(self.freqRespScr)
        self.primaryScreen.addWidget(self.FFTScr)
        self.primaryScreen.addWidget(self.helpScr)

        primary_scr_layout = QVBoxLayout(self.screen1)
        primary_scr_layout.setContentsMargins(0, 0, 0, 0)
        primary_scr_layout.setSpacing(0)
        primary_scr_layout.addWidget(self.primaryScreen)
        self.primaryScreen.setCurrentIndex(0)
    #     #Main:
        #self.screen1.setGeometry(0, 0, 500, 230)
    #     #alterar cor do background: (5, 5, 18)
    #     # #FFT:
    #     self.screen1.setGeometry(0, 360, 1010, 460)
    #     #alterar cor do background: ((16, 5, 5))
    #     # #FreqResp:
    #     self.screen1.setGeometry(0, 360, 1010, 460)
    #    #alterar cor do background: ((5, 16, 5))
    #    #PhasDiag/Lissajous:
    #     self.screen1.setGeometry(-130, 360, 1120, 560)
        #alterar cor do background: ((18, 18, 0))
        self.screen1.setStyleSheet("background-color: transparent;")

        

        # Tela 2: suporte à tela 1 com Trigger, Measure e outras funções
        self.secondaryScreen = QtWidgets.QStackedWidget()
        self.standbyScr2 = Standby_Screen2()
        self.trigger = Trigger()
        self.measure = Measure()
        self.cursor = Cursor()
        self.phasDiag_and_lissaj_scr2 = PhasDiag_and_Lissajous_scr2()
        self.FFT_scr2 = FFT_screen2()
        self.cursorFFT = CursorFFT()
        self.mainScr2_1 = Main_for_Screen2_1()
        self.mainScr2_2 = Main_for_Screen2_2()
        self.freqResp_scr2 = FreqResp_forScr2()
        self.cursorFreqResp_Magn = CursorFreqResp_Magnitude()
        self.cursorFreqResp_Phase = CursorFreqResp_Phase()
        self.calib_scr2 = Calibration_scr2()

        self.secondaryScreen.addWidget(self.standbyScr2)
        self.secondaryScreen.addWidget(self.trigger)
        self.secondaryScreen.addWidget(self.measure)
        self.secondaryScreen.addWidget(self.cursor)
        self.secondaryScreen.addWidget(self.phasDiag_and_lissaj_scr2)
        self.secondaryScreen.addWidget(self.FFT_scr2)
        self.secondaryScreen.addWidget(self.cursorFFT)
        self.secondaryScreen.addWidget(self.mainScr2_1)
        self.secondaryScreen.addWidget(self.mainScr2_2)
        self.secondaryScreen.addWidget(self.freqResp_scr2)
        self.secondaryScreen.addWidget(self.cursorFreqResp_Magn)
        self.secondaryScreen.addWidget(self.cursorFreqResp_Phase)
        self.secondaryScreen.addWidget(self.calib_scr2)


        self.FFT_scr2.page1.btRestoreDefault.clicked.connect(self.FFT_restoreDefault)
        self.phasDiag_and_lissaj_scr2.page1.isolateScreen.stateChanged.connect(self.togglePhasDiag)
        self.phasDiag_and_lissaj_scr2.page2.isolateScreen.stateChanged.connect(self.toggleLissaj)
        self.currentMainScr2_Scr = 1
        self.phasDiagMagnitVoltage = "RMS"
        self.phasDiag_and_lissaj_scr2.page1.magnitudeVoltageCB.currentIndexChanged.connect(self.phasDiagChangeMagnitVoltage)
        self.mainScr2_1.page2Button.clicked.connect(self.changeMainSecondScr_1_to_2)
        self.mainScr2_2.page1Button.clicked.connect(self.changeMainSecondScr_2_to_1)

        self.mainScr2_1.customTimeScaleLE.returnPressed.connect(self.SubmitTimeValue)
        self.mainScr2_1.refChannelCB.currentTextChanged.connect(self.ChangeRefChannel)
        self.mainScr2_1.attnFactorCB_CH1.currentTextChanged.connect(self.ChangeAttnFactorCH1)
        self.mainScr2_1.attnFactorCB_CH2.currentTextChanged.connect(self.ChangeAttnFactorCH2)
        

        self.screen2 = QtWidgets.QWidget(self)
        secondary_scr_layout = QVBoxLayout(self.screen2)
        secondary_scr_layout.setContentsMargins(0, 0, 0, 0)
        secondary_scr_layout.setSpacing(0)
        secondary_scr_layout.addWidget(self.secondaryScreen)
        self.secondaryScreen.setCurrentIndex(0)
        self.screen2.setGeometry(int(self.p * 1015), int(self.p * 300), int(self.p * 175), int(self.p * 580))
        self.screen2.setStyleSheet("background-color: transparent;")
        self.calib_scr2.phaseCorr_CheckBox.stateChanged.connect(self.activatePhaseCorr)
        self.calib_scr2.LPF_CheckBox.stateChanged.connect(self.changeState_LPF)
        self.calib_scr2.LPF_LE.returnPressed.connect(self.changeLPF_cutoffFreq)

        # Tela 3: Gerador de Funções, aba de Calibração e Recurso Math+
        self.tertiaryScreen = QtWidgets.QStackedWidget()
        self.blackScreenScr3 = BlackScreen()
        self.WFMgeneratorScr = Waveform_Generator()
        self.calibrationScr = Calibration()
        self.exportScr = Export_forScreen3()
        self.mathPlusScr = MathPlus_forScreen3()
        self.freqSweepScr = FreqRespSweepScr()
        self.tertiaryScreen.addWidget(self.blackScreenScr3)
        self.tertiaryScreen.addWidget(self.WFMgeneratorScr)
        self.tertiaryScreen.addWidget(self.calibrationScr)
        self.tertiaryScreen.addWidget(self.exportScr)
        self.tertiaryScreen.addWidget(self.mathPlusScr)
        self.tertiaryScreen.addWidget(self.freqSweepScr)

        self.screen3 = QtWidgets.QWidget(self)
        self.screen3.setGeometry(int(self.p * 1140), int(self.p * 105), int(self.p * 745), int(self.p * 165))
        tertiary_scr_layout = QVBoxLayout(self.screen3)
        tertiary_scr_layout.setContentsMargins(0, 0, 0, 0)
        tertiary_scr_layout.setSpacing(0)
        tertiary_scr_layout.addWidget(self.tertiaryScreen)
        self.tertiaryScreen.setCurrentIndex(0)

        
        self.WFMgeneratorScr.btQuestionMark.clicked.connect(self.open_WFM_supportScreen)
        self.WFM_supportScreen = WFM_SupportWindow()
        self.calibManualScreen = QtWidgets.QWidget(self)
        self.calibManualScreen.setStyleSheet("background-color: transparent")
        self.calibManuallayout = QVBoxLayout(self.calibManualScreen)
        self.calibManualScr = CalibManual()
        self.calibManuallayout.addWidget(self.calibManualScr)
        self.calibManualScreen.setGeometry(0, 0, 0, 0)
        self.calibrationScr.btCalibManual.clicked.connect(self.openCalibManual)
        self.calibManualScr.btClose.clicked.connect(self.closeCalibManual)
        self.calibManual_isOn = False
        self.calibManualScr.offsetCH1SB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_offsetCH1)
        self.calibManualScr.offsetCH1SB.lineEdit().textEdited.connect(self.onSpinBoxTyping_offsetCH1)
        self.calibManualScr.offsetCH1SB.valueChanged.connect(self.onSpinBoxValueChanged_offsetCH1)
        self.user_is_typing_offsetCH1 = False
        self.calibManualScr.offsetCH2SB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_offsetCH2)
        self.calibManualScr.offsetCH2SB.lineEdit().textEdited.connect(self.onSpinBoxTyping_offsetCH2)
        self.calibManualScr.offsetCH2SB.valueChanged.connect(self.onSpinBoxValueChanged_offsetCH2)
        self.user_is_typing_offsetCH2 = False
        self.calibManualScr.attnCH1SB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_attnCH1)
        self.calibManualScr.attnCH1SB.lineEdit().textEdited.connect(self.onSpinBoxTyping_attnCH1)
        self.calibManualScr.attnCH1SB.valueChanged.connect(self.onSpinBoxValueChanged_attnCH1)
        self.user_is_typing_attnCH1 = False
        self.calibManualScr.attnCH2SB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_attnCH2)
        self.calibManualScr.attnCH2SB.lineEdit().textEdited.connect(self.onSpinBoxTyping_attnCH2)
        self.calibManualScr.attnCH2SB.valueChanged.connect(self.onSpinBoxValueChanged_attnCH2)
        self.user_is_typing_attnCH2 = False
        self.calibManualScr.phaseCorrectSB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_phaseCorr)
        self.calibManualScr.phaseCorrectSB.lineEdit().textEdited.connect(self.onSpinBoxTyping_phaseCorr)
        self.calibManualScr.phaseCorrectSB.valueChanged.connect(self.onSpinBoxValueChanged_phaseCorr)
        self.user_is_typing_phaseCorr = False
        self.calibManualScr.samplingRateSB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_samplingRate)
        self.calibManualScr.samplingRateSB.lineEdit().textEdited.connect(self.onSpinBoxTyping_samplingRate)
        self.calibManualScr.samplingRateSB.valueChanged.connect(self.onSpinBoxValueChanged_samplingRate)
        self.user_is_typing_samplingRate = False
        self.calibManualScr.btSave.clicked.connect(self.btSave_calibManual_clicked)
        self.savedCalibScr = SavedCalibWindow()
        self.calibrationScr.btCalibWizard.clicked.connect(self.calibWizardIsOn)
        

        

        self.BlackScreen_scr4 = BlackScreen_Scr4()
        self.quaternaryScreen = QtWidgets.QStackedWidget()  # COM Port
        self.COMPort = COM_Port() #screen4
        self.quaternaryScreen.addWidget(self.BlackScreen_scr4)
        self.quaternaryScreen.addWidget(self.COMPort)
        self.screen4 = QtWidgets.QWidget(self)
        self.screen4.setGeometry(int(self.p * 113), int(self.p * 900), int(self.p * 407), int(self.p * 80))
        quaternary_scr_layout = QVBoxLayout(self.screen4)
        quaternary_scr_layout.setContentsMargins(0, 0, 0, 0)
        quaternary_scr_layout.setSpacing(0)
        quaternary_scr_layout.addWidget(self.quaternaryScreen)
        self.quaternaryScreen.setCurrentIndex(0)
        self.COMPortScr = COM_Port_Window() #janela pop-up
        self.PARAMETERS_FILE = "parameters.txt"

        #Para efeito de inicialização (flags para alterar os knobs de tensão quando está na escala de corrente)
        self.currentForCH1Scale = False
        self.currentForCH2Scale = False
        self.currentForMathScale = False
        

        if self.should_show_welcome():
            self.welcomeWindow = WelcomeWindow()
            self.welcomeWindow.OkButton.clicked.connect(self.closeWelcomeWindow)
            self.welcomeWindow.setWindowModality(Qt.ApplicationModal)
            self.welcomeWindow.show()

        

         
        self.bt_Wfm = Button(self, int(self.p * 1600), int(self.p * 105), int(self.p * 50), int(self.p * 50),"WFM",
                     "images_svg/Bt_WFM.svg", "images_svg/Bt_WFM.svg", False)
        self.bt_Wfm.clicked.connect(self.WFM_In_Screen3)

        self.bt_Calibration = Button(self, int(self.p * 1675), int(self.p * 105), int(self.p * 50), int(self.p * 50), "Calib",
                                    "images_svg/Bt_Calibration.svg", "images_svg/Bt_Calibration.svg", False)
        self.bt_Calibration.clicked.connect(self.Calib_In_Screen3)

        self.bt_Exp = Button(self, int(self.p * 1750), int(self.p * 105), int(self.p * 50), int(self.p * 50), "Export",
                            "images_svg/Bt_Exp.svg", "images_svg/Bt_Exp.svg", False)
        self.bt_Exp.clicked.connect(self.Export_In_Screen3)
        self.exportScr.btImage.clicked.connect(self.exportImage)
        self.exportScr.btData.clicked.connect(self.exportData)

        self.bt_MathPlus = Button(self, int(self.p * 1825), int(self.p * 105), int(self.p * 50), int(self.p * 50), "Math+",
                                "images_svg/Bt_Math+.svg", "images_svg/Bt_Math+.svg", False)
        self.bt_MathPlus.clicked.connect(self.MathPlus_In_Screen3)
        self.mathPlusBiggerWindow = MathPlus_BigScreen()
        #self.mathPlusScr.btMore.clicked.connect(self.OpenBiggerMathWindow)
        self.mathPlusScr.simpleOperationsCB.currentTextChanged.connect(
            self.ChangeMathMode)
        self.bt_Wfm.moveButton(1670, -400)
        self.bt_Calibration.moveButton(1730, -400)
        self.bt_Exp.moveButton(1740, -400)
        self.bt_MathPlus.moveButton(1790, -400)

        # Botões principais:
        # Main
        self.btMain = Button(self, int(self.p * 163), int(self.p * 194), int(self.p * 225), int(self.p * 44), "Main",
                     "images_svg/Bt_Main.svg", "images_svg/Bt_Main_Chosen.svg", False)
        self.btMain.clicked.connect(self.MainScreen)

        # FFT
        self.btFFT = Button(self, int(self.p * 400), int(self.p * 194), int(self.p * 225), int(self.p * 44), "FFT",
                            "images_svg/Bt_FFT.svg", "images_svg/Bt_FFT_Chosen.svg", False)
        self.btFFT.clicked.connect(self.FFTScreen)

        # Frequency Response
        self.btFreqResp = Button(self, int(self.p * 638), int(self.p * 194), int(self.p * 225), int(self.p * 44), "Freq Resp",
                                "images_svg/Bt_Freq_Resp.svg", "images_svg/Bt_Freq_Resp_Chosen.svg", False)
        self.btFreqResp.clicked.connect(self.FreqRespScreen)

        # Phasor Diagram
        self.btPhasDiag = Button(self, int(self.p * 875), int(self.p * 194), int(self.p * 225), int(self.p * 44), "Phas Diag",
                                "images_svg/Bt_Phas_Diag.svg", "images_svg/Bt_Phas_Diag_Chosen.svg", False)
        self.btPhasDiag.clicked.connect(self.PhasDiagScreen)

        #Help
        self.btHelp = Button(self, int(self.p * 638), int(self.p * 120), int(self.p * 225), int(self.p * 44), "Freq Resp",
                                "images_svg/Bt_Help.svg", "images_svg/Bt_Help_Chosen.svg", False)
        self.btHelp.clicked.connect(self.HelpScreenBt)


        self.btSite = Button(self, int(self.p * 1000), int(self.p * 80), int(self.p * 100), int(self.p * 100), "Site",
                            "images_svg/bt_site_myosc.svg", "images_svg/bt_site_myosc.svg", False)
        self.btSite.clicked.connect(self.openSite)
        
        self.btCredits = Button(self, int(self.p * 15), int(self.p * 115), int(self.p * 135), int(self.p * 135), "",
                            "", "", False)
        self.creditsScreen = CreditsWindow(self.version)
        self.btCredits.clicked.connect(self.openCredits)

        # Botões dos canais e de On/Off
        self.btMath = Button(self, int(self.p * 1806), int(self.p * 588), int(self.p * 76), int(self.p * 113), "Math",
                            "images_svg/Bt_Math_Off.svg", "images_svg/Bt_Math_On.svg", False)
        self.btMath.clicked.connect(self.btMathClicked)

        self.btOnOff = Button(self, int(self.p * 1063), int(self.p * 910), int(self.p * 80), int(self.p * 80), "ON/OFF",
                            "images_svg/Bt_OFF.svg", "images_svg/Bt_ON.svg", False)
        self.btOnOff.clicked.connect(self.ONOFF)

        self.btCH1 = Button(self, int(self.p * 1481), int(self.p * 588), int(self.p * 75), int(self.p * 113), "CH1",
                            "images_svg/Bt_CH1_Off.svg", "images_svg/Bt_CH1_On.svg", False)
        self.btCH2 = Button(self, int(self.p * 1644), int(self.p * 588), int(self.p * 75), int(self.p * 113), "CH2",
                            "images_svg/Bt_CH2_Off.svg", "images_svg/Bt_CH2_On.svg", False)
        self.btCH1.clicked.connect(self.btCH1Clicked)
        self.btCH2.clicked.connect(self.btCH2Clicked)
        self.CH1Label = QLabel("CH1: 1 V/div", self)
        self.CH1Label.setGeometry(int(self.p * 340), int(self.p * 300), int(self.p * 150), int(self.p * 50))
        self.CH1Label.setStyleSheet(""" color: "blue"; 
                                        background-color: transparent""")
        self.CH1Label.setFont(QFont("Microsoft Sans Serif", 14))
        self.CH1Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.CH1Label.hide()


        self.posCH1Label = QLabel("CH1 Position \n     V", self)
        self.posCH1Label.setGeometry(int(self.p * 210), int(self.p * 830), int(self.p * 115), int(self.p * 50))
        self.posCH1Label.setStyleSheet(""" color: blue; 
                                        background-color: transparent""")
        self.posCH1Label.setFont(QFont("Microsoft Sans Serif", 14))
        self.posCH1Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.posCH1Label.hide()


  
        self.CH2Label = QLabel("CH2: 1 V/div", self)
        self.CH2Label.setGeometry(int(self.p * 510), int(self.p * 300), int(self.p * 150), int(self.p * 60))
        self.CH2Label.setStyleSheet(""" color: "red"; 
                                        background-color: transparent""")
        self.CH2Label.setFont(QFont("Microsoft Sans Serif", 14))
        self.CH2Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.CH2Label.hide()


        self.posCH2Label = QLabel("CH2 Position \n     V", self)
        self.posCH2Label.setGeometry(int(self.p * 360), int(self.p * 830), int(self.p * 115), int(self.p * 50))
        self.posCH2Label.setStyleSheet(""" color: "red"; 
                                        background-color: transparent""")
        self.posCH2Label.setFont(QFont("Microsoft Sans Serif", 14))
        self.posCH2Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.posCH2Label.hide()


        

        # Relativo a Time e escala horizontal
        self.timeKnob = Knob(self, int(self.p * 1219), int(self.p * 388), int(self.p * 194), int(self.p * 194), 
                            "images_svg/Knob1.svg", -5, 5, "Time", -9, 5, 1)
        self.timeKnob.raise_()
        self.timeKnob.valueChanged.connect(self.UpdateTimeScale)
        self.timeLabel = QLabel("Time: 1 ms/div", self)
        self.timeLabel.setGeometry(int(self.p * 860), int(self.p * 300), int(self.p * 150), int(self.p * 40))
        self.timeLabel.setStyleSheet(""" color: "white"; 
                                        background-color: transparent""")
        self.timeLabel.setFont(QFont("Microsoft Sans Serif", 14))
        self.timeLabel.hide()

        self.vdivMathKnob = Knob(self, int(self.p * 1781), int(self.p * 438), int(self.p * 125), int(self.p * 125), 
                         "images/Knob2.png", -5, 5, "V/div", -5, 5, 1)
        self.vdivMathKnob.raise_()
        self.vdivMathKnob.valueChanged.connect(self.UpdateVDivMath)

        self.posMathKnob = Knob(self, int(self.p * 1794), int(self.p * 719), int(self.p * 100), int(self.p * 100), 
                                "images/Knob3.png", -5, 5, "Position", -40, 40, 1)
        self.posMathKnob.raise_()
        self.posMathKnob.valueChanged.connect(self.UpdatePositionMath)

        # Labels do Math na tela:
        self.mathvDivLabel = QLabel("Math: 1 V/div", self)
        self.mathvDivLabel.setGeometry(int(self.p * 685), int(self.p * 300), int(self.p * 155), int(self.p * 50))
        self.mathvDivLabel.setStyleSheet(""" color: "cyan"; 
                                        background-color: transparent""")
        self.mathvDivLabel.setFont(QFont("Microsoft Sans Serif", 14))
        self.mathvDivLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mathvDivLabel.hide()


        self.mathPosLabel = QLabel("Math Position \n     V", self)
        self.mathPosLabel.setGeometry(int(self.p * 510), int(self.p * 830), int(self.p * 120), int(self.p * 50))
        self.mathPosLabel.setStyleSheet(""" color: "cyan"; 
                                        background-color: transparent""")
        self.mathPosLabel.setFont(QFont("Microsoft Sans Serif", 14))
        self.mathPosLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.mathPosLabel.hide()
        

        self.vdivCH1Knob = Knob(self, int(self.p * 1456), int(self.p * 438), int(self.p * 125), int(self.p * 125), 
                        "images/Knob2.png", -5, 5, "V/div", -5, 5, 1)
        self.vdivCH1Knob.raise_()
        self.vdivCH1Knob.valueChanged.connect(self.UpdateVDivCH1)
        

        self.vdivCH2Knob = Knob(self, int(self.p * 1619), int(self.p * 438), int(self.p * 125), int(self.p * 125), 
                                "images/Knob2.png", -5, 5, "V/div", -5, 5, 1)
        self.vdivCH2Knob.raise_()
        self.vdivCH2Knob.valueChanged.connect(self.UpdateVDivCH2)

        self.posCH1Knob = Knob(self, int(self.p * 1469), int(self.p * 719), int(self.p * 100), int(self.p * 100), 
                       "images/Knob3.png", -5, 5, "Position", -40, 40, 1)
        self.posCH1Knob.raise_()
        self.posCH1Knob.valueChanged.connect(self.UpdatePositionCH1)

        self.posCH2Knob = Knob(self, int(self.p * 1631), int(self.p * 719), int(self.p * 100), int(self.p * 100), 
                            "images/Knob3.png", -5, 5, "Position", -40, 40, 1)
        self.posCH2Knob.raise_()
        self.posCH2Knob.valueChanged.connect(self.UpdatePositionCH2)

        self.cursorKnob = Knob(self, int(self.p * 1256), int(self.p * 794), int(self.p * 125), int(self.p * 125), 
                       "images/Knob2.png", -500, 500, "Cursor", -500, 500, 1)
        self.cursorKnob.raise_()
        # Relativo ao cursor:
        self.X1Value = 0
        self.X2Value = 0.01
        self.Y1Value = -5
        self.Y2Value = 5
        self.cursor.cursorX1LE.setText("0.00")
        self.cursor.cursorX2LE.setText("10.00")
        self.cursor.cursorY1LE.setText("-5.00")
        self.cursor.cursorY2LE.setText("5.00")
        self.cursor.cursorDeltaX_LE.setText("10.00")
        self.cursor.cursorDeltaY_LE.setText("10.00")
        self.cursorKnobLineAssigned = "X1"
        self.cursorKnobLineAssigned_FFT = "X1"
        self.cursorKnobLineAssigned_FreqResp_Magn = "X1"
        self.cursorKnobLineAssigned_FreqResp_Phase = "X1"
        self.cursorKnob.valueChanged.connect(self.CursorKnob)
        self.cursorKnob.valueChanged.connect(self.CursorKnob_FFT)
        self.cursorKnob.valueChanged.connect(self.CursorKnob_FreqResp_Magn)
        self.cursorKnob.valueChanged.connect(self.CursorKnob_FreqResp_Phase)
        self.btCursor = Button(self, int(self.p * 1213), int(self.p * 925), int(self.p * 206), int(self.p * 41), "Cursor",
                       "images_svg/Bt_Cursor.svg", "images_svg/Bt_Cursor_Chosen.svg", False)
        self.btCursor.clicked.connect(self.CursorActivated)
        self.cursor.cursorSelectCB.currentTextChanged.connect(
            self.CursorSelectCBChanged)
        self.cursor.cursorX1LE.returnPressed.connect(self.Cursor_X1_LEChanged)
        self.cursor.cursorX2LE.returnPressed.connect(self.Cursor_X2_LEChanged)
        self.cursor.cursorY1LE.returnPressed.connect(self.Cursor_Y1_LEChanged)
        self.cursor.cursorY2LE.returnPressed.connect(self.Cursor_Y2_LEChanged)
        self.cursorProportionalLabel = QLabel(
            "Cursor lines Y1 and Y2 are adjusted to \nCH1 V/div scale", self)
        self.cursorProportionalLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorProportionalLabel.setGeometry(int(self.p * 675), int(self.p * 830), int(self.p * 302), int(self.p * 70))
        self.cursorProportionalLabel.setStyleSheet(
            """ color: rgb(240, 240, 240); 
                                        background-color: transparent""")
        self.cursorProportionalLabel.setFont(QFont("Microsoft Sans Serif", 12))
        self.cursorProportionalLabel.hide()
        
        self.cursorLinesOn = False

        #Cursor do FFT:
        self.cursorFFT.cursorX1LE.setText("10.0")
        self.cursorFFT.cursorX2LE.setText("10000.0")
        self.cursorFFT.cursorY1LE.setText("-65.0")
        self.cursorFFT.cursorY2LE.setText("15.0")
        self.cursorFFT.cursorDeltaX_LE.setText("10000.0")
        self.cursorFFT.cursorDeltaY_LE.setText("90.00")
        self.cursorFFT.cursorX1LE.returnPressed.connect(self.Cursor_X1_LEChanged_FFT)
        self.cursorFFT.cursorX2LE.returnPressed.connect(self.Cursor_X2_LEChanged_FFT)
        self.cursorFFT.cursorY1LE.returnPressed.connect(self.Cursor_Y1_LEChanged_FFT)
        self.cursorFFT.cursorY2LE.returnPressed.connect(self.Cursor_Y2_LEChanged_FFT)
        self.cursorFFTLabel = QLabel("Cursor lines X1 and X2 are in \nlogarithmic scale!", self)
        self.cursorFFTLabel.setGeometry(int(self.p * 675), int(self.p * 830), int(self.p * 302), int(self.p * 70))
        self.cursorFFTLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.cursorFFTLabel.setStyleSheet( """ color: yellow; 
                                        background-color: transparent""")
        self.cursorFFTLabel.setFont(QFont("Microsoft Sans Serif", 12))
        self.cursorFFTLabel.hide()

        self.cursorFFT.cursorSelectCB.currentTextChanged.connect(
            self.CursorSelectCBChanged_FFT)
        self.cursorLinesFFT = False



        # Relativo ao trigger:
        self.triggerKnob = Knob(self, int(self.p * 1256), int(self.p * 606), int(self.p * 125), int(self.p * 125), 
                                "images/Knob2.png", -5, 5, "Trigger", -50, 50, 2)
        self.triggerKnob.raise_()
        self.triggerKnob.valueChanged.connect(self.UpdateTriggerLine)

        self.trigPrevValue = 0
        self.triggerOn = False
        self.xTrigger = np.arange(0, 0.5, 0.5/1000)
        self.yTrigger = np.ones_like(
            self.xTrigger) * self.mainScr.triggerEdgeValue
        self.graphTriggerLine = mkPen(color="Orange", width=1.7)
        self.yZeroLine = np.zeros_like(self.xTrigger)
        self.graphZeroLine = mkPen(color="Yellow", width=0.7)
        self.graphicZeroLineTrigger = self.mainScr.plot(
            self.xTrigger, self.yZeroLine, pen=self.graphZeroLine)
        self.graphicPlottingTrigger = self.mainScr.plot(self.xTrigger, self.yTrigger,
                                                        pen=self.graphTriggerLine)  # Apenas inicialização
        self.mainScr.removeItem(self.graphicPlottingTrigger)
        self.btTrigger = Button(self, int(self.p * 1213), int(self.p * 738), int(self.p * 206), int(self.p * 41), "Trigger",
                                "images_svg/Bt_Trigger.svg", "images_svg/Bt_Trigger_Chosen.svg", False)
        self.btTrigger.clicked.connect(self.TriggerActivated)
        # self.trigger.trigChannelCB.currentTextChanged.connect(
        #     self.TrigChannelCBChanged)
        self.trigger.trigTypeCB.currentTextChanged.connect(
            self.TrigTypeCBChanged)
        self.trigger.trigModeCB.currentTextChanged.connect(
            self.TrigModeCBChanged)
        self.triggerLabel = QLabel("Trigger \n0.0 V", self)
        self.triggerLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.triggerLabel.setGeometry(int(self.p * 30), int(self.p * 300), int(self.p * 110), int(self.p * 50))
        self.triggerLabel.setStyleSheet(""" color: "orange"; 
                                        background-color: transparent""")
        self.triggerLabel.setFont(QFont("Microsoft Sans Serif", 14))
        self.triggerLabel.hide()
        
        self.triggerProportionLabel = QLabel(
            "Trigger line adjusted \nto CH1 V/div scale", self)
        self.triggerProportionLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.triggerProportionLabel.setGeometry(int(self.p * 150), int(self.p * 300), int(self.p * 190), int(self.p * 50))
        self.triggerProportionLabel.setStyleSheet(""" color: "yellow"; 
                                        background-color: transparent""")
        self.triggerProportionLabel.setFont(QFont("Microsoft Sans Serif", 12))
        self.triggerProportionLabel.hide()

        # Relativo ao Measure:
        self.btMeas = Button(self, int(self.p * 1625), int(self.p * 925), int(self.p * 206), int(self.p * 41), "Measure",
                            "images_svg/Bt_Meas.svg", "images_svg/Bt_Meas_Chosen.svg", False)
        self.btMeas.clicked.connect(self.MeasureActivated)

        
        self.measChannelSelected = "CH1"
        self.measure.channelSelectCB.currentTextChanged.connect(
            self.MeasChannelSelectCBChanged)
        self.phaseLabel = QLabel("Reference Channel: \nCH1", self)
        self.phaseLabel.setGeometry(int(self.p * 10), int(self.p * 830), int(self.p * 180), int(self.p * 50))
        self.phaseLabel.setStyleSheet(""" color: "green"; 
                                        background-color: transparent""")
        self.phaseLabel.setFont(QFont("Microsoft Sans Serif", 14))
        self.phaseLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.phaseLabel.hide()
        self.updateMeasureTimer = QtCore.QTimer()
        self.updateMeasureTimer.start(400)
        self.updateMeasureTimer.setSingleShot(True)

        self.btFreeze = Button(self, int(self.p * 1688), int(self.p * 313), int(self.p * 206), int(self.p * 41), "Freeze",
                            "images_svg/Bt_Freeze.svg", "images_svg/Bt_Freeze_Chosen.svg", False)
        self.btFreeze.clicked.connect(self.FreezeActivated)

        

        # Labels da tela Main:
        self.blackLabel1 = QLabel("", self)
        self.blackLabel1.setStyleSheet("background-color: rgb(5, 5, 18)")
        self.blackLabel1.setGeometry(int(self.p * 10), int(self.p * 360), int(self.p * 37), int(self.p * 460))
        self.blackLabel2 = QLabel("", self)
        self.blackLabel2.setStyleSheet("background-color: rgb(5, 5, 18)")
        self.blackLabel2.setGeometry(int(self.p * 974), int(self.p * 360), int(self.p * 38), int(self.p * 460))
        self.blackLabel1.hide()
        self.blackLabel2.hide()

        self.whiteLabel = QLabel("", self)
        self.whiteLabel.setStyleSheet("background-color: 'white'")
        self.whiteLabel.setGeometry(1, 1, 1, 1)

        self.exportLabel = QLabel("Label", self)
        self.exportLabel.setStyleSheet(""" background-color: 'white' """)
        self.exportLabel.setFont(QFont("Microsoft Sans Serif", 12))
        self.exportLabel.setAlignment(Qt.AlignHCenter)
        self.exportLabel.setGeometry(int(self.p * 200), int(self.p * 700), int(self.p * 450), int(self.p * 50))
        self.exportLabel.move(-60, -60)

        self.fadeLabelScr1 = QLabel("", self)
        # self.fadeLabelScr1.setGeometry(15, 310, 1170, 563)
        self.fadeLabelScr1.setGeometry(1, 1, 1, 1)
        self.fadeLabelScr1.setStyleSheet(""" background-color: 'white' """)

        self.fadeLabelScr3 = QLabel("", self)
        #self.fadeLabelScr3.setGeometry(1140, 105, 745, 165)
        self.fadeLabelScr3.setGeometry(1, 1, 1, 1)
        self.fadeLabelScr3.setStyleSheet(""" background-color: 'white' """)

        self.fadeLabelScr4 = QLabel("", self)
        # self.fadeLabelScr4.setGeometry(113, 910, 407, 80)
        self.fadeLabelScr4.setGeometry(1, 1, 1, 1)
        self.fadeLabelScr4.setStyleSheet(""" background-color: 'white' """)

        self.screen1.raise_()

        self.timeKnobLabel = QLabel("Time", self)
        self.timeKnobLabel.setGeometry(int(self.p * 1250), int(self.p * 338), int(self.p * 138), int(self.p * 38))
        self.timeKnobLabel.setStyleSheet(""" color: rgb(80, 80, 80);
                                          background-color: transparent; """)
        self.timeKnobLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.timeKnobLabel.setFont(QFont("Microsoft Sans Serif", 20))

        self.vdivLabel1 = QLabel("V/div", self)
        self.vdivLabel1.setGeometry(int(self.p * 1488), int(self.p * 400), int(self.p * 63), int(self.p * 38))
        self.vdivLabel1.setStyleSheet(""" color: rgb(80, 80, 80); 
                                          background-color: transparent;""")
        self.vdivLabel1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.vdivLabel1.setFont(QFont("Microsoft Sans Serif", 20))
        

        self.vdivLabel2 = QLabel("V/div", self)
        self.vdivLabel2.setGeometry(int(self.p * 1650), int(self.p * 400), int(self.p * 63), int(self.p * 38))
        self.vdivLabel2.setStyleSheet(""" color: rgb(80, 80, 80);
                                          background-color: transparent;""")
        self.vdivLabel2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.vdivLabel2.setFont(QFont("Microsoft Sans Serif", 20))

        self.vdivLabel3 = QLabel("V/div", self)
        self.vdivLabel3.setGeometry(int(self.p * 1813), int(self.p * 400), int(self.p * 63), int(self.p * 38))
        self.vdivLabel3.setStyleSheet(""" color: rgb(80, 80, 80);
                                          background-color: transparent;""")
        self.vdivLabel3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.vdivLabel3.setFont(QFont("Microsoft Sans Serif", 20))

        self.positionLabel1 = QLabel("Position", self)
        self.positionLabel1.setGeometry(int(self.p * 1488), int(self.p * 831), int(self.p * 63), int(self.p * 38))
        self.positionLabel1.setStyleSheet(""" color: rgb(80, 80, 80); 
                                          background-color: transparent;""")
        self.positionLabel1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.positionLabel1.setFont(QFont("Microsoft Sans Serif", 12))

        self.positionLabel2 = QLabel("Position", self)
        self.positionLabel2.setGeometry(int(self.p * 1650), int(self.p * 831), int(self.p * 63), int(self.p * 38))
        self.positionLabel2.setStyleSheet(""" color: rgb(80, 80, 80); 
                                          background-color: transparent;""")
        self.positionLabel2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.positionLabel2.setFont(QFont("Microsoft Sans Serif", 12))

        self.positionLabel3 = QLabel("Position", self)
        self.positionLabel3.setGeometry(int(self.p * 1813), int(self.p * 831), int(self.p * 63), int(self.p * 38))
        self.positionLabel3.setStyleSheet(""" color: rgb(80, 80, 80); 
                                          background-color: transparent;""")
        self.positionLabel3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.positionLabel3.setFont(QFont("Microsoft Sans Serif", 12))



        
        self.FFT_scr2.page1.x_botLim_LE.returnPressed.connect(
            self.FFT_xBotLimLE_Changed)
        self.FFT_scr2.page1.x_topLim_LE.returnPressed.connect(
            self.FFT_xTopLimLE_Changed)
        self.FFT_scr2.page1.y_botLim_LE.returnPressed.connect(
            self.FFT_yBotLimLE_Changed)
        self.FFT_scr2.page1.y_topLim_LE.returnPressed.connect(
            self.FFT_yTopLimLE_Changed)
        self.FFT_scr2.page1.btRestoreDefault.clicked.emit()
        

        self.firstTimeSearchingCOMPorts = True
        self.COMPort.btSearch.clicked.connect(self.searchCOMPorts)

        
        # Analisar se isso muda algo no executável
        self.setWindowIcon(QIcon("images/MyOscPi_BlueIcon.png"))

        self.shuntRes_CH1 = 1
        self.shuntRes_CH2 = 1
        self.shuntRes_Math = 1
        self.mainScr2_2.currentInVerticalScaleCheckBox_CH1.stateChanged.connect(self.currentInVerticalScale)
        self.mainScr2_2.currentInVerticalScaleCheckBox_CH2.stateChanged.connect(self.currentInVerticalScale)
        self.mainScr2_2.currentInVerticalScaleCheckBox_Math.stateChanged.connect(self.currentInVerticalScale)
        
        self.mainScr2_2.resistorValueLE_CH1.returnPressed.connect(self.shuntResLineEdit_CH1)
        self.mainScr2_2.resistorValueLE_CH2.returnPressed.connect(self.shuntResLineEdit_CH2)
        self.mainScr2_2.resistorValueLE_Math.returnPressed.connect(self.shuntResLineEdit_Math)


        #De Frequency Response:
        self.freqResp_scr2.freqResp_page1.btSweep_Play.clicked.connect(self.sweepControl_Play)
        self.freqResp_scr2.freqResp_page1.btSweep_Stop.clicked.connect(self.sweepControl_Stop)
        self.notStartedProgressBar = True
        self.freqSweepScr.progressBar.valueChanged.connect(self.sweepProgressBar_valueChanged)
        self.freqResp_nPoints = 60
        self.freqResp_initFreq = 20
        self.freqResp_finalFreq = 9000


        
        self.samplingIndex = 0
        self.currentFrequency = None

        self.sweepTimer = QTimer(self)
        self.sweepTimer.setInterval(1200) 
        self.sweepTimer.timeout.connect(self.advanceSweep)

        self.freqResp_scr2.freqResp_page1.btSweep_Play.clicked.connect(self.playPauseSweep)
        self.freqResp_scr2.freqResp_page1.btSweep_Stop.clicked.connect(self.stopSweep)
        
        self.freqRespCurves = []
        self.freqRespCurves_phase = []      
        self.currentSamples = None  
        self.currentSamples_phase = None   
        self.currentCurve = None
        self.nextSweepColor = "w"
        self.sweepRunning = False
        self.sweepPaused = False
        self.pendingCapture = False
        self.freqResp_scr2.freqResp_page2.plotColorCB.currentIndexChanged.connect(self.changePlotColor)
        self.freqResp_scr2.freqResp_page2.functionTypeCB.currentIndexChanged.connect(self.changeFunctionType)
        
        self.sweepHaveNotStarted = True
        self.functionType = "CH2/CH1" 

        self.freqResp_scr2.freqResp_page1.numberPointsLE.returnPressed.connect(self.change_numPoints_LE_FreqResp)
        self.freqResp_scr2.freqResp_page1.initialFreqLE.returnPressed.connect(self.change_initFreq_LE_FreqResp)    
        self.freqResp_scr2.freqResp_page1.finalFreqLE.returnPressed.connect(self.change_finalFreq_LE_FreqResp)

        self.freqResp_scr2.freqResp_page3.x_botLim_LE.returnPressed.connect(self.FreqResp_xBotLimLE_Changed)
        self.freqResp_scr2.freqResp_page3.x_topLim_LE.returnPressed.connect(self.FreqResp_xTopLimLE_Changed)
        self.freqResp_scr2.freqResp_page3.y_botLim_LE.returnPressed.connect(self.FreqResp_yBotLimLE_Changed)
        self.freqResp_scr2.freqResp_page3.y_topLim_LE.returnPressed.connect(self.FreqResp_yTopLimLE_Changed)
        self.freqResp_scr2.freqResp_page3.btRestoreDefault.clicked.connect(self.FreqResp_restoreDefault)

        self.freqResp_scr2.freqResp_page2.y_AxisCB.currentIndexChanged.connect(self.changeFreqRespAxis)
        
        self.freqResp_scr2.freqResp_page3.y_botLim_LE_phase.returnPressed.connect(self.FreqResp_yBotLimLE_phase_Changed)
        self.freqResp_scr2.freqResp_page3.y_topLim_LE_phase.returnPressed.connect(self.FreqResp_yTopLimLE_phase_Changed) 

        self.freqResp_scr2.freqResp_page2.btclearScreen.clicked.connect(self.clearSweeps)
        self.cursorFreqResp_Magn.cursorX1LE.setText("10.0")
        self.cursorFreqResp_Magn.cursorX2LE.setText("10000.0")
        self.cursorFreqResp_Magn.cursorY1LE.setText("-65.0")
        self.cursorFreqResp_Magn.cursorY2LE.setText("15.0")
        self.cursorFreqResp_Magn.cursorDeltaX_LE.setText("10000.0")
        self.cursorFreqResp_Magn.cursorDeltaY_LE.setText("80.0")

        self.cursorFreqResp_Phase.cursorX1LE.setText("0.0")
        self.cursorFreqResp_Phase.cursorX2LE.setText("10000.0")
        self.cursorFreqResp_Phase.cursorY1LE.setText("-180.0")
        self.cursorFreqResp_Phase.cursorY2LE.setText("180.0")
        self.cursorFreqResp_Phase.cursorDeltaX_LE.setText("10000.0")
        self.cursorFreqResp_Phase.cursorDeltaY_LE.setText("360.0")

        

        self.X1ValueFreqResp_Magn = 10
        self.X2ValueFreqResp_Magn = 10000
        self.Y1ValueFreqResp_Magn = -65
        self.Y2ValueFreqResp_Magn = 15

        self.X1ValueFreqResp_Phase = 10
        self.X2ValueFreqResp_Phase = 10000
        self.Y1ValueFreqResp_Phase = -180
        self.Y2ValueFreqResp_Phase = 180

        self.cursorFreqResp_Magn.cursorSelectCB.currentIndexChanged.connect(self.CursorSelectCBChanged_FreqResp_Magn)
        self.cursorFreqResp_Magn.cursorX1LE.returnPressed.connect(self.Cursor_X1_LEChanged_FreqResp_Magn)
        self.cursorFreqResp_Magn.cursorX2LE.returnPressed.connect(self.Cursor_X2_LEChanged_FreqResp_Magn)
        self.cursorFreqResp_Magn.cursorY1LE.returnPressed.connect(self.Cursor_Y1_LEChanged_FreqResp_Magn)
        self.cursorFreqResp_Magn.cursorY2LE.returnPressed.connect(self.Cursor_Y2_LEChanged_FreqResp_Magn)

        self.cursorFreqResp_Phase.cursorSelectCB.currentIndexChanged.connect(self.CursorSelectCBChanged_FreqResp_Phase)
        self.cursorFreqResp_Phase.cursorX1LE.returnPressed.connect(self.Cursor_X1_LEChanged_FreqResp_Phase)
        self.cursorFreqResp_Phase.cursorX2LE.returnPressed.connect(self.Cursor_X2_LEChanged_FreqResp_Phase)
        self.cursorFreqResp_Phase.cursorY1LE.returnPressed.connect(self.Cursor_Y1_LEChanged_FreqResp_Phase)
        self.cursorFreqResp_Phase.cursorY2LE.returnPressed.connect(self.Cursor_Y2_LEChanged_FreqResp_Phase)

        self.measurementsTimer = QtCore.QTimer()
        self.measurementsTimer.timeout.connect(self.measurements)

        self.mainScr.updateTimer.timeout.connect(self.isSerialOk)
        #deixar no final do init:
        self.showMaximized()

        self.WFMgeneratorScr.btOnOff.clicked.connect(lambda: self.pauseTrigger(1700))
        self.WFMgeneratorScr.freq_SpinBox.valueChanged.connect(lambda: self.pauseTrigger(800))
        self.WFMgeneratorScr.amplitKnob.valueChanged.connect(lambda: self.pauseTrigger(800))
        self.WFMgeneratorScr.amplitLE.returnPressed.connect(lambda: self.pauseTrigger(800))
        self.WFMgeneratorScr.signalTypeCB.currentIndexChanged.connect(lambda: self.pauseTrigger(800))

        self.loadLanguage()

        if self.language == "English": self.COMPort.COM_PortLE.setText("No Port.")
        else:                          self.COMPort.COM_PortLE.setText("Nenhuma Porta.")

        self.whiteExportLabel = QLabel("", self)
        self.whiteExportLabel.setGeometry(int(self.p/0.8 * 5), int(self.p/0.8 * 240), int(self.p/0.8 * 800), int(self.p/0.8 * 465))
        self.whiteExportLabel.setStyleSheet("background-color: white;")
        self.whiteExportLabel.hide()

        self.whiteExportLabel_lissaj = QLabel("", self)
        self.whiteExportLabel_lissaj.setGeometry(int(self.p/0.8 * 250), int(self.p/0.8 * 280), int(self.p/0.8 * 350), int(self.p/0.8 * 350))
        self.whiteExportLabel_lissaj.setStyleSheet("background-color: white;")
        self.whiteExportLabel_lissaj.hide()

        self.whiteExportLabel_phasDiag = QLabel("", self)
        self.whiteExportLabel_phasDiag.setGeometry(int(self.p/0.8 * 370), int(self.p/0.8 * 280), int(self.p/0.8 * 360), int(self.p/0.8 * 350))
        self.whiteExportLabel_phasDiag.setStyleSheet("background-color: white;")
        self.whiteExportLabel_phasDiag.hide()

        
        
    
    """Associando o arquivo principal com os métodos dos outros arquivos!!!!!!!!"""
    ONOFF = ONOFF
    btCH1Clicked = btCH1Clicked
    btCH2Clicked = btCH2Clicked
    btMathClicked = btMathClicked
    MainScreen = MainScreen
    FFTScreen = FFTScreen
    FreqRespScreen = FreqRespScreen
    PhasDiagScreen = PhasDiagScreen
    HelpScreenBt = HelpScreenBt
    UpdatePrimaryButtons = UpdatePrimaryButtons
    UpdateSecondaryButtons = UpdateSecondaryButtons
    turnEverythingToOFF = turnEverythingToOFF
    MeasureActivated = MeasureActivated
    UpdateMeasure = UpdateMeasure
    MeasChannelSelectCBChanged = MeasChannelSelectCBChanged
    CursorActivated = CursorActivated
    CursorSelectCBChanged = CursorSelectCBChanged
    Cursor_X1_LEChanged = Cursor_X1_LEChanged
    Cursor_X2_LEChanged = Cursor_X2_LEChanged
    Cursor_Y1_LEChanged = Cursor_Y1_LEChanged
    Cursor_Y2_LEChanged = Cursor_Y2_LEChanged
    UpdateCursorDeltaX = UpdateCursorDeltaX
    UpdateCursorDeltaY = UpdateCursorDeltaY
    CursorKnob = CursorKnob
    CursorSelectCBChanged_FFT = CursorSelectCBChanged_FFT
    Cursor_X1_LEChanged_FFT = Cursor_X1_LEChanged_FFT
    Cursor_X2_LEChanged_FFT = Cursor_X2_LEChanged_FFT
    Cursor_Y1_LEChanged_FFT = Cursor_Y1_LEChanged_FFT
    Cursor_Y2_LEChanged_FFT = Cursor_Y2_LEChanged_FFT
    UpdateCursorDeltaX_FFT = UpdateCursorDeltaX_FFT
    UpdateCursorDeltaY_FFT = UpdateCursorDeltaY_FFT
    CursorKnob_FFT = CursorKnob_FFT
    CursorSelectCBChanged_FreqResp_Magn = CursorSelectCBChanged_FreqResp_Magn
    Cursor_X1_LEChanged_FreqResp_Magn = Cursor_X1_LEChanged_FreqResp_Magn
    Cursor_X2_LEChanged_FreqResp_Magn = Cursor_X2_LEChanged_FreqResp_Magn
    Cursor_Y1_LEChanged_FreqResp_Magn = Cursor_Y1_LEChanged_FreqResp_Magn
    Cursor_Y2_LEChanged_FreqResp_Magn = Cursor_Y2_LEChanged_FreqResp_Magn
    UpdateCursorDeltaX_FreqResp_Magn = UpdateCursorDeltaX_FreqResp_Magn
    UpdateCursorDeltaY_FreqResp_Magn = UpdateCursorDeltaY_FreqResp_Magn
    CursorKnob_FreqResp_Magn = CursorKnob_FreqResp_Magn
    CursorSelectCBChanged_FreqResp_Phase = CursorSelectCBChanged_FreqResp_Phase
    Cursor_X1_LEChanged_FreqResp_Phase = Cursor_X1_LEChanged_FreqResp_Phase
    Cursor_X2_LEChanged_FreqResp_Phase = Cursor_X2_LEChanged_FreqResp_Phase
    Cursor_Y1_LEChanged_FreqResp_Phase = Cursor_Y1_LEChanged_FreqResp_Phase
    Cursor_Y2_LEChanged_FreqResp_Phase = Cursor_Y2_LEChanged_FreqResp_Phase
    UpdateCursorDeltaX_FreqResp_Phase = UpdateCursorDeltaX_FreqResp_Phase
    UpdateCursorDeltaY_FreqResp_Phase = UpdateCursorDeltaY_FreqResp_Phase
    CursorKnob_FreqResp_Phase = CursorKnob_FreqResp_Phase
    removeCursorLines = removeCursorLines
    TriggerActivated = TriggerActivated
    TrigTypeCBChanged = TrigTypeCBChanged
    TrigModeCBChanged = TrigModeCBChanged
    UpdateTriggerLine = UpdateTriggerLine
    UpdateTimeScale = UpdateTimeScale
    UpdateVDivCH1 = UpdateVDivCH1
    UpdateVDivCH2 = UpdateVDivCH2
    UpdateVDivMath = UpdateVDivMath
    UpdatePositionCH1 = UpdatePositionCH1
    UpdatePositionCH2 = UpdatePositionCH2
    UpdatePositionMath = UpdatePositionMath
    FreezeActivated = FreezeActivated
    ChangeMathMode = ChangeMathMode
    resizeEvent = resizeEvent
    resizeHelp = resizeHelp
    resetSystem = resetSystem
    FFT_xBotLimLE_Changed = FFT_xBotLimLE_Changed
    FFT_xTopLimLE_Changed = FFT_xTopLimLE_Changed
    FFT_yBotLimLE_Changed = FFT_yBotLimLE_Changed
    FFT_yTopLimLE_Changed = FFT_yTopLimLE_Changed
    FFT_restoreDefault = FFT_restoreDefault
    updateLissajous = updateLissajous
    updatePhasDiag = updatePhasDiag
    togglePhasDiag = togglePhasDiag
    toggleLissaj = toggleLissaj
    phasDiagChangeMagnitVoltage = phasDiagChangeMagnitVoltage
    exportData = exportData
    exportImage = exportImage
    fadeIn = fadeIn
    fadeOut = fadeOut
    should_show_welcome = should_show_welcome
    closeWelcomeWindow = closeWelcomeWindow
    save_show_welcome = save_show_welcome
    changeMainSecondScr_1_to_2 = changeMainSecondScr_1_to_2
    changeMainSecondScr_2_to_1 = changeMainSecondScr_2_to_1
    SubmitTimeValue = SubmitTimeValue
    ChangeRefChannel = ChangeRefChannel
    ChangeAttnFactorCH1 = ChangeAttnFactorCH1
    ChangeAttnFactorCH2 = ChangeAttnFactorCH2
    currentInVerticalScale = currentInVerticalScale
    adjustCursorYAxisLabels = adjustCursorYAxisLabels
    shuntResLineEdit_CH1 = shuntResLineEdit_CH1
    shuntResLineEdit_CH2 = shuntResLineEdit_CH2
    shuntResLineEdit_Math = shuntResLineEdit_Math
    openCalibManual = openCalibManual
    closeCalibManual = closeCalibManual
    onSpinBoxTyping_offsetCH1 = onSpinBoxTyping_offsetCH1
    onSpinBoxEditingFinished_offsetCH1 = onSpinBoxEditingFinished_offsetCH1
    onSpinBoxValueChanged_offsetCH1 = onSpinBoxValueChanged_offsetCH1
    changeFrequency_Mouse_offsetCH1 = changeFrequency_Mouse_offsetCH1
    changeFrequency_Keyboard_offsetCH1 = changeFrequency_Keyboard_offsetCH1
    onSpinBoxTyping_offsetCH2 = onSpinBoxTyping_offsetCH2
    onSpinBoxEditingFinished_offsetCH2 = onSpinBoxEditingFinished_offsetCH2
    onSpinBoxValueChanged_offsetCH2 = onSpinBoxValueChanged_offsetCH2
    changeFrequency_Mouse_offsetCH2 = changeFrequency_Mouse_offsetCH2
    changeFrequency_Keyboard_offsetCH2 = changeFrequency_Keyboard_offsetCH2
    onSpinBoxTyping_attnCH1 = onSpinBoxTyping_attnCH1
    onSpinBoxEditingFinished_attnCH1 = onSpinBoxEditingFinished_attnCH1
    onSpinBoxValueChanged_attnCH1 = onSpinBoxValueChanged_attnCH1
    changeFrequency_Mouse_attnCH1 = changeFrequency_Mouse_attnCH1
    changeFrequency_Keyboard_attnCH1 = changeFrequency_Keyboard_attnCH1
    onSpinBoxTyping_attnCH2 = onSpinBoxTyping_attnCH2
    onSpinBoxEditingFinished_attnCH2 = onSpinBoxEditingFinished_attnCH2
    onSpinBoxValueChanged_attnCH2 = onSpinBoxValueChanged_attnCH2
    changeFrequency_Mouse_attnCH2 = changeFrequency_Mouse_attnCH2
    changeFrequency_Keyboard_attnCH2 = changeFrequency_Keyboard_attnCH2
    onSpinBoxTyping_phaseCorr = onSpinBoxTyping_phaseCorr
    onSpinBoxEditingFinished_phaseCorr = onSpinBoxEditingFinished_phaseCorr
    onSpinBoxValueChanged_phaseCorr = onSpinBoxValueChanged_phaseCorr
    changeFrequency_Mouse_phaseCorr = changeFrequency_Mouse_phaseCorr
    changeFrequency_Keyboard_phaseCorr = changeFrequency_Keyboard_phaseCorr
    onSpinBoxTyping_samplingRate = onSpinBoxTyping_samplingRate
    onSpinBoxEditingFinished_samplingRate = onSpinBoxEditingFinished_samplingRate
    onSpinBoxValueChanged_samplingRate = onSpinBoxValueChanged_samplingRate
    changeFrequency_Mouse_samplingRate = changeFrequency_Mouse_samplingRate
    changeFrequency_Keyboard_samplingRate = changeFrequency_Keyboard_samplingRate
    btSave_calibManual_clicked = btSave_calibManual_clicked
    saveCalibrationParams = saveCalibrationParams
    calibWizardIsOn = calibWizardIsOn
    manageCalibWizard = manageCalibWizard
    onSpinBoxTyping_samplingRate_sampRateWin = onSpinBoxTyping_samplingRate_sampRateWin
    onSpinBoxEditingFinished_samplingRate_sampRateWin = onSpinBoxEditingFinished_samplingRate_sampRateWin
    onSpinBoxValueChanged_samplingRate_sampRateWin = onSpinBoxValueChanged_samplingRate_sampRateWin
    changeFrequency_Mouse_samplingRate_sampRateWin = changeFrequency_Mouse_samplingRate_sampRateWin
    changeFrequency_Keyboard_samplingRate_sampRateWin = changeFrequency_Keyboard_samplingRate_sampRateWin
    onSpinBoxTyping_samplingRate_finalWin = onSpinBoxTyping_samplingRate_finalWin
    onSpinBoxEditingFinished_samplingRate_finalWin = onSpinBoxEditingFinished_samplingRate_finalWin
    onSpinBoxValueChanged_samplingRate_finalWin = onSpinBoxValueChanged_samplingRate_finalWin
    changeFrequency_Mouse_samplingRate_finalWin = changeFrequency_Mouse_samplingRate_finalWin
    changeFrequency_Keyboard_samplingRate_finalWin = changeFrequency_Keyboard_samplingRate_finalWin
    onSpinBoxTyping_offsCH1_offsSoftWin = onSpinBoxTyping_offsCH1_offsSoftWin
    onSpinBoxEditingFinished_offsCH1_offsSoftWin = onSpinBoxEditingFinished_offsCH1_offsSoftWin
    onSpinBoxValueChanged_offsCH1_offsSoftWin = onSpinBoxValueChanged_offsCH1_offsSoftWin
    changeFrequency_Mouse_offsCH1_offsSoftWin = changeFrequency_Mouse_offsCH1_offsSoftWin
    changeFrequency_Keyboard_offsCH1_offsSoftWin = changeFrequency_Keyboard_offsCH1_offsSoftWin
    onSpinBoxTyping_offsCH1_finalWin = onSpinBoxTyping_offsCH1_finalWin
    onSpinBoxEditingFinished_offsCH1_finalWin = onSpinBoxEditingFinished_offsCH1_finalWin
    onSpinBoxValueChanged_offsCH1_finalWin = onSpinBoxValueChanged_offsCH1_finalWin
    changeFrequency_Mouse_offsCH1_finalWin = changeFrequency_Mouse_offsCH1_finalWin
    changeFrequency_Keyboard_offsCH1_finalWin = changeFrequency_Keyboard_offsCH1_finalWin
    onSpinBoxTyping_offsCH2_offsSoftWin = onSpinBoxTyping_offsCH2_offsSoftWin
    onSpinBoxEditingFinished_offsCH2_offsSoftWin = onSpinBoxEditingFinished_offsCH2_offsSoftWin
    onSpinBoxValueChanged_offsCH2_offsSoftWin = onSpinBoxValueChanged_offsCH2_offsSoftWin
    changeFrequency_Mouse_offsCH2_offsSoftWin = changeFrequency_Mouse_offsCH2_offsSoftWin
    changeFrequency_Keyboard_offsCH2_offsSoftWin = changeFrequency_Keyboard_offsCH2_offsSoftWin
    onSpinBoxTyping_offsCH2_finalWin = onSpinBoxTyping_offsCH2_finalWin
    onSpinBoxEditingFinished_offsCH2_finalWin = onSpinBoxEditingFinished_offsCH2_finalWin
    onSpinBoxValueChanged_offsCH2_finalWin = onSpinBoxValueChanged_offsCH2_finalWin
    changeFrequency_Mouse_offsCH2_finalWin = changeFrequency_Mouse_offsCH2_finalWin
    changeFrequency_Keyboard_offsCH2_finalWin = changeFrequency_Keyboard_offsCH2_finalWin
    onSpinBoxTyping_attnCH1_attnWin = onSpinBoxTyping_attnCH1_attnWin
    onSpinBoxEditingFinished_attnCH1_attnWin = onSpinBoxEditingFinished_attnCH1_attnWin
    onSpinBoxValueChanged_attnCH1_attnWin = onSpinBoxValueChanged_attnCH1_attnWin
    changeFrequency_Mouse_attnCH1_attnWin = changeFrequency_Mouse_attnCH1_attnWin
    changeFrequency_Keyboard_attnCH1_attnWin = changeFrequency_Keyboard_attnCH1_attnWin
    onSpinBoxTyping_attnCH1_finalWin = onSpinBoxTyping_attnCH1_finalWin
    onSpinBoxEditingFinished_attnCH1_finalWin = onSpinBoxEditingFinished_attnCH1_finalWin
    onSpinBoxValueChanged_attnCH1_finalWin = onSpinBoxValueChanged_attnCH1_finalWin
    changeFrequency_Mouse_attnCH1_finalWin = changeFrequency_Mouse_attnCH1_finalWin
    changeFrequency_Keyboard_attnCH1_finalWin = changeFrequency_Keyboard_attnCH1_finalWin
    onSpinBoxTyping_attnCH2_attnWin = onSpinBoxTyping_attnCH2_attnWin
    onSpinBoxEditingFinished_attnCH2_attnWin = onSpinBoxEditingFinished_attnCH2_attnWin
    onSpinBoxValueChanged_attnCH2_attnWin = onSpinBoxValueChanged_attnCH2_attnWin
    changeFrequency_Mouse_attnCH2_attnWin = changeFrequency_Mouse_attnCH2_attnWin
    changeFrequency_Keyboard_attnCH2_attnWin = changeFrequency_Keyboard_attnCH2_attnWin
    onSpinBoxTyping_attnCH2_finalWin = onSpinBoxTyping_attnCH2_finalWin
    onSpinBoxEditingFinished_attnCH2_finalWin = onSpinBoxEditingFinished_attnCH2_finalWin
    onSpinBoxValueChanged_attnCH2_finalWin = onSpinBoxValueChanged_attnCH2_finalWin
    changeFrequency_Mouse_attnCH2_finalWin = changeFrequency_Mouse_attnCH2_finalWin
    changeFrequency_Keyboard_attnCH2_finalWin = changeFrequency_Keyboard_attnCH2_finalWin
    onSpinBoxTyping_phaseCorr_phaseCorrWin = onSpinBoxTyping_phaseCorr_phaseCorrWin
    onSpinBoxEditingFinished_phaseCorr_phaseCorrWin = onSpinBoxEditingFinished_phaseCorr_phaseCorrWin
    onSpinBoxValueChanged_phaseCorr_phaseCorrWin = onSpinBoxValueChanged_phaseCorr_phaseCorrWin
    changeFrequency_Mouse_phaseCorr_phaseCorrWin = changeFrequency_Mouse_phaseCorr_phaseCorrWin
    changeFrequency_Keyboard_phaseCorr_phaseCorrWin = changeFrequency_Keyboard_phaseCorr_phaseCorrWin
    onSpinBoxTyping_phaseCorr_finalWin = onSpinBoxTyping_phaseCorr_finalWin
    onSpinBoxEditingFinished_phaseCorr_finalWin = onSpinBoxEditingFinished_phaseCorr_finalWin
    onSpinBoxValueChanged_phaseCorr_finalWin = onSpinBoxValueChanged_phaseCorr_finalWin
    changeFrequency_Mouse_phaseCorr_finalWin = changeFrequency_Mouse_phaseCorr_finalWin
    changeFrequency_Keyboard_phaseCorr_finalWin = changeFrequency_Keyboard_phaseCorr_finalWin
    updateCalibWizLineEdits = updateCalibWizLineEdits
    CalibWizSupportAdjusts = CalibWizSupportAdjusts
    resetCalibWizChanges = resetCalibWizChanges
    saveCalibWizChanges = saveCalibWizChanges
    resizeCalibWiz = resizeCalibWiz
    playPauseSweep = playPauseSweep
    start_sweep = start_sweep
    advanceSweep = advanceSweep
    captureSamples = captureSamples
    pauseOrResumeSweep = pauseOrResumeSweep
    stopSweep = stopSweep
    clearSweeps = clearSweeps
    changePlotColor = changePlotColor
    changeFunctionType = changeFunctionType
    change_numPoints_LE_FreqResp = change_numPoints_LE_FreqResp
    change_initFreq_LE_FreqResp = change_initFreq_LE_FreqResp
    change_finalFreq_LE_FreqResp = change_finalFreq_LE_FreqResp
    syncXAxis = syncXAxis
    FreqResp_xBotLimLE_Changed = FreqResp_xBotLimLE_Changed
    FreqResp_xTopLimLE_Changed = FreqResp_xTopLimLE_Changed
    FreqResp_yBotLimLE_Changed = FreqResp_yBotLimLE_Changed
    FreqResp_yTopLimLE_Changed = FreqResp_yTopLimLE_Changed
    FreqResp_yBotLimLE_phase_Changed = FreqResp_yBotLimLE_phase_Changed
    FreqResp_yTopLimLE_phase_Changed = FreqResp_yTopLimLE_phase_Changed
    FreqResp_restoreDefault = FreqResp_restoreDefault
    changeFreqRespAxis = changeFreqRespAxis
    sweepControl_Play = sweepControl_Play
    sweepControl_Stop = sweepControl_Stop
    finish_stop = finish_stop
    sweepProgressBar_valueChanged = sweepProgressBar_valueChanged
    measurements = measurements
    plotUpdate = plotUpdate
    saveLanguage = saveLanguage
    loadLanguage = loadLanguage
    changeSystemLanguage = changeSystemLanguage
    helpScrLangEnglish = helpScrLangEnglish
    
    

    def pauseTrigger(self, interval):
        self.mainScr.dataHandler.triggerPauseTimer.setInterval(interval)
        self.mainScr.dataHandler.triggerPauseTimer.start()

    def open_WFM_supportScreen(self):
        self.WFM_supportScreen.open()


    def WFM_In_Screen3(self):
        self.tertiaryScreen.setCurrentIndex(1)
        
    def Calib_In_Screen3(self):
        self.tertiaryScreen.setCurrentIndex(2)
        
    
    def Export_In_Screen3(self):
        self.tertiaryScreen.setCurrentIndex(3)
        

    def MathPlus_In_Screen3(self):
        self.tertiaryScreen.setCurrentIndex(4)
        
        
    def OpenBiggerMathWindow(self):
        self.mathPlusBiggerWindow.exec()

    
    def openSite(self): #botão de site
        QDesktopServices.openUrl(QUrl("https://myoscilloscope.lme.usp.br/"))

    def openCredits(self): 
        self.creditsScreen.open()

    def isSerialOk(self): #entenda o nome da função como uma pergunta
        if self.mainScr.serialErrorFlag: self.serialConnectionError()

    def activatePhaseCorr(self):
        if self.calib_scr2.phaseCorr_CheckBox.isChecked():
            self.mainScr.phaseCorrActive = True
        else:
            self.mainScr.phaseCorrActive = False

    def changeState_LPF(self):
        if self.calib_scr2.LPF_CheckBox.isChecked():
            self.mainScr.LPF_isOn = True
            self.mainScr.cutoffFreq = int(self.mainScr.samplingRate/2)
            self.calib_scr2.LPF_LE.setText(f"{int(self.mainScr.samplingRate/2)}")
        else:
            self.mainScr.LPF_isOn = False

    def changeLPF_cutoffFreq(self):
        insertedText = self.calib_scr2.LPF_LE.text()

        try:
            value = float(insertedText)
            self.mainScr.cutoffFreq = value
            if value < 20:
                value = 20
                self.calib_scr2.LPF_LE.setText("20")
            elif value > 5e5:
                value = 500000
                self.calib_scr2.LPF_LE.setText("500000")

        except ValueError:
            self.mainScr.cutoffFreq = int(self.mainScr.samplingRate/2)
            self.calib_scr2.LPF_LE.setText(f"{int(self.mainScr.samplingRate/2)}")


    #Funções de comunicação serial
    def searchCOMPorts(self):
        if not self.mainScr.COMPortON:
            serial_connection = None
            port = "COM1"
            baudrate = 1000000
            bytesize = 8
            parity = 'N'
            stopbits = 1
            timeout = None

            for i in range(0, 100):
                self.mainScr.startSerial(
                    f"COM{i}", firstTry=False, notViaMain=True)
                if self.mainScr.COMPortON:
                    self.COMPort.COM_PortLE.setText(f"COM{i}")
                    self.COMPort.signalIconGreen.setGeometry(int(self.p * 350), int(self.p * 32), int(self.p * 38), int(self.p * 38))
                    self.COMPort.signalIconRed.setGeometry(-400, -400, -400, -400)

                    self.screen1.setGeometry(int(self.p * 17), int(self.p * 336), int(self.p * 990), int(self.p * 511))
                    if self.language == "English": self.standbyScr1.updatePixmap(self.standbyScr1.pixmap1)
                    else: self.standbyScr1.updatePixmap(self.standbyScr1.pixmap3)
                    self.WFMgeneratorScr.serialBlockingWFM = False

                    try:
                        if self.COMPortScr: self.COMPortScr.closeWindow()
                    except (AttributeError, RuntimeError):
                        pass
                    return
                
            #Se chegou até aqui, comunicação mal-sucedida...
            self.screen1.setGeometry(int(self.p * 17), int(self.p * 336), int(self.p * 990), int(self.p * 511))
            if self.language == "English": 
                self.standbyScr1.updatePixmap(self.standbyScr1.pixmap2)

            else: 
                self.standbyScr1.updatePixmap(self.standbyScr1.pixmap4)

            self.COMPortScr.open()
            self.WFMgeneratorScr.serialBlockingWFM = True

    def serialConnectionError(self):
        if self.mainScr.serialErrorFlag: self.mainScr.serialErrorFlag = False
        self.primaryScreen.setCurrentIndex(0)
        self.secondaryScreen.setCurrentIndex(0)
        self.turnEverythingToOFF(partialShutdown=True)
        if self.WFMgeneratorScr.btOnOff_isOn: self.WFMgeneratorScr.WFMBtOnOff()
            
        if self.btOnOff.isOn: 
            #para evitar um bug:
            self.screenName = ""
            self.UpdatePrimaryButtons()
        
        self.screen1.setGeometry(int(self.p * 17), int(self.p * 336), int(self.p * 990), int(self.p * 511))
        if self.language == "English": self.standbyScr1.updatePixmap(self.standbyScr1.pixmap2)
        else: self.standbyScr1.updatePixmap(self.standbyScr1.pixmap4)

       
        if self.language == "English": self.COMPort.COM_PortLE.setText("No Port.")
        else:                          self.COMPort.COM_PortLE.setText("Nenhuma Porta.")

        try:
            self.raise_()
            if self.WFM_supportScreen: self.WFM_supportScreen.close()
            if self.calibWizScr: self.calibWizScr.close()
            if self.savedCalibScr: self.savedCalibScr.close()
            if self.captureScreen: self.captureScreen.close()
        except (AttributeError, RuntimeError):
            pass

        if self.btOnOff.isOn: self.COMPortScr.open()
        self.COMPort.signalIconRed.setGeometry(int(self.p * 350), int(self.p * 32), int(self.p * 38), int(self.p * 38))
        self.COMPort.signalIconGreen.setGeometry(-400, -400, -400, -400)
        self.WFMgeneratorScr.serialBlockingWFM = True
        

    #O que ocorre quando a janela principal encerra...
    def closeEvent(self, event):
        
            self.mainScr.stopSerial()
            try:
                if self.WFM_supportScreen: self.WFM_supportScreen.close()
            except (AttributeError, RuntimeError):
                pass
            try:
                if self.calibWizScr: self.calibWizScr.close()
            except (AttributeError, RuntimeError):
                pass
            try:
                if self.savedCalibScr: self.savedCalibScr.close()
            except (AttributeError, RuntimeError):
                pass
            try:
                if self.COMPortScr: self.COMPortScr.closeWindow()
            except (AttributeError, RuntimeError):
                pass
            try:
                if self.creditsScreen: self.creditsScreen.close()
            except (AttributeError, RuntimeError):
                pass
            try:
                if self.captureScreen: self.captureScreen.close()
            except (AttributeError, RuntimeError):
                pass
        
if __name__ == '__main__':
    app = QApplication([])
    window = MyOscPiWindow()
    window.show()
    app.exec()