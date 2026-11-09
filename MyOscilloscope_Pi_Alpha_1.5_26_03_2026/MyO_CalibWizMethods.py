from MyO_CalibWizClasses import *
from MyO_CalibManual_Methods import *


def calibWizardIsOn(self):
    if not self.screenName == "":
        self.calibWizScr = CalibWizard()
        self.calibWizScr.showNormal()
        self.calibWizScr.raise_()
        self.manageCalibWizard()

        #ajuste de idioma:
        self.calibWizScr.language = self.language
        self.calibWizScr.ChangeLanguage()

    if self.width() <= 1366: 
        self.resizeCalibWiz()
        

def resizeCalibWiz(self):
    p = self.width()/1920
    self.calibWizScr.move(int((self.width() - 1024)/2), 0)
    self.calibWizScr.setFixedSize(1024, 680)
    # --------------- mainWin ----------------------------
    self.calibWizScr.mainWin.mainLabel.setGeometry(30, 0, 970, 350)
    self.calibWizScr.mainWin.mainLabel.setPixmap(
        self.calibWizScr.mainWin.mainImage
        .scaled(self.calibWizScr.mainWin.mainLabel.size())
    )

    self.calibWizScr.mainWin.sentenceLabel.setGeometry(190, 310, 650, 70)
        
    self.calibWizScr.mainWin.samplingRateAdjustCheckBox.setGeometry(190, 370, 300, 50)      

    self.calibWizScr.mainWin.offsetSoftwareAdjustCheckBox.setGeometry(190, 420, 300, 50)
        
    self.calibWizScr.mainWin.offsetPhysicalAdjustCheckbox.setGeometry(190, 470, 300, 50)
        
    self.calibWizScr.mainWin.attenuationAdjustCheckBox.setGeometry(190, 520, 300, 50)
        
    self.calibWizScr.mainWin.phaseCorrAdjustCheckBox.setGeometry(190, 570, 300, 50)
        

    self.calibWizScr.mainWin.CancelButton.setGeometry(10, 640, 200, 40)
    self.calibWizScr.mainWin.CancelButton.visual.setGeometry(10, 640, 200, 40)
    self.calibWizScr.mainWin.CancelButton._update_visual()
    
    self.calibWizScr.mainWin.NextButton.setGeometry(800, 640, 450, 40)
    self.calibWizScr.mainWin.NextButton.visual.setGeometry(800, 640, 450, 40)
    self.calibWizScr.mainWin.NextButton._update_visual()

    self.calibWizScr.mainWin.languageSelectLabel.setGeometry(290, 260, 250, 30)

    self.calibWizScr.mainWin.languageSelectLabelCB.setGeometry(500, 260, 200, 30)
        
    self.calibWizScr.mainWin.checkBoxSupportLabel.setGeometry(250, 630, 500, 30)
        

    # ----------- samplingRate Window ------------------
    # self.calibWizScr.stack.setCurrentIndex(1)
    self.calibWizScr.sampRateWin.mainLabel.setGeometry(10, -10, 400, 175)
    self.calibWizScr.sampRateWin.titleLabel.setGeometry(500, 20, 450, 100)
    self.calibWizScr.sampRateWin.sentence1Label.setGeometry(
        10, int(p * 150), 1010, 90
    )
    self.calibWizScr.sampRateWin.shieldLabel.setGeometry(150, 160, 300, 240)
    self.calibWizScr.sampRateWin.shieldSupportLabel.setGeometry(220, 410, 200, 30)
    self.calibWizScr.sampRateWin.cableSupportLabel.setGeometry(630, 410, 170, 30)
    self.calibWizScr.sampRateWin.cableLabel.setGeometry(550, 160, 300, 240)
    self.calibWizScr.sampRateWin.sentence2Label.setGeometry(10, 440, 1010, 500)
    self.calibWizScr.sampRateWin.measureLabel.setGeometry(420, 590, 151, 28)
    self.calibWizScr.sampRateWin.frequencyLabel.setGeometry(425, 620, 141, 22)
    self.calibWizScr.sampRateWin.freqLE.setGeometry(425, 640, 141, 20)
    self.calibWizScr.sampRateWin.frequencyLabel_WFM.setGeometry(425, 520, 141, 42)
    self.calibWizScr.sampRateWin.freqLE_WFM.setGeometry(425, 560, 141, 20)
    self.calibWizScr.sampRateWin.samplingRateLabel.setGeometry(50, 520, 160, 100)
    self.calibWizScr.sampRateWin.samplingRateSB.setGeometry(205, 520, 100, 30)
    self.calibWizScr.sampRateWin.samplingRateSupportLabel.setGeometry(60, 560, 260, 30)
    self.calibWizScr.sampRateWin.backgroundLabel.setGeometry(0, 510, 1024, 160)

    self.calibWizScr.sampRateWin.CancelButton.setGeometry(10, 640, 200, 40)
    self.calibWizScr.sampRateWin.CancelButton.visual.setGeometry(10, 640, 200, 40)
    self.calibWizScr.sampRateWin.CancelButton._update_visual()
    
    self.calibWizScr.sampRateWin.NextButton.setGeometry(800, 640, 450, 40)
    self.calibWizScr.sampRateWin.NextButton.visual.setGeometry(800, 640, 450, 40)
    self.calibWizScr.sampRateWin.NextButton._update_visual()
    
    self.calibWizScr.sampRateWin.PreviousButton.setGeometry(800, 580, 450, 40)
    self.calibWizScr.sampRateWin.PreviousButton.visual.setGeometry(800, 580, 450, 40)
    self.calibWizScr.sampRateWin.PreviousButton._update_visual()

    # ----------- offsetSoftware Window ---------------
    
    self.calibWizScr.offsSoftwareWin.mainLabel.setGeometry(10, -10, 400, 175)
    self.calibWizScr.offsSoftwareWin.titleLabel.setGeometry(500, 20, 450, 100)

    self.calibWizScr.offsSoftwareWin.sentence1Label.setGeometry(10, 100, 1010, 150)
    self.calibWizScr.offsSoftwareWin.shieldLabel.setGeometry(340, 190, 300, 240)
    self.calibWizScr.offsSoftwareWin.shieldSupportLabel.setGeometry(410, 430, 200, 30)
    self.calibWizScr.offsSoftwareWin.sentence2Label.setGeometry(10, 460, 1010, 150)
    self.calibWizScr.offsSoftwareWin.measureLabel.setGeometry(440, 550, 151, 28)
    self.calibWizScr.offsSoftwareWin.meanLabel_CH1.setGeometry(445, 620, 141, 22)
    self.calibWizScr.offsSoftwareWin.meanLE_CH1.setGeometry(445, 640, 141, 20)
    self.calibWizScr.offsSoftwareWin.meanLabel_CH2.setGeometry(620, 620, 141, 22)
    self.calibWizScr.offsSoftwareWin.meanLE_CH2.setGeometry(620, 640, 141, 20)
    self.calibWizScr.offsSoftwareWin.CH1Label.setGeometry(435, 590, 151, 22)
    self.calibWizScr.offsSoftwareWin.CH2Label.setGeometry(610, 590, 151, 22)
    self.calibWizScr.offsSoftwareWin.offsetCH1Label.setGeometry(100, 580, 100, 22)
    self.calibWizScr.offsSoftwareWin.offsetCH1SB.setGeometry(225, 575, 100, 30)
    self.calibWizScr.offsSoftwareWin.offsetCH2Label.setGeometry(100, 620, 100, 22)
    self.calibWizScr.offsSoftwareWin.offsetCH2SB.setGeometry(225, 615, 100, 30)
    self.calibWizScr.offsSoftwareWin.offsetSupportLabel.setGeometry(70, 550, 260, 20)
    self.calibWizScr.offsSoftwareWin.backgroundLabel.setGeometry(0, 540, 1024, 150)

    self.calibWizScr.offsSoftwareWin.CancelButton.setGeometry(10, 640, 200, 40)
    self.calibWizScr.offsSoftwareWin.CancelButton.visual.setGeometry(10, 640, 200, 40)
    self.calibWizScr.offsSoftwareWin.CancelButton._update_visual()
    
    self.calibWizScr.offsSoftwareWin.NextButton.setGeometry(800, 640, 450, 40)
    self.calibWizScr.offsSoftwareWin.NextButton.visual.setGeometry(800, 640, 450, 40)
    self.calibWizScr.offsSoftwareWin.NextButton._update_visual()
    
    self.calibWizScr.offsSoftwareWin.PreviousButton.setGeometry(800, 580, 450, 40)
    self.calibWizScr.offsSoftwareWin.PreviousButton.visual.setGeometry(800, 580, 450, 40)
    self.calibWizScr.offsSoftwareWin.PreviousButton._update_visual()


    # ----------- offsetPhysical Window ---------------
    
    self.calibWizScr.offsPhysicalWin.mainLabel.setGeometry(10, -10, 400, 175)
    self.calibWizScr.offsPhysicalWin.titleLabel.setGeometry(500, 20, 450, 100)

    self.calibWizScr.offsPhysicalWin.sentence1Label.setGeometry(10, 100, 1010, 150)
    self.calibWizScr.offsPhysicalWin.calibPotentiometersLabel.setGeometry(90, 190, 850, 240)
    self.calibWizScr.offsPhysicalWin.sentence2Label.setGeometry(10, 470, 1010, 150)
    self.calibWizScr.offsPhysicalWin.measureLabel.setGeometry(385, 550, 151, 28)
    self.calibWizScr.offsPhysicalWin.meanLabel_CH1.setGeometry(305, 620, 141, 22)
    self.calibWizScr.offsPhysicalWin.meanLE_CH1.setGeometry(305, 640, 141, 20)
    self.calibWizScr.offsPhysicalWin.meanLabel_CH2.setGeometry(480, 620, 141, 22)
    self.calibWizScr.offsPhysicalWin.meanLE_CH2.setGeometry(480, 640, 141, 20)
    self.calibWizScr.offsPhysicalWin.CH1Label.setGeometry(295, 590, 151, 22)
    self.calibWizScr.offsPhysicalWin.CH2Label.setGeometry(470, 590, 151, 22)
    self.calibWizScr.offsPhysicalWin.backgroundLabel.setGeometry(0, 540, 1024, 150)

    self.calibWizScr.offsPhysicalWin.CancelButton.setGeometry(10, 640, 200, 40)
    self.calibWizScr.offsPhysicalWin.CancelButton.visual.setGeometry(10, 640, 200, 40)
    self.calibWizScr.offsPhysicalWin.CancelButton._update_visual()
    
    self.calibWizScr.offsPhysicalWin.NextButton.setGeometry(800, 640, 450, 40)
    self.calibWizScr.offsPhysicalWin.NextButton.visual.setGeometry(800, 640, 450, 40)
    self.calibWizScr.offsPhysicalWin.NextButton._update_visual()
    
    self.calibWizScr.offsPhysicalWin.PreviousButton.setGeometry(800, 580, 450, 40)
    self.calibWizScr.offsPhysicalWin.PreviousButton.visual.setGeometry(800, 580, 450, 40)
    self.calibWizScr.offsPhysicalWin.PreviousButton._update_visual()

    # ----------- attn window ------------------------
    self.calibWizScr.attnWin.mainLabel.setGeometry(10, -10, 400, 175)
    self.calibWizScr.attnWin.titleLabel.setGeometry(500, 20, 450, 100)

    self.calibWizScr.attnWin.sentence1Label.setGeometry(10, 100, 1010, 150)
    self.calibWizScr.attnWin.shieldLabel.setGeometry(340, 190, 300, 240)
    self.calibWizScr.attnWin.sentence2Label.setGeometry(10, 450, 1010, 150)
    self.calibWizScr.attnWin.measureLabel.setGeometry(440, 550, 151, 28)
    self.calibWizScr.attnWin.meanLabel_CH1.setGeometry(445, 620, 141, 22)
    self.calibWizScr.attnWin.meanLE_CH1.setGeometry(445, 640, 141, 20)
    self.calibWizScr.attnWin.meanLabel_CH2.setGeometry(620, 620, 141, 22)
    self.calibWizScr.attnWin.meanLE_CH2.setGeometry(620, 640, 141, 20)
    self.calibWizScr.attnWin.CH1Label.setGeometry(435, 590, 151, 22)
    self.calibWizScr.attnWin.CH2Label.setGeometry(610, 590, 151, 22)
    self.calibWizScr.attnWin.attnCH1Label.setGeometry(100, 580, 100, 22)
    self.calibWizScr.attnWin.attnCH1SB.setGeometry(225, 575, 100, 30)
    self.calibWizScr.attnWin.attnCH2Label.setGeometry(100, 620, 100, 22)
    self.calibWizScr.attnWin.attnCH2SB.setGeometry(225, 615, 100, 30)
    self.calibWizScr.attnWin.attnSupportLabel.setGeometry(70, 550, 260, 20)
    self.calibWizScr.attnWin.backgroundLabel.setGeometry(0, 540, 1024, 150)

    self.calibWizScr.attnWin.CancelButton.setGeometry(10, 640, 200, 40)
    self.calibWizScr.attnWin.CancelButton.visual.setGeometry(10, 640, 200, 40)
    self.calibWizScr.attnWin.CancelButton._update_visual()
    
    self.calibWizScr.attnWin.NextButton.setGeometry(800, 640, 450, 40)
    self.calibWizScr.attnWin.NextButton.visual.setGeometry(800, 640, 450, 40)
    self.calibWizScr.attnWin.NextButton._update_visual()
    
    self.calibWizScr.attnWin.PreviousButton.setGeometry(800, 580, 450, 40)
    self.calibWizScr.attnWin.PreviousButton.visual.setGeometry(800, 580, 450, 40)
    self.calibWizScr.attnWin.PreviousButton._update_visual()

    # ------------ phaseCorr window ------------------
    self.calibWizScr.phaseCorrWin.mainLabel.setGeometry(10, -10, 400, 175)
    self.calibWizScr.phaseCorrWin.titleLabel.setGeometry(500, 20, 450, 100)

    self.calibWizScr.phaseCorrWin.sentence1Label.setGeometry(10, 100, 1010, 150)
    self.calibWizScr.phaseCorrWin.shieldLabel.setGeometry(370, 220, 250, 190)
    self.calibWizScr.phaseCorrWin.shieldSupportLabel.setGeometry(410, 410, 200, 30)
    self.calibWizScr.phaseCorrWin.sentence2Label.setGeometry(10, 450, 1010, 150)
    self.calibWizScr.phaseCorrWin.measureLabel.setGeometry(530, 550, 151, 28)
    self.calibWizScr.phaseCorrWin.phaseLabel_CH1.setGeometry(445, 620, 141, 22)
    self.calibWizScr.phaseCorrWin.phaseLE_CH1.setGeometry(445, 640, 141, 20)
    self.calibWizScr.phaseCorrWin.phaseLabel_CH2.setGeometry(620, 620, 141, 22)
    self.calibWizScr.phaseCorrWin.phaseLE_CH2.setGeometry(620, 640, 141, 20)
    self.calibWizScr.phaseCorrWin.CH1Label.setGeometry(435, 590, 151, 22)
    self.calibWizScr.phaseCorrWin.CH2Label.setGeometry(610, 590, 151, 22)
    self.calibWizScr.phaseCorrWin.phaseCorrectLabel.setGeometry(95, 580, 100, 22)
    self.calibWizScr.phaseCorrWin.phaseCorrectSB.setGeometry(200, 580, 100, 30)
    self.calibWizScr.phaseCorrWin.phaseCorrSupportLabel.setGeometry(70, 550, 260, 20)
    self.calibWizScr.phaseCorrWin.backgroundLabel.setGeometry(0, 540, 1024, 150)

    self.calibWizScr.phaseCorrWin.CancelButton.setGeometry(10, 640, 200, 40)
    self.calibWizScr.phaseCorrWin.CancelButton.visual.setGeometry(10, 640, 200, 40)
    self.calibWizScr.phaseCorrWin.CancelButton._update_visual()
    
    self.calibWizScr.phaseCorrWin.NextButton.setGeometry(800, 640, 450, 40)
    self.calibWizScr.phaseCorrWin.NextButton.visual.setGeometry(800, 640, 450, 40)
    self.calibWizScr.phaseCorrWin.NextButton._update_visual()
    
    self.calibWizScr.phaseCorrWin.PreviousButton.setGeometry(800, 580, 450, 40)
    self.calibWizScr.phaseCorrWin.PreviousButton.visual.setGeometry(800, 580, 450, 40)
    self.calibWizScr.phaseCorrWin.PreviousButton._update_visual()
    

    # ------------- final window --------------------
    self.calibWizScr.finalWin.sentence2Label.setGeometry(0, 520, 1024, 70)
    self.calibWizScr.finalWin.samplingRateLabel.setGeometry(140, 390, 80, 22)
    self.calibWizScr.finalWin.samplingRateSB.setGeometry(235, 385, 100, 30)
    self.calibWizScr.finalWin.offsetCH1Label.setGeometry(355, 390, 100, 22)
    self.calibWizScr.finalWin.offsetCH1SB.setGeometry(460, 385, 100, 30)
    self.calibWizScr.finalWin.offsetCH2Label.setGeometry(355, 450, 100, 22)
    self.calibWizScr.finalWin.offsetCH2SB.setGeometry(460, 445, 100, 30)
    self.calibWizScr.finalWin.attnCH1Label.setGeometry(580, 390, 100, 22)
    self.calibWizScr.finalWin.attnCH1SB.setGeometry(685, 385, 100, 30)
    self.calibWizScr.finalWin.attnCH2Label.setGeometry(580, 450, 100, 22)
    self.calibWizScr.finalWin.attnCH2SB.setGeometry(685, 445, 100, 30)
    self.calibWizScr.finalWin.phaseCorrectLabel.setGeometry(130, 450, 100, 22)
    self.calibWizScr.finalWin.phaseCorrectSB.setGeometry(235, 445, 100, 30)

    self.calibWizScr.finalWin.CancelButton.setGeometry(10, 640, 200, 40)
    self.calibWizScr.finalWin.CancelButton.visual.setGeometry(10, 640, 200, 40)
    self.calibWizScr.finalWin.CancelButton._update_visual()
    
    self.calibWizScr.finalWin.SaveButton.setGeometry(800, 640, 450, 40)
    self.calibWizScr.finalWin.SaveButton.visual.setGeometry(800, 640, 450, 40)
    self.calibWizScr.finalWin.SaveButton._update_visual()
    
    self.calibWizScr.finalWin.PreviousButton.setGeometry(800, 580, 450, 40)
    self.calibWizScr.finalWin.PreviousButton.visual.setGeometry(800, 580, 450, 40)
    self.calibWizScr.finalWin.PreviousButton._update_visual()


def manageCalibWizard(self):
    #Carregando inicialmente os parâmetros de calibração:
    self.calibWizScr.sampRateWin.samplingRateSB.setValue(int(self.mainScr.dataHandler.samplingRate))
    self.calibWizScr.offsSoftwareWin.offsetCH1SB.setValue(self.mainScr.dataHandler.offsCH1)
    self.calibWizScr.offsSoftwareWin.offsetCH2SB.setValue(self.mainScr.dataHandler.offsCH2)
    self.calibWizScr.attnWin.attnCH1SB.setValue(self.mainScr.dataHandler.attnCH1)
    self.calibWizScr.attnWin.attnCH2SB.setValue(self.mainScr.dataHandler.attnCH2)
    self.calibWizScr.phaseCorrWin.phaseCorrectSB.setValue(self.mainScr.phaseCorrTime)

    self.calibWizScr.finalWin.samplingRateSB.setValue(int(self.mainScr.samplingRate))
    self.calibWizScr.finalWin.offsetCH1SB.setValue(self.mainScr.dataHandler.offsCH1)
    self.calibWizScr.finalWin.offsetCH2SB.setValue(self.mainScr.dataHandler.offsCH2)
    self.calibWizScr.finalWin.attnCH1SB.setValue(self.mainScr.dataHandler.attnCH1)
    self.calibWizScr.finalWin.attnCH2SB.setValue(self.mainScr.dataHandler.attnCH2)
    self.calibWizScr.finalWin.phaseCorrectSB.setValue(self.mainScr.phaseCorrTime)

    self.updateCalibWizLineEditsTimer = QtCore.QTimer()
    self.updateCalibWizLineEditsTimer.setInterval(300)
    self.updateCalibWizLineEditsTimer.setSingleShot(True) 
    self.updateCalibWizLineEditsTimer.start()
    self.updateCalibWizLineEditsTimer.timeout.connect(self.updateCalibWizLineEdits)

    #Ligação dos doze spinBoxes do calibration wizard às suas funções de edição (com ajuste de interferência entre 
    # mouse e teclado e ligação entre o spinBox da janela principal e a sua contraparte da tela final)
    self.calibWizScr.sampRateWin.samplingRateSB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_samplingRate_sampRateWin)
    self.calibWizScr.sampRateWin.samplingRateSB.lineEdit().textEdited.connect(self.onSpinBoxTyping_samplingRate_sampRateWin)
    self.calibWizScr.sampRateWin.samplingRateSB.valueChanged.connect(self.onSpinBoxValueChanged_samplingRate_sampRateWin)
    self.user_is_typing_samplingRate_sampRateWin = False

    self.calibWizScr.finalWin.samplingRateSB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_samplingRate_finalWin)
    self.calibWizScr.finalWin.samplingRateSB.lineEdit().textEdited.connect(self.onSpinBoxTyping_samplingRate_finalWin)
    self.calibWizScr.finalWin.samplingRateSB.valueChanged.connect(self.onSpinBoxValueChanged_samplingRate_finalWin)
    self.user_is_typing_samplingRate_finalWin = False

    self.calibWizScr.offsSoftwareWin.offsetCH1SB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_offsCH1_offsSoftWin)
    self.calibWizScr.offsSoftwareWin.offsetCH1SB.lineEdit().textEdited.connect(self.onSpinBoxTyping_offsCH1_offsSoftWin)
    self.calibWizScr.offsSoftwareWin.offsetCH1SB.valueChanged.connect(self.onSpinBoxValueChanged_offsCH1_offsSoftWin)
    self.user_is_typing_offsCH1_offsSoftWin = False

    self.calibWizScr.offsSoftwareWin.offsetCH2SB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_offsCH2_offsSoftWin)
    self.calibWizScr.offsSoftwareWin.offsetCH2SB.lineEdit().textEdited.connect(self.onSpinBoxTyping_offsCH2_offsSoftWin)
    self.calibWizScr.offsSoftwareWin.offsetCH2SB.valueChanged.connect(self.onSpinBoxValueChanged_offsCH2_offsSoftWin)
    self.user_is_typing_offsCH2_offsSoftWin = False

    self.calibWizScr.finalWin.offsetCH1SB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_offsCH1_finalWin)
    self.calibWizScr.finalWin.offsetCH1SB.lineEdit().textEdited.connect(self.onSpinBoxTyping_offsCH1_finalWin)
    self.calibWizScr.finalWin.offsetCH1SB.valueChanged.connect(self.onSpinBoxValueChanged_offsCH1_finalWin)
    self.user_is_typing_offsCH1_finalWin = False

    self.calibWizScr.finalWin.offsetCH2SB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_offsCH2_finalWin)
    self.calibWizScr.finalWin.offsetCH2SB.lineEdit().textEdited.connect(self.onSpinBoxTyping_offsCH2_finalWin)
    self.calibWizScr.finalWin.offsetCH2SB.valueChanged.connect(self.onSpinBoxValueChanged_offsCH2_finalWin)
    self.user_is_typing_offsCH2_finalWin = False

    self.calibWizScr.attnWin.attnCH1SB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_attnCH1_attnWin)
    self.calibWizScr.attnWin.attnCH1SB.lineEdit().textEdited.connect(self.onSpinBoxTyping_attnCH1_attnWin)
    self.calibWizScr.attnWin.attnCH1SB.valueChanged.connect(self.onSpinBoxValueChanged_attnCH1_attnWin)
    self.user_is_typing_attnCH1_attnWin = False

    self.calibWizScr.attnWin.attnCH2SB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_attnCH2_attnWin)
    self.calibWizScr.attnWin.attnCH2SB.lineEdit().textEdited.connect(self.onSpinBoxTyping_attnCH2_attnWin)
    self.calibWizScr.attnWin.attnCH2SB.valueChanged.connect(self.onSpinBoxValueChanged_attnCH2_attnWin)
    self.user_is_typing_attnCH2_attnWin = False

    self.calibWizScr.finalWin.attnCH1SB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_attnCH1_finalWin)
    self.calibWizScr.finalWin.attnCH1SB.lineEdit().textEdited.connect(self.onSpinBoxTyping_attnCH1_finalWin)
    self.calibWizScr.finalWin.attnCH1SB.valueChanged.connect(self.onSpinBoxValueChanged_attnCH1_finalWin)
    self.user_is_typing_attnCH1_finalWin = False

    self.calibWizScr.finalWin.attnCH2SB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_attnCH2_finalWin)
    self.calibWizScr.finalWin.attnCH2SB.lineEdit().textEdited.connect(self.onSpinBoxTyping_attnCH2_finalWin)
    self.calibWizScr.finalWin.attnCH2SB.valueChanged.connect(self.onSpinBoxValueChanged_attnCH2_finalWin)
    self.user_is_typing_attnCH2_finalWin = False

    self.calibWizScr.phaseCorrWin.phaseCorrectSB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_phaseCorr_phaseCorrWin)
    self.calibWizScr.phaseCorrWin.phaseCorrectSB.lineEdit().textEdited.connect(self.onSpinBoxTyping_phaseCorr_phaseCorrWin)
    self.calibWizScr.phaseCorrWin.phaseCorrectSB.valueChanged.connect(self.onSpinBoxValueChanged_phaseCorr_phaseCorrWin)
    self.user_is_typing_phaseCorr_phaseCorrWin = False

    self.calibWizScr.finalWin.phaseCorrectSB.lineEdit().returnPressed.connect(self.onSpinBoxEditingFinished_phaseCorr_finalWin)
    self.calibWizScr.finalWin.phaseCorrectSB.lineEdit().textEdited.connect(self.onSpinBoxTyping_phaseCorr_finalWin)
    self.calibWizScr.finalWin.phaseCorrectSB.valueChanged.connect(self.onSpinBoxValueChanged_phaseCorr_finalWin)
    self.user_is_typing_phaseCorr_finalWin = False

    self.calibWizScr.calibrationSupportTimer.timeout.connect(self.CalibWizSupportAdjusts)

    #Salvar parâmetros de calibração antes dos ajustes para caso o usuário se arrependa
    self.mainScr.samplingRate_preWiz = self.mainScr.samplingRate
    self.mainScr.dataHandler.offsCH1_preWiz = self.mainScr.dataHandler.offsCH1
    self.mainScr.dataHandler.offsCH2_preWiz = self.mainScr.dataHandler.offsCH2
    self.mainScr.dataHandler.attnCH1_preWiz = self.mainScr.dataHandler.attnCH1
    self.mainScr.dataHandler.attnCH2_preWiz = self.mainScr.dataHandler.attnCH2
    self.phaseCorr_preWiz = self.mainScr.phaseCorrTime

    self.calibWizScr.resetCalibWizChangesTimer.timeout.connect(self.resetCalibWizChanges)
    self.calibWizScr.finalWin.SaveButton.clicked.connect(self.saveCalibWizChanges)



# --------- sampling rate - calibration wizard --------------
def onSpinBoxTyping_samplingRate_sampRateWin(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_samplingRate_sampRateWin = True

def onSpinBoxEditingFinished_samplingRate_sampRateWin(self):
    if self.user_is_typing_samplingRate_sampRateWin:
        self.user_is_typing_samplingRate_sampRateWin = False
        self.changeFrequency_Keyboard_samplingRate_sampRateWin()

def onSpinBoxValueChanged_samplingRate_sampRateWin(self):
    if not self.user_is_typing_samplingRate_sampRateWin:
        self.changeFrequency_Mouse_samplingRate_sampRateWin()

def changeFrequency_Mouse_samplingRate_sampRateWin(self):
    value = self.calibWizScr.sampRateWin.samplingRateSB.value() 
    if value % 2 == 0: self.mainScr.samplingRate = value
    else: self.mainScr.samplingRate = value + 1
    blocker = QSignalBlocker(self.calibWizScr.sampRateWin.samplingRateSB) #evita recursão causada ao alterar o line edit
    self.calibWizScr.sampRateWin.samplingRateSB.setValue(self.mainScr.samplingRate)
    self.calibWizScr.finalWin.samplingRateSB.setValue(self.mainScr.samplingRate)
    #self.reloadSamplingRate()

def changeFrequency_Keyboard_samplingRate_sampRateWin(self):
    value = self.calibWizScr.sampRateWin.samplingRateSB.value() 
    if value % 2 == 0: self.mainScr.samplingRate = value
    else: self.mainScr.samplingRate = value + 1
    blocker = QSignalBlocker(self.calibWizScr.sampRateWin.samplingRateSB) #evita recursão causada ao alterar o line edit
    self.calibWizScr.sampRateWin.samplingRateSB.setValue(self.mainScr.samplingRate)
    self.calibWizScr.finalWin.samplingRateSB.setValue(self.mainScr.samplingRate)
    #self.reloadSamplingRate()

def onSpinBoxTyping_samplingRate_finalWin(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_samplingRate_finalWin = True

def onSpinBoxEditingFinished_samplingRate_finalWin(self):
    if self.user_is_typing_samplingRate_finalWin:
        self.user_is_typing_samplingRate_finalWin = False
        self.changeFrequency_Keyboard_samplingRate_finalWin()

def onSpinBoxValueChanged_samplingRate_finalWin(self):
    if not self.user_is_typing_samplingRate_finalWin:
        self.changeFrequency_Mouse_samplingRate_finalWin()

def changeFrequency_Mouse_samplingRate_finalWin(self):
    value = self.calibWizScr.finalWin.samplingRateSB.value() 
    if value % 2 == 0: self.mainScr.samplingRate = value
    else: self.mainScr.samplingRate = value + 1
    blocker = QSignalBlocker(self.calibWizScr.finalWin.samplingRateSB) #evita recursão causada ao alterar o line edit
    self.calibWizScr.sampRateWin.samplingRateSB.setValue(self.mainScr.samplingRate)
    self.calibWizScr.finalWin.samplingRateSB.setValue(self.mainScr.samplingRate)
    #self.reloadSamplingRate()

def changeFrequency_Keyboard_samplingRate_finalWin(self):
    value = self.calibWizScr.finalWin.samplingRateSB.value() 
    if value % 2 == 0: self.mainScr.samplingRate = value
    else: self.mainScr.samplingRate = value + 1
    blocker = QSignalBlocker(self.calibWizScr.finalWin.samplingRateSB) #evita recursão causada ao alterar o line edit
    self.calibWizScr.sampRateWin.samplingRateSB.setValue(self.mainScr.samplingRate)
    self.calibWizScr.finalWin.samplingRateSB.setValue(self.mainScr.samplingRate)
    #self.reloadSamplingRate()


# ---------------- offset_CH1 - calibration wizard ----------------
def onSpinBoxTyping_offsCH1_offsSoftWin(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_offsCH1_offsSoftWin = True

def onSpinBoxEditingFinished_offsCH1_offsSoftWin(self):
    if self.user_is_typing_offsCH1_offsSoftWin:
        self.user_is_typing_offsCH1_offsSoftWin = False
        self.changeFrequency_Keyboard_offsCH1_offsSoftWin()

def onSpinBoxValueChanged_offsCH1_offsSoftWin(self):
    if not self.user_is_typing_offsCH1_offsSoftWin:
        self.changeFrequency_Mouse_offsCH1_offsSoftWin()

def changeFrequency_Mouse_offsCH1_offsSoftWin(self):
    if self.calibWizScr.offsSoftwareWin.offsetCH1SB.value() > 20: 
        self.calibWizScr.offsSoftwareWin.offsetCH1SB.setValue(20.000)
        self.calibWizScr.finalWin.offsetCH1SB.setValue(20.000)
    else:
        self.calibWizScr.offsSoftwareWin.offsetCH1SB.setValue(self.calibWizScr.offsSoftwareWin.offsetCH1SB.value())
        self.calibWizScr.finalWin.offsetCH1SB.setValue(self.calibWizScr.offsSoftwareWin.offsetCH1SB.value())
    self.mainScr.dataHandler.offsCH1 = self.calibWizScr.offsSoftwareWin.offsetCH1SB.value()

def changeFrequency_Keyboard_offsCH1_offsSoftWin(self):
    if self.calibWizScr.offsSoftwareWin.offsetCH1SB.value() > 20: 
        self.calibWizScr.offsSoftwareWin.offsetCH1SB.setValue(20.000)
        self.calibWizScr.finalWin.offsetCH1SB.setValue(20.000)
    else:
        self.calibWizScr.offsSoftwareWin.offsetCH1SB.setValue(self.calibWizScr.offsSoftwareWin.offsetCH1SB.value())
        self.calibWizScr.finalWin.offsetCH1SB.setValue(self.calibWizScr.offsSoftwareWin.offsetCH1SB.value())
    self.mainScr.dataHandler.offsCH1 = self.calibWizScr.offsSoftwareWin.offsetCH1SB.value()

def onSpinBoxTyping_offsCH1_finalWin(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_offsCH1_FinalWin = True

def onSpinBoxEditingFinished_offsCH1_finalWin(self):
    if self.user_is_typing_offsCH1_finalWin:
        self.user_is_typing_offsCH1_finalWin = False
        self.changeFrequency_Keyboard_offsCH1_finalWin()

def onSpinBoxValueChanged_offsCH1_finalWin(self):
    if not self.user_is_typing_offsCH1_finalWin:
        self.changeFrequency_Mouse_offsCH1_finalWin()

def changeFrequency_Mouse_offsCH1_finalWin(self):
    if self.calibWizScr.finalWin.offsetCH1SB.value() > 20: 
        self.calibWizScr.offsSoftwareWin.offsetCH1SB.setValue(20.000)
        self.calibWizScr.finalWin.offsetCH1SB.setValue(20.000)
    else:
        self.calibWizScr.offsSoftwareWin.offsetCH1SB.setValue(self.calibWizScr.finalWin.offsetCH1SB.value())
        self.calibWizScr.finalWin.offsetCH1SB.setValue(self.calibWizScr.finalWin.offsetCH1SB.value())
    self.mainScr.dataHandler.offsCH1 = self.calibWizScr.finalWin.offsetCH1SB.value()

def changeFrequency_Keyboard_offsCH1_finalWin(self):
    if self.calibWizScr.finalWin.offsetCH1SB.value() > 20: 
        self.calibWizScr.offsSoftwareWin.offsetCH1SB.setValue(20.000)
        self.calibWizScr.finalWin.offsetCH1SB.setValue(20.000)
    else:
        self.calibWizScr.offsSoftwareWin.offsetCH1SB.setValue(self.calibWizScr.finalWin.offsetCH1SB.value())
        self.calibWizScr.finalWin.offsetCH1SB.setValue(self.calibWizScr.finalWin.offsetCH1SB.value())
    self.mainScr.dataHandler.offsCH1 = self.calibWizScr.finalWin.offsetCH1SB.value()

# -------------- offset_CH2 - calibration wizard ---------------------
def onSpinBoxTyping_offsCH2_offsSoftWin(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_offsCH2_offsSoftWin = True

def onSpinBoxEditingFinished_offsCH2_offsSoftWin(self):
    if self.user_is_typing_offsCH2_offsSoftWin:
        self.user_is_typing_offsCH2_offsSoftWin = False
        self.changeFrequency_Keyboard_offsCH2_offsSoftWin()

def onSpinBoxValueChanged_offsCH2_offsSoftWin(self):
    if not self.user_is_typing_offsCH2_offsSoftWin:
        self.changeFrequency_Mouse_offsCH2_offsSoftWin()

def changeFrequency_Mouse_offsCH2_offsSoftWin(self):
    if self.calibWizScr.offsSoftwareWin.offsetCH2SB.value() > 20: 
        self.calibWizScr.offsSoftwareWin.offsetCH2SB.setValue(20.000)
        self.calibWizScr.finalWin.offsetCH2SB.setValue(20.000)
    else:
        self.calibWizScr.offsSoftwareWin.offsetCH2SB.setValue(self.calibWizScr.offsSoftwareWin.offsetCH2SB.value())
        self.calibWizScr.finalWin.offsetCH2SB.setValue(self.calibWizScr.offsSoftwareWin.offsetCH2SB.value())
    self.mainScr.dataHandler.offsCH2 = self.calibWizScr.offsSoftwareWin.offsetCH2SB.value()

def changeFrequency_Keyboard_offsCH2_offsSoftWin(self):
    if self.calibWizScr.offsSoftwareWin.offsetCH2SB.value() > 20: 
        self.calibWizScr.offsSoftwareWin.offsetCH2SB.setValue(20.000)
        self.calibWizScr.finalWin.offsetCH2SB.setValue(20.000)
    else:
        self.calibWizScr.offsSoftwareWin.offsetCH2SB.setValue(self.calibWizScr.offsSoftwareWin.offsetCH2SB.value())
        self.calibWizScr.finalWin.offsetCH2SB.setValue(self.calibWizScr.offsSoftwareWin.offsetCH2SB.value())
    self.mainScr.dataHandler.offsCH2 = self.calibWizScr.offsSoftwareWin.offsetCH2SB.value()

def onSpinBoxTyping_offsCH2_finalWin(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_offsCH2_FinalWin = True

def onSpinBoxEditingFinished_offsCH2_finalWin(self):
    if self.user_is_typing_offsCH2_finalWin:
        self.user_is_typing_offsCH2_finalWin = False
        self.changeFrequency_Keyboard_offsCH2_finalWin()

def onSpinBoxValueChanged_offsCH2_finalWin(self):
    if not self.user_is_typing_offsCH2_finalWin:
        self.changeFrequency_Mouse_offsCH2_finalWin()

def changeFrequency_Mouse_offsCH2_finalWin(self):
    if self.calibWizScr.finalWin.offsetCH2SB.value() > 20: 
        self.calibWizScr.offsSoftwareWin.offsetCH2SB.setValue(20.000)
        self.calibWizScr.finalWin.offsetCH2SB.setValue(20.000)
    else:
        self.calibWizScr.offsSoftwareWin.offsetCH2SB.setValue(self.calibWizScr.finalWin.offsetCH2SB.value())
        self.calibWizScr.finalWin.offsetCH2SB.setValue(self.calibWizScr.finalWin.offsetCH2SB.value())
    self.mainScr.dataHandler.offsCH2 = self.calibWizScr.finalWin.offsetCH2SB.value()

def changeFrequency_Keyboard_offsCH2_finalWin(self):
    if self.calibWizScr.finalWin.offsetCH2SB.value() > 20: 
        self.calibWizScr.offsSoftwareWin.offsetCH2SB.setValue(20.000)
        self.calibWizScr.finalWin.offsetCH2SB.setValue(20.000)
    else:
        self.calibWizScr.offsSoftwareWin.offsetCH2SB.setValue(self.calibWizScr.finalWin.offsetCH2SB.value())
        self.calibWizScr.finalWin.offsetCH2SB.setValue(self.calibWizScr.finalWin.offsetCH2SB.value())
    self.mainScr.dataHandler.offsCH2 = self.calibWizScr.finalWin.offsetCH2SB.value()


# ---------------- attn_CH1 - calibration wizard ----------------
def onSpinBoxTyping_attnCH1_attnWin(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_attnCH1_attnWin = True

def onSpinBoxEditingFinished_attnCH1_attnWin(self):
    if self.user_is_typing_attnCH1_attnWin:
        self.user_is_typing_attnCH1_attnWin = False
        self.changeFrequency_Keyboard_attnCH1_attnWin()

def onSpinBoxValueChanged_attnCH1_attnWin(self):
    if not self.user_is_typing_attnCH1_attnWin:
        self.changeFrequency_Mouse_attnCH1_attnWin()

def changeFrequency_Mouse_attnCH1_attnWin(self):
    if self.calibWizScr.attnWin.attnCH1SB.value() > 20: 
        self.calibWizScr.attnWin.attnCH1SB.setValue(20.000)
        self.calibWizScr.finalWin.attnCH1SB.setValue(20.000)
    else:
        self.calibWizScr.attnWin.attnCH1SB.setValue(self.calibWizScr.attnWin.attnCH1SB.value())
        self.calibWizScr.finalWin.attnCH1SB.setValue(self.calibWizScr.attnWin.attnCH1SB.value())
    self.mainScr.dataHandler.attnCH1 = self.calibWizScr.attnWin.attnCH1SB.value()

def changeFrequency_Keyboard_attnCH1_attnWin(self):
    if self.calibWizScr.attnWin.attnCH1SB.value() > 20: 
        self.calibWizScr.attnWin.attnCH1SB.setValue(20.000)
        self.calibWizScr.finalWin.attnCH1SB.setValue(20.000)
    else:
        self.calibWizScr.attnWin.attnCH1SB.setValue(self.calibWizScr.attnWin.attnCH1SB.value())
        self.calibWizScr.finalWin.attnCH1SB.setValue(self.calibWizScr.attnWin.attnCH1SB.value())
    self.mainScr.dataHandler.attnCH1 = self.calibWizScr.attnWin.attnCH1SB.value()

def onSpinBoxTyping_attnCH1_finalWin(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_attnCH1_FinalWin = True

def onSpinBoxEditingFinished_attnCH1_finalWin(self):
    if self.user_is_typing_attnCH1_finalWin:
        self.user_is_typing_attnCH1_finalWin = False
        self.changeFrequency_Keyboard_attnCH1_finalWin()

def onSpinBoxValueChanged_attnCH1_finalWin(self):
    if not self.user_is_typing_attnCH1_finalWin:
        self.changeFrequency_Mouse_attnCH1_finalWin()

def changeFrequency_Mouse_attnCH1_finalWin(self):
    if self.calibWizScr.finalWin.attnCH1SB.value() > 20: 
        self.calibWizScr.attnWin.attnCH1SB.setValue(20.000)
        self.calibWizScr.finalWin.attnCH1SB.setValue(20.000)
    else:
        self.calibWizScr.attnWin.attnCH1SB.setValue(self.calibWizScr.finalWin.attnCH1SB.value())
        self.calibWizScr.finalWin.attnCH1SB.setValue(self.calibWizScr.finalWin.attnCH1SB.value())
    self.mainScr.dataHandler.attnCH1 = self.calibWizScr.finalWin.attnCH1SB.value()

def changeFrequency_Keyboard_attnCH1_finalWin(self):
    if self.calibWizScr.finalWin.attnCH1SB.value() > 20: 
        self.calibWizScr.attnWin.attnCH1SB.setValue(20.000)
        self.calibWizScr.finalWin.attnCH1SB.setValue(20.000)
    else:
        self.calibWizScr.attnWin.attnCH1SB.setValue(self.calibWizScr.finalWin.attnCH1SB.value())
        self.calibWizScr.finalWin.attnCH1SB.setValue(self.calibWizScr.finalWin.attnCH1SB.value())
    self.mainScr.dataHandler.attnCH1 = self.calibWizScr.finalWin.attnCH1SB.value()

# -------------- attn_CH2 - calibration wizard ---------------------
def onSpinBoxTyping_attnCH2_attnWin(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_attnCH2_attnWin = True

def onSpinBoxEditingFinished_attnCH2_attnWin(self):
    if self.user_is_typing_attnCH2_attnWin:
        self.user_is_typing_attnCH2_attnWin = False
        self.changeFrequency_Keyboard_attnCH2_attnWin()

def onSpinBoxValueChanged_attnCH2_attnWin(self):
    if not self.user_is_typing_attnCH2_attnWin:
        self.changeFrequency_Mouse_attnCH2_attnWin()

def changeFrequency_Mouse_attnCH2_attnWin(self):
    if self.calibWizScr.attnWin.attnCH2SB.value() > 20: 
        self.calibWizScr.attnWin.attnCH2SB.setValue(20.000)
        self.calibWizScr.finalWin.attnCH2SB.setValue(20.000)
    else:
        self.calibWizScr.attnWin.attnCH2SB.setValue(self.calibWizScr.attnWin.attnCH2SB.value())
        self.calibWizScr.finalWin.attnCH2SB.setValue(self.calibWizScr.attnWin.attnCH2SB.value())
    self.mainScr.dataHandler.attnCH2 = self.calibWizScr.attnWin.attnCH2SB.value()

def changeFrequency_Keyboard_attnCH2_attnWin(self):
    if self.calibWizScr.attnWin.attnCH2SB.value() > 20: 
        self.calibWizScr.attnWin.attnCH2SB.setValue(20.000)
        self.calibWizScr.finalWin.attnCH2SB.setValue(20.000)
    else:
        self.calibWizScr.attnWin.attnCH2SB.setValue(self.calibWizScr.attnWin.attnCH2SB.value())
        self.calibWizScr.finalWin.attnCH2SB.setValue(self.calibWizScr.attnWin.attnCH2SB.value())
    self.mainScr.dataHandler.attnCH2 = self.calibWizScr.attnWin.attnCH2SB.value()

def onSpinBoxTyping_attnCH2_finalWin(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_attnCH2_FinalWin = True

def onSpinBoxEditingFinished_attnCH2_finalWin(self):
    if self.user_is_typing_attnCH2_finalWin:
        self.user_is_typing_attnCH2_finalWin = False
        self.changeFrequency_Keyboard_attnCH2_finalWin()

def onSpinBoxValueChanged_attnCH2_finalWin(self):
    if not self.user_is_typing_attnCH2_finalWin:
        self.changeFrequency_Mouse_attnCH2_finalWin()

def changeFrequency_Mouse_attnCH2_finalWin(self):
    if self.calibWizScr.finalWin.attnCH2SB.value() > 20: 
        self.calibWizScr.attnWin.attnCH2SB.setValue(20.000)
        self.calibWizScr.finalWin.attnCH2SB.setValue(20.000)
    else:
        self.calibWizScr.attnWin.attnCH2SB.setValue(self.calibWizScr.finalWin.attnCH2SB.value())
        self.calibWizScr.finalWin.attnCH2SB.setValue(self.calibWizScr.finalWin.attnCH2SB.value())
    self.mainScr.dataHandler.attnCH2 = self.calibWizScr.finalWin.attnCH2SB.value()

def changeFrequency_Keyboard_attnCH2_finalWin(self):
    if self.calibWizScr.finalWin.attnCH2SB.value() > 20: 
        self.calibWizScr.attnWin.attnCH2SB.setValue(20.000)
        self.calibWizScr.finalWin.attnCH2SB.setValue(20.000)
    else:
        self.calibWizScr.attnWin.attnCH2SB.setValue(self.calibWizScr.finalWin.attnCH2SB.value())
        self.calibWizScr.finalWin.attnCH2SB.setValue(self.calibWizScr.finalWin.attnCH2SB.value())
    self.mainScr.dataHandler.attnCH2 = self.calibWizScr.finalWin.attnCH2SB.value()

# ----------------- phaseCorrection -----------------
def onSpinBoxTyping_phaseCorr_phaseCorrWin(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_phaseCorr_phaseCorrWin = True

def onSpinBoxEditingFinished_phaseCorr_phaseCorrWin(self):
    if self.user_is_typing_phaseCorr_phaseCorrWin:
        self.user_is_typing_phaseCorr_phaseCorrWin = False
        self.changeFrequency_Keyboard_phaseCorr_phaseCorrWin()

def onSpinBoxValueChanged_phaseCorr_phaseCorrWin(self):
    if not self.user_is_typing_phaseCorr_phaseCorrWin:
        self.changeFrequency_Mouse_phaseCorr_phaseCorrWin()

def changeFrequency_Mouse_phaseCorr_phaseCorrWin(self):
    if self.calibWizScr.phaseCorrWin.phaseCorrectSB.value() > 30: 
        self.calibWizScr.phaseCorrWin.phaseCorrectSB.setValue(30.000)
        self.calibWizScr.finalWin.phaseCorrectSB.setValue(30.000)
    elif self.calibWizScr.phaseCorrWin.phaseCorrectSB.value() < -30: 
        self.calibWizScr.phaseCorrWin.phaseCorrectSB.setValue(-30.000)
        self.calibWizScr.finalWin.phaseCorrectSB.setValue(-30.000)
    else:
        self.calibWizScr.phaseCorrWin.phaseCorrectSB.setValue(self.calibWizScr.phaseCorrWin.phaseCorrectSB.value())
        self.calibWizScr.finalWin.phaseCorrectSB.setValue(self.calibWizScr.phaseCorrWin.phaseCorrectSB.value())
    self.mainScr.phaseCorrTime = self.calibWizScr.phaseCorrWin.phaseCorrectSB.value()

def changeFrequency_Keyboard_phaseCorr_phaseCorrWin(self):
    if self.calibWizScr.phaseCorrWin.phaseCorrectSB.value() > 30: 
        self.calibWizScr.phaseCorrWin.phaseCorrectSB.setValue(30.000)
        self.calibWizScr.finalWin.phaseCorrectSB.setValue(30.000)
    elif self.calibWizScr.phaseCorrWin.phaseCorrectSB.value() < -30: 
        self.calibWizScr.phaseCorrWin.phaseCorrectSB.setValue(-30.000)
        self.calibWizScr.finalWin.phaseCorrectSB.setValue(-30.000)
    else:
        self.calibWizScr.phaseCorrWin.phaseCorrectSB.setValue(self.calibWizScr.phaseCorrWin.phaseCorrectSB.value())
        self.calibWizScr.finalWin.phaseCorrectSB.setValue(self.calibWizScr.phaseCorrWin.phaseCorrectSB.value())
    self.mainScr.phaseCorrTime = self.calibWizScr.phaseCorrWin.phaseCorrectSB.value()

def onSpinBoxTyping_phaseCorr_finalWin(self):
    # Qualquer digitação via teclado ativa essa flag
    self.user_is_typing_phaseCorr_finalWin = True

def onSpinBoxEditingFinished_phaseCorr_finalWin(self):
    if self.user_is_typing_phaseCorr_finalWin:
        self.user_is_typing_phaseCorr_finalWin = False
        self.changeFrequency_Keyboard_phaseCorr_finalWin()

def onSpinBoxValueChanged_phaseCorr_finalWin(self):
    if not self.user_is_typing_phaseCorr_finalWin:
        self.changeFrequency_Mouse_phaseCorr_finalWin()

def changeFrequency_Mouse_phaseCorr_finalWin(self):
    if self.calibWizScr.finalWin.phaseCorrectSB.value() > 30: 
        self.calibWizScr.phaseCorrWin.phaseCorrectSB.setValue(30.000)
        self.calibWizScr.finalWin.phaseCorrectSB.setValue(30.000)
    elif self.calibWizScr.finalWin.phaseCorrectSB.value() < -30: 
        self.calibWizScr.phaseCorrWin.phaseCorrectSB.setValue(-30.000)
        self.calibWizScr.finalWin.phaseCorrectSB.setValue(-30.000)
    else:
        self.calibWizScr.phaseCorrWin.phaseCorrectSB.setValue(self.calibWizScr.finalWin.phaseCorrectSB.value())
        self.calibWizScr.finalWin.phaseCorrectSB.setValue(self.calibWizScr.finalWin.phaseCorrectSB.value())
    self.mainScr.phaseCorrTime = self.calibWizScr.finalWin.phaseCorrectSB.value()

def changeFrequency_Keyboard_phaseCorr_finalWin(self):
    if self.calibWizScr.finalWin.phaseCorrectSB.value() > 30: 
        self.calibWizScr.phaseCorrWin.phaseCorrectSB.setValue(30.000)
        self.calibWizScr.finalWin.phaseCorrectSB.setValue(30.000)
    elif self.calibWizScr.finalWin.phaseCorrectSB.value() < -30: 
        self.calibWizScr.phaseCorrWin.phaseCorrectSB.setValue(-30.000)
        self.calibWizScr.finalWin.phaseCorrectSB.setValue(-30.000)
    else:
        self.calibWizScr.phaseCorrWin.phaseCorrectSB.setValue(self.calibWizScr.finalWin.phaseCorrectSB.value())
        self.calibWizScr.finalWin.phaseCorrectSB.setValue(self.calibWizScr.finalWin.phaseCorrectSB.value())
    self.mainScr.phaseCorrTime = self.calibWizScr.finalWin.phaseCorrectSB.value()


def updateCalibWizLineEdits(self):
    try:
        #Atualização automática (não depende do usuário) dos line edits presentes no wizard
        self.calibWizScr.sampRateWin.freqLE_WFM.setText(f"{self.WFMgeneratorScr.freq_SpinBox.value()} Hz")
        self.calibWizScr.sampRateWin.freqLE.setText(f"{(self.freqCH1):.3f} Hz")
        self.calibWizScr.offsSoftwareWin.meanLE_CH1.setText(f"{(self.CH1MeanValue*1000):.3f} mV")
        self.calibWizScr.offsSoftwareWin.meanLE_CH2.setText(f"{(self.CH2MeanValue*1000):.3f} mV")
        self.calibWizScr.offsPhysicalWin.meanLE_CH1.setText(f"{(self.CH1MeanValue*1000):.3f} mV")
        self.calibWizScr.offsPhysicalWin.meanLE_CH2.setText(f"{(self.CH2MeanValue*1000):.3f} mV")
        self.calibWizScr.attnWin.meanLE_CH1.setText(f"{(self.CH1MeanValue):.3f} V")
        self.calibWizScr.attnWin.meanLE_CH2.setText(f"{(self.CH2MeanValue):.3f} V")
        self.calibWizScr.phaseCorrWin.phaseLE_CH1.setText(f"{(self.CH1Phase):.2f} °")
        self.calibWizScr.phaseCorrWin.phaseLE_CH2.setText(f"{(self.CH2Phase):.2f} °")

        if self.calibWizScr.updateTimerIsOn: self.updateCalibWizLineEditsTimer.start() #desativado no closeEvent do Wizard
    
    except RuntimeError:
        pass

def CalibWizSupportAdjusts(self):
    #Alterações na interface principal em alguns momentos do assistente de calibração:

    # ------------ offset software ou zero físico 1 ---------------
    if self.calibWizScr.stack.currentIndex() == 2: #offset software
        self.mainScr.vdivCH1Scale = 0.02
        self.mainScr.vdivCH2Scale = 0.02
    else:
        self.mainScr.vdivCH1Scale = 0.5
        self.mainScr.vdivCH2Scale = 0.5

    #Ajustes dos labels:
    if not self.currentForCH1Scale:
        if self.mainScr.vdivCH1Scale >= 0.5: self.CH1Label.setText(f"CH1: {self.mainScr.vdivCH1Scale} V/div")
        else: self.CH1Label.setText(f"CH1: {(self.mainScr.vdivCH1Scale * 1000):.0f} mV/div")
    else:
        if self.mainScr.vdivCH1Scale/self.shuntRes_CH1 >= 0.5:
            self.CH1Label.setText(f"CH1: {(self.mainScr.vdivCH1Scale/self.shuntRes_CH1):.2f} A/div")
        elif self.mainScr.vdivCH1Scale/self.shuntRes_CH1  >= 0.5 * 1e-3:
            self.CH1Label.setText(f"CH1: {(self.mainScr.vdivCH1Scale/self.shuntRes_CH1 * 1000):.2f} mA/div")

        else:
            self.CH1Label.setText(f"CH1: {(self.mainScr.vdivCH1Scale/self.shuntRes_CH1 * 1e6):.2f} µA/div")

    if not self.currentForCH2Scale:
        if self.mainScr.vdivCH2Scale >= 0.5: self.CH2Label.setText(f"CH2: {self.mainScr.vdivCH2Scale} V/div")
        else: self.CH2Label.setText(f"CH2: {(self.mainScr.vdivCH2Scale * 1000):.0f} mV/div")
    else:
        if self.mainScr.vdivCH2Scale/self.shuntRes_CH2 >= 0.5:
            self.CH2Label.setText(f"CH2: {(self.vdivCH2Scale/self.shuntRes_CH2):.2f} A/div")

        elif self.mainScr.vdivCH2Scale/self.shuntRes_CH2  >= 0.5 * 1e-3:
            self.CH2Label.setText(f"CH2: {(self.mainScr.vdivCH2Scale/self.shuntRes_CH2 * 1000):.2f} mA/div")
        
        else:
            self.CH2Label.setText(f"CH2: {(self.mainScr.vdivCH2Scale/self.shuntRes_CH2 * 1e6):.2f} µA/div")

    # ------------ correção de fase -----------------
    if self.calibWizScr.stack.currentIndex() == 5: 
        self.WFMgeneratorScr.generator.set_freq(9000)
        self.WFMgeneratorScr.freq_SpinBox.lineEdit().setText(str(9000))
    else:                                          
        self.WFMgeneratorScr.generator.set_freq(500)
        self.WFMgeneratorScr.freq_SpinBox.lineEdit().setText(str(500))

def resetCalibWizChanges(self):
    self.mainScr.samplingRate = self.mainScr.samplingRate_preWiz
    self.mainScr.dataHandler.offsCH1 = self.mainScr.dataHandler.offsCH1_preWiz
    self.mainScr.dataHandler.offsCH2 = self.mainScr.dataHandler.offsCH2_preWiz
    self.mainScr.dataHandler.attnCH1 = self.mainScr.dataHandler.attnCH1_preWiz
    self.mainScr.dataHandler.attnCH2 = self.mainScr.dataHandler.attnCH2_preWiz
    self.mainScr.phaseCorrTime = self.phaseCorr_preWiz

    self.mainScr.vdivCH1Scale = 0.5
    self.mainScr.vdivCH2Scale = 0.5

    #Ajustes dos labels:
    if not self.currentForCH1Scale:
        if self.mainScr.vdivCH1Scale >= 0.5: self.CH1Label.setText(f"CH1: {self.mainScr.vdivCH1Scale} V/div")
        else: self.CH1Label.setText(f"CH1: {(self.mainScr.vdivCH1Scale * 1000):.0f} mV/div")
    else:
        if self.mainScr.vdivCH1Scale/self.shuntRes_CH1 >= 0.5:
            self.CH1Label.setText(f"CH1: {(self.mainScr.vdivCH1Scale/self.shuntRes_CH1):.2f} A/div")
        elif self.mainScr.vdivCH1Scale/self.shuntRes_CH1  >= 0.5 * 1e-3:
            self.CH1Label.setText(f"CH1: {(self.mainScr.vdivCH1Scale/self.shuntRes_CH1 * 1000):.2f} mA/div")

        else:
            self.CH1Label.setText(f"CH1: {(self.mainScr.vdivCH1Scale/self.shuntRes_CH1 * 1e6):.2f} µA/div")

    if not self.currentForCH2Scale:
        if self.mainScr.vdivCH2Scale >= 0.5: self.CH2Label.setText(f"CH2: {self.mainScr.vdivCH2Scale} V/div")
        else: self.CH2Label.setText(f"CH2: {(self.mainScr.vdivCH2Scale * 1000):.0f} mV/div")
    else:
        if self.mainScr.vdivCH2Scale/self.shuntRes_CH2 >= 0.5:
            self.CH2Label.setText(f"CH2: {(self.mainScr.vdivCH2Scale/self.shuntRes_CH2):.2f} A/div")

        elif self.mainScr.vdivCH2Scale/self.shuntRes_CH2  >= 0.5 * 1e-3:
            self.CH2Label.setText(f"CH2: {(self.mainScr.vdivCH2Scale/self.shuntRes_CH2 * 1000):.2f} mA/div")
        
        else:
            self.CH2Label.setText(f"CH2: {(self.mainScr.vdivCH2Scale/self.shuntRes_CH2 * 1e6):.2f} µA/div")

    self.WFMgeneratorScr.generator.set_freq(500)
    self.WFMgeneratorScr.freq_SpinBox.lineEdit().setText(str(500))


def saveCalibWizChanges(self):
    self.calibManualScr.samplingRateSB.setValue(self.calibWizScr.finalWin.samplingRateSB.value())
    self.calibManualScr.offsetCH1SB.setValue(self.calibWizScr.finalWin.offsetCH1SB.value())
    self.calibManualScr.offsetCH2SB.setValue(self.calibWizScr.finalWin.offsetCH2SB.value())
    self.calibManualScr.attnCH1SB.setValue(self.calibWizScr.finalWin.attnCH1SB.value())
    self.calibManualScr.attnCH2SB.setValue(self.calibWizScr.finalWin.attnCH2SB.value())
    self.calibManualScr.phaseCorrectSB.setValue(self.calibWizScr.finalWin.phaseCorrectSB.value())
    self.saveCalibrationParams(self.mainScr.dataHandler.offsCH1, self.mainScr.dataHandler.offsCH2, self.mainScr.dataHandler.attnCH1, 
                                self.mainScr.dataHandler.attnCH2, self.mainScr.phaseCorrTime, self.mainScr.samplingRate)
    self.savedCalibScr.open()