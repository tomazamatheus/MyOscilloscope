
#NOTA: Se está procurando pela seção associada a Math para ajustes, talvez encontre o que procura na classe
# DataHandler(), em MainScreen1.py

def ChangeMathMode(self):
    if self.mathPlusScr.simpleOperationsCB.currentText() == "CH1 + CH2":
        self.mainScr.dataHandler.mathMode = "CH1 + CH2"

    elif self.mathPlusScr.simpleOperationsCB.currentText() == "CH1 - CH2":
        self.mainScr.dataHandler.mathMode = "CH1 - CH2"

    elif self.mathPlusScr.simpleOperationsCB.currentText() == "CH2 - CH1":
        self.mainScr.dataHandler.mathMode = "CH2 - CH1"

    elif self.mathPlusScr.simpleOperationsCB.currentText() == "CH1 * CH2":
        self.mainScr.dataHandler.mathMode = "CH1 * CH2"

    elif self.mathPlusScr.simpleOperationsCB.currentText() == "CH1 / CH2":
        self.mainScr.dataHandler.mathMode = "CH1 / CH2"

    elif self.mathPlusScr.simpleOperationsCB.currentText() == "CH2 / CH1":
        self.mainScr.dataHandler.mathMode = "CH2 / CH1"

