def fadeIn(self):
    self.screen1.hide()
    self.screen2.setGeometry(1, 1, 1, 1)
    self.screen3.setGeometry(1, 1, 1, 1)
    self.screen4.setGeometry(1, 1, 1, 1)
    
    self.fadeLabelScr1.setGeometry(int(self.p * 15), int(self.p * 310), int(self.p * 1170), int(self.p * 563))
    self.fadeLabelScr3.setGeometry(int(self.p * 1140), int(self.p * 105), int(self.p * 745), int(self.p * 165))
    self.fadeLabelScr4.setGeometry(int(self.p * 113), int(self.p * 900), int(self.p * 407), int(self.p * 80))
    if self.i <= 150:
        color = f"background-color: rgb({self.i}, {self.i}, {self.i});"
        self.fadeLabelScr1.setStyleSheet(color)
        self.fadeLabelScr3.setStyleSheet(color)
        self.fadeLabelScr4.setStyleSheet(color)
        self.i += 4
        self.btOnOff.setEnabled(False)
    else:
        self.fadeInTimer.stop()
        self.fadeLabelScr1.setGeometry(1, 1, 1, 1)
        self.fadeLabelScr3.setGeometry(1, 1, 1, 1)
        self.fadeLabelScr4.setGeometry(1, 1, 1, 1)
        self.screen1.show()
        self.screen1.setGeometry(int(self.p * 17), int(self.p * 336), int(self.p * 990), int(self.p * 511))
        if self.mainScr.COMPortON: 
            if self.language == "English": self.standbyScr1.updatePixmap(self.standbyScr1.pixmap1)
            else: self.standbyScr1.updatePixmap(self.standbyScr1.pixmap3)
        self.screen2.setGeometry(int(self.p * 1015), int(self.p * 300), int(self.p * 175), int(self.p * 580))
        self.screen3.setGeometry(int(self.p * 1140), int(self.p * 105), int(self.p * 745), int(self.p * 165))
        self.screen4.setGeometry(int(self.p * 113), int(self.p * 900), int(self.p * 407), int(self.p * 80))
        self.bt_Wfm.moveButton(int(self.p * 1600), int(self.p * 105))
        self.bt_Calibration.moveButton(int(self.p * 1675), int(self.p * 105))
        self.bt_Exp.moveButton(int(self.p * 1750), int(self.p * 105))
        self.bt_MathPlus.moveButton(int(self.p * 1825), int(self.p * 105))
        self.btOnOff.setEnabled(True)
        #self.bt_site_and_bt_videos_off.move(-3000, -3000)
    
    

def fadeOut(self):

    self.screen1.setGeometry(1, 1, 1, 1)
    self.screen2.setGeometry(1, 1, 1, 1)
    self.screen3.setGeometry(1, 1, 1, 1)
    self.screen4.setGeometry(1, 1, 1, 1)
    self.blackLabel1.hide()
    self.blackLabel2.hide()
    self.phaseLabel.move(3000, 3000)
    self.fadeLabelScr1.setGeometry(int(self.p * 15), int(self.p * 310), int(self.p * 1170), int(self.p * 563))
    self.fadeLabelScr3.setGeometry(int(self.p * 1140), int(self.p * 105), int(self.p * 745), int(self.p * 165))
    self.fadeLabelScr4.setGeometry(int(self.p * 113), int(self.p * 900), int(self.p * 407), int(self.p * 80))

    self.bt_Wfm.moveButton(-100, -100)
    self.bt_Calibration.moveButton(-100, -100)
    self.bt_Exp.moveButton(-100, -100)
    self.bt_MathPlus.moveButton(-100, -100)
    if self.i >= 0:
        color = f"background-color: rgb({self.i}, {self.i}, {self.i});"
        self.fadeLabelScr1.setStyleSheet(color)
        self.fadeLabelScr3.setStyleSheet(color)
        self.fadeLabelScr4.setStyleSheet(color)
        self.i -= 4
        self.btOnOff.setEnabled(False)
    else:
        self.fadeOutTimer.stop()
        self.fadeLabelScr1.setGeometry(1, 1, 1, 1)
        self.fadeLabelScr3.setGeometry(1, 1, 1, 1)
        self.fadeLabelScr4.setGeometry(1, 1, 1, 1)
        self.btOnOff.setEnabled(True)
    #self.bt_site_and_bt_videos_off.move(int(p*870), int(p*70))