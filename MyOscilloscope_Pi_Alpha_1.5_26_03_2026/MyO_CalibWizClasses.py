
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QLabel, QCheckBox, QLineEdit, QSpinBox, QDoubleSpinBox, QStackedWidget, QComboBox
from PySide6.QtGui import QIcon, QFont, QPixmap
from PySide6 import QtCore
from PySide6.QtCore import Qt
from button import Button


class CalibWizard(QMainWindow):
    def __init__(self ):
        super(CalibWizard, self).__init__()
        self.setGeometry(350, 350, 1024, 768)
        self.setFixedSize(1024, 768)
        self.setWindowTitle("Calibration Wizard")
        self.setWindowIcon(QIcon("images/MyOscPi_RedIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        #para deixar a janela no centro da tela - também aplicado nas demais janelas
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())

        # pega o X centralizado
        x = window_geometry.topLeft().x()

        # força Y = 0
        self.move(x, 0)

        #Coloca todas as janelas num StackedWidget (pilha de janelas):
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        

        self.mainWin = CalibWizardMainWindow()
        self.sampRateWin = CalibWizardSampRateWindow()
        self.offsSoftwareWin = CalibWizardOffsetSoftwareWindow()
        self.offsPhysicalWin = CalibWizardOffsetPhysicalWindow()
        self.attnWin = CalibWizardAttenuationWindow()
        self.phaseCorrWin = CalibWizardPhaseCorrectionWindow()
        self.finalWin = CalibWizardFinalWindow()

        self.stack.addWidget(self.mainWin)
        self.stack.addWidget(self.sampRateWin)
        self.stack.addWidget(self.offsSoftwareWin)
        self.stack.addWidget(self.offsPhysicalWin)
        self.stack.addWidget(self.attnWin)
        self.stack.addWidget(self.phaseCorrWin)
        self.stack.addWidget(self.finalWin)
        self.stack.setCurrentIndex(0)

        #Flags dos checkboxes da janela inicial:
        self.sampRateOn = True
        self.offsSoftOn = True
        self.offsPhysOn = True
        self.attnOn = True
        self.phaseCorrOn = True

        #Alteração das flags acima conforme variação das checkboxes da janela inicial:
        self.mainWin.samplingRateAdjustCheckBox.stateChanged.connect(self.ChangeCheckboxFlags_sampRate)
        self.mainWin.offsetSoftwareAdjustCheckBox.stateChanged.connect(self.ChangeCheckboxFlags_offsSoft)
        self.mainWin.offsetPhysicalAdjustCheckbox.stateChanged.connect(self.ChangeCheckboxFlags_offsPhys)
        self.mainWin.attenuationAdjustCheckBox.stateChanged.connect(self.ChangeCheckboxFlags_attn)
        self.mainWin.phaseCorrAdjustCheckBox.stateChanged.connect(self.ChangeCheckboxFlags_phaseCorr)
        

        #Conectando todos os botões Cancel ao fechamento da janela:
        self.mainWin.CancelButton.clicked.connect(self.closeWizard_btCancel)
        self.sampRateWin.CancelButton.clicked.connect(self.closeWizard_btCancel)
        self.offsSoftwareWin.CancelButton.clicked.connect(self.closeWizard_btCancel)
        self.offsPhysicalWin.CancelButton.clicked.connect(self.closeWizard_btCancel)
        self.attnWin.CancelButton.clicked.connect(self.closeWizard_btCancel)
        self.phaseCorrWin.CancelButton.clicked.connect(self.closeWizard_btCancel)
        self.finalWin.CancelButton.clicked.connect(self.closeWizard_btCancel)

        self.finalWin.SaveButton.clicked.connect(self.closeWizard_btSave)

        #Conexão de todos os demais botões do sistema da "central de atualização de botões"
        self.mainWin.NextButton.clicked.connect(self.Main_NextBt)

        self.sampRateWin.PreviousButton.clicked.connect(self.SampRate_PrevBt)
        self.sampRateWin.NextButton.clicked.connect(self.SampRate_NextBt)

        self.offsSoftwareWin.PreviousButton.clicked.connect(self.OffsSoft_PrevBt)
        self.offsSoftwareWin.NextButton.clicked.connect(self.OffsSoft_NextBt)

        self.offsPhysicalWin.PreviousButton.clicked.connect(self.OffsPhys_PrevBt)
        self.offsPhysicalWin.NextButton.clicked.connect(self.OffsPhys_NextBt)

        self.attnWin.PreviousButton.clicked.connect(self.Attn_PrevBt)
        self.attnWin.NextButton.clicked.connect(self.Attn_NextBt)

        self.phaseCorrWin.PreviousButton.clicked.connect(self.PhaseCorr_PrevBt)
        self.phaseCorrWin.NextButton.clicked.connect(self.PhaseCorr_NextBt)

        self.finalWin.PreviousButton.clicked.connect(self.Final_PrevBt)


        #idioma:
        self.language = "English"


        #timer para atualizar os line edits em MyOscilloscopePi.py
        self.updateTimerIsOn = True

        #timer para realizar alterações no programa principal em momentos específicos da calibração:
        
        self.calibrationSupportTimer = QtCore.QTimer()
        self.calibrationSupportTimer.setInterval(10)
        self.calibrationSupportTimer.setSingleShot(True)

        #Para fechar o programa de maneira diferente entre fechar pelo X, pelo Cancel ou pelo Save.
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.CLOSE_CANCEL = 0
        self.CLOSE_SAVE = 1
        self.closeReason = self.CLOSE_CANCEL

        #timer para resetar alterações no programa principal ao clicar em algum Cancel ou no X:
        
        self.resetCalibWizChangesTimer = QtCore.QTimer()
        self.resetCalibWizChangesTimer.setInterval(10)
        self.resetCalibWizChangesTimer.setSingleShot(True)
    

    def Main_NextBt(self):
        if self.sampRateOn: self.stack.setCurrentIndex(1)
        elif self.offsSoftOn: self.stack.setCurrentIndex(2)
        elif self.offsPhysOn: self.stack.setCurrentIndex(3)
        elif self.attnOn: self.stack.setCurrentIndex(4) 
        elif self.phaseCorrOn: self.stack.setCurrentIndex(5)
        else: self.stack.setCurrentIndex(6)
        self.ChangeWindowName()
        self.calibrationSupportTimer.start()

    def SampRate_PrevBt(self):
        self.stack.setCurrentIndex(0)
        self.ChangeWindowName()
        self.calibrationSupportTimer.start()
        

    def SampRate_NextBt(self):
        if self.offsSoftOn: self.stack.setCurrentIndex(2)
        elif self.offsPhysOn: self.stack.setCurrentIndex(3)
        elif self.attnOn: self.stack.setCurrentIndex(4) 
        elif self.phaseCorrOn: self.stack.setCurrentIndex(5)
        else: self.stack.setCurrentIndex(6)
        self.ChangeWindowName()
        self.calibrationSupportTimer.start()

    def OffsSoft_PrevBt(self):
        if self.sampRateOn: self.stack.setCurrentIndex(1)
        else: self.stack.setCurrentIndex(0)
        self.ChangeWindowName()
        self.calibrationSupportTimer.start()

    def OffsSoft_NextBt(self):
        if self.offsPhysOn: self.stack.setCurrentIndex(3)
        elif self.attnOn: self.stack.setCurrentIndex(4) 
        elif self.phaseCorrOn: self.stack.setCurrentIndex(5)
        else: self.stack.setCurrentIndex(6)
        self.ChangeWindowName()
        self.calibrationSupportTimer.start()

    def OffsPhys_PrevBt(self):
        if self.offsSoftOn: self.stack.setCurrentIndex(2)
        elif self.sampRateOn: self.stack.setCurrentIndex(1)
        else: self.stack.setCurrentIndex(0)
        self.ChangeWindowName()
        self.calibrationSupportTimer.start()

    def OffsPhys_NextBt(self):
        if self.attnOn: self.stack.setCurrentIndex(4) 
        elif self.phaseCorrOn: self.stack.setCurrentIndex(5)
        else: self.stack.setCurrentIndex(6)
        self.ChangeWindowName()
        self.calibrationSupportTimer.start()

    def Attn_PrevBt(self):
        if self.offsPhysOn: self.stack.setCurrentIndex(3)
        elif self.offsSoftOn: self.stack.setCurrentIndex(2)
        elif self.sampRateOn: self.stack.setCurrentIndex(1)
        else: self.stack.setCurrentIndex(0)
        self.ChangeWindowName()
        self.calibrationSupportTimer.start()

    def Attn_NextBt(self):
        if self.phaseCorrOn: self.stack.setCurrentIndex(5)
        else: self.stack.setCurrentIndex(6)
        self.ChangeWindowName()
        self.calibrationSupportTimer.start()

    def PhaseCorr_PrevBt(self):
        if self.attnOn: self.stack.setCurrentIndex(4)
        elif self.offsPhysOn: self.stack.setCurrentIndex(3)
        elif self.offsSoftOn: self.stack.setCurrentIndex(2)
        elif self.sampRateOn: self.stack.setCurrentIndex(1)
        else: self.stack.setCurrentIndex(0)
        self.ChangeWindowName()
        self.calibrationSupportTimer.start()
    
    def PhaseCorr_NextBt(self):
        self.stack.setCurrentIndex(6)
        self.ChangeWindowName()
        self.calibrationSupportTimer.start()

    def Final_PrevBt(self):
        if self.phaseCorrOn: self.stack.setCurrentIndex(5)
        elif self.attnOn: self.stack.setCurrentIndex(4)
        elif self.offsPhysOn: self.stack.setCurrentIndex(3)
        elif self.offsSoftOn: self.stack.setCurrentIndex(2)
        elif self.sampRateOn: self.stack.setCurrentIndex(1)
        else: self.stack.setCurrentIndex(0)
        self.ChangeWindowName()
        self.calibrationSupportTimer.start()

    def ChangeCheckboxFlags_sampRate(self):
        self.sampRateOn = self.mainWin.samplingRateAdjustCheckBox.isChecked()

    def ChangeCheckboxFlags_offsSoft(self):
        self.offsSoftOn = self.mainWin.offsetSoftwareAdjustCheckBox.isChecked()

    def ChangeCheckboxFlags_offsPhys(self):
        self.offsPhysOn = self.mainWin.offsetPhysicalAdjustCheckbox.isChecked()

    def ChangeCheckboxFlags_attn(self):
        self.attnOn = self.mainWin.attenuationAdjustCheckBox.isChecked()

    def ChangeCheckboxFlags_phaseCorr(self):
        self.phaseCorrOn = self.mainWin.phaseCorrAdjustCheckBox.isChecked()

    def ChangeWindowName(self):
        if self.language == "English":
            
            if self.stack.currentIndex() == 1: self.setWindowTitle("Calibration Wizard - Sampling Rate")
            elif self.stack.currentIndex() == 2: self.setWindowTitle("Calibration Wizard - Offset (Software)")
            elif self.stack.currentIndex() == 3: self.setWindowTitle("Calibration Wizard - Offset (Physical)")
            elif self.stack.currentIndex() == 4: self.setWindowTitle("Calibration Wizard - Attenuation")
            elif self.stack.currentIndex() == 5: self.setWindowTitle("Calibration Wizard - Phase Correction")
            else: self.setWindowTitle("Calibration Wizard")

        else: #self.language == "Português":
            if self.stack.currentIndex() == 1: self.setWindowTitle("Assistente de Calibração - Frequência de Amostragem")
            elif self.stack.currentIndex() == 2: self.setWindowTitle("Assistente de Calibração - Zero Físico 1")
            elif self.stack.currentIndex() == 3: self.setWindowTitle("Assistente de Calibração - Zero Físico 2")
            elif self.stack.currentIndex() == 4: self.setWindowTitle("Assistente de Calibração - Atenuação")
            elif self.stack.currentIndex() == 5: self.setWindowTitle("Assistente de Calibração - Correção de Fase")
            else: self.setWindowTitle("Assistente de Calibração")

    def ChangeLanguage(self):
        self.ChangeWindowName()

        if self.language == "English":
            #Labels de Main:
            self.mainWin.sentenceLabel.setText("Welcome to Calibration Wizard!\nPlease select the adjustments you want to perform:")
            self.mainWin.samplingRateAdjustCheckBox.setText("Sampling Rate Adjust")
            self.mainWin.offsetSoftwareAdjustCheckBox.setText("Offset Adjust (Software)")
            self.mainWin.offsetPhysicalAdjustCheckbox.setText("Offset Adjust (Shield)")
            self.mainWin.attenuationAdjustCheckBox.setText("Channel Attenuation Adjust")
            self.mainWin.phaseCorrAdjustCheckBox.setText("Phase Correction Adjust")
            self.mainWin.checkBoxSupportLabel.setText("It is recommended to perform all adjustments in the indicated order for proper calibration.")

            #Labels de SamplingRate:
            self.sampRateWin.titleLabel.setText("Sampling Rate")
            self.sampRateWin.titleLabel.setFont(QFont("Calibri", 42))
            # self.sampRateWin.titleLabel.setGeometry(500, 60, 450, 100)
            #self.sampRateWin.sentence1Label.setGeometry(10, 150, 1010, 90)
            self.sampRateWin.sentence1Label.setText(
                "Take the P2 cable included in the kit. Connect its P2 end to the computer audio output, "
                "connect its\nblack jumper wire to a GND input "
                "and its other jumper wires to the AC1 and AC2 inputs on the Shield."
            )

            self.sampRateWin.sentence2Label.setText(
                "Set a signal frequency and turn on the Waveform Generator. "
                "\nAdjust the calibration parameter until the measured frequency matches the generated value."
            )

            self.sampRateWin.shieldSupportLabel.setText("Shield with indicated inputs")
            self.sampRateWin.cableSupportLabel.setText("P2-jumper wires cable")
            self.sampRateWin.samplingRateLabel.setText("Sampling Rate\n(S/s):")
            self.sampRateWin.samplingRateSupportLabel.setText("Adjust here and then click Next!")


            #Labels de Offset Software:
            self.offsSoftwareWin.titleLabel.setText("Offset (Software)")

            self.offsSoftwareWin.sentence1Label.setText(
                "Turn off the Waveform Generator and disconnect the jumper wires of the P2 cable from the\n"
                "Shield. Using two jumper wires, connect the DC1 and "
                "DC2 inputs to its GND input."
            )

            self.offsSoftwareWin.sentence2Label.setText(
                "Both channels should indicate a constant, zero-level signal, which may require "
                "calibration to achieve.\nCH1 and CH2 are set to the smallest possible vertical scale. "
                "For each channel, adjust the\ncalibration parameter so that the absolute value of the "
                "average signal is less than or equal to 1 mV."
            )

            self.offsSoftwareWin.shieldSupportLabel.setText("Shield with indicated inputs")
            self.offsSoftwareWin.offsetSupportLabel.setText("Adjust here and then click Next!")
            self.offsSoftwareWin.meanLabel_CH1.setText("DC - Mean")
            self.offsSoftwareWin.meanLabel_CH2.setText("DC - Mean")


            #Labels de Offset Physical:
            self.offsPhysicalWin.titleLabel.setText("Offset (Physical)")

            self.offsPhysicalWin.sentence1Label.setText(
                "In this adjustment, no calibration parameters in the interface will be modified. This time, "
                "the\nadjustment is performed directly on the Shield by adjusting the calibration "
                "potentiometers. For this,\na tool such as a screwdriver or something that allows you to "
                "adjust the potentiometers will be required."
            )

            self.offsPhysicalWin.sentence2Label.setText(
                "Disconnect the jumper wires from all Shield inputs. Adjust the potentiometers so that,\n"
                "in this condition, the average value of each channel is as close to zero as possible."
            )
            self.offsPhysicalWin.meanLabel_CH1.setText("DC - Mean")
            self.offsPhysicalWin.meanLabel_CH2.setText("DC - Mean")


            #Labels de Attn:
            self.attnWin.titleLabel.setText("Attenuation")

            self.attnWin.sentence1Label.setText(
                "Using two jumper wires, connect the DC1 and "
                "DC2 inputs\nto the 2.5 V reference voltage input of the Shield."
            )

            self.attnWin.sentence2Label.setText(
                "Both channels should indicate a 2.5 VDC signal, which may require "
                "calibration to achieve.\n"
                "For each channel, adjust the calibration parameter so that the average signal is as close as possible\n"
                "to 2.5 V."
            )

            
            self.attnWin.attnSupportLabel.setText("Adjust here and then click Next!")
            self.attnWin.meanLabel_CH1.setText("DC - Mean")
            self.attnWin.meanLabel_CH2.setText("DC - Mean")


            #Labels de Phase Corr:
            self.phaseCorrWin.titleLabel.setText("Phase Correction")

            self.phaseCorrWin.sentence1Label.setText(
                "The Waveform Generator frequency is now set to 9 kHz. Take the P2 cable and connect it "
                "to the\ncomputer’s audio output. Connect the black jumper wire of the cable to a GND input "
                "and another\njumper wire of the cable to the DC1 input. The remaining jumper wire should "
                "remain disconnected.\nTake an additional jumper wire and connect the DC1 input to the DC2 input."
            )

            self.phaseCorrWin.sentence2Label.setText(
                "Turn on Waveform Generator with 100% Amplitude signal. Since both channels are measuring the same signal, the phase difference between them should be as close to zero as possible. To achieve this, adjust the phase correction calibration parameter."
            )

            self.phaseCorrWin.shieldSupportLabel.setText("Shield with indicated inputs")
            self.phaseCorrWin.phaseCorrSupportLabel.setText("Adjust here and then click Next!")
            
            self.phaseCorrWin.phaseLabel_CH1.setText("Phase Shift")
            self.phaseCorrWin.phaseLabel_CH2.setText("Phase Shift")

            #Labels tela final:
            self.finalWin.sentenceLabel.setText("The obtained calibration parameters are listed below.")
            self.finalWin.sentence2Label.setText(
                "Click Save to save them, or click Cancel to exit the wizard without saving.")
            

        else: #self.language == "Português":
            #Labels de Main:
            self.mainWin.sentenceLabel.setText("Bem-vindo(a) ao Assistente de Calibração!\nSelecione os ajustes que deseja realizar:")
            self.mainWin.samplingRateAdjustCheckBox.setText("Frequência de Amostragem")
            self.mainWin.offsetSoftwareAdjustCheckBox.setText("Zero Físico 1")
            self.mainWin.offsetPhysicalAdjustCheckbox.setText("Zero Físico 2")
            self.mainWin.attenuationAdjustCheckBox.setText("Atenuação")
            self.mainWin.phaseCorrAdjustCheckBox.setText("Correção de Fase")
            self.mainWin.checkBoxSupportLabel.setText("Recomenda-se realizar todos os ajustes, na ordem indicada, para uma boa calibração.")

            #Labels de SamplingRate:
            self.sampRateWin.titleLabel.setText("Frequência de Amostragem")
            self.sampRateWin.titleLabel.setGeometry(390, 20, 650, 260)
            self.sampRateWin.titleLabel.setFont(QFont("Calibri", 32))
            # self.sampRateWin.sentence1Label.setStyleSheet("""
            #     color: rgb(240, 240, 240);
            #     background-color: rgba(0, 255, 0, 80);
            # """)
            #self.sampRateWin.sentence1Label.setGeometry(10, 190, 1010, 90)
            self.sampRateWin.sentence1Label.setText(
                "Pegue o cabo P2 presente no kit. Conecte sua saída P2 à saída de áudio do computador. Conecte o jumper preto desse cabo a uma entrada GND, e os demais jumpers nas entradas AC1 e AC2 do Shield, como indicado na figura."
            )

            self.sampRateWin.sentence2Label.setText(
                "No Waveform Generator, defina uma frequência (500 Hz, por exemplo) e o ligue. Ajuste o parâmetro de calibração até que a frequência medida coincida com a gerada."
            )

            self.sampRateWin.shieldSupportLabel.setText("Shield com entradas indicadas")
            self.sampRateWin.cableSupportLabel.setText("Cabo P2-jumpers")
            self.sampRateWin.samplingRateLabel.setText("Freq. Amost. \n(S/s):")
            self.sampRateWin.samplingRateSupportLabel.setText("Ajuste aqui e, então, clique em Next!")
            self.sampRateWin.frequencyLabel.setText("Frequência:")
            self.sampRateWin.frequencyLabel_WFM.setText("WFM Generator\nFrequência:")


            #Labels de Offset Software:
            self.offsSoftwareWin.titleLabel.setText("Zero Físico 1")

            self.offsSoftwareWin.sentence1Label.setText(
                "Desligue o Waveform Generator e desconecte os jumpers do cabo P2 do Shield. Usando dois jumpers avulsos, conecte as entradas DC1 e DC2 a uma de suas entradas GND."
            )

            self.offsSoftwareWin.sentence2Label.setText(
                "Nessa situação, os dois canais devem indicar sinal constante e nulo, o que deve requerer calibração. CH1 e CH2 já estão automaticamente definidos na menor escala vertical possível. Para cada canal, ajuste os parâmetros de calibração de maneira que o valor médio dos sinais seja menor ou igual a 1 mV."
            )

            self.offsSoftwareWin.shieldSupportLabel.setText("Shield com entradas indicadas")
            self.offsSoftwareWin.offsetSupportLabel.setText("Ajuste aqui e, então, clique em Next!")
            self.offsSoftwareWin.meanLabel_CH1.setText("Valor médio (DC):")
            self.offsSoftwareWin.meanLabel_CH2.setText("Valor médio (DC):")


            #Labels de Offset Physical:
            self.offsPhysicalWin.titleLabel.setText("Zero Físico 2")

            self.offsPhysicalWin.sentence1Label.setText(
                "Neste ajuste, não iremos alterar nenhum parâmetro de calibração. Desta vez, o ajuste será realizado diretamente no Shield, ao ajustar os potenciômetros de calibração. Para isso, uma ferramenta como uma chave de fenda ou algo que te permita ajustar os potenciômetros será necessário."
            )

            self.offsPhysicalWin.sentence2Label.setText(
                "Desconecte os jumpers de todas as entradas do Shield, se houver. Ajuste os dois potenciômetros da placa para que, nessa condição, o valor médio de cada canal seja o mais próximo de zero que puder."
            )
            self.offsPhysicalWin.meanLabel_CH1.setText("Valor médio (DC):")
            self.offsPhysicalWin.meanLabel_CH2.setText("Valor médio (DC):")

            #Labels de Attn:
            self.attnWin.titleLabel.setText("Atenuação")

            self.attnWin.sentence1Label.setText(
                "Usando dois jumpers, conecte as entradas DC1 e DC2 na entrada com tensão de referência de 2,5 V DC do Shield."
            )

            self.attnWin.sentence2Label.setText(
                "Os dois canais devem indicar valor médio de 2,5 V, o que pode exigir calibração para que aconteça. Para cada canal, ajuste os parâmetros de calibração para que o valor médio seja o mais próximo de 2,5 V."
            )

            
            self.attnWin.attnSupportLabel.setText("Ajuste aqui e, então, clique em Next!")
            self.attnWin.meanLabel_CH1.setText("Valor médio (DC):")
            self.attnWin.meanLabel_CH2.setText("Valor médio (DC):")

            #Labels de Phase Corr:
            self.phaseCorrWin.titleLabel.setText("Correção de Fase")

            self.phaseCorrWin.sentence1Label.setText(
                "A frequência do Waveform Generator está automaticamente definida em 9 kHz. Pegue o cabo P2 e o conecte na saída de áudio do computador. Conecte o jumper preto do cabo à uma entrada GND e outro jumper do cabo à entrada DC1. O jumper restante deve permanecer desconectado. Pegue um jumper avulso e conecte a entrada DC1 à entrada DC2."
            )

            self.phaseCorrWin.sentence2Label.setText(
                "Ligue o Waveform Generator e o deixe com amplitude em 100%. Uma vez que ambos os canais medem o mesmo sinal, a defasagem entre ambos deve ser a mais próxima possível de zero. Para alcançar isso, ajuste o parâmetro de calibração de correção de fase."
            )

            self.phaseCorrWin.shieldSupportLabel.setText("Shield com entradas indicadas")
            self.phaseCorrWin.phaseCorrSupportLabel.setText("Ajuste aqui e, então, clique em Next!")
            self.phaseCorrWin.phaseLabel_CH1.setText("Defasagem:")
            self.phaseCorrWin.phaseLabel_CH2.setText("Defasagem:")

            #Labels tela final:
            self.finalWin.sentenceLabel.setText("Os parâmetros de calibração obtidos estão presentes abaixo.")
            self.finalWin.sentence2Label.setText(
                "Para salvá-los, clique em Save. Para sair sem salvar, clique em Cancel.")

    def closeWizard_btCancel(self):
        self.closeReason = self.CLOSE_CANCEL
        self.close()

    def closeWizard_btSave(self):
        self.closeReason = self.CLOSE_SAVE
        self.close()

    def closeEvent(self, event): #Também chamado em MyOscilloscopePi.py
        if self.closeReason == self.CLOSE_CANCEL: self.resetCalibWizChangesTimer.start()
        self.stack.setCurrentIndex(0)
        self.updateTimerIsOn = False
        event.accept()


class CalibWizardMainWindow(QMainWindow):
    def __init__(self ):
        super(CalibWizardMainWindow, self).__init__()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setGeometry(350, 350, 1024, 768)
        self.setFixedSize(1024, 768)
        self.setWindowTitle("Calibration Wizard")
        self.setWindowIcon(QIcon("images/MyOscPi_RedIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        #para deixar a janela no centro da tela - também aplicado nas demais janelas
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())


        self.mainLabel = QLabel("", self)
        self.mainLabel.setAlignment(Qt.AlignHCenter)
        self.mainLabel.setGeometry(20, 30, 970, 350)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.mainImage = QPixmap("images/calibWizard.png")

        scaled_mainImage = self.mainImage.scaled(
            self.mainLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.mainLabel.setPixmap(scaled_mainImage)

        self.sentenceLabel = QLabel("Welcome to Calibration Wizard!\nPlease select the adjustments you want to perform:", self)
        self.sentenceLabel.setGeometry(190, 335, 600, 70)
        self.sentenceLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentenceLabel.setAlignment(Qt.AlignHCenter)
        self.sentenceLabel.setFont(QFont("Franklin Gothic Medium", 16))

        self.samplingRateAdjustCheckBox = QCheckBox("Sampling Rate Adjust", self)
        self.samplingRateAdjustCheckBox.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.samplingRateAdjustCheckBox.setFont(QFont("Franklin Gothic Medium", 14))
        self.samplingRateAdjustCheckBox.setGeometry(190, 430, 300, 50)
        self.samplingRateAdjustCheckBox.setChecked(True)

        self.offsetSoftwareAdjustCheckBox = QCheckBox("Offset Adjust (Software)", self)
        self.offsetSoftwareAdjustCheckBox.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.offsetSoftwareAdjustCheckBox.setFont(QFont("Franklin Gothic Medium", 14))
        self.offsetSoftwareAdjustCheckBox.setGeometry(190, 480, 300, 50)
        self.offsetSoftwareAdjustCheckBox.setChecked(True)

        self.offsetPhysicalAdjustCheckbox = QCheckBox("Offset Adjust (Shield)", self)
        self.offsetPhysicalAdjustCheckbox.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.offsetPhysicalAdjustCheckbox.setFont(QFont("Franklin Gothic Medium", 14))
        self.offsetPhysicalAdjustCheckbox.setGeometry(190, 530, 300, 50)
        self.offsetPhysicalAdjustCheckbox.setChecked(True)

        self.attenuationAdjustCheckBox = QCheckBox("Channel Attenuation Adjust", self)
        self.attenuationAdjustCheckBox.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.attenuationAdjustCheckBox.setFont(QFont("Franklin Gothic Medium", 14))
        self.attenuationAdjustCheckBox.setGeometry(190, 580, 300, 50)
        self.attenuationAdjustCheckBox.setChecked(True)

        self.phaseCorrAdjustCheckBox = QCheckBox("Phase Correction", self)
        self.phaseCorrAdjustCheckBox.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.phaseCorrAdjustCheckBox.setFont(QFont("Franklin Gothic Medium", 14))
        self.phaseCorrAdjustCheckBox.setGeometry(190, 630, 300, 50)
        self.phaseCorrAdjustCheckBox.setChecked(True)

        self.CancelButton = Button(self, 10, 720, 200, 40, "",
                                    "images/Bt_Cancel.png", "images/Bt_Cancel.png",  False)
        
        self.NextButton = Button(self, 800, 720, 450, 40, "",
                                    "images/Bt_Next.png", "images/Bt_Next.png",  False)
        
        

        self.checkBoxSupportLabel = QLabel("It is recommended to perform all adjustments in the indicated order for proper calibration.", self)
        self.checkBoxSupportLabel.setGeometry(-30, 680, 1024, 30)
        self.checkBoxSupportLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.checkBoxSupportLabel.setAlignment(Qt.AlignHCenter)
        self.checkBoxSupportLabel.setFont(QFont("Franklin Gothic Medium", 9))


class CalibWizardSampRateWindow(QMainWindow):
    def __init__(self ):
        super(CalibWizardSampRateWindow, self).__init__()
        #self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setGeometry(350, 350, 1024, 768)
        self.setFixedSize(1024, 768)
        self.setWindowTitle("Calibration Wizard - Sampling Rate")
        self.setWindowIcon(QIcon("images/MyOscPi_RedIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())


        self.mainLabel = QLabel("", self)
        self.mainLabel.setAlignment(Qt.AlignHCenter)
        self.mainLabel.setGeometry(10, 30, 400, 175)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        mainImage = QPixmap("images/calibWizard.png")

        scaled_mainImage = mainImage.scaled(
            self.mainLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.mainLabel.setPixmap(scaled_mainImage)

        self.titleLabel = QLabel("Sampling Rate", self)
        self.titleLabel.setGeometry(500, 60, 450, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.titleLabel.setAlignment(Qt.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 42))

        self.sentence1Label = QLabel("Take the P2 cable included in the kit. Connect its P2 end to the computer audio output, "+ 
                                    "connect its\nblack jumper wire to a GND input " + 
                                    "and its other jumper wires to the AC1 and AC2 inputs on the Shield.", self)

                                    
        self.sentence1Label.setGeometry(10, 150, 1010, 90)
        self.sentence1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentence1Label.setAlignment(Qt.AlignHCenter)
        self.sentence1Label.setFont(QFont("Franklin Gothic Medium", 14))
        self.sentence1Label.setWordWrap(True)

        self.shieldLabel = QLabel("Shield image", self)
        self.shieldLabel.setGeometry(550, 250, 400, 240)
        self.shieldLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: rgba(255, 0, 0, 80);
        """)

        shieldImage = QPixmap("images/calibWizardSampRateShield.png")
        scaled_shieldImage = shieldImage.scaled(
            self.shieldLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.shieldLabel.setPixmap(scaled_shieldImage)


        self.shieldSupportLabel = QLabel("Shield with indicated inputs", self)
        self.shieldSupportLabel.setGeometry(680, 490, 200, 30)
        self.shieldSupportLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)

        self.cableSupportLabel = QLabel("P2-jumper wires cable", self)
        self.cableSupportLabel.setGeometry(190, 490, 170, 30)
        self.cableSupportLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)

        self.cableLabel = QLabel("P2 image", self)
        self.cableLabel.setGeometry(100, 250, 300, 240)
        self.cableLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: rgba(0, 255, 0, 80);
        """)

        cableImage = QPixmap("images/calibWizardSampRateP2Cable.png")
        scaled_cableImage = cableImage.scaled(
            self.cableLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.cableLabel.setPixmap(scaled_cableImage)

        self.sentence2Label = QLabel("Set a signal frequency and turn on the Waveform Generator. " +
        "\nAdjust the calibration parameter until the measured frequency matches the generated value.", self)
                       
        self.sentence2Label.setGeometry(10, 520, 1010, 500)
        self.sentence2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentence2Label.setAlignment(Qt.AlignHCenter)
        self.sentence2Label.setFont(QFont("Franklin Gothic Medium", 14))
        self.sentence2Label.setWordWrap(True)

        #da aba measure
        self.measureLabel = QLabel("Measure", self)
        self.measureLabel.setGeometry(420, 670, 151, 28)
        self.measureLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.measureLabel.setAlignment(Qt.AlignHCenter)
        self.measureLabel.setFont(QFont("Microsoft Sans Serif", 16))
        self.frequencyLabel = QLabel("Frequency ", self)
        self.frequencyLabel.setGeometry(425, 700, 141, 22)
        self.frequencyLabel.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.frequencyLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.frequencyLabel.setAlignment(Qt.AlignHCenter)
        self.freqLE = QLineEdit(self)
        self.freqLE.setGeometry(425, 720, 141, 20)
        self.freqLE.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.freqLE.setText("500 Hz")
        self.freqLE.setAlignment(Qt.AlignHCenter)
        self.freqLE.setReadOnly(True)

        #baseado no gerador de funções:
        self.frequencyLabel_WFM = QLabel("WFM Generator\nFrequency:", self)
        self.frequencyLabel_WFM.setGeometry(425, 600, 141, 42)
        self.frequencyLabel_WFM.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.frequencyLabel_WFM.setFont(QFont("Microsoft Sans Serif", 10))
        self.frequencyLabel_WFM.setAlignment(Qt.AlignHCenter)
        self.freqLE_WFM = QLineEdit(self)
        self.freqLE_WFM.setGeometry(425, 640, 141, 20)
        self.freqLE_WFM.setStyleSheet("background-color: rgb(62, 200, 52); color: rgb(240, 240, 240) ")
        self.freqLE_WFM.setText("500 Hz")
        self.freqLE_WFM.setAlignment(Qt.AlignHCenter)
        self.freqLE_WFM.setReadOnly(True)

        #da janela calibManual:
        self.samplingRateLabel = QLabel("Sampling Rate\n(S/s):", self)
        self.samplingRateLabel.setGeometry(50, 600, 160, 100)
        self.samplingRateLabel.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.samplingRateLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.samplingRateLabel.setAlignment(Qt.AlignHCenter)
        self.samplingRateSB = QSpinBox(self)
        self.samplingRateSB.setRange(0, 250000)  # mínimo e máximo
        self.samplingRateSB.setSingleStep(2)  # incremento/decremento
        self.samplingRateSB.setValue(19232)
        self.samplingRateSB.setGeometry(205, 600, 100, 30)
        self.samplingRateSB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.samplingRateSB.setAlignment(Qt.AlignHCenter)
        self.samplingRateSB.setFont(QFont("Microsoft Sans Serif", 10))
        self.samplingRateSB.setReadOnly(False)

        self.samplingRateSupportLabel = QLabel("Adjust here and then click Next!", self)
        self.samplingRateSupportLabel.setGeometry(60, 640, 260, 30)
        self.samplingRateSupportLabel.setStyleSheet(""" color: blue""")
        self.samplingRateSupportLabel.setFont(QFont("Calibri", 10))
        self.samplingRateSupportLabel.setAlignment(Qt.AlignHCenter)


        self.CancelButton = Button(self, 10, 720, 200, 40, "",
                                    "images/Bt_Cancel.png", "images/Bt_Cancel.png",  False)
        
        self.NextButton = Button(self, 800, 720, 450, 40, "",
                                    "images/Bt_Next.png", "images/Bt_Next.png",  False)
        
        self.PreviousButton = Button(self, 800, 660, 450, 40, "",
                                    "images/Bt_Previous.png", "images/Bt_Previous.png",  False)
        
        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: rgba(150, 150, 150, 50);
        """)
        self.backgroundLabel.setGeometry(0, 590, 1024, 160)
        self.backgroundLabel.setAttribute(Qt.WA_TransparentForMouseEvents)


class CalibWizardOffsetSoftwareWindow(QMainWindow):
    def __init__(self ):
        super(CalibWizardOffsetSoftwareWindow, self).__init__()
        #self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setGeometry(350, 350, 1024, 768)
        self.setFixedSize(1024, 768)
        self.setWindowTitle("Calibration Wizard - Offset (Software)")
        self.setWindowIcon(QIcon("images/MyOscPi_RedIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())


        self.mainLabel = QLabel("", self)
        self.mainLabel.setAlignment(Qt.AlignHCenter)
        self.mainLabel.setGeometry(10, 30, 400, 175)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        mainImage = QPixmap("images/calibWizard.png")

        scaled_mainImage = mainImage.scaled(
            self.mainLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.mainLabel.setPixmap(scaled_mainImage)

        self.titleLabel = QLabel("Offset (Software)", self)
        self.titleLabel.setGeometry(450, 60, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.titleLabel.setAlignment(Qt.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 42))

        self.sentence1Label = QLabel("Turn off the Waveform Generator and disconnect the jumper wires of the P2 cable from the\n"+
                                     "Shield. Using two jumper wires, connect the DC1 and " +
                                      "DC2 inputs to its GND input.", self)

        # "Set a signal frequency in the Waveform Generator. " +
        # "\nAdjust the calibration parameter until the measured frequency matches the generated value."
                                    
        self.sentence1Label.setGeometry(10, 160, 1010, 150)
        self.sentence1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentence1Label.setAlignment(Qt.AlignHCenter)
        self.sentence1Label.setFont(QFont("Franklin Gothic Medium", 14))
        self.sentence1Label.setWordWrap(True)

        self.shieldLabel = QLabel("Shield image", self)
        self.shieldLabel.setGeometry(190, 240, 650, 240)
        self.shieldLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: rgba(255, 0, 0, 80);
        """)

        shieldImage = QPixmap("images/calibWizardOffsetShield.png")
        scaled_shieldImage = shieldImage.scaled(
            self.shieldLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.shieldLabel.setPixmap(scaled_shieldImage)


        self.shieldSupportLabel = QLabel("Shield with indicated inputs", self)
        self.shieldSupportLabel.setGeometry(430, 480, 200, 30)
        self.shieldSupportLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)

        self.sentence2Label = QLabel("Both channels should indicate a constant, zero-level signal, which may require " + 
                                     "calibration to achieve.\nCH1 and CH2 are set to the smallest possible vertical scale. "+
                                     "For each channel, adjust the\ncalibration parameter so that the absolute value of the " + 
                                     "average signal is less than or equal to 1 mV.", self)

        # "Set a signal frequency in the Waveform Generator. " +
        # "\nAdjust the calibration parameter until the measured frequency matches the generated value."
                                    
        self.sentence2Label.setGeometry(10, 510, 1010, 150)
        self.sentence2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentence2Label.setAlignment(Qt.AlignHCenter)
        self.sentence2Label.setFont(QFont("Franklin Gothic Medium", 14))
        self.sentence2Label.setWordWrap(True)

        #da aba measure
        self.measureLabel = QLabel("Measure", self)
        self.measureLabel.setGeometry(440, 610, 151, 28)
        self.measureLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.measureLabel.setAlignment(Qt.AlignHCenter)
        self.measureLabel.setFont(QFont("Microsoft Sans Serif", 16))
        self.meanLabel_CH1 = QLabel("DC - Mean ", self)
        self.meanLabel_CH1.setGeometry(445, 680, 141, 22)
        self.meanLabel_CH1.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.meanLabel_CH1.setFont(QFont("Microsoft Sans Serif", 10))
        self.meanLabel_CH1.setAlignment(Qt.AlignHCenter)
        self.meanLE_CH1 = QLineEdit(self)
        self.meanLE_CH1.setGeometry(445, 700, 141, 20)
        self.meanLE_CH1.setAlignment(Qt.AlignHCenter)
        self.meanLE_CH1.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.meanLE_CH1.setText("1.2 V")
        self.meanLE_CH1.setReadOnly(True)

        self.meanLabel_CH2 = QLabel("DC - Mean ", self)
        self.meanLabel_CH2.setGeometry(620, 680, 141, 22)
        self.meanLabel_CH2.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.meanLabel_CH2.setFont(QFont("Microsoft Sans Serif", 10))
        self.meanLabel_CH2.setAlignment(Qt.AlignHCenter)
        self.meanLE_CH2 = QLineEdit(self)
        self.meanLE_CH2.setGeometry(620, 700, 141, 20)
        self.meanLE_CH2.setAlignment(Qt.AlignHCenter)
        self.meanLE_CH2.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.meanLE_CH2.setText("1.2 V")
        self.meanLE_CH2.setReadOnly(True)

        self.CH1Label = QLabel("CH1", self)
        self.CH1Label.setGeometry(435, 650, 151, 22)
        self.CH1Label.setStyleSheet(""" color: blue """)
        self.CH1Label.setAlignment(Qt.AlignHCenter)
        self.CH1Label.setFont(QFont("Microsoft Sans Serif", 11))

        self.CH2Label = QLabel("CH2", self)
        self.CH2Label.setGeometry(610, 650, 151, 22)
        self.CH2Label.setStyleSheet(""" color: red """)
        self.CH2Label.setAlignment(Qt.AlignHCenter)
        self.CH2Label.setFont(QFont("Microsoft Sans Serif", 11))

        self.offsetCH1Label = QLabel("Offset CH1:", self)
        self.offsetCH1Label.setGeometry(100, 640, 100, 22)
        self.offsetCH1Label.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.offsetCH1Label.setFont(QFont("Microsoft Sans Serif", 10))
        self.offsetCH1Label.setAlignment(Qt.AlignHCenter)
        self.offsetCH1SB = QDoubleSpinBox(self)
        self.offsetCH1SB.setRange(0, 1000000.000)  # mínimo e máximo
        self.offsetCH1SB.setSingleStep(0.010)  # incremento/decremento
        self.offsetCH1SB.setValue(1.500)
        self.offsetCH1SB.setDecimals(3)
        self.offsetCH1SB.setGeometry(205, 635, 100, 30)
        self.offsetCH1SB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.offsetCH1SB.setAlignment(Qt.AlignHCenter)
        self.offsetCH1SB.setFont(QFont("Microsoft Sans Serif", 10))
        self.offsetCH1SB.setReadOnly(False)

        self.offsetCH2Label = QLabel("Offset CH2:", self)
        self.offsetCH2Label.setGeometry(100, 680, 100, 22)
        self.offsetCH2Label.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.offsetCH2Label.setFont(QFont("Microsoft Sans Serif", 10))
        self.offsetCH2Label.setAlignment(Qt.AlignHCenter)
        self.offsetCH2SB = QDoubleSpinBox(self)
        self.offsetCH2SB.setRange(0, 1000000.000)  # mínimo e máximo
        self.offsetCH2SB.setSingleStep(0.010)  # incremento/decremento
        self.offsetCH2SB.setValue(1.500)
        self.offsetCH2SB.setDecimals(3)
        self.offsetCH2SB.setGeometry(205, 675, 100, 30)
        self.offsetCH2SB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.offsetCH2SB.setAlignment(Qt.AlignHCenter)
        self.offsetCH2SB.setFont(QFont("Microsoft Sans Serif", 10))
        self.offsetCH2SB.setReadOnly(False)

        self.offsetSupportLabel = QLabel("Adjust here and then click Next!", self)
        self.offsetSupportLabel.setGeometry(70, 610, 260, 20)
        self.offsetSupportLabel.setStyleSheet(""" color: blue""")
        self.offsetSupportLabel.setFont(QFont("Calibri", 10))
        self.offsetSupportLabel.setAlignment(Qt.AlignHCenter)

        self.CancelButton = Button(self, 10, 720, 200, 40, "",
                                    "images/Bt_Cancel.png", "images/Bt_Cancel.png",  False)
        
        self.NextButton = Button(self, 800, 720, 450, 40, "",
                                    "images/Bt_Next.png", "images/Bt_Next.png",  False)
        
        self.PreviousButton = Button(self, 800, 660, 450, 40, "",
                                    "images/Bt_Previous.png", "images/Bt_Previous.png",  False)
        
        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: rgba(150, 150, 150, 50);
        """)
        self.backgroundLabel.setGeometry(0, 600, 1024, 150)
        self.backgroundLabel.setAttribute(Qt.WA_TransparentForMouseEvents)

class CalibWizardOffsetPhysicalWindow(QMainWindow):
    def __init__(self ):
        super(CalibWizardOffsetPhysicalWindow, self).__init__()
        #self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setGeometry(350, 350, 1024, 768)
        self.setFixedSize(1024, 768)
        self.setWindowTitle("Calibration Wizard - Offset (Physical)")
        self.setWindowIcon(QIcon("images/MyOscPi_RedIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

        self.mainLabel = QLabel("", self)
        self.mainLabel.setAlignment(Qt.AlignHCenter)
        self.mainLabel.setGeometry(10, 30, 400, 175)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        mainImage = QPixmap("images/calibWizard.png")

        scaled_mainImage = mainImage.scaled(
            self.mainLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.mainLabel.setPixmap(scaled_mainImage)

        self.titleLabel = QLabel("Offset (Physical)", self)
        self.titleLabel.setGeometry(450, 60, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.titleLabel.setAlignment(Qt.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 42))

        self.sentence1Label = QLabel("In this adjustment, no calibration parameters in the interface will be modified. This time, "+
                                     "the\nadjustment is performed directly on the Shield by adjusting the calibration " + ""
                                     "potentiometers. For this,\na tool such as a screwdriver or something that allows you to " +
                                     "adjust the potentiometers will be required.", self)

        # "Set a signal frequency in the Waveform Generator. " +
        # "\nAdjust the calibration parameter until the measured frequency matches the generated value."
                                    
        self.sentence1Label.setGeometry(10, 160, 1010, 150)
        self.sentence1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentence1Label.setAlignment(Qt.AlignHCenter)
        self.sentence1Label.setFont(QFont("Franklin Gothic Medium", 14))
        self.sentence1Label.setWordWrap(True)

        self.calibPotentiometersLabel = QLabel("calibPotentiometers image", self)
        self.calibPotentiometersLabel.setGeometry(90, 250, 850, 240)
        self.calibPotentiometersLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: rgba(255, 0, 0, 80);
        """)

        calibPotentiometersImage = QPixmap("images/calibWizardCalibPotentiometers.png")
        scaled_calibPotentiometersImage = calibPotentiometersImage.scaled(
            self.calibPotentiometersLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.calibPotentiometersLabel.setPixmap(scaled_calibPotentiometersImage)


        # self.shieldSupportLabel = QLabel("Calibration potentiometers Time!", self)
        # self.shieldSupportLabel.setGeometry(410, 490, 300, 30)
        # self.shieldSupportLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)

        self.sentence2Label = QLabel("Disconnect the jumper wires from all Shield inputs. Adjust the potentiometers so that,\n" +
                                     "in this condition, the average value of each channel is as close to zero as possible.", self)

        # "Set a signal frequency in the Waveform Generator. " +
        # "\nAdjust the calibration parameter until the measured frequency matches the generated value."
                                    
        self.sentence2Label.setGeometry(10, 530, 1010, 150)
        self.sentence2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentence2Label.setAlignment(Qt.AlignHCenter)
        self.sentence2Label.setFont(QFont("Franklin Gothic Medium", 14))
        self.sentence2Label.setWordWrap(True)

        #da aba measure
        self.measureLabel = QLabel("Measure", self)
        self.measureLabel.setGeometry(385, 610, 151, 28)
        self.measureLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.measureLabel.setAlignment(Qt.AlignHCenter)
        self.measureLabel.setFont(QFont("Microsoft Sans Serif", 16))
        self.meanLabel_CH1 = QLabel("DC - Mean ", self)
        self.meanLabel_CH1.setGeometry(305, 680, 141, 22)
        self.meanLabel_CH1.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.meanLabel_CH1.setFont(QFont("Microsoft Sans Serif", 10))
        self.meanLabel_CH1.setAlignment(Qt.AlignHCenter)
        self.meanLE_CH1 = QLineEdit(self)
        self.meanLE_CH1.setGeometry(305, 700, 141, 20)
        self.meanLE_CH1.setAlignment(Qt.AlignHCenter)
        self.meanLE_CH1.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.meanLE_CH1.setText("1.2 V")
        self.meanLE_CH1.setReadOnly(True)

        self.meanLabel_CH2 = QLabel("DC - Mean ", self)
        self.meanLabel_CH2.setGeometry(480, 680, 141, 22)
        self.meanLabel_CH2.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.meanLabel_CH2.setFont(QFont("Microsoft Sans Serif", 10))
        self.meanLabel_CH2.setAlignment(Qt.AlignHCenter)
        self.meanLE_CH2 = QLineEdit(self)
        self.meanLE_CH2.setGeometry(480, 700, 141, 20)
        self.meanLE_CH2.setAlignment(Qt.AlignHCenter)
        self.meanLE_CH2.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.meanLE_CH2.setText("1.2 V")
        self.meanLE_CH2.setReadOnly(True)

        self.CH1Label = QLabel("CH1", self)
        self.CH1Label.setGeometry(295, 650, 151, 22)
        self.CH1Label.setStyleSheet(""" color: blue """)
        self.CH1Label.setAlignment(Qt.AlignHCenter)
        self.CH1Label.setFont(QFont("Microsoft Sans Serif", 11))

        self.CH2Label = QLabel("CH2", self)
        self.CH2Label.setGeometry(470, 650, 151, 22)
        self.CH2Label.setStyleSheet(""" color: red """)
        self.CH2Label.setAlignment(Qt.AlignHCenter)
        self.CH2Label.setFont(QFont("Microsoft Sans Serif", 11))

        self.CancelButton = Button(self, 10, 720, 200, 40, "",
                                    "images/Bt_Cancel.png", "images/Bt_Cancel.png",  False)
        
        self.NextButton = Button(self, 800, 720, 450, 40, "",
                                    "images/Bt_Next.png", "images/Bt_Next.png",  False)
        
        self.PreviousButton = Button(self, 800, 660, 450, 40, "",
                                    "images/Bt_Previous.png", "images/Bt_Previous.png",  False)
        
        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: rgba(150, 150, 150, 50);
        """)
        self.backgroundLabel.setGeometry(0, 600, 1024, 150)
        self.backgroundLabel.setAttribute(Qt.WA_TransparentForMouseEvents)

class CalibWizardAttenuationWindow(QMainWindow):
    def __init__(self ):
        super(CalibWizardAttenuationWindow, self).__init__()
        #self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setGeometry(350, 350, 1024, 768)
        self.setFixedSize(1024, 768)
        self.setWindowTitle("Calibration Wizard - Attenuation")
        self.setWindowIcon(QIcon("images/MyOscPi_RedIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())


        self.mainLabel = QLabel("", self)
        self.mainLabel.setAlignment(Qt.AlignHCenter)
        self.mainLabel.setGeometry(10, 30, 400, 175)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        mainImage = QPixmap("images/calibWizard.png")

        scaled_mainImage = mainImage.scaled(
            self.mainLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.mainLabel.setPixmap(scaled_mainImage)

        self.titleLabel = QLabel("Attenuation", self)
        self.titleLabel.setGeometry(450, 60, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.titleLabel.setAlignment(Qt.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 42))

        self.sentence1Label = QLabel("Using two jumper wires, connect the DC1 and" +
                                      " DC2 inputs\nto the 2.5 V reference voltage input of the Shield.", self)

        # "Set a signal frequency in the Waveform Generator. " +
        # "\nAdjust the calibration parameter until the measured frequency matches the generated value."
                                    
        self.sentence1Label.setGeometry(10, 160, 1010, 150)
        self.sentence1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentence1Label.setAlignment(Qt.AlignHCenter)
        self.sentence1Label.setFont(QFont("Franklin Gothic Medium", 14))
        self.sentence1Label.setWordWrap(True)

        self.shieldLabel = QLabel("Shield image", self)
        self.shieldLabel.setGeometry(180, 240, 660, 240)
        self.shieldLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: rgba(255, 0, 0, 80);
        """)

        shieldImage = QPixmap("images/calibWizardAttenuation.png")
        scaled_shieldImage = shieldImage.scaled(
            self.shieldLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.shieldLabel.setPixmap(scaled_shieldImage)


        # self.shieldSupportLabel = QLabel("Shield with indicated inputs", self)
        # self.shieldSupportLabel.setGeometry(410, 490, 200, 30)
        # self.shieldSupportLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)

        self.sentence2Label = QLabel("Both channels should indicate a 2.5 VDC signal, which may require " + 
                                     "calibration to achieve.\n"+
                                     "For each channel, adjust the calibration parameter so that the average signal is as close as possible\nto 2.5 V.", self)

        # "Set a signal frequency in the Waveform Generator. " +
        # "\nAdjust the calibration parameter until the measured frequency matches the generated value."
                                    
        self.sentence2Label.setGeometry(10, 510, 1010, 150)
        self.sentence2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentence2Label.setAlignment(Qt.AlignHCenter)
        self.sentence2Label.setFont(QFont("Franklin Gothic Medium", 14))
        self.sentence2Label.setWordWrap(True)

        #da aba measure
        self.measureLabel = QLabel("Measure", self)
        self.measureLabel.setGeometry(440, 610, 151, 28)
        self.measureLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.measureLabel.setAlignment(Qt.AlignHCenter)
        self.measureLabel.setFont(QFont("Microsoft Sans Serif", 16))
        self.meanLabel_CH1 = QLabel("DC - Mean ", self)
        self.meanLabel_CH1.setGeometry(445, 680, 141, 22)
        self.meanLabel_CH1.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.meanLabel_CH1.setFont(QFont("Microsoft Sans Serif", 10))
        self.meanLabel_CH1.setAlignment(Qt.AlignHCenter)
        self.meanLE_CH1 = QLineEdit(self)
        self.meanLE_CH1.setGeometry(445, 700, 141, 20)
        self.meanLE_CH1.setAlignment(Qt.AlignHCenter)
        self.meanLE_CH1.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.meanLE_CH1.setText("1.2 V")
        self.meanLE_CH1.setReadOnly(True)

        self.meanLabel_CH2 = QLabel("DC - Mean ", self)
        self.meanLabel_CH2.setGeometry(620, 680, 141, 22)
        self.meanLabel_CH2.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.meanLabel_CH2.setFont(QFont("Microsoft Sans Serif", 10))
        self.meanLabel_CH2.setAlignment(Qt.AlignHCenter)
        self.meanLE_CH2 = QLineEdit(self)
        self.meanLE_CH2.setGeometry(620, 700, 141, 20)
        self.meanLE_CH2.setAlignment(Qt.AlignHCenter)
        self.meanLE_CH2.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.meanLE_CH2.setText("1.2 V")
        self.meanLE_CH2.setReadOnly(True)

        self.CH1Label = QLabel("CH1", self)
        self.CH1Label.setGeometry(435, 650, 151, 22)
        self.CH1Label.setStyleSheet(""" color: blue """)
        self.CH1Label.setAlignment(Qt.AlignHCenter)
        self.CH1Label.setFont(QFont("Microsoft Sans Serif", 11))

        self.CH2Label = QLabel("CH2", self)
        self.CH2Label.setGeometry(610, 650, 151, 22)
        self.CH2Label.setStyleSheet(""" color: red """)
        self.CH2Label.setAlignment(Qt.AlignHCenter)
        self.CH2Label.setFont(QFont("Microsoft Sans Serif", 11))

        self.attnCH1Label = QLabel("Attn CH1:", self)
        self.attnCH1Label.setGeometry(100, 640, 100, 22)
        self.attnCH1Label.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.attnCH1Label.setFont(QFont("Microsoft Sans Serif", 10))
        self.attnCH1Label.setAlignment(Qt.AlignHCenter)
        self.attnCH1SB = QDoubleSpinBox(self)
        self.attnCH1SB.setRange(0, 1000000.000)  # mínimo e máximo
        self.attnCH1SB.setSingleStep(0.010)  # incremento/decremento
        self.attnCH1SB.setValue(1.500)
        self.attnCH1SB.setDecimals(3)
        self.attnCH1SB.setGeometry(205, 635, 100, 30)
        self.attnCH1SB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.attnCH1SB.setAlignment(Qt.AlignHCenter)
        self.attnCH1SB.setFont(QFont("Microsoft Sans Serif", 10))
        self.attnCH1SB.setReadOnly(False)

        self.attnCH2Label = QLabel("Attn CH2:", self)
        self.attnCH2Label.setGeometry(100, 680, 100, 22)
        self.attnCH2Label.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.attnCH2Label.setFont(QFont("Microsoft Sans Serif", 10))
        self.attnCH2Label.setAlignment(Qt.AlignHCenter)
        self.attnCH2SB = QDoubleSpinBox(self)
        self.attnCH2SB.setRange(0, 1000000.000)  # mínimo e máximo
        self.attnCH2SB.setSingleStep(0.010)  # incremento/decremento
        self.attnCH2SB.setValue(1.500)
        self.attnCH2SB.setDecimals(3)
        self.attnCH2SB.setGeometry(205, 675, 100, 30)
        self.attnCH2SB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.attnCH2SB.setAlignment(Qt.AlignHCenter)
        self.attnCH2SB.setFont(QFont("Microsoft Sans Serif", 10))
        self.attnCH2SB.setReadOnly(False)

        self.attnSupportLabel = QLabel("Adjust here and then click Next!", self)
        self.attnSupportLabel.setGeometry(70, 610, 260, 20)
        self.attnSupportLabel.setStyleSheet(""" color: blue""")
        self.attnSupportLabel.setFont(QFont("Calibri", 10))
        self.attnSupportLabel.setAlignment(Qt.AlignHCenter)

        self.CancelButton = Button(self, 10, 720, 200, 40, "",
                                    "images/Bt_Cancel.png", "images/Bt_Cancel.png",  False)
        
        self.NextButton = Button(self, 800, 720, 450, 40, "",
                                    "images/Bt_Next.png", "images/Bt_Next.png",  False)
        
        self.PreviousButton = Button(self, 800, 660, 450, 40, "",
                                    "images/Bt_Previous.png", "images/Bt_Previous.png",  False)
        
        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: rgba(150, 150, 150, 50);
        """)
        self.backgroundLabel.setGeometry(0, 600, 1024, 150)
        self.backgroundLabel.setAttribute(Qt.WA_TransparentForMouseEvents)

class CalibWizardPhaseCorrectionWindow(QMainWindow):
    def __init__(self ):
        super(CalibWizardPhaseCorrectionWindow, self).__init__()
        #self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setGeometry(350, 350, 1024, 768)
        self.setFixedSize(1024, 768)
        self.setWindowTitle("Calibration Wizard - Phase Correction")
        self.setWindowIcon(QIcon("images/MyOscPi_RedIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())


        self.mainLabel = QLabel("", self)
        self.mainLabel.setAlignment(Qt.AlignHCenter)
        self.mainLabel.setGeometry(10, 30, 400, 175)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        mainImage = QPixmap("images/calibWizard.png")

        scaled_mainImage = mainImage.scaled(
            self.mainLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.mainLabel.setPixmap(scaled_mainImage)

        self.titleLabel = QLabel("Phase Correction", self)
        self.titleLabel.setGeometry(450, 60, 550, 100)
        self.titleLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.titleLabel.setAlignment(Qt.AlignHCenter)
        self.titleLabel.setFont(QFont("Calibri", 42))

        self.sentence1Label = QLabel("The Waveform Generator frequency is now set to 9 kHz. Take the P2 cable and connect it "+
                                     "to the\ncomputer’s audio output. Connect the black jumper wire of the cable to a GND input "+
                                     "and another\njumper wire of the cable to the DC1 input. The remaining jumper wire should "+
                                     "remain disconnected.\nTake an additional jumper wire and connect the DC1 input to the DC2 input.", self)

        # "Set a signal frequency in the Waveform Generator. " +
        # "\nAdjust the calibration parameter until the measured frequency matches the generated value."
                                    
        self.sentence1Label.setGeometry(10, 160, 1010, 150)
        self.sentence1Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentence1Label.setAlignment(Qt.AlignHCenter)
        self.sentence1Label.setFont(QFont("Franklin Gothic Medium", 14))
        self.sentence1Label.setWordWrap(True)

        self.shieldLabel = QLabel("Shield image", self)
        self.shieldLabel.setGeometry(220, 280, 580, 190)
        self.shieldLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: rgba(255, 0, 0, 80);
        """)

        shieldImage = QPixmap("images/calibWizardPhaseCorrection.png")
        scaled_shieldImage = shieldImage.scaled(
            self.shieldLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.shieldLabel.setPixmap(scaled_shieldImage)


        self.shieldSupportLabel = QLabel("Shield with indicated inputs", self)
        self.shieldSupportLabel.setGeometry(410, 470, 200, 30)
        self.shieldSupportLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)

        self.sentence2Label = QLabel(
                "Turn on Waveform Generator. Since both channels are measuring the same signal, the phase\ndifference between them "
                "should be as close to zero as possible.\nTo achieve this, adjust the phase correction "
                "calibration parameter.", self)

        # "Set a signal frequency in the Waveform Generator. " +
        # "\nAdjust the calibration parameter until the measured frequency matches the generated value."
                                    
        self.sentence2Label.setGeometry(10, 510, 1010, 150)
        self.sentence2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentence2Label.setAlignment(Qt.AlignHCenter)
        self.sentence2Label.setFont(QFont("Franklin Gothic Medium", 14))
        self.sentence2Label.setWordWrap(True)

        #da aba measure
        self.measureLabel = QLabel("Measure", self)
        self.measureLabel.setGeometry(530, 610, 151, 28)
        self.measureLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.measureLabel.setAlignment(Qt.AlignHCenter)
        self.measureLabel.setFont(QFont("Microsoft Sans Serif", 16))

        self.phaseLabel_CH1 = QLabel("Phase Shift", self)
        self.phaseLabel_CH1.setGeometry(445, 680, 141, 22)
        self.phaseLabel_CH1.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.phaseLabel_CH1.setFont(QFont("Microsoft Sans Serif", 10))
        self.phaseLabel_CH1.setAlignment(Qt.AlignHCenter)
        self.phaseLE_CH1 = QLineEdit(self)
        self.phaseLE_CH1.setGeometry(445, 700, 141, 20)
        self.phaseLE_CH1.setAlignment(Qt.AlignHCenter)
        self.phaseLE_CH1.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.phaseLE_CH1.setText("")
        self.phaseLE_CH1.setReadOnly(True)

        self.phaseLabel_CH2 = QLabel("Phase Shift", self)
        self.phaseLabel_CH2.setGeometry(620, 680, 141, 22)
        self.phaseLabel_CH2.setStyleSheet(""" color: rgb(240, 240, 240);  """)
        self.phaseLabel_CH2.setFont(QFont("Microsoft Sans Serif", 10))
        self.phaseLabel_CH2.setAlignment(Qt.AlignHCenter)
        self.phaseLE_CH2 = QLineEdit(self)
        self.phaseLE_CH2.setGeometry(620, 700, 141, 20)
        self.phaseLE_CH2.setAlignment(Qt.AlignHCenter)
        self.phaseLE_CH2.setStyleSheet(
            """color: rgb(240, 240, 240); background-color: rgb(56, 56, 56)""")
        self.phaseLE_CH2.setText("")
        self.phaseLE_CH2.setReadOnly(True)

        self.CH1Label = QLabel("CH1", self)
        self.CH1Label.setGeometry(435, 650, 151, 22)
        self.CH1Label.setStyleSheet(""" color: blue """)
        self.CH1Label.setAlignment(Qt.AlignHCenter)
        self.CH1Label.setFont(QFont("Microsoft Sans Serif", 11))

        self.CH2Label = QLabel("CH2", self)
        self.CH2Label.setGeometry(610, 650, 151, 22)
        self.CH2Label.setStyleSheet(""" color: red """)
        self.CH2Label.setAlignment(Qt.AlignHCenter)
        self.CH2Label.setFont(QFont("Microsoft Sans Serif", 11))

        self.phaseCorrectLabel = QLabel("Phase Corr.:", self)
        self.phaseCorrectLabel.setGeometry(95, 650, 100, 22)
        self.phaseCorrectLabel.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.phaseCorrectLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.phaseCorrectLabel.setAlignment(Qt.AlignHCenter)
        self.phaseCorrectSB = QDoubleSpinBox(self)
        self.phaseCorrectSB.setRange(-1000000, 1000000)  # mínimo e máximo
        self.phaseCorrectSB.setSingleStep(0.001)  # incremento/decremento
        self.phaseCorrectSB.setValue(0.00)
        self.phaseCorrectSB.setDecimals(5)
        self.phaseCorrectSB.setGeometry(200, 645, 100, 30)
        self.phaseCorrectSB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.phaseCorrectSB.setAlignment(Qt.AlignHCenter)
        self.phaseCorrectSB.setFont(QFont("Microsoft Sans Serif", 10))
        self.phaseCorrectSB.setReadOnly(False)

        self.phaseCorrSupportLabel = QLabel("Adjust here and then click Next!", self)
        self.phaseCorrSupportLabel.setGeometry(70, 610, 260, 20)
        self.phaseCorrSupportLabel.setStyleSheet(""" color: blue""")
        self.phaseCorrSupportLabel.setFont(QFont("Calibri", 10))
        self.phaseCorrSupportLabel.setAlignment(Qt.AlignHCenter)

        self.CancelButton = Button(self, 10, 720, 200, 40, "",
                                    "images/Bt_Cancel.png", "images/Bt_Cancel.png",  False)
        
        self.NextButton = Button(self, 800, 720, 450, 40, "",
                                    "images/Bt_Next.png", "images/Bt_Next.png",  False)
        
        self.PreviousButton = Button(self, 800, 660, 450, 40, "",
                                    "images/Bt_Previous.png", "images/Bt_Previous.png",  False)
        
        self.backgroundLabel = QLabel("", self)
        self.backgroundLabel.setStyleSheet("""
            color: rgb(240, 240, 240);
            background-color: rgba(150, 150, 150, 50);
        """)
        self.backgroundLabel.setGeometry(0, 600, 1024, 150)
        self.backgroundLabel.setAttribute(Qt.WA_TransparentForMouseEvents)

class CalibWizardFinalWindow(QMainWindow):
    def __init__(self ):
        super(CalibWizardFinalWindow, self).__init__()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setGeometry(350, 350, 1024, 768)
        self.setFixedSize(1024, 768)
        self.setWindowTitle("Calibration Wizard")
        self.setWindowIcon(QIcon("images/MyOscPi_RedIcon.png"))
        self.setStyleSheet("background-color: rgb(40, 40, 40);")

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())


        self.mainLabel = QLabel("", self)
        self.mainLabel.setAlignment(Qt.AlignHCenter)
        self.mainLabel.setGeometry(20, 30, 970, 350)
        self.mainLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        mainImage = QPixmap("images/calibWizard.png")

        scaled_mainImage = mainImage.scaled(
            self.mainLabel.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.mainLabel.setPixmap(scaled_mainImage)

        self.sentenceLabel = QLabel("The obtained calibration parameters are listed below.", self)
        self.sentenceLabel.setGeometry(-30, 300, 1024, 70)
        self.sentenceLabel.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentenceLabel.setAlignment(Qt.AlignHCenter)
        self.sentenceLabel.setFont(QFont("Franklin Gothic Medium", 16))

        self.sentence2Label = QLabel("Click Save to save them, or click Cancel to exit the wizard without saving.", self)
        self.sentence2Label.setGeometry(0, 580, 1024, 70)
        self.sentence2Label.setStyleSheet(""" color: rgb(240, 240, 240) """)
        self.sentence2Label.setAlignment(Qt.AlignHCenter)
        self.sentence2Label.setFont(QFont("Franklin Gothic Medium", 16))

        # de calibManual
        self.samplingRateLabel = QLabel("Fs (S/s):", self)
        self.samplingRateLabel.setGeometry(140, 450, 80, 22)
        self.samplingRateLabel.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.samplingRateLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.samplingRateLabel.setAlignment(Qt.AlignHCenter)
        self.samplingRateSB = QSpinBox(self)
        self.samplingRateSB.setRange(0, 250000)  # mínimo e máximo
        self.samplingRateSB.setSingleStep(2)  # incremento/decremento
        self.samplingRateSB.setValue(19232)
        self.samplingRateSB.setGeometry(235, 445, 100, 30)
        self.samplingRateSB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.samplingRateSB.setAlignment(Qt.AlignHCenter)
        self.samplingRateSB.setFont(QFont("Microsoft Sans Serif", 10))
        self.samplingRateSB.setReadOnly(False)

        self.offsetCH1Label = QLabel("Offset CH1:", self)
        self.offsetCH1Label.setGeometry(355, 450, 100, 22)
        self.offsetCH1Label.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.offsetCH1Label.setFont(QFont("Microsoft Sans Serif", 10))
        self.offsetCH1Label.setAlignment(Qt.AlignHCenter)
        self.offsetCH1SB = QDoubleSpinBox(self)
        self.offsetCH1SB.setRange(0, 1000000.000)  # mínimo e máximo
        self.offsetCH1SB.setSingleStep(0.010)  # incremento/decremento
        self.offsetCH1SB.setValue(1.500)
        self.offsetCH1SB.setDecimals(3)
        self.offsetCH1SB.setGeometry(460, 445, 100, 30)
        self.offsetCH1SB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.offsetCH1SB.setAlignment(Qt.AlignHCenter)
        self.offsetCH1SB.setFont(QFont("Microsoft Sans Serif", 10))
        self.offsetCH1SB.setReadOnly(False)

        self.offsetCH2Label = QLabel("Offset CH2:", self)
        self.offsetCH2Label.setGeometry(355, 510, 100, 22)
        self.offsetCH2Label.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.offsetCH2Label.setFont(QFont("Microsoft Sans Serif", 10))
        self.offsetCH2Label.setAlignment(Qt.AlignHCenter)
        self.offsetCH2SB = QDoubleSpinBox(self)
        self.offsetCH2SB.setRange(0, 1000000.000)  # mínimo e máximo
        self.offsetCH2SB.setSingleStep(0.010)  # incremento/decremento
        self.offsetCH2SB.setValue(1.500)
        self.offsetCH2SB.setDecimals(3)
        self.offsetCH2SB.setGeometry(460, 505, 100, 30)
        self.offsetCH2SB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.offsetCH2SB.setAlignment(Qt.AlignHCenter)
        self.offsetCH2SB.setFont(QFont("Microsoft Sans Serif", 10))
        self.offsetCH2SB.setReadOnly(False)

        self.attnCH1Label = QLabel("Attn CH1:", self)
        self.attnCH1Label.setGeometry(580, 450, 100, 22)
        self.attnCH1Label.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.attnCH1Label.setFont(QFont("Microsoft Sans Serif", 10))
        self.attnCH1Label.setAlignment(Qt.AlignHCenter)
        self.attnCH1SB = QDoubleSpinBox(self)
        self.attnCH1SB.setRange(0, 1000000.000)  # mínimo e máximo
        self.attnCH1SB.setSingleStep(0.010)  # incremento/decremento
        self.attnCH1SB.setValue(1.500)
        self.attnCH1SB.setDecimals(3)
        self.attnCH1SB.setGeometry(685, 445, 100, 30)
        self.attnCH1SB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.attnCH1SB.setAlignment(Qt.AlignHCenter)
        self.attnCH1SB.setFont(QFont("Microsoft Sans Serif", 10))
        self.attnCH1SB.setReadOnly(False)

        self.attnCH2Label = QLabel("Attn CH2:", self)
        self.attnCH2Label.setGeometry(580, 510, 100, 22)
        self.attnCH2Label.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.attnCH2Label.setFont(QFont("Microsoft Sans Serif", 10))
        self.attnCH2Label.setAlignment(Qt.AlignHCenter)
        self.attnCH2SB = QDoubleSpinBox(self)
        self.attnCH2SB.setRange(0, 1000000.000)  # mínimo e máximo
        self.attnCH2SB.setSingleStep(0.010)  # incremento/decremento
        self.attnCH2SB.setValue(1.500)
        self.attnCH2SB.setDecimals(3)
        self.attnCH2SB.setGeometry(685, 505, 100, 30)
        self.attnCH2SB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.attnCH2SB.setAlignment(Qt.AlignHCenter)
        self.attnCH2SB.setFont(QFont("Microsoft Sans Serif", 10))
        self.attnCH2SB.setReadOnly(False)

        self.phaseCorrectLabel = QLabel("Phase Corr.:", self)
        self.phaseCorrectLabel.setGeometry(130, 510, 100, 22)
        self.phaseCorrectLabel.setStyleSheet(""" color: rgb(240, 240, 240)""")
        self.phaseCorrectLabel.setFont(QFont("Microsoft Sans Serif", 10))
        self.phaseCorrectLabel.setAlignment(Qt.AlignHCenter)
        self.phaseCorrectSB = QDoubleSpinBox(self)
        self.phaseCorrectSB.setRange(-1000000, 1000000)  # mínimo e máximo
        self.phaseCorrectSB.setSingleStep(0.001)  # incremento/decremento
        self.phaseCorrectSB.setValue(0.00)
        self.phaseCorrectSB.setDecimals(5)
        self.phaseCorrectSB.setGeometry(235, 505, 100, 30)
        self.phaseCorrectSB.setStyleSheet("background-color: rgb(50, 50, 50); color: rgb(240, 240, 240) ")
        self.phaseCorrectSB.setAlignment(Qt.AlignHCenter)
        self.phaseCorrectSB.setFont(QFont("Microsoft Sans Serif", 10))
        self.phaseCorrectSB.setReadOnly(False)


        self.CancelButton = Button(self, 10, 720, 200, 40, "",
                                    "images/Bt_Cancel.png", "images/Bt_Cancel.png",  False)
        
        self.PreviousButton = Button(self, 800, 660, 450, 40, "",
                                    "images/Bt_Previous.png", "images/Bt_Previous.png",  False)
        
        self.SaveButton = Button(self, 800, 720, 450, 40, "",
                                    "images/Bt_SaveCalib.png", "images/Bt_SaveCalib.png",  False)

    def closeWindow(self):
        self.close()
        
        
        
if __name__ == '__main__':
    app = QApplication([])
    window = CalibWizardPhaseCorrectionWindow()
    window.show()
    app.exec_()