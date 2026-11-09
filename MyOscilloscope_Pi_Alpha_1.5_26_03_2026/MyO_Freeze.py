from PySide6.QtCore import Qt
import numpy as np

# 

#Método de Freeze
def FreezeActivated(self): #Freeze não foi incluso na classe Button pelo formato diferente...
    if self.btOnOff.isOn == True:
        #self.UpdateSecondaryButtonImages()
        if self.btFreeze.isOn == True: self.mainScr.freezeTime = True
        else:                          self.mainScr.freezeTime = False
    else:
        self.mainScr.freezeTime = False
        self.btFreeze.label.setPixmap(self.btFreeze.image1.scaled(self.btFreeze.label.size(),
                                                              Qt.KeepAspectRatio))







