from PySide6.QtGui import QPainter, QFont, QPixmap
from PySide6.QtCore import Qt
from pyqtgraph import QtCore


'''
NOTA 1: Alguns widgets, mesmo que apareçam aqui, sofrem alterações nos métodos fadeIn e fadeOut!
NOTA 2: os widgets de screen2 sofrem alterações de tamanho no próprio arquivo.
'''


def resizeEvent(self, event):

        self.phasDiag_and_lissajScr.phasDiag.move(int(self.p*610), 0)
        self.phasDiag_and_lissajScr.lissaj.move(int(self.p*150), 0)

        self.COMPort.backgroundSvg.setGeometry(0, 0, int(self.p * 410), int(self.p * 82))
        self.COMPort.COM_PortLE.setGeometry(int(self.p * 6), int(self.p * 38), int(self.p * 138), int(self.p * 32))
        self.COMPort.btSearch.setGeometry(int(self.p * 163), int(self.p * 38), int(self.p * 157), int(self.p * 32))
        self.COMPort.btSearch.visual.setGeometry(int(self.p * 163), int(self.p * 38), int(self.p * 157), int(self.p * 32))
        self.COMPort.btSearch._update_visual()
        self.COMPort.signalIconRed.setGeometry(int(self.p * 350), int(self.p * 32), int(self.p * 38), int(self.p * 38))

        
        self.WFMgeneratorScr.squareLabel.setGeometry(int(self.p * 20), int(self.p * 85), int(self.p * 70), int(self.p * 70))
        self.WFMgeneratorScr.squareLabel.setPixmap(
            self.WFMgeneratorScr.squarePixmap.scaled(
                self.WFMgeneratorScr.squareLabel.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )
        self.WFMgeneratorScr.signalLabel.setPixmap(self.WFMgeneratorScr.sineWavePixmap
                                                   .scaled(self.WFMgeneratorScr.signalLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation))  
        self.WFMgeneratorScr.signalLabel.setGeometry(int(self.p * 25), int(self.p * 90), int(self.p * 60), int(self.p * 60)) 
        self.WFMgeneratorScr.btOnOff.setGeometry(int(self.p * 650), int(self.p * 70), int(self.p * 90), int(self.p * 65)) 
        self.WFMgeneratorScr.btOnOffImageLabel.setGeometry(int(self.p * 650), int(self.p * 70), int(self.p * 90), int(self.p * 65)) 
        self.WFMgeneratorScr.btOnOffLabel.setGeometry(int(self.p * 608), int(self.p * 140), int(self.p * 151), int(self.p * 22))
        self.WFMgeneratorScr.btOnOffImageLabel.setPixmap(self.WFMgeneratorScr.btOFFPixmap.scaled(self.WFMgeneratorScr.btOnOffImageLabel.size(),
                                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                                Qt.TransformationMode.SmoothTransformation)) 
        self.WFMgeneratorScr.signalTypeLabel.setGeometry(int(self.p * 130), int(self.p * 85), int(self.p * 151), int(self.p * 22)) 
        self.WFMgeneratorScr.signalTypeCB.setGeometry(int(self.p * 100), int(self.p * 115), int(self.p * 151), int(self.p * 30)) 
        self.WFMgeneratorScr.amplitLabel.setGeometry(int(self.p * 435), int(self.p * 70), int(self.p * 151), int(self.p * 22)) 
        self.WFMgeneratorScr.amplitLE.setGeometry(int(self.p * 510), int(self.p * 110), int(self.p * 60), int(self.p * 30)) 
        self.WFMgeneratorScr.amplitKnob.setGeometry(int(self.p * 420), int(self.p * 90), int(self.p * 70), int(self.p * 70))
        self.WFMgeneratorScr.amplitKnob.create()
        self.WFMgeneratorScr.amplitKnob.rotate_image(
            self.WFMgeneratorScr.amplitKnob.value()
        )

        self.WFMgeneratorScr.btQuestionMark.setGeometry(int(self.p * 595), int(self.p * 75), int(self.p * 30), int(self.p * 30)) 
        self.WFMgeneratorScr.freqLabel.setGeometry(int(self.p * 255), int(self.p * 85), int(self.p * 151), int(self.p * 22)) 
        self.WFMgeneratorScr.freq_SpinBox.setGeometry(int(self.p * 270), int(self.p * 115), int(self.p * 120), int(self.p * 30)) 
        self.WFMgeneratorScr.backgroundSvg.setGeometry(int(self.p * 0), int(self.p * 0), int(self.p * 810), int(self.p * 119)) 
        self.WFMgeneratorScr.btQuestionMark.setStyleSheet(f"""
            QPushButton {{
                color: white;
                background-color: rgb(0, 120, 0);   
                font-family: "Microsoft Sans Serif";
                font-size: 12pt;
                border-radius: {int(self.p * 15)}px; 
            }}
            """)
        
        self.calibrationScr.mainLabel.setGeometry(int(self.p * 250), int(self.p * 70), int(self.p * 250), int(self.p * 150))
        self.calibrationScr.btCalibManual.setGeometry(int(self.p * 60), int(self.p * 90), int(self.p * 200), int(self.p * 40))
        self.calibrationScr.btCalibManual.visual.setGeometry(int(self.p * 60), int(self.p * 90), int(self.p * 200), int(self.p * 40))
        self.calibrationScr.btCalibManual._update_visual()
        
        self.calibrationScr.btCalibWizard.setGeometry(int(self.p * 490), int(self.p * 90), int(self.p * 200), int(self.p * 40))
        self.calibrationScr.btCalibWizard.visual.setGeometry(int(self.p * 490), int(self.p * 90), int(self.p * 200), int(self.p * 40))
        self.calibrationScr.btCalibWizard._update_visual()

        self.calibrationScr.backgroundSvg.setGeometry(0, 0, int(self.p * 750), int(self.p * 119))

        self.exportScr.backgroundSvg.setGeometry(0, 0, int(self.p * 750), int(self.p * 119))
        self.exportScr.mainLabel.setGeometry(0, int(self.p * 80), int(self.p * 750), int(self.p * 70))
        self.exportScr.btImage.setGeometry(int(self.p * 440), int(self.p * 100), int(self.p * 200), int(self.p * 40))
        self.exportScr.btImage.visual.setGeometry(int(self.p * 440), int(self.p * 100), int(self.p * 200), int(self.p * 40))
        self.exportScr.btImage._update_visual()

        self.exportScr.btData.setGeometry(int(self.p * 100), int(self.p * 100), int(self.p * 200), int(self.p * 40))
        self.exportScr.btData.visual.setGeometry(int(self.p * 100), int(self.p * 100), int(self.p * 200), int(self.p * 40))
        self.exportScr.btData._update_visual()


        self.mathPlusScr.mainLabel.setGeometry(int(self.p * 270), int(self.p * 85), int(self.p * 200), int(self.p * 42))
        self.mathPlusScr.simpleOperationsCB.setGeometry(int(self.p * 270), int(self.p * 130), int(self.p * 195), int(self.p * 30))

        self.mathPlusScr.backgroundSvg.setGeometry(0, 0, int(self.p * 750), int(self.p * 119))

        self.phasDiag_and_lissajScr.phasDiag.setGeometry(int(self.p * 610), 0, int(self.p * 430), int(self.p * 430))
        self.phasDiag_and_lissajScr.lissaj.setGeometry(int(self.p * 150), 0, int(self.p * 410), int(self.p * 410))

        self.freqSweepScr.backgroundSvg.setGeometry(0, 0, int(self.p * 750), int(self.p * 165))
        self.freqSweepScr.label1.setGeometry(0, int(self.p * 55), int(self.p * 750), int(self.p * 50))
        self.freqSweepScr.progressBar.setGeometry(int(self.p * 10), int(self.p * 105), int(self.p * 720), int(self.p * 25))
        self.freqSweepScr.label2.setGeometry(0, int(self.p * 135), int(self.p * 750), int(self.p * 50))
        

        if not self.width() == 1920: self.p_help = self.p/0.8
        else: self.p_help = self.p * 1.25
        #self.p_help = 1
        self.helpScr.supportBarLabel.setGeometry(0, int(self.p_help * 405), int(self.p_help * 800), int(self.p_help * 60))
        self.helpScr.sectionLabel.setGeometry(int(self.p_help * 75), int(self.p_help * 410), int(self.p_help * 151), int(self.p_help * 20))
        self.helpScr.sectionCB.setGeometry(int(self.p_help * 75), int(self.p_help * 430), int(self.p_help * 181), int(self.p_help * 25))
        
        self.helpScr.pageChangerContainer.setGeometry(int(self.p_help * 600), int(self.p_help * 385), 160, 100)
        self.helpScr.HelpPages.setGeometry(0, 0, int(self.p_help * 800), int(self.p_help * 405))
        self.resizeHelp(self.p_help)

        if self.width() <= 1600:
            self.vdivLabel1.setFont(QFont("Microsoft Sans Serif", 17))
            self.vdivLabel2.setFont(QFont("Microsoft Sans Serif", 17))
            self.vdivLabel3.setFont(QFont("Microsoft Sans Serif", 17))
            self.timeKnobLabel.setFont(QFont("Microsoft Sans Serif", 17))
            
            self.positionLabel1.setFont(QFont("Microsoft Sans Serif", 10))
            self.positionLabel2.setFont(QFont("Microsoft Sans Serif", 10))
            self.positionLabel3.setFont(QFont("Microsoft Sans Serif", 10))

            self.CH1Label.setFont(QFont("Microsoft Sans Serif", 12))
            self.CH2Label.setFont(QFont("Microsoft Sans Serif", 12))
            self.posCH1Label.setFont(QFont("Microsoft Sans Serif", 12))
            self.posCH2Label.setFont(QFont("Microsoft Sans Serif", 12))
            self.timeLabel.setFont(QFont("Microsoft Sans Serif", 12))
            self.mathvDivLabel.setFont(QFont("Microsoft Sans Serif", 12))
            self.mathPosLabel.setFont(QFont("Microsoft Sans Serif", 12))
            self.phaseLabel.setFont(QFont("Microsoft Sans Serif", 12))
            self.triggerLabel.setFont(QFont("Microsoft Sans Serif", 12))
            self.triggerProportionLabel.setFont(QFont("Microsoft Sans Serif", 10))
            self.cursorProportionalLabel.setFont(QFont("Microsoft Sans Serif", 10))
            self.cursorFFTLabel.setFont(QFont("Microsoft Sans Serif", 10))

            self.WFMgeneratorScr.signalTypeCB.setFont(QFont("Microsoft Sans Serif", 10))
            self.WFMgeneratorScr.amplitLE.setFont(QFont("Microsoft Sans Serif", 10))
            self.WFMgeneratorScr.freq_SpinBox.setStyleSheet("""
                QSpinBox {
                    background-color: rgb(62, 200, 52);
                    color: rgb(240, 240, 240);
                    font-size: 10pt;
                    font-family: "Microsoft Sans Serif";
                }
            """)
            

        if self.width() <= 1366:
            self.vdivLabel1.setFont(QFont("Microsoft Sans Serif", 15))
            self.vdivLabel2.setFont(QFont("Microsoft Sans Serif", 15))
            self.vdivLabel3.setFont(QFont("Microsoft Sans Serif", 15))
            self.timeKnobLabel.setFont(QFont("Microsoft Sans Serif", 15))
            self.timeKnobLabel.setFont(QFont("Microsoft Sans Serif", 15))
            
            self.positionLabel1.setFont(QFont("Microsoft Sans Serif", 9))
            self.positionLabel2.setFont(QFont("Microsoft Sans Serif", 9))
            self.positionLabel3.setFont(QFont("Microsoft Sans Serif", 9))

            self.CH1Label.setFont(QFont("Microsoft Sans Serif", 10))
            self.CH2Label.setFont(QFont("Microsoft Sans Serif", 10))
            self.posCH1Label.setFont(QFont("Microsoft Sans Serif", 10))
            self.posCH2Label.setFont(QFont("Microsoft Sans Serif", 10))
            self.timeLabel.setFont(QFont("Microsoft Sans Serif", 10))
            self.mathvDivLabel.setFont(QFont("Microsoft Sans Serif", 10))
            self.mathPosLabel.setFont(QFont("Microsoft Sans Serif", 10))
            self.phaseLabel.setFont(QFont("Microsoft Sans Serif", 10))
            self.triggerLabel.setFont(QFont("Microsoft Sans Serif", 10))
            self.triggerProportionLabel.setFont(QFont("Microsoft Sans Serif", 10))
            self.cursorProportionalLabel.setFont(QFont("Microsoft Sans Serif", 8))
            self.cursorFFTLabel.setFont(QFont("Microsoft Sans Serif", 8))
            self.mathPlusScr.mainLabel.setFont(QFont("Microsoft Sans Serif", 8))
            self.mathPlusScr.simpleOperationsCB.setFont(QFont("Microsoft Sans Serif", 8))
            self.WFMgeneratorScr.signalTypeLabel.setGeometry(int(self.p * 120), int(self.p * 85), int(self.p * 151), int(self.p * 22)) 
def resizeHelp(self, p):
    #page1
    self.helpScr.page1.imageLabel.setGeometry(0, int(p * 20), int(p * 800), int(p* 300))
    self.helpScr.page1.label1.setGeometry(int(p* 5), int(p * 330), int(p * 790), int(p * 100))
    self.helpScr.page1.imageLabel.setPixmap(self.helpScr.page1.imagePixmap.scaled(
            self.helpScr.page1.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    
    #page2
    self.helpScr.page2.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page2.backgroundLabel.setGeometry(int(p *0 ), int(p * 10 ), int(p * 800), int(p *60 ))
    self.helpScr.page2.titleLabel.setGeometry(int(p * 280), int(p * 10), int(p * 550 ), int(p * 100))
    self.helpScr.page2.label1.setGeometry(int(p * 5), int(p * 330), int(p * 790), int(p * 100))
    self.helpScr.page2.imageLabel.setGeometry(int(p * 60), int(p * 100), int(p * 660), int(p * 220))
    self.helpScr.page2.imageLabel.setPixmap(self.helpScr.page2.imagePixmap.scaled(
            self.helpScr.page2.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page2.logoLabel.setPixmap(self.helpScr.page2.logoPixmap.scaled(
            self.helpScr.page2.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page3
    self.helpScr.page3.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page3.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page3.titleLabel.setGeometry(int(p * 280), int(p * 10), int(p * 550), int(p * 100))
    self.helpScr.page3.label1.setGeometry(int(p * 70), int(p * 150), int(p * 260), int(p * 200))
    self.helpScr.page3.imageLabel.setGeometry(int(p * 380), int(p * 100), int(p * 370), int(p * 280))
    self.helpScr.page3.imageLabel.setPixmap(self.helpScr.page3.imagePixmap.scaled(
            self.helpScr.page3.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
    ))
    self.helpScr.page3.logoLabel.setPixmap(self.helpScr.page3.logoPixmap.scaled(
            self.helpScr.page3.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page4
    self.helpScr.page4.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page4.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page4.titleLabel.setGeometry(int(p * 280), int(p * 10), int(p * 550), int(p * 100))
    self.helpScr.page4.label1.setGeometry(int(p * 480), int(p * 150), int(p * 260), int(p * 200))
    self.helpScr.page4.imageLabel.setGeometry(int(p * 20), int(p * 100), int(p * 420), int(p * 280))
    self.helpScr.page4.imageLabel.setPixmap(self.helpScr.page4.imagePixmap.scaled(
            self.helpScr.page4.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page4.logoLabel.setPixmap(self.helpScr.page4.logoPixmap.scaled(
            self.helpScr.page4.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))


    #page5
    self.helpScr.page5.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page5.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page5.titleLabel.setGeometry(int(p * 280), int(p * 10), int(p * 550), int(p * 100))
    self.helpScr.page5.label1.setGeometry(int(p * 70), int(p * 150), int(p * 260), int(p * 200))
    self.helpScr.page5.imageLabel1.setGeometry(int(p * 520), int(p * 70), int(p * 190), int(p * 187))
    self.helpScr.page5.imageLabel2.setGeometry(int(p * 470), int(p * 260), int(p * 300), int(p * 147))
    self.helpScr.page5.imageLabel1.setPixmap(self.helpScr.page5.imagePixmap1.scaled(
            self.helpScr.page5.imageLabel1.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page5.imageLabel2.setPixmap(self.helpScr.page5.imagePixmap2.scaled(
            self.helpScr.page5.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page5.logoLabel.setPixmap(self.helpScr.page5.logoPixmap.scaled(
            self.helpScr.page5.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page6
    self.helpScr.page6.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page6.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page6.titleLabel.setGeometry(int(p * 280), int(p * 10), int(p * 550), int(p * 100))
    self.helpScr.page6.label1.setGeometry(int(p * 5), int(p * 80), int(p * 790), int(p * 100))
    self.helpScr.page6.imageLabel.setGeometry(int(p * 250), int(p * 150), int(p * 285), int(p * 250))
    self.helpScr.page6.sourceLabel.setGeometry(int(p * 550), int(p * 380), int(p * 60), int(p * 40))
    self.helpScr.page6.imageLabel.setPixmap(self.helpScr.page6.imagePixmap.scaled(
            self.helpScr.page6.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page6.logoLabel.setPixmap(self.helpScr.page6.logoPixmap.scaled(
            self.helpScr.page6.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page7
    self.helpScr.page7.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page7.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page7.titleLabel.setGeometry(int(p * 280), int(p * 10), int(p * 550), int(p * 100))
    self.helpScr.page7.label1.setGeometry(int(p * 70), int(p * 80), int(p * 260), int(p * 320))
    self.helpScr.page7.imageLabel.setGeometry(int(p * 380), int(p * 100), int(p * 400), int(p * 240))
    self.helpScr.page7.sourceLabel.setGeometry(int(p * 720), int(p * 350), int(p * 60), int(p * 40))
    self.helpScr.page7.imageLabel.setPixmap(self.helpScr.page7.imagePixmap.scaled(
            self.helpScr.page7.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page7.logoLabel.setPixmap(self.helpScr.page7.logoPixmap.scaled(
            self.helpScr.page7.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page8
    self.helpScr.page8.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page8.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page8.titleLabel.setGeometry(int(p * 280), int(p * 10), int(p * 550), int(p * 100))
    self.helpScr.page8.label1.setGeometry(int(p * 5), int(p * 70), int(p * 790), int(p * 100))
    self.helpScr.page8.imageLabel.setGeometry(int(p * 250), int(p * 160), int(p * 270), int(p * 200))
    self.helpScr.page8.label2.setGeometry(int(p * 5), int(p * 330), int(p * 790), int(p * 100))
    self.helpScr.page8.imageLabel.setPixmap(self.helpScr.page8.imagePixmap.scaled(
            self.helpScr.page8.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page8.logoLabel.setPixmap(self.helpScr.page8.logoPixmap.scaled(
            self.helpScr.page8.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page9
    self.helpScr.page9.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page9.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page9.titleLabel.setGeometry(int(p * 280), int(p * 5), int(p * 550), int(p * 100))
    self.helpScr.page9.label1.setGeometry(int(p * 5), int(p * 80), int(p * 790), int(p * 100))
    self.helpScr.page9.imageLabel.setGeometry(int(p * 120), int(p * 140), int(p * 550), int(p * 250))
    self.helpScr.page9.imageLabel.setPixmap(self.helpScr.page9.imagePixmap.scaled(
            self.helpScr.page9.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page9.logoLabel.setPixmap(self.helpScr.page9.logoPixmap.scaled(
            self.helpScr.page9.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))


    #page10
    self.helpScr.page10.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page10.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page10.titleLabel.setGeometry(int(p * 280), int(p * 5), int(p * 550), int(p * 100))
    self.helpScr.page10.label1.setGeometry(int(p * 5), int(p * 80), int(p * 790), int(p * 100))
    self.helpScr.page10.imageLabel.setGeometry(int(p * 120), int(p * 140), int(p * 550), int(p * 250))
    self.helpScr.page10.imageLabel.setPixmap(self.helpScr.page10.imagePixmap.scaled(
            self.helpScr.page10.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page10.logoLabel.setPixmap(self.helpScr.page10.logoPixmap.scaled(
            self.helpScr.page10.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page11
    self.helpScr.page11.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page11.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page11.titleLabel.setGeometry(int(p * 280), int(p * 5), int(p * 550), int(p * 100))
    self.helpScr.page11.label1.setGeometry(int(p * 5), int(p * 150), int(p * 790), int(p * 300))
    self.helpScr.page11.logoLabel.setPixmap(self.helpScr.page11.logoPixmap.scaled(
            self.helpScr.page11.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page12
    self.helpScr.page12.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page12.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page12.titleLabel.setGeometry(int(p * 280), int(p * 10), int(p * 550), int(p * 100))
    self.helpScr.page12.label1.setGeometry(int(p * 70), int(p * 80), int(p * 650), int(p * 100))
    self.helpScr.page12.imageLabel1.setGeometry(int(p * 60), int(p * 180), int(p * 225), int(p * 187))
    self.helpScr.page12.imageLabel2.setGeometry(int(p * 340), int(p * 210), int(p * 440), int(p * 100))
    self.helpScr.page12.imageLabel1.setPixmap(self.helpScr.page12.imagePixmap1.scaled(
            self.helpScr.page12.imageLabel1.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page12.imageLabel2.setPixmap(self.helpScr.page12.imagePixmap2.scaled(
            self.helpScr.page12.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page12.logoLabel.setPixmap(self.helpScr.page12.logoPixmap.scaled(
            self.helpScr.page12.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page13
    self.helpScr.page13.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page13.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page13.titleLabel.setGeometry(int(p * 280), int(p * 10), int(p * 550), int(p * 100))
    self.helpScr.page13.label1.setGeometry(int(p * 460), int(p * 120), int(p * 260), int(p * 200))
    self.helpScr.page13.imageLabel.setGeometry(int(p * 40), int(p * 100), int(p * 310), int(p * 260))
    self.helpScr.page13.imageLabel.setPixmap(self.helpScr.page13.imagePixmap.scaled(
            self.helpScr.page13.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page13.logoLabel.setPixmap(self.helpScr.page13.logoPixmap.scaled(
            self.helpScr.page13.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page14
    self.helpScr.page14.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page14.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page14.titleLabel.setGeometry(int(p * 280), int(p * 10), int(p * 550), int(p * 100))
    self.helpScr.page14.label1.setGeometry(int(p * 60), int(p * 120), int(p * 260), int(p * 200))
    self.helpScr.page14.imageLabel.setGeometry(int(p * 460), int(p * 75), int(p * 165), int(p * 320))
    self.helpScr.page14.imageLabel.setPixmap(self.helpScr.page14.imagePixmap.scaled(
            self.helpScr.page14.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page14.logoLabel.setPixmap(self.helpScr.page14.logoPixmap.scaled(
            self.helpScr.page14.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page15
    self.helpScr.page15.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page15.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page15.titleLabel.setGeometry(int(p * 280), int(p * 10), int(p * 550), int(p * 100))
    self.helpScr.page15.label1.setGeometry(int(p * 300), int(p * 90), int(p * 450), int(p * 400))
    self.helpScr.page15.imageLabel.setGeometry(int(p * 60), int(p * 75), int(p * 165), int(p * 320))
    self.helpScr.page15.imageLabel.setPixmap(self.helpScr.page15.imagePixmap.scaled(
            self.helpScr.page15.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page15.logoLabel.setPixmap(self.helpScr.page15.logoPixmap.scaled(
            self.helpScr.page15.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))


    #page16
    self.helpScr.page16.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page16.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page16.titleLabel.setGeometry(int(p * 280), int(p * 10), int(p * 550), int(p * 100))
    self.helpScr.page16.label1.setGeometry(int(p * 5), int(p * 80), int(p * 790), int(p * 100))
    self.helpScr.page16.imageLabel.setGeometry(int(p * 130), int(p * 130), int(p * 510), int(p * 270))
    self.helpScr.page16.imageLabel.setPixmap(self.helpScr.page16.imagePixmap.scaled(
            self.helpScr.page16.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page16.logoLabel.setPixmap(self.helpScr.page16.logoPixmap.scaled(
            self.helpScr.page16.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page17
    self.helpScr.page17.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page17.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page17.titleLabel.setGeometry(int(p * 280), int(p * 10), int(p * 550), int(p * 100))
    self.helpScr.page17.label1.setGeometry(int(p * 5), int(p * 110), int(p * 790), int(p * 400))
    self.helpScr.page17.imageLabel.setGeometry(int(p * 130), int(p * 170), int(p * 510), int(p * 115))
    self.helpScr.page17.imageLabel.setPixmap(self.helpScr.page17.imagePixmap.scaled(
            self.helpScr.page17.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page17.logoLabel.setPixmap(self.helpScr.page17.logoPixmap.scaled(
            self.helpScr.page17.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page18
    self.helpScr.page18.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page18.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page18.titleLabel.setGeometry(int(p * 280), int(p * 10), int(p * 550), int(p * 100))
    self.helpScr.page18.label1.setGeometry(int(p * 5), int(p * 110), int(p * 790), int(p * 400))
    self.helpScr.page18.imageLabel1.setGeometry(int(p * 200), int(p * 240), int(p * 423), int(p * 110))
    self.helpScr.page18.imageLabel2.setGeometry(int(p * 0), int(p * 340), int(p * 360), int(p * 55))
    self.helpScr.page18.imageLabel3.setGeometry(int(p * 500), int(p * 320), int(p * 510), int(p * 115))

    self.helpScr.page18.imageLabel1.setPixmap(self.helpScr.page18.imagePixmap1.scaled(
            self.helpScr.page18.imageLabel1.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page18.imageLabel2.setPixmap(self.helpScr.page18.imagePixmap2.scaled(
            self.helpScr.page18.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page18.imageLabel3.setPixmap(self.helpScr.page18.imagePixmap3.scaled(
            self.helpScr.page18.imageLabel3.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page18.logoLabel.setPixmap(self.helpScr.page18.logoPixmap.scaled(
            self.helpScr.page18.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    


    #page19
    self.helpScr.page19.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page19.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page19.titleLabel.setGeometry(int(p * 280), int(p * 5), int(p * 550), int(p * 100))
    self.helpScr.page19.label1.setGeometry(int(p * 5), int(p * 80), int(p * 790), int(p * 100))
    self.helpScr.page19.imageLabel.setGeometry(int(p * 0), int(p * 200), int(p * 800), int(p * 135))
    self.helpScr.page19.imageLabel.setPixmap(self.helpScr.page19.imagePixmap.scaled(
            self.helpScr.page19.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page19.logoLabel.setPixmap(self.helpScr.page19.logoPixmap.scaled(
            self.helpScr.page19.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page20
    self.helpScr.page20.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page20.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page20.titleLabel.setGeometry(int(p * 280), int(p * 5), int(p * 550), int(p * 100))
    self.helpScr.page20.label1.setGeometry(int(p * 5), int(p * 80), int(p * 790), int(p * 400))
    self.helpScr.page20.imageLabel.setGeometry(int(p * 210), int(p * 150), int(p * 345), int(p * 200))
    self.helpScr.page20.imageLabel.setPixmap(self.helpScr.page20.imagePixmap.scaled(
            self.helpScr.page20.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page20.logoLabel.setPixmap(self.helpScr.page20.logoPixmap.scaled(
            self.helpScr.page20.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page21
    self.helpScr.page21.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page21.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page21.titleLabel.setGeometry(int(p * 280), int(p * 5), int(p * 550), int(p * 100))
    self.helpScr.page21.label1.setGeometry(int(p * 5), int(p * 80), int(p * 790), int(p * 400))
    self.helpScr.page21.label2.setGeometry(int(p * 430), int(p * 210), int(p * 350), int(p * 400))
    self.helpScr.page21.imageLabel.setGeometry(int(p * 10), int(p * 190), int(p * 410), int(p * 200))
    self.helpScr.page21.imageLabel.setPixmap(self.helpScr.page21.imagePixmap.scaled(
            self.helpScr.page21.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    self.helpScr.page21.logoLabel.setPixmap(self.helpScr.page21.logoPixmap.scaled(
            self.helpScr.page21.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page22
    self.helpScr.page22.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page22.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page22.titleLabel.setGeometry(int(p * 280), int(p * 5), int(p * 550), int(p * 100))
    self.helpScr.page22.label1.setGeometry(int(p * 5), int(p * 80), int(p * 340), int(p * 400))
    self.helpScr.page22.imageLabel.setGeometry(int(p * 500), int(p * 90), int(p * 250), int(p * 243))
    self.helpScr.page22.imageLabel2.setGeometry(int(p * 520), int(p * 340), int(p * 220), int(p * 55))
    self.helpScr.page22.imageLabel.setPixmap(self.helpScr.page22.imagePixmap.scaled(
            self.helpScr.page22.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page22.imageLabel2.setPixmap(self.helpScr.page22.imagePixmap2.scaled(
            self.helpScr.page22.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page22.logoLabel.setPixmap(self.helpScr.page22.logoPixmap.scaled(
            self.helpScr.page22.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page23
    self.helpScr.page23.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page23.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page23.titleLabel.setGeometry(int(p * 280), int(p * 5), int(p * 550), int(p * 100))
    self.helpScr.page23.label1.setGeometry(int(p * 250), int(p * 120), int(p * 340), int(p * 400))
    self.helpScr.page23.label2.setGeometry(int(p * 230), int(p * 250), int(p * 340), int(p * 400))
    self.helpScr.page23.imageLabel.setGeometry(int(p * 50), int(p * 90), int(p * 160), int(p * 175))
    self.helpScr.page23.imageLabel2.setGeometry(int(p * 600), int(p * 230), int(p * 160), int(p * 175))
    self.helpScr.page23.imageLabel.setPixmap(self.helpScr.page23.imagePixmap.scaled(
            self.helpScr.page23.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page23.imageLabel2.setPixmap(self.helpScr.page23.imagePixmap2.scaled(
            self.helpScr.page23.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page23.logoLabel.setPixmap(self.helpScr.page23.logoPixmap.scaled(
            self.helpScr.page23.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page24
    self.helpScr.page24.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page24.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page24.titleLabel.setGeometry(int(p * 280), int(p * 5), int(p * 550), int(p * 100))
    self.helpScr.page24.label1.setGeometry(int(p * 5), int(p * 90), int(p * 780), int(p * 400))
    self.helpScr.page24.imageLabel.setGeometry(int(p * 50), int(p * 200), int(p * 220), int(p * 175))
    self.helpScr.page24.imageLabel2.setGeometry(int(p * 500), int(p * 200), int(p * 220), int(p * 175))
    self.helpScr.page24.imageLabel.setPixmap(self.helpScr.page24.imagePixmap.scaled(
            self.helpScr.page24.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page24.imageLabel2.setPixmap(self.helpScr.page24.imagePixmap2.scaled(
            self.helpScr.page24.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page24.logoLabel.setPixmap(self.helpScr.page24.logoPixmap.scaled(
            self.helpScr.page24.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page25
    self.helpScr.page25.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page25.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page25.titleLabel.setGeometry(int(p * 280), int(p * 5), int(p * 550), int(p * 100))
    self.helpScr.page25.label1.setGeometry(int(p * 0), int(p * 90), int(p * 800), int(p * 400))
    self.helpScr.page25.imageLabel.setGeometry(int(p * 80), int(p * 185), int(p * 125), int(p * 200))
    self.helpScr.page25.imageLabel2.setGeometry(int(p * 500), int(p * 185), int(p * 280), int(p * 120))
    self.helpScr.page25.imageLabel3.setGeometry(int(p * 500), int(p * 310), int(p * 280), int(p * 50))
    self.helpScr.page25.imageLabel.setPixmap(self.helpScr.page25.imagePixmap.scaled(
            self.helpScr.page25.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page25.imageLabel2.setPixmap(self.helpScr.page25.imagePixmap2.scaled(
            self.helpScr.page25.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    self.helpScr.page25.imageLabel3.setPixmap(self.helpScr.page25.imagePixmap3.scaled(
            self.helpScr.page25.imageLabel3.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page25.logoLabel.setPixmap(self.helpScr.page25.logoPixmap.scaled(
            self.helpScr.page25.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page26
    self.helpScr.page26.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page26.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page26.titleLabel.setGeometry(int(p * 280), int(p * 5), int(p * 550), int(p * 100))
    self.helpScr.page26.label1.setGeometry(int(p * 20), int(p * 120), int(p * 340), int(p * 400))
    self.helpScr.page26.label2.setGeometry(int(p * 370), int(p * 250), int(p * 340), int(p * 400))
    self.helpScr.page26.imageLabel.setGeometry(int(p * 500), int(p * 90), int(p * 170), int(p * 120))
    self.helpScr.page26.imageLabel2.setGeometry(int(p * 80), int(p * 250), int(p * 170), int(p * 80))
    self.helpScr.page26.label3.setGeometry(int(p * -5), int(p * 370), int(p * 790), int(p * 100))
    self.helpScr.page26.imageLabel.setPixmap(self.helpScr.page26.imagePixmap.scaled(
            self.helpScr.page26.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page26.imageLabel2.setPixmap(self.helpScr.page26.imagePixmap2.scaled(
            self.helpScr.page26.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page26.logoLabel.setPixmap(self.helpScr.page26.logoPixmap.scaled(
            self.helpScr.page26.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    

    #page27
    self.helpScr.page27.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page27.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page27.titleLabel.setGeometry(int(p * 260), int(p * 5), int(p * 550), int(p * 100))
    self.helpScr.page27.imageLabel.setGeometry(int(p * 80), int(p * 90), int(p * 625), int(p * 270))
    self.helpScr.page27.imageLabel.setPixmap(self.helpScr.page27.imagePixmap.scaled(
            self.helpScr.page27.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page27.logoLabel.setPixmap(self.helpScr.page27.logoPixmap.scaled(
            self.helpScr.page27.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page28
    self.helpScr.page28.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page28.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page28.titleLabel.setGeometry(int(p * 260), int(p * 5), int(p * 550), int(p * 100))
    self.helpScr.page28.label1.setGeometry(int(p * 0), int(p * 360), int(p * 800), int(p * 400))
    self.helpScr.page28.imageLabel.setGeometry(int(p * 80), int(p * 80), int(p * 625), int(p * 270))
    self.helpScr.page28.imageLabel.setPixmap(self.helpScr.page28.imagePixmap.scaled(
            self.helpScr.page28.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page28.logoLabel.setPixmap(self.helpScr.page28.logoPixmap.scaled(
            self.helpScr.page28.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page29
    self.helpScr.page29.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page29.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page29.titleLabel.setGeometry(int(p * 220), int(p * 15), int(p * 550), int(p * 100))
    self.helpScr.page29.label1.setGeometry(int(p * 0), int(p * 90), int(p * 800), int(p * 400))
    self.helpScr.page29.label2.setGeometry(int(p * 430), int(p * 200), int(p * 350), int(p * 400))
    self.helpScr.page29.imageLabel.setGeometry(int(p * 20), int(p * 150), int(p * 400), int(p * 200))
    self.helpScr.page29.imageLabel.setPixmap(self.helpScr.page29.imagePixmap.scaled(
            self.helpScr.page29.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page29.logoLabel.setPixmap(self.helpScr.page29.logoPixmap.scaled(
            self.helpScr.page29.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page30
    self.helpScr.page30.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page30.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page30.titleLabel.setGeometry(int(p * 220), int(p * 15), int(p * 550), int(p * 100))
    self.helpScr.page30.label1.setGeometry(int(p * 160), int(p * 120), int(p * 660), int(p * 400))
    self.helpScr.page30.label2.setGeometry(int(p * 190), int(p * 215), int(p * 350), int(p * 400))
    self.helpScr.page30.label3.setGeometry(int(p * 190), int(p * 340), int(p * 350), int(p * 400))
    self.helpScr.page30.imageLabel.setGeometry(int(p * 20), int(p * 90), int(p * 100), int(p * 300))
    self.helpScr.page30.imageLabel2.setGeometry(int(p * 550), int(p * 170), int(p * 240), int(p * 140))
    self.helpScr.page30.imageLabel3.setGeometry(int(p * 550), int(p * 320), int(p * 220), int(p * 70))
    self.helpScr.page30.imageLabel.setPixmap(self.helpScr.page30.imagePixmap.scaled(
            self.helpScr.page30.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page30.imageLabel2.setPixmap(self.helpScr.page30.imagePixmap2.scaled(
            self.helpScr.page30.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    self.helpScr.page30.imageLabel3.setPixmap(self.helpScr.page30.imagePixmap3.scaled(
            self.helpScr.page30.imageLabel3.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page30.logoLabel.setPixmap(self.helpScr.page30.logoPixmap.scaled(
            self.helpScr.page30.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page31
    self.helpScr.page31.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page31.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page31.titleLabel.setGeometry(int(p * 220), int(p * 15), int(p * 550), int(p * 100))
    self.helpScr.page31.label1.setGeometry(int(p * 390), int(p * 110), int(p * 400), int(p * 400))
    self.helpScr.page31.label2.setGeometry(int(p * 0), int(p * 290), int(p * 390), int(p * 400))
    self.helpScr.page31.imageLabel.setGeometry(int(p * 0), int(p * 110), int(p * 370), int(p * 85))
    self.helpScr.page31.imageLabel2.setGeometry(int(p * 430), int(p * 290), int(p * 370), int(p * 85))
    self.helpScr.page31.imageLabel.setPixmap(self.helpScr.page31.imagePixmap.scaled(
            self.helpScr.page31.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page31.imageLabel2.setPixmap(self.helpScr.page31.imagePixmap2.scaled(
            self.helpScr.page31.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page31.logoLabel.setPixmap(self.helpScr.page31.logoPixmap.scaled(
            self.helpScr.page31.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page32
    self.helpScr.page32.logoLabel.setGeometry(int(p * 0), int(p * 0), int(p * 200), int(p * 70))
    self.helpScr.page32.backgroundLabel.setGeometry(int(p * 0), int(p * 10), int(p * 800), int(p * 60))
    self.helpScr.page32.titleLabel.setGeometry(int(p * 220), int(p * 15), int(p * 550), int(p * 100))
    self.helpScr.page32.label1.setGeometry(int(p * 240), int(p * 110), int(p * 400), int(p * 400))
    self.helpScr.page32.label2.setGeometry(int(p * 120), int(p * 290), int(p * 390), int(p * 400))
    self.helpScr.page32.imageLabel.setGeometry(int(p * 80), int(p * 80), int(p * 150), int(p * 150))
    self.helpScr.page32.imageLabel2.setGeometry(int(p * 520), int(p * 210), int(p * 170), int(p * 190))
    self.helpScr.page32.imageLabel.setPixmap(self.helpScr.page32.imagePixmap.scaled(
            self.helpScr.page32.imageLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page32.imageLabel2.setPixmap(self.helpScr.page32.imagePixmap2.scaled(
            self.helpScr.page32.imageLabel2.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
    
    self.helpScr.page32.logoLabel.setPixmap(self.helpScr.page32.logoPixmap.scaled(
            self.helpScr.page32.logoLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))

    #page33
    self.helpScr.page33.backgroundLabel.setGeometry(int(p * 0), int(p * 100), int(p * 800), int(p * 230))
    self.helpScr.page33.titleLabel.setGeometry(int(p * 0), int(p * 15), int(p * 800), int(p * 100))
    self.helpScr.page33.label1.setGeometry(int(p * 10), int(p * 110), int(p * 780), int(p * 400))

    if p <= 1366/(1920 * 0.8): #resolução com largura <= 1366
        self.helpScr.pageChangerContainer.setGeometry(int(self.p_help * 600), int(self.p_help * 385), 160, 90)

        #page4
        self.helpScr.page4.label1.setFont(QFont("Microsoft Sans Serif", 12))
        self.helpScr.page4.label1.setGeometry(int(p * 480), int(p * 150), int(p * 260), int(p * 200))

        #page7
        self.helpScr.page7.label1.setFont(QFont("Microsoft Sans Serif", 12))

        #page9, 10, 11
        self.helpScr.page9.titleLabel.setFont(QFont("Calibri", 18))
        self.helpScr.page10.titleLabel.setFont(QFont("Calibri", 18))
        self.helpScr.page11.titleLabel.setFont(QFont("Calibri", 18))

        #page13
        self.helpScr.page13.label1.setFont(QFont("Microsoft Sans Serif", 12))

        #page14
        self.helpScr.page14.label1.setFont(QFont("Microsoft Sans Serif", 12))

        #page15
        self.helpScr.page15.label1.setFont(QFont("Microsoft Sans Serif", 12))

        #page19
        self.helpScr.page19.titleLabel.setFont(QFont("Calibri", 18))

        #page24, 25, 26, 27, 28, 29, 30, 31
        self.helpScr.page24.titleLabel.setFont(QFont("Calibri", 18))
        self.helpScr.page25.titleLabel.setFont(QFont("Calibri", 18))
        self.helpScr.page26.titleLabel.setFont(QFont("Calibri", 18))
        self.helpScr.page27.titleLabel.setFont(QFont("Calibri", 16))
        self.helpScr.page28.titleLabel.setFont(QFont("Calibri", 16))
        self.helpScr.page29.titleLabel.setFont(QFont("Calibri", 18))
        self.helpScr.page30.titleLabel.setFont(QFont("Calibri", 18))
        self.helpScr.page31.titleLabel.setFont(QFont("Calibri", 18))

        #page31
        self.helpScr.page31.label2.setFont(QFont("Microsoft Sans Serif", 12))
        self.helpScr.page31.label2.setGeometry(int(p * 0), int(p * 260), int(p * 390), int(p * 400))

        #page33
        #ver por que não está funcionando:
        self.helpScr.page33.backgroundLabel.setGeometry(int(p * 0), int(p * 100), int(p * 800), int(p * 270))


        
        
        

