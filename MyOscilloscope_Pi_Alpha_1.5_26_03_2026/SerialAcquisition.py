import sys
import serial
import numpy as np
import os
os.environ["PYQTGRAPH_QT_LIB"] = "PySide6" #necessário para pyqtgraph com PySide6
import pyqtgraph as pg
from pyqtgraph import mkPen
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QObject, QThread, Signal


class SerialAcquisition(QObject):
    channels_buffers = Signal(list, list)
    errorSignal = Signal(bool)

    def __init__(self, serialPort, samplingRate, refreshRate):
        super().__init__()
        self.serialPort = serialPort
        self.running = True
        self.synchronized = False
        self.samplingRate = samplingRate
        self.refreshRate = refreshRate
        self.CH1Buffer = [0.0] *  int(0.5 * self.samplingRate)
        self.CH2Buffer = [0.0] *  int(0.5 * self.samplingRate)
        
        self.numberOfSerialReadings = self.samplingRate * 2 * (self.refreshRate * 2.5/1000)
        
    def run(self):
        j = 0
        k = 0
        while self.running:
            if not self.synchronized:
                    while self.running: #while True se thread ativa
                        try:
                            read = self.serialPort.read(1)
                            if read and read[0] == 10: 
                                self.synchronized = True
                            break

                        except serial.SerialException as e:
                            self.stop()
                            self.errorSignal.emit(True)
                            print("Serial error:", e)

                        
            else:
                try:
                    reading = self.serialPort.read(int(self.numberOfSerialReadings))
                    if not reading: raise serial.SerialException("Serial disconnected")
                    read = list(reading)
                    
                    arr = [] #vetor auxiliar
                    endOfVector = False
                    swapChannels = False
                    phaseCompensation = False #flag para ajustar um erro de defasagem associado a swapChannels
                    #separar a amostra coletada entre os dois canais, e evitar erro de inversão (quando o que é de um canal vai para o outro)
                    self.CH1 = []
                    self.CH2 = []
                    while self.running: #while true se thread ativa
                        if len(read) == 0: break
                        for k in range(len(read)): 
                            if read[k] == 10 or k == len(read) - 1: #se encontrar um \n ou o final de read:
                                if not k == len(read) - 1:
                                    arr = read[:k] #arr recebe o conteúdo de read do início até o \n 
                                    read = read[k+1:] #read fica com o que sobrou
                                    endOfVector = False
                                else:
                                    arr = read[: k+1]
                                    endOfVector = True
                                
                                if (len(arr)) % 2 == 1 and not endOfVector: swapChannels = True
                                else: swapChannels = False
                                    
                                    
                                # adiciona aos canais
                                
                                if not swapChannels:
                                    self.CH1.extend(arr[0::2])
                                    aux = arr[1::2]
                                    if phaseCompensation: 
                                        for i in range(len(aux) - 1): aux[i] = aux[i+1]
                                        #if len(self.CH2) > 1: self.CH2[-1] = aux[0]
                                    self.CH2.extend(aux)
                                    
                                else:
                                    phaseCompensation = True
                                    self.CH1.extend(arr[1::2])
                                    aux = arr[0::2]
                                    for i in range(len(aux) - 1): aux[i] = aux[i+1]
                                    if len(self.CH2) > 0: self.CH2[-1] = aux[0]
                                    self.CH2.extend(aux)
                                break

                        if endOfVector: break

                    
                except serial.SerialException as e:
                    self.stop()
                    self.errorSignal.emit(True)
                    print("Serial error:", e)

                
                if len(self.CH1) > 0 and len(self.CH2) > 0:
                    #Adicionando os bytes novos e "empurrando" os mais antigos para a esquerda
                    self.CH1Buffer[: len(self.CH1Buffer) - len(self.CH1)] = self.CH1Buffer[len(self.CH1) :]
                    self.CH1Buffer[len(self.CH1Buffer) - len(self.CH1):] = self.CH1[:]

                    self.CH2Buffer[: len(self.CH2Buffer) - len(self.CH2)] = self.CH2Buffer[len(self.CH2) :]
                    self.CH2Buffer[len(self.CH2Buffer) - len(self.CH2):] = self.CH2[:]
                    self.channels_buffers.emit(self.CH1Buffer, self.CH2Buffer)
                
                
    def stop(self):
        self.running = False
        try:
            if self.serialPort and self.serialPort.is_open:
                self.serialPort.close()
        except Exception:
            pass