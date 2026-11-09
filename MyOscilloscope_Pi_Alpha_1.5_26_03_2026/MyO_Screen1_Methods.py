from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt
from pyqtgraph import QtCore

#Método da subjanela Main
def MainScreen(self):
    if self.mainScr.COMPortON: #Tudo ocorre se houver comunicação serial estabelecida
        if(self.btOnOff.isOn == True): #A seguir, tudo ocorre se o osciloscópio estiver ligado
            self.screenName = "Main"
            self.mainScr.allowUpdateGraph = True
            self.FFTScr.allowUpdateGraph = False
            self.setWindowIcon(QIcon("images/MyOscPi_BlueIcon.png")) #muda o ícone do programa para azul
            self.primaryScreen.setCurrentIndex(1) #muda a tela primária para Main
            #Ativa os labels de tempo e labels auxiliares da tela Main:
            self.timeLabel.show()
            

            #A lógica True/False é definida antes dessa função, numa função definida em Button.py. Se o botão foi clicado
            #e definido como True:
            if(self.btMain.isOn == True):
                self.blackLabel1.show()
                self.blackLabel2.show()
                self.blackLabel1.raise_()
                self.blackLabel2.raise_()
                p = self.width()/1920 #as abas principais são diferentes em tamanho
                if not self.calibManual_isOn: 
                    self.screen1.setGeometry(int(self.p * 10), int(self.p * 360), int(self.p * 1000), int(self.p * 460))
                    
                else: 
                    self.screen1.setGeometry(int(self.p * 10), int(self.p * 360), int(self.p * 1000), int(self.p * 320))
                    #self.calibManualScr.setStyleSheet("background-color: rgb(5, 5, 18)")
                    
                    self.calibManualScreen.raise_()
                self.backgroundLabel5.setStyleSheet("""
                    background-color: rgb(5, 5, 18);
                    border-radius: 10px;
                """)
                

                #Ativa os knobs e labels de escala vertical e de posição conforme canais ativados
                if(self.btCH1.isOn == True):
                    self.posCH1Knob.buttonIsOn = True
                    self.CH1Label.show()
                if(self.btCH2.isOn == True):
                    self.posCH2Knob.buttonIsOn = True
                    self.CH2Label.show()
                if(self.btMath.isOn == True):
                    self.posMathKnob.buttonIsOn = True
                    self.mathvDivLabel.show()

                if not self.posCH1Knob.usefulValue == 0 and self.btCH1.isOn == True:
                    self.posCH1Label.show()
                if not self.posCH2Knob.usefulValue == 0 and self.btCH2.isOn == True:
                    self.posCH2Label.show()
                if not self.posMathKnob.usefulValue == 0 and self.btMath.isOn == True:
                    self.mathPosLabel.show()

                #Com Main ativado, houve alteração na tela principal. Resetar o cursor se estiver ligado:
                if self.btCursor.isOn:
                    self.btCursor.isOn = False
                    self.CursorActivated() #Para desligar o cursor ativado (lógica toggle)

                #Ativando o obtainMeasureValues de mainScreen:
                self.mainScr.obtainMeasureValuesOn = True 

            
                

            self.vdivCH1Knob.buttonIsOn = True
            self.vdivCH2Knob.buttonIsOn = True
            self.vdivMathKnob.buttonIsOn = True
            self.timeKnob.buttonIsOn = True
            

    #Os else a seguir mudam a imagem do botão Main para a forma desativada (casos em que a aba Main não tem "permissão para abrir")
        else:
            self.btMain._update_visual()
    else:
        self.btMain._update_visual()
        self.primaryScreen.setCurrentIndex(0) #Tela primária vai para standbyScreen
    self.UpdatePrimaryButtons() #função que ajusta interações mais complexas entre os elementos da interface

#Método da subjanela FFT
def FFTScreen(self):
    if self.mainScr.COMPortON: #Tudo ocorre se houver comunicação serial estabelecida
        if (self.btOnOff.isOn == True): #A seguir, tudo ocorre se o osciloscópio estiver ligado
            self.screenName = "FFT"
            self.setWindowIcon(QIcon("images/MyOscPi_RedIcon.png")) #muda o ícone do programa para vermelho
            self.primaryScreen.setCurrentIndex(4) #muda a tela primária para FFT
            self.mainScr.allowUpdateGraph = True
            self.FFTScr.allowUpdateGraph = True

        if self.btFFT.isOn:
            p = self.width()/1920 #as abas principais são diferentes em tamanho
            if not self.calibManual_isOn: self.screen1.setGeometry(int(self.p * 10), int(self.p * 360), int(self.p * 1000), int(self.p * 460))
            else: 
                self.screen1.setGeometry(int(self.p * 10), int(self.p * 360), int(self.p * 1000), int(self.p * 320))
                #self.calibManualScr.setStyleSheet("background-color: rgb(16, 5, 5)")
            self.backgroundLabel5.setStyleSheet("""
                    background-color: rgb(16, 5, 5);
                    border-radius: 10px;
                """)
                                                                       
            #Desativa a tela secundária do cursor ou measure caso esteja ativada e o botão do FFT tenha sido clicado:
            if self.btCursor.isOn:
                self.btCursor.isOn = False
                self.CursorActivated() #Para desligar o cursor ativado (lógica toggle)

            if self.btMeas.isOn:
                self.btMeas.isOn = False
                self.MeasureActivated()

            #Ativando o obtainMeasureValues de mainScreen:
            self.mainScr.obtainMeasureValuesOn = True
            
        #Os else a seguir mudam a imagem do botão FFT para a forma desativada (casos em que a aba FFT não tem "permissão para abrir")
        else:
            self.btFFT._update_visual()
    else:
        self.btFFT._update_visual()
        self.primaryScreen.setCurrentIndex(0) #tela primária vai para standbyScreen
    self.UpdatePrimaryButtons() #função que ajusta interações mais complexas entre os elementos da interface

# Método da subjanela Frequency Response
def FreqRespScreen(self):
    if self.mainScr.COMPortON:
        if (self.btOnOff.isOn == True):
            self.screenName = "Freq Resp"
            self.setWindowIcon(QIcon("images/MyOscPi_GreenIcon.png")) #muda o ícone do programa para verde
            self.primaryScreen.setCurrentIndex(3) #muda tela primária para Frequency Response
            self.mainScr.allowUpdateGraph = True

            if self.btFreqResp.isOn:
                p = self.width()/1920
                if not self.calibManual_isOn: self.screen1.setGeometry(int(self.p * 10), int(self.p * 360), int(self.p * 1000), int(self.p * 460))
                else: 
                    self.screen1.setGeometry(int(self.p * 10), int(self.p * 360), int(self.p * 1000), int(self.p * 320))
                    #self.calibManualScr.setStyleSheet("background-color: rgb(5, 16, 5)") 
                self.backgroundLabel5.setStyleSheet("""
                    background-color: rgb(5, 16, 5);
                    border-radius: 10px;
                """)

                self.mainScr.obtainMeasureValuesOn = True 

                if self.btCursor.isOn:
                    self.btCursor.isOn = False
                    self.CursorActivated() #Para desligar o cursor ativado (lógica toggle)

                if self.btMeas.isOn:
                    self.btMeas.isOn = False
                    self.MeasureActivated()

        else:
            self.btFreqResp._update_visual()
            
    else:
        self.btFreqResp._update_visual()
        self.primaryScreen.setCurrentIndex(0)
    self.UpdatePrimaryButtons()

# Método da subjanela Phasor Diagram
def PhasDiagScreen(self):
    if self.mainScr.COMPortON: #Tudo ocorre se houver comunicação serial estabelecida
        if (self.btOnOff.isOn == True):
            self.screenName = "Phas Diag"
            self.setWindowIcon(QIcon("images/MyOscPi_YellowIcon.png")) #muda o ícone do programa para amarelo
            self.primaryScreen.setCurrentIndex(2) #muda tela primária para Phasor Diagram/Lissajous
            self.mainScr.allowUpdateGraph = True
            p = self.width()/1920 #as abas principais são diferentes em tamanho
            if not self.calibManual_isOn: self.screen1.setGeometry(int(self.p * (-130)), int(self.p * 360), int(self.p * 1120), int(self.p * 560))
            else: 
                self.screen1.setGeometry(int(self.p * (-130)), int(self.p * 360), int(self.p * 1120), int(self.p * 520))
                self.calibManualScreen.raise_()
                #self.calibManualScr.setStyleSheet("background-color: rgb(18, 18, 0)")
            self.backgroundLabel5.setStyleSheet("""
                    background-color: rgb(18, 18, 0);
                    border-radius: 10px;
                """)
        #Os else a seguir mudam a imagem do botão para a forma desativada (casos em que a aba não tem "permissão para abrir")
        else:
            self.btPhasDiag._update_visual()
            
    else:
        self.btPhasDiag._update_visual()
        self.primaryScreen.setCurrentIndex(0) #standby screen
    self.UpdatePrimaryButtons() #vide comentário na função MainScreen desse arquivo
    #Ativação do label do canal de referência:
    if not self.calibManual_isOn:
        self.phaseLabel.raise_()
        if self.btPhasDiag.isOn: 
            if self.language == "English": self.phaseLabel.setText(f"Reference Channel: \n{self.mainScr.referencePhase}")
            else: self.phaseLabel.setText(f"Canal de Ref.: \n{self.mainScr.referencePhase}")
            self.phaseLabel.show()


    if self.btPhasDiag.isOn:
        #Ativando o obtainMeasureValues de mainScreen:
        self.mainScr.obtainMeasureValuesOn = True

def HelpScreenBt(self):
        if self.btHelp.isOn == True and self.btOnOff.isOn == True:
            self.screenName = "Help"
            self.setWindowIcon(QIcon("images/MyOscPi_OrangeIcon.png"))
            self.primaryScreen.setCurrentIndex(5)

            # p = self.width()/1920 #as abas principais são diferentes em tamanho
            # if not self.calibManual_isOn: self.screen1.setGeometry(int(self.p * (0)), int(self.p * 0), int(self.p * 800), int(self.p * 465))
            # else: 
            #     self.screen1.setGeometry(int(self.p * (-130)), int(self.p * 360), int(self.p * 1120), int(self.p * 520))
            #     self.calibManualScreen.raise_()
            
            if self.calibManual_isOn: self.calibManualScr.btClose.clicked.emit()
            if True: self.screen1.setGeometry(int(self.p/0.8 * (10)), int(self.p/0.8 * 240), int(self.p/0.8 * 800), int(self.p/0.8 * 460))
            #else: (int(self.p/0.8 * 5), int(self.p/0.8 * 240), int(self.p/0.8 * 800), int(self.p/0.8 * 465))
            #else: (int(self.p * 5), int(self.p * 240), int(self.p * 800), int(self.p * 465))
        else:
            self.screenName = ""
        self.UpdatePrimaryButtons()
                     

