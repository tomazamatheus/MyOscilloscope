from PySide6.QtGui import QPixmap, QPainter
import ExportImage_MeasurementsBar
import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import QRect, Qt
from ExportImage_MeasurementsBar import *
from MyO_PopUpWindows import *


def exportImage(self):
    if not self.screenName == "" and not self.screenName == "Help":
        if self.language == "English": windowName = "Save Capture as .png"
        else: windowName = "Salvar captura como .png"

        finalOutput, _ = QFileDialog.getSaveFileName(
        self,
        windowName,
        "",
        "PNG Files (*.png);;All Files (*)"
        )

        if not finalOutput:  # Caso a tela seja fechada
            return
        
        if not finalOutput.endswith(".png"): finalOutput += ".png"
        
        self.exp_bar = ExpImage_MeasureBar()
        self.exp_bar.resize(842, 200)

        if self.btCH1.isOn: print("CH1 on")
        if self.btCH2.isOn: print("CH2 on")
        if self.btMath.isOn: print("Math on")

        self.exp_bar.mainLabel2.setText("CH1")
        self.exp_bar.mainLabel2.setStyleSheet(""" color: rgb(0, 70, 134) """)

        #Ajustes de idioma:
        if self.language == "Português":
            self.exp_bar.freqLabel_1.setText("Frequência:")
            self.exp_bar.freqLabel_2.setText("Frequência:")
            self.exp_bar.freqLabel_3.setText("Frequência:")
            self.exp_bar.periodLabel_1.setText("Período:")
            self.exp_bar.periodLabel_2.setText("Período:")
            self.exp_bar.periodLabel_3.setText("Período:")
            self.exp_bar.DCLabel_1.setText("Valor Médio-DC:")
            self.exp_bar.DCLabel_2.setText("Valor Médio-DC:")
            self.exp_bar.DCLabel_3.setText("Valor Médio-DC:")
            self.exp_bar.RMSLabel_1.setText("RMS:")
            self.exp_bar.RMSLabel_2.setText("RMS:")
            self.exp_bar.RMSLabel_3.setText("RMS:")
            self.exp_bar.Pk_to_PkLabel_1.setText("Pico-a-Pico:")
            self.exp_bar.Pk_to_PkLabel_2.setText("Pico-a-Pico:")
            self.exp_bar.Pk_to_PkLabel_3.setText("Pico-a-Pico:")
            self.exp_bar.MinLabel_1.setText("Valor Mín.:")
            self.exp_bar.MinLabel_2.setText("Valor Mín.:")
            self.exp_bar.MinLabel_3.setText("Valor Mín.:")
            self.exp_bar.MaxLabel_1.setText("Valor Máx.:")
            self.exp_bar.MaxLabel_2.setText("Valor Máx.:")
            self.exp_bar.MaxLabel_3.setText("Valor Máx.:")
            self.exp_bar.phaseShiftLabel_1.setText("Defasagem:")
            self.exp_bar.phaseShiftLabel_2.setText("Defasagem:")
            self.exp_bar.phaseShiftLabel_3.setText("Defasagem:")

        def fill_lineEdits(labelNum, CH):
            if labelNum == 1:
                if CH == "CH1":
                    if self.freqCH1 < 1000:
                        self.exp_bar.freqLE_1.setText(f"{self.freqCH1:.3f} Hz")
                    else:
                        self.exp_bar.freqLE_1.setText(f"{(self.freqCH1/1000):.3f} kHz")

                    if self.periodCH1 > 0.001:
                        self.exp_bar.periodLE_1.setText(f"{(self.periodCH1 * 1000):.3f} ms")
                    elif self.periodCH1 > 0.000001:
                        self.exp_bar.periodLE_1.setText(f"{(self.periodCH1 * 1000000):.3f} us")
                    else:
                        self.exp_bar.periodLE_1.setText(f"< 1 us")

                    if not self.currentForCH1Scale:
                        if self.CH1MeanValue > 0.9 or self.CH1MeanValue < -0.9:
                            self.exp_bar.DCLE_1.setText(f"{self.CH1MeanValue:.3f} V")
                        elif self.CH1MeanValue > 0.001 or self.CH1MeanValue < -0.001:
                            self.exp_bar.DCLE_1.setText(f"{(self.CH1MeanValue * 1000):.2f} mV")
                        elif self.CH1MeanValue > 0.000001 or self.CH1MeanValue < -0.000001:
                            self.exp_bar.DCLE_1.setText(f"{(self.CH1MeanValue * 1000000):.1f} µV")

                        if self.CH1VppValue > 0.9 or self.CH1VppValue < -0.9:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{self.CH1VppValue:.2f} V")
                        elif self.CH1VppValue > 0.001 or self.CH1VppValue < -0.001:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{(self.CH1VppValue * 1000):.2f} mV")
                        elif self.CH1VppValue > 0.000001 or self.CH1VppValue < -0.000001:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{(self.CH1VppValue * 1000000):.2f} µV")

                        if self.CH1VRMSValue > 0.9 or self.CH1VRMSValue < -0.9:
                            self.exp_bar.RMSLE_1.setText(f"{self.CH1VRMSValue:.2f} V")
                        elif self.CH1VRMSValue > 0.001 or self.CH1VRMSValue < -0.001:
                            self.exp_bar.RMSLE_1.setText(f"{(self.CH1VRMSValue * 1000):.2f} mV")
                        elif self.CH1VRMSValue > 0.000001 or self.CH1VRMSValue < -0.000001:
                            self.exp_bar.RMSLE_1.setText(f"{(self.CH1VRMSValue * 1000000):.2f} µV")

                        if self.yMaxCH1 > 0.9 or self.yMaxCH1 < -0.9:
                            self.exp_bar.MaxLE_1.setText(f"{self.yMaxCH1:.2f} V")
                        elif self.yMaxCH1 > 0.001 or self.yMaxCH1 < -0.001:
                            self.exp_bar.MaxLE_1.setText(f"{(self.yMaxCH1 * 1000):.2f} mV")
                        elif self.yMaxCH1 > 0.000001 or self.yMaxCH1 < -0.000001:
                            self.exp_bar.MaxLE_1.setText(f"{(self.yMaxCH1 * 1000000):.2f} µV")

                        if self.yMinCH1 > 0.9 or self.yMinCH1 < -0.9:
                            self.exp_bar.MinLE_1.setText(f"{self.yMinCH1:.2f} V")
                        elif self.yMinCH1 > 0.001 or self.yMinCH1 < -0.001:
                            self.exp_bar.MinLE_1.setText(f"{(self.yMinCH1 * 1000):.2f} mV")
                        elif self.yMinCH1 > 0.000001 or self.yMinCH1 < -0.000001:
                            self.exp_bar.MinLE_1.setText(f"{(self.yMinCH1 * 1000000):.2f} µV")

                    else:
                        if self.CH1MeanValue/self.shuntRes_CH1 > 0.9 or self.CH1MeanValue/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.DCLE_1.setText(f"{self.CH1MeanValue/self.shuntRes_CH1:.3f} A")
                        elif self.CH1MeanValue/self.shuntRes_CH1 > 0.001 or self.CH1MeanValue/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.DCLE_1.setText(f"{(self.CH1MeanValue/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.CH1MeanValue/self.shuntRes_CH1 > 0.000001 or self.CH1MeanValue/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.DCLE_1.setText(f"{(self.CH1MeanValue/self.shuntRes_CH1 * 1000000):.1f} µA")

                        if self.CH1VppValue/self.shuntRes_CH1 > 0.9 or self.CH1VppValue/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{self.CH1VppValue/self.shuntRes_CH1:.2f} A")
                        elif self.CH1VppValue/self.shuntRes_CH1 > 0.001 or self.CH1VppValue/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{(self.CH1VppValue/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.CH1VppValue/self.shuntRes_CH1 > 0.000001 or self.CH1VppValue/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{(self.CH1VppValue/self.shuntRes_CH1 * 1000000):.2f} µA")

                        if self.CH1VRMSValue/self.shuntRes_CH1 > 0.9 or self.CH1VRMSValue/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.RMSLE_1.setText(f"{self.CH1VRMSValue/self.shuntRes_CH1:.2f} A")
                        elif self.CH1VRMSValue/self.shuntRes_CH1 > 0.001 or self.CH1VRMSValue/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.RMSLE_1.setText(f"{(self.CH1VRMSValue/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.CH1VRMSValue/self.shuntRes_CH1 > 0.000001 or self.CH1VRMSValue/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.RMSLE_1.setText(f"{(self.CH1VRMSValue/self.shuntRes_CH1 * 1000000):.2f} µA")

                        if self.yMaxCH1/self.shuntRes_CH1 > 0.9 or self.yMaxCH1/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.MaxLE_1.setText(f"{self.yMaxCH1/self.shuntRes_CH1:.2f} A")
                        elif self.yMaxCH1/self.shuntRes_CH1 > 0.001 or self.yMaxCH1/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.MaxLE_1.setText(f"{(self.yMaxCH1/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.yMaxCH1/self.shuntRes_CH1 > 0.000001 or self.yMaxCH1/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.MaxLE_1.setText(f"{(self.yMaxCH1/self.shuntRes_CH1 * 1000000):.2f} µA")

                        if self.yMinCH1/self.shuntRes_CH1 > 0.9 or self.yMinCH1/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.MinLE_1.setText(f"{self.yMinCH1/self.shuntRes_CH1:.2f} A")
                        elif self.yMinCH1/self.shuntRes_CH1 > 0.001 or self.yMinCH1/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.MinLE_1.setText(f"{(self.yMinCH1/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.yMinCH1/self.shuntRes_CH1 > 0.000001 or self.yMinCH1/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.MinLE_1.setText(f"{(self.yMinCH1/self.shuntRes_CH1 * 1000000):.2f} µA")


                    self.exp_bar.phaseShiftLE_1.setText(f"{self.CH1Phase:.1f}°")

                elif CH == "CH2":
                    if self.freqCH2 < 1000:
                        self.exp_bar.freqLE_1.setText(f"{self.freqCH2:.3f} Hz")
                    else:
                        self.exp_bar.freqLE_1.setText(f"{(self.freqCH2/1000):.3f} kHz")

                    if self.periodCH2 > 0.001:
                        self.exp_bar.periodLE_1.setText(f"{(self.periodCH2 * 1000):.3f} ms")
                    elif self.periodCH2 > 0.000001:
                        self.exp_bar.periodLE_1.setText(f"{(self.periodCH2 * 1000000):.3f} us")
                    else:
                        self.exp_bar.periodLE_1.setText(f"< 1 us")

                    if not self.currentForCH2Scale:
                        if self.CH2MeanValue > 0.9 or self.CH2MeanValue < -0.9:
                            self.exp_bar.DCLE_1.setText(f"{self.CH2MeanValue:.3f} V")
                        elif self.CH2MeanValue > 0.001 or self.CH2MeanValue < -0.001:
                            self.exp_bar.DCLE_1.setText(f"{(self.CH2MeanValue * 1000):.2f} mV")
                        elif self.CH2MeanValue > 0.000001 or self.CH2MeanValue < -0.000001:
                            self.exp_bar.DCLE_1.setText(f"{(self.CH2MeanValue * 1000000):.1f} µV")

                        if self.CH2VppValue > 0.9 or self.CH2VppValue < -0.9:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{self.CH2VppValue:.2f} V")
                        elif self.CH2VppValue > 0.001 or self.CH2VppValue < -0.001:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{(self.CH2VppValue * 1000):.2f} mV")
                        elif self.CH2VppValue > 0.000001 or self.CH2VppValue < -0.000001:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{(self.CH2VppValue * 1000000):.2f} µV")

                        if self.CH2VRMSValue > 0.9 or self.CH2VRMSValue < -0.9:
                            self.exp_bar.RMSLE_1.setText(f"{self.CH2VRMSValue:.2f} V")
                        elif self.CH2VRMSValue > 0.001 or self.CH2VRMSValue < -0.001:
                            self.exp_bar.RMSLE_1.setText(f"{(self.CH2VRMSValue * 1000):.2f} mV")
                        elif self.CH2VRMSValue > 0.000001 or self.CH2VRMSValue < -0.000001:
                            self.exp_bar.RMSLE_1.setText(f"{(self.CH2VRMSValue * 1000000):.2f} µV")

                        if self.yMaxCH2 > 0.9 or self.yMaxCH2 < -0.9:
                            self.exp_bar.MaxLE_1.setText(f"{self.yMaxCH2:.2f} V")
                        elif self.yMaxCH2 > 0.001 or self.yMaxCH2 < -0.001:
                            self.exp_bar.MaxLE_1.setText(f"{(self.yMaxCH2 * 1000):.2f} mV")
                        elif self.yMaxCH2 > 0.000001 or self.yMaxCH2 < -0.000001:
                            self.exp_bar.MaxLE_1.setText(f"{(self.yMaxCH2 * 1000000):.2f} µV")

                        if self.yMinCH2 > 0.9 or self.yMinCH2 < -0.9:
                            self.exp_bar.MinLE_1.setText(f"{self.yMinCH2:.2f} V")
                        elif self.yMinCH2 > 0.001 or self.yMinCH2 < -0.001:
                            self.exp_bar.MinLE_1.setText(f"{(self.yMinCH2 * 1000):.2f} mV")
                        elif self.yMinCH2 > 0.000001 or self.yMinCH2 < -0.000001:
                            self.exp_bar.MinLE_1.setText(f"{(self.yMinCH2 * 1000000):.2f} µV")

                    else:
                        if self.CH2MeanValue/self.shuntRes_CH2 > 0.9 or self.CH2MeanValue/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.DCLE_1.setText(f"{self.CH2MeanValue/self.shuntRes_CH2:.3f} A")
                        elif self.CH2MeanValue/self.shuntRes_CH2 > 0.001 or self.CH2MeanValue/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.DCLE_1.setText(f"{(self.CH2MeanValue/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.CH2MeanValue/self.shuntRes_CH2 > 0.000001 or self.CH2MeanValue/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.DCLE_1.setText(f"{(self.CH2MeanValue/self.shuntRes_CH2 * 1000000):.1f} µA")

                        if self.CH2VppValue/self.shuntRes_CH2 > 0.9 or self.CH2VppValue/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{self.CH2VppValue/self.shuntRes_CH2:.2f} A")
                        elif self.CH2VppValue/self.shuntRes_CH2 > 0.001 or self.CH2VppValue/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{(self.CH2VppValue/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.CH2VppValue/self.shuntRes_CH2 > 0.000001 or self.CH2VppValue/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{(self.CH2VppValue/self.shuntRes_CH2 * 1000000):.2f} µA")

                        if self.CH2VRMSValue/self.shuntRes_CH2 > 0.9 or self.CH2VRMSValue/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.RMSLE_1.setText(f"{self.CH2VRMSValue/self.shuntRes_CH2:.2f} A")
                        elif self.CH2VRMSValue/self.shuntRes_CH2 > 0.001 or self.CH2VRMSValue/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.RMSLE_1.setText(f"{(self.CH2VRMSValue/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.CH2VRMSValue/self.shuntRes_CH2 > 0.000001 or self.CH2VRMSValue/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.RMSLE_1.setText(f"{(self.CH2VRMSValue/self.shuntRes_CH2 * 1000000):.2f} µA")

                        if self.yMaxCH2/self.shuntRes_CH2 > 0.9 or self.yMaxCH2/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.MaxLE_1.setText(f"{self.yMaxCH2/self.shuntRes_CH2:.2f} A")
                        elif self.yMaxCH2/self.shuntRes_CH2 > 0.001 or self.yMaxCH2/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.MaxLE_1.setText(f"{(self.yMaxCH2/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.yMaxCH2/self.shuntRes_CH2 > 0.000001 or self.yMaxCH2/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.MaxLE_1.setText(f"{(self.yMaxCH2/self.shuntRes_CH2 * 1000000):.2f} µA")

                        if self.yMinCH2/self.shuntRes_CH2 > 0.9 or self.yMinCH2/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.MinLE_1.setText(f"{self.yMinCH2/self.shuntRes_CH2:.2f} A")
                        elif self.yMinCH2/self.shuntRes_CH2 > 0.001 or self.yMinCH2/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.MinLE_1.setText(f"{(self.yMinCH2/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.yMinCH2/self.shuntRes_CH2 > 0.000001 or self.yMinCH2/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.MinLE_1.setText(f"{(self.yMinCH2/self.shuntRes_CH2 * 1000000):.2f} µA")


                    self.exp_bar.phaseShiftLE_1.setText(f"{self.CH2Phase:.1f}°")

                elif CH == "Math":
                    if self.freqMath < 1000:
                        self.exp_bar.freqLE_1.setText(f"{self.freqMath:.3f} Hz")
                    else:
                        self.exp_bar.freqLE_1.setText(f"{(self.freqMath/1000):.3f} kHz")

                    if self.periodMath > 0.001:
                        self.exp_bar.periodLE_1.setText(f"{(self.periodMath * 1000):.3f} ms")
                    elif self.periodMath > 0.000001:
                        self.exp_bar.periodLE_1.setText(f"{(self.periodMath * 1000000):.3f} us")
                    else:
                        self.exp_bar.periodLE_1.setText(f"< 1 us")

                    if not self.currentForMathScale:
                        if self.mathMeanValue > 0.9 or self.mathMeanValue < -0.9:
                            self.exp_bar.DCLE_1.setText(f"{self.mathMeanValue:.3f} V")
                        elif self.mathMeanValue > 0.001 or self.mathMeanValue < -0.001:
                            self.exp_bar.DCLE_1.setText(f"{(self.mathMeanValue * 1000):.2f} mV")
                        elif self.mathMeanValue > 0.000001 or self.mathMeanValue < -0.000001:
                            self.exp_bar.DCLE_1.setText(f"{(self.mathMeanValue * 1000000):.1f} µV")

                        if self.mathVppValue > 0.9 or self.mathVppValue < -0.9:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{self.mathVppValue:.2f} V")
                        elif self.mathVppValue > 0.001 or self.mathVppValue < -0.001:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{(self.mathVppValue * 1000):.2f} mV")
                        elif self.mathVppValue > 0.000001 or self.mathVppValue < -0.000001:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{(self.mathVppValue * 1000000):.2f} µV")

                        if self.mathVRMSValue > 0.9 or self.mathVRMSValue < -0.9:
                            self.exp_bar.RMSLE_1.setText(f"{self.mathVRMSValue:.2f} V")
                        elif self.mathVRMSValue > 0.001 or self.mathVRMSValue < -0.001:
                            self.exp_bar.RMSLE_1.setText(f"{(self.mathVRMSValue * 1000):.2f} mV")
                        elif self.mathVRMSValue > 0.000001 or self.mathVRMSValue < -0.000001:
                            self.exp_bar.RMSLE_1.setText(f"{(self.mathVRMSValue * 1000000):.2f} µV")

                        if self.yMaxMath > 0.9 or self.yMaxMath < -0.9:
                            self.exp_bar.MaxLE_1.setText(f"{self.yMaxMath:.2f} V")
                        elif self.yMaxMath > 0.001 or self.yMaxMath < -0.001:
                            self.exp_bar.MaxLE_1.setText(f"{(self.yMaxMath * 1000):.2f} mV")
                        elif self.yMaxMath > 0.000001 or self.yMaxMath < -0.000001:
                            self.exp_bar.MaxLE_1.setText(f"{(self.yMaxMath * 1000000):.2f} µV")

                        if self.yMinMath > 0.9 or self.yMinMath < -0.9:
                            self.exp_bar.MinLE_1.setText(f"{self.yMinMath:.2f} V")
                        elif self.yMinMath > 0.001 or self.yMinMath < -0.001:
                            self.exp_bar.MinLE_1.setText(f"{(self.yMinMath * 1000):.2f} mV")
                        elif self.yMinMath > 0.000001 or self.yMinMath < -0.000001:
                            self.exp_bar.MinLE_1.setText(f"{(self.yMinMath * 1000000):.2f} µV")

                    else:
                        if self.mathMeanValue/self.shuntRes_Math > 0.9 or self.mathMeanValue/self.shuntRes_Math < -0.9:
                            self.exp_bar.DCLE_1.setText(f"{self.mathMeanValue/self.shuntRes_Math:.3f} A")
                        elif self.mathMeanValue/self.shuntRes_Math > 0.001 or self.mathMeanValue/self.shuntRes_Math < -0.001:
                            self.exp_bar.DCLE_1.setText(f"{(self.mathMeanValue/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.mathMeanValue/self.shuntRes_Math > 0.000001 or self.mathMeanValue/self.shuntRes_Math < -0.000001:
                            self.exp_bar.DCLE_1.setText(f"{(self.mathMeanValue/self.shuntRes_Math * 1000000):.1f} µA")

                        if self.mathVppValue/self.shuntRes_Math > 0.9 or self.mathVppValue/self.shuntRes_Math < -0.9:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{self.mathVppValue/self.shuntRes_Math:.2f} A")
                        elif self.mathVppValue/self.shuntRes_Math > 0.001 or self.mathVppValue/self.shuntRes_Math < -0.001:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{(self.mathVppValue/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.mathVppValue/self.shuntRes_Math > 0.000001 or self.mathVppValue/self.shuntRes_Math < -0.000001:
                            self.exp_bar.Pk_to_PkLE_1.setText(f"{(self.mathVppValue/self.shuntRes_Math * 1000000):.2f} µA")

                        if self.mathVRMSValue/self.shuntRes_Math > 0.9 or self.mathVRMSValue/self.shuntRes_Math < -0.9:
                            self.exp_bar.RMSLE_1.setText(f"{self.mathVRMSValue/self.shuntRes_Math:.2f} A")
                        elif self.mathVRMSValue/self.shuntRes_Math > 0.001 or self.mathVRMSValue/self.shuntRes_Math < -0.001:
                            self.exp_bar.RMSLE_1.setText(f"{(self.mathVRMSValue/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.mathVRMSValue/self.shuntRes_Math > 0.000001 or self.mathVRMSValue/self.shuntRes_Math < -0.000001:
                            self.exp_bar.RMSLE_1.setText(f"{(self.mathVRMSValue/self.shuntRes_Math * 1000000):.2f} µA")

                        if self.yMaxMath/self.shuntRes_Math > 0.9 or self.yMaxMath/self.shuntRes_Math < -0.9:
                            self.exp_bar.MaxLE_1.setText(f"{self.yMaxMath/self.shuntRes_Math:.2f} A")
                        elif self.yMaxMath/self.shuntRes_Math > 0.001 or self.yMaxMath/self.shuntRes_Math < -0.001:
                            self.exp_bar.MaxLE_1.setText(f"{(self.yMaxMath/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.yMaxMath/self.shuntRes_Math > 0.000001 or self.yMaxMath/self.shuntRes_Math < -0.000001:
                            self.exp_bar.MaxLE_1.setText(f"{(self.yMaxMath/self.shuntRes_Math * 1000000):.2f} µA")

                        if self.yMinMath/self.shuntRes_Math > 0.9 or self.yMinMath/self.shuntRes_Math < -0.9:
                            self.exp_bar.MinLE_1.setText(f"{self.yMinMath/self.shuntRes_Math:.2f} A")
                        elif self.yMinMath/self.shuntRes_Math > 0.001 or self.yMinMath/self.shuntRes_Math < -0.001:
                            self.exp_bar.MinLE_1.setText(f"{(self.yMinMath/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.yMinMath/self.shuntRes_Math > 0.000001 or self.yMinMath/self.shuntRes_Math < -0.000001:
                            self.exp_bar.MinLE_1.setText(f"{(self.yMinMath/self.shuntRes_Math * 1000000):.2f} µA")


                    self.exp_bar.phaseShiftLE_1.setText(f"{self.mathPhase:.1f}°")

            elif labelNum == 2:
                if CH == "CH1":
                    if self.freqCH1 < 1000:
                        self.exp_bar.freqLE_2.setText(f"{self.freqCH1:.3f} Hz")
                    else:
                        self.exp_bar.freqLE_2.setText(f"{(self.freqCH1/1000):.3f} kHz")

                    if self.periodCH1 > 0.001:
                        self.exp_bar.periodLE_2.setText(f"{(self.periodCH1 * 1000):.3f} ms")
                    elif self.periodCH1 > 0.000001:
                        self.exp_bar.periodLE_2.setText(f"{(self.periodCH1 * 1000000):.3f} us")
                    else:
                        self.exp_bar.periodLE_2.setText(f"< 1 us")

                    if not self.currentForCH1Scale:
                        if self.CH1MeanValue > 0.9 or self.CH1MeanValue < -0.9:
                            self.exp_bar.DCLE_2.setText(f"{self.CH1MeanValue:.3f} V")
                        elif self.CH1MeanValue > 0.001 or self.CH1MeanValue < -0.001:
                            self.exp_bar.DCLE_2.setText(f"{(self.CH1MeanValue * 1000):.2f} mV")
                        elif self.CH1MeanValue > 0.000001 or self.CH1MeanValue < -0.000001:
                            self.exp_bar.DCLE_2.setText(f"{(self.CH1MeanValue * 1000000):.1f} µV")

                        if self.CH1VppValue > 0.9 or self.CH1VppValue < -0.9:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{self.CH1VppValue:.2f} V")
                        elif self.CH1VppValue > 0.001 or self.CH1VppValue < -0.001:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{(self.CH1VppValue * 1000):.2f} mV")
                        elif self.CH1VppValue > 0.000001 or self.CH1VppValue < -0.000001:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{(self.CH1VppValue * 1000000):.2f} µV")

                        if self.CH1VRMSValue > 0.9 or self.CH1VRMSValue < -0.9:
                            self.exp_bar.RMSLE_2.setText(f"{self.CH1VRMSValue:.2f} V")
                        elif self.CH1VRMSValue > 0.001 or self.CH1VRMSValue < -0.001:
                            self.exp_bar.RMSLE_2.setText(f"{(self.CH1VRMSValue * 1000):.2f} mV")
                        elif self.CH1VRMSValue > 0.000001 or self.CH1VRMSValue < -0.000001:
                            self.exp_bar.RMSLE_2.setText(f"{(self.CH1VRMSValue * 1000000):.2f} µV")

                        if self.yMaxCH1 > 0.9 or self.yMaxCH1 < -0.9:
                            self.exp_bar.MaxLE_2.setText(f"{self.yMaxCH1:.2f} V")
                        elif self.yMaxCH1 > 0.001 or self.yMaxCH1 < -0.001:
                            self.exp_bar.MaxLE_2.setText(f"{(self.yMaxCH1 * 1000):.2f} mV")
                        elif self.yMaxCH1 > 0.000001 or self.yMaxCH1 < -0.000001:
                            self.exp_bar.MaxLE_2.setText(f"{(self.yMaxCH1 * 1000000):.2f} µV")

                        if self.yMinCH1 > 0.9 or self.yMinCH1 < -0.9:
                            self.exp_bar.MinLE_2.setText(f"{self.yMinCH1:.2f} V")
                        elif self.yMinCH1 > 0.001 or self.yMinCH1 < -0.001:
                            self.exp_bar.MinLE_2.setText(f"{(self.yMinCH1 * 1000):.2f} mV")
                        elif self.yMinCH1 > 0.000001 or self.yMinCH1 < -0.000001:
                            self.exp_bar.MinLE_2.setText(f"{(self.yMinCH1 * 1000000):.2f} µV")

                    else:
                        if self.CH1MeanValue/self.shuntRes_CH1 > 0.9 or self.CH1MeanValue/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.DCLE_2.setText(f"{self.CH1MeanValue/self.shuntRes_CH1:.3f} A")
                        elif self.CH1MeanValue/self.shuntRes_CH1 > 0.001 or self.CH1MeanValue/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.DCLE_2.setText(f"{(self.CH1MeanValue/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.CH1MeanValue/self.shuntRes_CH1 > 0.000001 or self.CH1MeanValue/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.DCLE_2.setText(f"{(self.CH1MeanValue/self.shuntRes_CH1 * 1000000):.1f} µA")

                        if self.CH1VppValue/self.shuntRes_CH1 > 0.9 or self.CH1VppValue/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{self.CH1VppValue/self.shuntRes_CH1:.2f} A")
                        elif self.CH1VppValue/self.shuntRes_CH1 > 0.001 or self.CH1VppValue/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{(self.CH1VppValue/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.CH1VppValue/self.shuntRes_CH1 > 0.000001 or self.CH1VppValue/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{(self.CH1VppValue/self.shuntRes_CH1 * 1000000):.2f} µA")

                        if self.CH1VRMSValue/self.shuntRes_CH1 > 0.9 or self.CH1VRMSValue/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.RMSLE_2.setText(f"{self.CH1VRMSValue/self.shuntRes_CH1:.2f} A")
                        elif self.CH1VRMSValue/self.shuntRes_CH1 > 0.001 or self.CH1VRMSValue/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.RMSLE_2.setText(f"{(self.CH1VRMSValue/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.CH1VRMSValue/self.shuntRes_CH1 > 0.000001 or self.CH1VRMSValue/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.RMSLE_2.setText(f"{(self.CH1VRMSValue/self.shuntRes_CH1 * 1000000):.2f} µA")

                        if self.yMaxCH1/self.shuntRes_CH1 > 0.9 or self.yMaxCH1/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.MaxLE_2.setText(f"{self.yMaxCH1/self.shuntRes_CH1:.2f} A")
                        elif self.yMaxCH1/self.shuntRes_CH1 > 0.001 or self.yMaxCH1/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.MaxLE_2.setText(f"{(self.yMaxCH1/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.yMaxCH1/self.shuntRes_CH1 > 0.000001 or self.yMaxCH1/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.MaxLE_2.setText(f"{(self.yMaxCH1/self.shuntRes_CH1 * 1000000):.2f} µA")

                        if self.yMinCH1/self.shuntRes_CH1 > 0.9 or self.yMinCH1/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.MinLE_2.setText(f"{self.yMinCH1/self.shuntRes_CH1:.2f} A")
                        elif self.yMinCH1/self.shuntRes_CH1 > 0.001 or self.yMinCH1/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.MinLE_2.setText(f"{(self.yMinCH1/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.yMinCH1/self.shuntRes_CH1 > 0.000001 or self.yMinCH1/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.MinLE_2.setText(f"{(self.yMinCH1/self.shuntRes_CH1 * 1000000):.2f} µA")


                    self.exp_bar.phaseShiftLE_2.setText(f"{self.CH1Phase:.1f}°")

                elif CH == "CH2":
                    if self.freqCH2 < 1000:
                        self.exp_bar.freqLE_2.setText(f"{self.freqCH2:.3f} Hz")
                    else:
                        self.exp_bar.freqLE_2.setText(f"{(self.freqCH2/1000):.3f} kHz")

                    if self.periodCH2 > 0.001:
                        self.exp_bar.periodLE_2.setText(f"{(self.periodCH2 * 1000):.3f} ms")
                    elif self.periodCH2 > 0.000001:
                        self.exp_bar.periodLE_2.setText(f"{(self.periodCH2 * 1000000):.3f} us")
                    else:
                        self.exp_bar.periodLE_2.setText(f"< 1 us")

                    if not self.currentForCH2Scale:
                        if self.CH2MeanValue > 0.9 or self.CH2MeanValue < -0.9:
                            self.exp_bar.DCLE_2.setText(f"{self.CH2MeanValue:.3f} V")
                        elif self.CH2MeanValue > 0.001 or self.CH2MeanValue < -0.001:
                            self.exp_bar.DCLE_2.setText(f"{(self.CH2MeanValue * 1000):.2f} mV")
                        elif self.CH2MeanValue > 0.000001 or self.CH2MeanValue < -0.000001:
                            self.exp_bar.DCLE_2.setText(f"{(self.CH2MeanValue * 1000000):.1f} µV")

                        if self.CH2VppValue > 0.9 or self.CH2VppValue < -0.9:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{self.CH2VppValue:.2f} V")
                        elif self.CH2VppValue > 0.001 or self.CH2VppValue < -0.001:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{(self.CH2VppValue * 1000):.2f} mV")
                        elif self.CH2VppValue > 0.000001 or self.CH2VppValue < -0.000001:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{(self.CH2VppValue * 1000000):.2f} µV")

                        if self.CH2VRMSValue > 0.9 or self.CH2VRMSValue < -0.9:
                            self.exp_bar.RMSLE_2.setText(f"{self.CH2VRMSValue:.2f} V")
                        elif self.CH2VRMSValue > 0.001 or self.CH2VRMSValue < -0.001:
                            self.exp_bar.RMSLE_2.setText(f"{(self.CH2VRMSValue * 1000):.2f} mV")
                        elif self.CH2VRMSValue > 0.000001 or self.CH2VRMSValue < -0.000001:
                            self.exp_bar.RMSLE_2.setText(f"{(self.CH2VRMSValue * 1000000):.2f} µV")

                        if self.yMaxCH2 > 0.9 or self.yMaxCH2 < -0.9:
                            self.exp_bar.MaxLE_2.setText(f"{self.yMaxCH2:.2f} V")
                        elif self.yMaxCH2 > 0.001 or self.yMaxCH2 < -0.001:
                            self.exp_bar.MaxLE_2.setText(f"{(self.yMaxCH2 * 1000):.2f} mV")
                        elif self.yMaxCH2 > 0.000001 or self.yMaxCH2 < -0.000001:
                            self.exp_bar.MaxLE_2.setText(f"{(self.yMaxCH2 * 1000000):.2f} µV")

                        if self.yMinCH2 > 0.9 or self.yMinCH2 < -0.9:
                            self.exp_bar.MinLE_2.setText(f"{self.yMinCH2:.2f} V")
                        elif self.yMinCH2 > 0.001 or self.yMinCH2 < -0.001:
                            self.exp_bar.MinLE_2.setText(f"{(self.yMinCH2 * 1000):.2f} mV")
                        elif self.yMinCH2 > 0.000001 or self.yMinCH2 < -0.000001:
                            self.exp_bar.MinLE_2.setText(f"{(self.yMinCH2 * 1000000):.2f} µV")

                    else:
                        if self.CH2MeanValue/self.shuntRes_CH2 > 0.9 or self.CH2MeanValue/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.DCLE_2.setText(f"{self.CH2MeanValue/self.shuntRes_CH2:.3f} A")
                        elif self.CH2MeanValue/self.shuntRes_CH2 > 0.001 or self.CH2MeanValue/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.DCLE_2.setText(f"{(self.CH2MeanValue/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.CH2MeanValue/self.shuntRes_CH2 > 0.000001 or self.CH2MeanValue/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.DCLE_2.setText(f"{(self.CH2MeanValue/self.shuntRes_CH2 * 1000000):.1f} µA")

                        if self.CH2VppValue/self.shuntRes_CH2 > 0.9 or self.CH2VppValue/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{self.CH2VppValue/self.shuntRes_CH2:.2f} A")
                        elif self.CH2VppValue/self.shuntRes_CH2 > 0.001 or self.CH2VppValue/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{(self.CH2VppValue/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.CH2VppValue/self.shuntRes_CH2 > 0.000001 or self.CH2VppValue/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{(self.CH2VppValue/self.shuntRes_CH2 * 1000000):.2f} µA")

                        if self.CH2VRMSValue/self.shuntRes_CH2 > 0.9 or self.CH2VRMSValue/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.RMSLE_2.setText(f"{self.CH2VRMSValue/self.shuntRes_CH2:.2f} A")
                        elif self.CH2VRMSValue/self.shuntRes_CH2 > 0.001 or self.CH2VRMSValue/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.RMSLE_2.setText(f"{(self.CH2VRMSValue/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.CH2VRMSValue/self.shuntRes_CH2 > 0.000001 or self.CH2VRMSValue/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.RMSLE_2.setText(f"{(self.CH2VRMSValue/self.shuntRes_CH2 * 1000000):.2f} µA")

                        if self.yMaxCH2/self.shuntRes_CH2 > 0.9 or self.yMaxCH2/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.MaxLE_2.setText(f"{self.yMaxCH2/self.shuntRes_CH2:.2f} A")
                        elif self.yMaxCH2/self.shuntRes_CH2 > 0.001 or self.yMaxCH2/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.MaxLE_2.setText(f"{(self.yMaxCH2/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.yMaxCH2/self.shuntRes_CH2 > 0.000001 or self.yMaxCH2/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.MaxLE_2.setText(f"{(self.yMaxCH2/self.shuntRes_CH2 * 1000000):.2f} µA")

                        if self.yMinCH2/self.shuntRes_CH2 > 0.9 or self.yMinCH2/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.MinLE_2.setText(f"{self.yMinCH2/self.shuntRes_CH2:.2f} A")
                        elif self.yMinCH2/self.shuntRes_CH2 > 0.001 or self.yMinCH2/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.MinLE_2.setText(f"{(self.yMinCH2/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.yMinCH2/self.shuntRes_CH2 > 0.000001 or self.yMinCH2/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.MinLE_2.setText(f"{(self.yMinCH2/self.shuntRes_CH2 * 1000000):.2f} µA")


                    self.exp_bar.phaseShiftLE_2.setText(f"{self.CH2Phase:.1f}°")

                elif CH == "Math":
                    if self.freqMath < 1000:
                        self.exp_bar.freqLE_2.setText(f"{self.freqMath:.3f} Hz")
                    else:
                        self.exp_bar.freqLE_2.setText(f"{(self.freqMath/1000):.3f} kHz")

                    if self.periodMath > 0.001:
                        self.exp_bar.periodLE_2.setText(f"{(self.periodMath * 1000):.3f} ms")
                    elif self.periodMath > 0.000001:
                        self.exp_bar.periodLE_2.setText(f"{(self.periodMath * 1000000):.3f} us")
                    else:
                        self.exp_bar.periodLE_2.setText(f"< 1 us")

                    if not self.currentForMathScale:
                        if self.mathMeanValue > 0.9 or self.mathMeanValue < -0.9:
                            self.exp_bar.DCLE_2.setText(f"{self.mathMeanValue:.3f} V")
                        elif self.mathMeanValue > 0.001 or self.mathMeanValue < -0.001:
                            self.exp_bar.DCLE_2.setText(f"{(self.mathMeanValue * 1000):.2f} mV")
                        elif self.mathMeanValue > 0.000001 or self.mathMeanValue < -0.000001:
                            self.exp_bar.DCLE_2.setText(f"{(self.mathMeanValue * 1000000):.1f} µV")

                        if self.mathVppValue > 0.9 or self.mathVppValue < -0.9:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{self.mathVppValue:.2f} V")
                        elif self.mathVppValue > 0.001 or self.mathVppValue < -0.001:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{(self.mathVppValue * 1000):.2f} mV")
                        elif self.mathVppValue > 0.000001 or self.mathVppValue < -0.000001:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{(self.mathVppValue * 1000000):.2f} µV")

                        if self.mathVRMSValue > 0.9 or self.mathVRMSValue < -0.9:
                            self.exp_bar.RMSLE_2.setText(f"{self.mathVRMSValue:.2f} V")
                        elif self.mathVRMSValue > 0.001 or self.mathVRMSValue < -0.001:
                            self.exp_bar.RMSLE_2.setText(f"{(self.mathVRMSValue * 1000):.2f} mV")
                        elif self.mathVRMSValue > 0.000001 or self.mathVRMSValue < -0.000001:
                            self.exp_bar.RMSLE_2.setText(f"{(self.mathVRMSValue * 1000000):.2f} µV")

                        if self.yMaxMath > 0.9 or self.yMaxMath < -0.9:
                            self.exp_bar.MaxLE_2.setText(f"{self.yMaxMath:.2f} V")
                        elif self.yMaxMath > 0.001 or self.yMaxMath < -0.001:
                            self.exp_bar.MaxLE_2.setText(f"{(self.yMaxMath * 1000):.2f} mV")
                        elif self.yMaxMath > 0.000001 or self.yMaxMath < -0.000001:
                            self.exp_bar.MaxLE_2.setText(f"{(self.yMaxMath * 1000000):.2f} µV")

                        if self.yMinMath > 0.9 or self.yMinMath < -0.9:
                            self.exp_bar.MinLE_2.setText(f"{self.yMinMath:.2f} V")
                        elif self.yMinMath > 0.001 or self.yMinMath < -0.001:
                            self.exp_bar.MinLE_2.setText(f"{(self.yMinMath * 1000):.2f} mV")
                        elif self.yMinMath > 0.000001 or self.yMinMath < -0.000001:
                            self.exp_bar.MinLE_2.setText(f"{(self.yMinMath * 1000000):.2f} µV")

                    else:
                        if self.mathMeanValue/self.shuntRes_Math > 0.9 or self.mathMeanValue/self.shuntRes_Math < -0.9:
                            self.exp_bar.DCLE_2.setText(f"{self.mathMeanValue/self.shuntRes_Math:.3f} A")
                        elif self.mathMeanValue/self.shuntRes_Math > 0.001 or self.mathMeanValue/self.shuntRes_Math < -0.001:
                            self.exp_bar.DCLE_2.setText(f"{(self.mathMeanValue/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.mathMeanValue/self.shuntRes_Math > 0.000001 or self.mathMeanValue/self.shuntRes_Math < -0.000001:
                            self.exp_bar.DCLE_2.setText(f"{(self.mathMeanValue/self.shuntRes_Math * 1000000):.1f} µA")

                        if self.mathVppValue/self.shuntRes_Math > 0.9 or self.mathVppValue/self.shuntRes_Math < -0.9:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{self.mathVppValue/self.shuntRes_Math:.2f} A")
                        elif self.mathVppValue/self.shuntRes_Math > 0.001 or self.mathVppValue/self.shuntRes_Math < -0.001:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{(self.mathVppValue/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.mathVppValue/self.shuntRes_Math > 0.000001 or self.mathVppValue/self.shuntRes_Math < -0.000001:
                            self.exp_bar.Pk_to_PkLE_2.setText(f"{(self.mathVppValue/self.shuntRes_Math * 1000000):.2f} µA")

                        if self.mathVRMSValue/self.shuntRes_Math > 0.9 or self.mathVRMSValue/self.shuntRes_Math < -0.9:
                            self.exp_bar.RMSLE_2.setText(f"{self.mathVRMSValue/self.shuntRes_Math:.2f} A")
                        elif self.mathVRMSValue/self.shuntRes_Math > 0.001 or self.mathVRMSValue/self.shuntRes_Math < -0.001:
                            self.exp_bar.RMSLE_2.setText(f"{(self.mathVRMSValue/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.mathVRMSValue/self.shuntRes_Math > 0.000001 or self.mathVRMSValue/self.shuntRes_Math < -0.000001:
                            self.exp_bar.RMSLE_2.setText(f"{(self.mathVRMSValue/self.shuntRes_Math * 1000000):.2f} µA")

                        if self.yMaxMath/self.shuntRes_Math > 0.9 or self.yMaxMath/self.shuntRes_Math < -0.9:
                            self.exp_bar.MaxLE_2.setText(f"{self.yMaxMath/self.shuntRes_Math:.2f} A")
                        elif self.yMaxMath/self.shuntRes_Math > 0.001 or self.yMaxMath/self.shuntRes_Math < -0.001:
                            self.exp_bar.MaxLE_2.setText(f"{(self.yMaxMath/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.yMaxMath/self.shuntRes_Math > 0.000001 or self.yMaxMath/self.shuntRes_Math < -0.000001:
                            self.exp_bar.MaxLE_2.setText(f"{(self.yMaxMath/self.shuntRes_Math * 1000000):.2f} µA")

                        if self.yMinMath/self.shuntRes_Math > 0.9 or self.yMinMath/self.shuntRes_Math < -0.9:
                            self.exp_bar.MinLE_2.setText(f"{self.yMinMath/self.shuntRes_Math:.2f} A")
                        elif self.yMinMath/self.shuntRes_Math > 0.001 or self.yMinMath/self.shuntRes_Math < -0.001:
                            self.exp_bar.MinLE_2.setText(f"{(self.yMinMath/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.yMinMath/self.shuntRes_Math > 0.000001 or self.yMinMath/self.shuntRes_Math < -0.000001:
                            self.exp_bar.MinLE_2.setText(f"{(self.yMinMath/self.shuntRes_Math * 1000000):.2f} µA")


                    self.exp_bar.phaseShiftLE_2.setText(f"{self.mathPhase:.1f}°")

            elif labelNum == 3:
                if CH == "CH1":
                    if self.freqCH1 < 1000:
                        self.exp_bar.freqLE_3.setText(f"{self.freqCH1:.3f} Hz")
                    else:
                        self.exp_bar.freqLE_3.setText(f"{(self.freqCH1/1000):.3f} kHz")

                    if self.periodCH1 > 0.001:
                        self.exp_bar.periodLE_3.setText(f"{(self.periodCH1 * 1000):.3f} ms")
                    elif self.periodCH1 > 0.000001:
                        self.exp_bar.periodLE_3.setText(f"{(self.periodCH1 * 1000000):.3f} us")
                    else:
                        self.exp_bar.periodLE_3.setText(f"< 1 us")

                    if not self.currentForCH1Scale:
                        if self.CH1MeanValue > 0.9 or self.CH1MeanValue < -0.9:
                            self.exp_bar.DCLE_3.setText(f"{self.CH1MeanValue:.3f} V")
                        elif self.CH1MeanValue > 0.001 or self.CH1MeanValue < -0.001:
                            self.exp_bar.DCLE_3.setText(f"{(self.CH1MeanValue * 1000):.2f} mV")
                        elif self.CH1MeanValue > 0.000001 or self.CH1MeanValue < -0.000001:
                            self.exp_bar.DCLE_3.setText(f"{(self.CH1MeanValue * 1000000):.1f} µV")

                        if self.CH1VppValue > 0.9 or self.CH1VppValue < -0.9:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{self.CH1VppValue:.2f} V")
                        elif self.CH1VppValue > 0.001 or self.CH1VppValue < -0.001:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{(self.CH1VppValue * 1000):.2f} mV")
                        elif self.CH1VppValue > 0.000001 or self.CH1VppValue < -0.000001:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{(self.CH1VppValue * 1000000):.2f} µV")

                        if self.CH1VRMSValue > 0.9 or self.CH1VRMSValue < -0.9:
                            self.exp_bar.RMSLE_3.setText(f"{self.CH1VRMSValue:.2f} V")
                        elif self.CH1VRMSValue > 0.001 or self.CH1VRMSValue < -0.001:
                            self.exp_bar.RMSLE_3.setText(f"{(self.CH1VRMSValue * 1000):.2f} mV")
                        elif self.CH1VRMSValue > 0.000001 or self.CH1VRMSValue < -0.000001:
                            self.exp_bar.RMSLE_3.setText(f"{(self.CH1VRMSValue * 1000000):.2f} µV")

                        if self.yMaxCH1 > 0.9 or self.yMaxCH1 < -0.9:
                            self.exp_bar.MaxLE_3.setText(f"{self.yMaxCH1:.2f} V")
                        elif self.yMaxCH1 > 0.001 or self.yMaxCH1 < -0.001:
                            self.exp_bar.MaxLE_3.setText(f"{(self.yMaxCH1 * 1000):.2f} mV")
                        elif self.yMaxCH1 > 0.000001 or self.yMaxCH1 < -0.000001:
                            self.exp_bar.MaxLE_3.setText(f"{(self.yMaxCH1 * 1000000):.2f} µV")

                        if self.yMinCH1 > 0.9 or self.yMinCH1 < -0.9:
                            self.exp_bar.MinLE_3.setText(f"{self.yMinCH1:.2f} V")
                        elif self.yMinCH1 > 0.001 or self.yMinCH1 < -0.001:
                            self.exp_bar.MinLE_3.setText(f"{(self.yMinCH1 * 1000):.2f} mV")
                        elif self.yMinCH1 > 0.000001 or self.yMinCH1 < -0.000001:
                            self.exp_bar.MinLE_3.setText(f"{(self.yMinCH1 * 1000000):.2f} µV")

                    else:
                        if self.CH1MeanValue/self.shuntRes_CH1 > 0.9 or self.CH1MeanValue/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.DCLE_3.setText(f"{self.CH1MeanValue/self.shuntRes_CH1:.3f} A")
                        elif self.CH1MeanValue/self.shuntRes_CH1 > 0.001 or self.CH1MeanValue/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.DCLE_3.setText(f"{(self.CH1MeanValue/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.CH1MeanValue/self.shuntRes_CH1 > 0.000001 or self.CH1MeanValue/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.DCLE_3.setText(f"{(self.CH1MeanValue/self.shuntRes_CH1 * 1000000):.1f} µA")

                        if self.CH1VppValue/self.shuntRes_CH1 > 0.9 or self.CH1VppValue/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{self.CH1VppValue/self.shuntRes_CH1:.2f} A")
                        elif self.CH1VppValue/self.shuntRes_CH1 > 0.001 or self.CH1VppValue/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{(self.CH1VppValue/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.CH1VppValue/self.shuntRes_CH1 > 0.000001 or self.CH1VppValue/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{(self.CH1VppValue/self.shuntRes_CH1 * 1000000):.2f} µA")

                        if self.CH1VRMSValue/self.shuntRes_CH1 > 0.9 or self.CH1VRMSValue/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.RMSLE_3.setText(f"{self.CH1VRMSValue/self.shuntRes_CH1:.2f} A")
                        elif self.CH1VRMSValue/self.shuntRes_CH1 > 0.001 or self.CH1VRMSValue/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.RMSLE_3.setText(f"{(self.CH1VRMSValue/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.CH1VRMSValue/self.shuntRes_CH1 > 0.000001 or self.CH1VRMSValue/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.RMSLE_3.setText(f"{(self.CH1VRMSValue/self.shuntRes_CH1 * 1000000):.2f} µA")

                        if self.yMaxCH1/self.shuntRes_CH1 > 0.9 or self.yMaxCH1/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.MaxLE_3.setText(f"{self.yMaxCH1/self.shuntRes_CH1:.2f} A")
                        elif self.yMaxCH1/self.shuntRes_CH1 > 0.001 or self.yMaxCH1/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.MaxLE_3.setText(f"{(self.yMaxCH1/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.yMaxCH1/self.shuntRes_CH1 > 0.000001 or self.yMaxCH1/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.MaxLE_3.setText(f"{(self.yMaxCH1/self.shuntRes_CH1 * 1000000):.2f} µA")

                        if self.yMinCH1/self.shuntRes_CH1 > 0.9 or self.yMinCH1/self.shuntRes_CH1 < -0.9:
                            self.exp_bar.MinLE_3.setText(f"{self.yMinCH1/self.shuntRes_CH1:.2f} A")
                        elif self.yMinCH1/self.shuntRes_CH1 > 0.001 or self.yMinCH1/self.shuntRes_CH1 < -0.001:
                            self.exp_bar.MinLE_3.setText(f"{(self.yMinCH1/self.shuntRes_CH1 * 1000):.2f} mA")
                        elif self.yMinCH1/self.shuntRes_CH1 > 0.000001 or self.yMinCH1/self.shuntRes_CH1 < -0.000001:
                            self.exp_bar.MinLE_3.setText(f"{(self.yMinCH1/self.shuntRes_CH1 * 1000000):.2f} µA")


                    self.exp_bar.phaseShiftLE_3.setText(f"{self.CH1Phase:.1f}°")

                elif CH == "CH2":
                    if self.freqCH2 < 1000:
                        self.exp_bar.freqLE_3.setText(f"{self.freqCH2:.3f} Hz")
                    else:
                        self.exp_bar.freqLE_3.setText(f"{(self.freqCH2/1000):.3f} kHz")

                    if self.periodCH2 > 0.001:
                        self.exp_bar.periodLE_3.setText(f"{(self.periodCH2 * 1000):.3f} ms")
                    elif self.periodCH2 > 0.000001:
                        self.exp_bar.periodLE_3.setText(f"{(self.periodCH2 * 1000000):.3f} us")
                    else:
                        self.exp_bar.periodLE_3.setText(f"< 1 us")

                    if not self.currentForCH2Scale:
                        if self.CH2MeanValue > 0.9 or self.CH2MeanValue < -0.9:
                            self.exp_bar.DCLE_3.setText(f"{self.CH2MeanValue:.3f} V")
                        elif self.CH2MeanValue > 0.001 or self.CH2MeanValue < -0.001:
                            self.exp_bar.DCLE_3.setText(f"{(self.CH2MeanValue * 1000):.2f} mV")
                        elif self.CH2MeanValue > 0.000001 or self.CH2MeanValue < -0.000001:
                            self.exp_bar.DCLE_3.setText(f"{(self.CH2MeanValue * 1000000):.1f} µV")

                        if self.CH2VppValue > 0.9 or self.CH2VppValue < -0.9:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{self.CH2VppValue:.2f} V")
                        elif self.CH2VppValue > 0.001 or self.CH2VppValue < -0.001:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{(self.CH2VppValue * 1000):.2f} mV")
                        elif self.CH2VppValue > 0.000001 or self.CH2VppValue < -0.000001:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{(self.CH2VppValue * 1000000):.2f} µV")

                        if self.CH2VRMSValue > 0.9 or self.CH2VRMSValue < -0.9:
                            self.exp_bar.RMSLE_3.setText(f"{self.CH2VRMSValue:.2f} V")
                        elif self.CH2VRMSValue > 0.001 or self.CH2VRMSValue < -0.001:
                            self.exp_bar.RMSLE_3.setText(f"{(self.CH2VRMSValue * 1000):.2f} mV")
                        elif self.CH2VRMSValue > 0.000001 or self.CH2VRMSValue < -0.000001:
                            self.exp_bar.RMSLE_3.setText(f"{(self.CH2VRMSValue * 1000000):.2f} µV")

                        if self.yMaxCH2 > 0.9 or self.yMaxCH2 < -0.9:
                            self.exp_bar.MaxLE_3.setText(f"{self.yMaxCH2:.2f} V")
                        elif self.yMaxCH2 > 0.001 or self.yMaxCH2 < -0.001:
                            self.exp_bar.MaxLE_3.setText(f"{(self.yMaxCH2 * 1000):.2f} mV")
                        elif self.yMaxCH2 > 0.000001 or self.yMaxCH2 < -0.000001:
                            self.exp_bar.MaxLE_3.setText(f"{(self.yMaxCH2 * 1000000):.2f} µV")

                        if self.yMinCH2 > 0.9 or self.yMinCH2 < -0.9:
                            self.exp_bar.MinLE_3.setText(f"{self.yMinCH2:.2f} V")
                        elif self.yMinCH2 > 0.001 or self.yMinCH2 < -0.001:
                            self.exp_bar.MinLE_3.setText(f"{(self.yMinCH2 * 1000):.2f} mV")
                        elif self.yMinCH2 > 0.000001 or self.yMinCH2 < -0.000001:
                            self.exp_bar.MinLE_3.setText(f"{(self.yMinCH2 * 1000000):.2f} µV")

                    else:
                        if self.CH2MeanValue/self.shuntRes_CH2 > 0.9 or self.CH2MeanValue/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.DCLE_3.setText(f"{self.CH2MeanValue/self.shuntRes_CH2:.3f} A")
                        elif self.CH2MeanValue/self.shuntRes_CH2 > 0.001 or self.CH2MeanValue/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.DCLE_3.setText(f"{(self.CH2MeanValue/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.CH2MeanValue/self.shuntRes_CH2 > 0.000001 or self.CH2MeanValue/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.DCLE_3.setText(f"{(self.CH2MeanValue/self.shuntRes_CH2 * 1000000):.1f} µA")

                        if self.CH2VppValue/self.shuntRes_CH2 > 0.9 or self.CH2VppValue/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{self.CH2VppValue/self.shuntRes_CH2:.2f} A")
                        elif self.CH2VppValue/self.shuntRes_CH2 > 0.001 or self.CH2VppValue/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{(self.CH2VppValue/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.CH2VppValue/self.shuntRes_CH2 > 0.000001 or self.CH2VppValue/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{(self.CH2VppValue/self.shuntRes_CH2 * 1000000):.2f} µA")

                        if self.CH2VRMSValue/self.shuntRes_CH2 > 0.9 or self.CH2VRMSValue/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.RMSLE_3.setText(f"{self.CH2VRMSValue/self.shuntRes_CH2:.2f} A")
                        elif self.CH2VRMSValue/self.shuntRes_CH2 > 0.001 or self.CH2VRMSValue/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.RMSLE_3.setText(f"{(self.CH2VRMSValue/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.CH2VRMSValue/self.shuntRes_CH2 > 0.000001 or self.CH2VRMSValue/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.RMSLE_3.setText(f"{(self.CH2VRMSValue/self.shuntRes_CH2 * 1000000):.2f} µA")

                        if self.yMaxCH2/self.shuntRes_CH2 > 0.9 or self.yMaxCH2/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.MaxLE_3.setText(f"{self.yMaxCH2/self.shuntRes_CH2:.2f} A")
                        elif self.yMaxCH2/self.shuntRes_CH2 > 0.001 or self.yMaxCH2/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.MaxLE_3.setText(f"{(self.yMaxCH2/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.yMaxCH2/self.shuntRes_CH2 > 0.000001 or self.yMaxCH2/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.MaxLE_3.setText(f"{(self.yMaxCH2/self.shuntRes_CH2 * 1000000):.2f} µA")

                        if self.yMinCH2/self.shuntRes_CH2 > 0.9 or self.yMinCH2/self.shuntRes_CH2 < -0.9:
                            self.exp_bar.MinLE_3.setText(f"{self.yMinCH2/self.shuntRes_CH2:.2f} A")
                        elif self.yMinCH2/self.shuntRes_CH2 > 0.001 or self.yMinCH2/self.shuntRes_CH2 < -0.001:
                            self.exp_bar.MinLE_3.setText(f"{(self.yMinCH2/self.shuntRes_CH2 * 1000):.2f} mA")
                        elif self.yMinCH2/self.shuntRes_CH2 > 0.000001 or self.yMinCH2/self.shuntRes_CH2 < -0.000001:
                            self.exp_bar.MinLE_3.setText(f"{(self.yMinCH2/self.shuntRes_CH2 * 1000000):.2f} µA")


                    self.exp_bar.phaseShiftLE_3.setText(f"{self.CH2Phase:.1f}°")

                elif CH == "Math":
                    if self.freqMath < 1000:
                        self.exp_bar.freqLE_3.setText(f"{self.freqMath:.3f} Hz")
                    else:
                        self.exp_bar.freqLE_3.setText(f"{(self.freqMath/1000):.3f} kHz")

                    if self.periodMath > 0.001:
                        self.exp_bar.periodLE_3.setText(f"{(self.periodMath * 1000):.3f} ms")
                    elif self.periodMath > 0.000001:
                        self.exp_bar.periodLE_3.setText(f"{(self.periodMath * 1000000):.3f} us")
                    else:
                        self.exp_bar.periodLE_3.setText(f"< 1 us")

                    if not self.currentForMathScale:
                        if self.mathMeanValue > 0.9 or self.mathMeanValue < -0.9:
                            self.exp_bar.DCLE_3.setText(f"{self.mathMeanValue:.3f} V")
                        elif self.mathMeanValue > 0.001 or self.mathMeanValue < -0.001:
                            self.exp_bar.DCLE_3.setText(f"{(self.mathMeanValue * 1000):.2f} mV")
                        elif self.mathMeanValue > 0.000001 or self.mathMeanValue < -0.000001:
                            self.exp_bar.DCLE_3.setText(f"{(self.mathMeanValue * 1000000):.1f} µV")

                        if self.mathVppValue > 0.9 or self.mathVppValue < -0.9:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{self.mathVppValue:.2f} V")
                        elif self.mathVppValue > 0.001 or self.mathVppValue < -0.001:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{(self.mathVppValue * 1000):.2f} mV")
                        elif self.mathVppValue > 0.000001 or self.mathVppValue < -0.000001:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{(self.mathVppValue * 1000000):.2f} µV")

                        if self.mathVRMSValue > 0.9 or self.mathVRMSValue < -0.9:
                            self.exp_bar.RMSLE_3.setText(f"{self.mathVRMSValue:.2f} V")
                        elif self.mathVRMSValue > 0.001 or self.mathVRMSValue < -0.001:
                            self.exp_bar.RMSLE_3.setText(f"{(self.mathVRMSValue * 1000):.2f} mV")
                        elif self.mathVRMSValue > 0.000001 or self.mathVRMSValue < -0.000001:
                            self.exp_bar.RMSLE_3.setText(f"{(self.mathVRMSValue * 1000000):.2f} µV")

                        if self.yMaxMath > 0.9 or self.yMaxMath < -0.9:
                            self.exp_bar.MaxLE_3.setText(f"{self.yMaxMath:.2f} V")
                        elif self.yMaxMath > 0.001 or self.yMaxMath < -0.001:
                            self.exp_bar.MaxLE_3.setText(f"{(self.yMaxMath * 1000):.2f} mV")
                        elif self.yMaxMath > 0.000001 or self.yMaxMath < -0.000001:
                            self.exp_bar.MaxLE_3.setText(f"{(self.yMaxMath * 1000000):.2f} µV")

                        if self.yMinMath > 0.9 or self.yMinMath < -0.9:
                            self.exp_bar.MinLE_3.setText(f"{self.yMinMath:.2f} V")
                        elif self.yMinMath > 0.001 or self.yMinMath < -0.001:
                            self.exp_bar.MinLE_3.setText(f"{(self.yMinMath * 1000):.2f} mV")
                        elif self.yMinMath > 0.000001 or self.yMinMath < -0.000001:
                            self.exp_bar.MinLE_3.setText(f"{(self.yMinMath * 1000000):.2f} µV")

                    else:
                        if self.mathMeanValue/self.shuntRes_Math > 0.9 or self.mathMeanValue/self.shuntRes_Math < -0.9:
                            self.exp_bar.DCLE_3.setText(f"{self.mathMeanValue/self.shuntRes_Math:.3f} A")
                        elif self.mathMeanValue/self.shuntRes_Math > 0.001 or self.mathMeanValue/self.shuntRes_Math < -0.001:
                            self.exp_bar.DCLE_3.setText(f"{(self.mathMeanValue/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.mathMeanValue/self.shuntRes_Math > 0.000001 or self.mathMeanValue/self.shuntRes_Math < -0.000001:
                            self.exp_bar.DCLE_3.setText(f"{(self.mathMeanValue/self.shuntRes_Math * 1000000):.1f} µA")

                        if self.mathVppValue/self.shuntRes_Math > 0.9 or self.mathVppValue/self.shuntRes_Math < -0.9:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{self.mathVppValue/self.shuntRes_Math:.2f} A")
                        elif self.mathVppValue/self.shuntRes_Math > 0.001 or self.mathVppValue/self.shuntRes_Math < -0.001:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{(self.mathVppValue/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.mathVppValue/self.shuntRes_Math > 0.000001 or self.mathVppValue/self.shuntRes_Math < -0.000001:
                            self.exp_bar.Pk_to_PkLE_3.setText(f"{(self.mathVppValue/self.shuntRes_Math * 1000000):.2f} µA")

                        if self.mathVRMSValue/self.shuntRes_Math > 0.9 or self.mathVRMSValue/self.shuntRes_Math < -0.9:
                            self.exp_bar.RMSLE_3.setText(f"{self.mathVRMSValue/self.shuntRes_Math:.2f} A")
                        elif self.mathVRMSValue/self.shuntRes_Math > 0.001 or self.mathVRMSValue/self.shuntRes_Math < -0.001:
                            self.exp_bar.RMSLE_3.setText(f"{(self.mathVRMSValue/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.mathVRMSValue/self.shuntRes_Math > 0.000001 or self.mathVRMSValue/self.shuntRes_Math < -0.000001:
                            self.exp_bar.RMSLE_3.setText(f"{(self.mathVRMSValue/self.shuntRes_Math * 1000000):.2f} µA")

                        if self.yMaxMath/self.shuntRes_Math > 0.9 or self.yMaxMath/self.shuntRes_Math < -0.9:
                            self.exp_bar.MaxLE_3.setText(f"{self.yMaxMath/self.shuntRes_Math:.2f} A")
                        elif self.yMaxMath/self.shuntRes_Math > 0.001 or self.yMaxMath/self.shuntRes_Math < -0.001:
                            self.exp_bar.MaxLE_3.setText(f"{(self.yMaxMath/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.yMaxMath/self.shuntRes_Math > 0.000001 or self.yMaxMath/self.shuntRes_Math < -0.000001:
                            self.exp_bar.MaxLE_3.setText(f"{(self.yMaxMath/self.shuntRes_Math * 1000000):.2f} µA")

                        if self.yMinMath/self.shuntRes_Math > 0.9 or self.yMinMath/self.shuntRes_Math < -0.9:
                            self.exp_bar.MinLE_3.setText(f"{self.yMinMath/self.shuntRes_Math:.2f} A")
                        elif self.yMinMath/self.shuntRes_Math > 0.001 or self.yMinMath/self.shuntRes_Math < -0.001:
                            self.exp_bar.MinLE_3.setText(f"{(self.yMinMath/self.shuntRes_Math * 1000):.2f} mA")
                        elif self.yMinMath/self.shuntRes_Math > 0.000001 or self.yMinMath/self.shuntRes_Math < -0.000001:
                            self.exp_bar.MinLE_3.setText(f"{(self.yMinMath/self.shuntRes_Math * 1000000):.2f} µA")


                    self.exp_bar.phaseShiftLE_3.setText(f"{self.mathPhase:.1f}°")

        #A forma como exp_bar é gerada depende da combinação de canais ligados
        if self.btCH1.isOn and self.btCH2.isOn and self.btMath.isOn:
            self.exp_bar.hideLabel1.hide()
            self.exp_bar.hideLabel2.hide()
            self.exp_bar.hideLabel3.hide()

            self.exp_bar.mainLabel1.setText("CH1")
            self.exp_bar.mainLabel1.setStyleSheet(""" color: rgb(0, 70, 134) """)
            fill_lineEdits(1, "CH1")

            self.exp_bar.mainLabel2.setText("CH2")
            self.exp_bar.mainLabel2.setStyleSheet(""" color: red """)
            fill_lineEdits(2, "CH2")

            self.exp_bar.mainLabel3.setText("Math")
            self.exp_bar.mainLabel3.setStyleSheet(""" color: rgb(2, 135, 255) """)
            fill_lineEdits(3, "Math")


        elif not self.btCH1.isOn and self.btCH2.isOn and self.btMath.isOn: #CH2 e Math
            self.exp_bar.hideLabel1.hide()
            self.exp_bar.hideLabel2.show()
            self.exp_bar.hideLabel3.hide()

            self.exp_bar.mainLabel1.setText("CH2")
            self.exp_bar.mainLabel1.setStyleSheet(""" color: red """)
            fill_lineEdits(1, "CH2")

            # self.exp_bar.mainLabel2.setText("CH2")
            # self.exp_bar.mainLabel2.setStyleSheet(""" color: red """)

            self.exp_bar.mainLabel3.setText("Math")
            self.exp_bar.mainLabel3.setStyleSheet(""" color: rgb(2, 135, 255) """)
            fill_lineEdits(3, "Math")

        elif self.btCH1.isOn and not self.btCH2.isOn and self.btMath.isOn: #CH1 e Math
            self.exp_bar.hideLabel1.hide()
            self.exp_bar.hideLabel2.show()
            self.exp_bar.hideLabel3.hide()

            self.exp_bar.mainLabel1.setText("CH1")
            self.exp_bar.mainLabel1.setStyleSheet(""" color: rgb(0, 70, 134) """)
            fill_lineEdits(1, "CH1")

            # self.exp_bar.mainLabel2.setText("CH2")
            # self.exp_bar.mainLabel2.setStyleSheet(""" color: red """)

            self.exp_bar.mainLabel3.setText("Math")
            self.exp_bar.mainLabel3.setStyleSheet(""" color: rgb(2, 135, 255) """)
            fill_lineEdits(3, "Math")

        elif self.btCH1.isOn and self.btCH2.isOn and not self.btMath.isOn: #CH1 e CH2
            self.exp_bar.hideLabel1.hide()
            self.exp_bar.hideLabel2.show()
            self.exp_bar.hideLabel3.hide()

            self.exp_bar.mainLabel1.setText("CH1")
            self.exp_bar.mainLabel1.setStyleSheet(""" color: rgb(0, 70, 134) """)
            fill_lineEdits(1, "CH1")

            # self.exp_bar.mainLabel2.setText("CH2")
            # self.exp_bar.mainLabel2.setStyleSheet(""" color: red """)

            self.exp_bar.mainLabel3.setText("CH2")
            self.exp_bar.mainLabel3.setStyleSheet(""" color: red """)
            fill_lineEdits(3, "CH2")

        elif self.btCH1.isOn and not self.btCH2.isOn and not self.btMath.isOn: #CH1
            self.exp_bar.hideLabel1.show()
            self.exp_bar.hideLabel2.hide()
            self.exp_bar.hideLabel3.show()

            #self.exp_bar.mainLabel1.setText("CH1")
            #self.exp_bar.mainLabel1.setStyleSheet(""" color: rgb(0, 70, 134) """)

            self.exp_bar.mainLabel2.setText("CH1")
            self.exp_bar.mainLabel2.setStyleSheet(""" color: rgb(0, 70, 134) """)
            fill_lineEdits(2, "CH1")

            #self.exp_bar.mainLabel3.setText("CH2")
            #self.exp_bar.mainLabel3.setStyleSheet(""" color: red """)

        elif not self.btCH1.isOn and self.btCH2.isOn and not self.btMath.isOn: #CH2
            self.exp_bar.hideLabel1.show()
            self.exp_bar.hideLabel2.hide()
            self.exp_bar.hideLabel3.show()

            #self.exp_bar.mainLabel1.setText("CH1")
            #self.exp_bar.mainLabel1.setStyleSheet(""" color: rgb(0, 70, 134) """)

            self.exp_bar.mainLabel2.setText("CH2")
            self.exp_bar.mainLabel2.setStyleSheet(""" color: red """)
            fill_lineEdits(2, "CH2")

            #self.exp_bar.mainLabel3.setText("CH2")
            #self.exp_bar.mainLabel3.setStyleSheet(""" color: red """)

        elif not self.btCH1.isOn and not self.btCH2.isOn and self.btMath.isOn: #Math
            self.exp_bar.hideLabel1.show()
            self.exp_bar.hideLabel2.hide()
            self.exp_bar.hideLabel3.show()

            #self.exp_bar.mainLabel1.setText("CH1")
            #self.exp_bar.mainLabel1.setStyleSheet(""" color: rgb(0, 70, 134) """)

            self.exp_bar.mainLabel2.setText("Math")
            self.exp_bar.mainLabel2.setStyleSheet(""" color: rgb(2, 135, 255) """)
            fill_lineEdits(2, "Math")

            #self.exp_bar.mainLabel3.setText("CH2")
            #self.exp_bar.mainLabel3.setStyleSheet(""" color: red """)

        else:
            self.exp_bar.hideLabel1.show()
            self.exp_bar.hideLabel2.show()
            self.exp_bar.hideLabel3.show()

        datetimeText = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.language == "English":
            if not self.screenName == "Freq Resp": 
                self.exp_bar.supportLabel1.setText(f"Reference Channel: {self.mainScr.referencePhase}")
                self.exp_bar.supportLabel1.setGeometry(150, 175, 845, 25)
            else:
                self.exp_bar.supportLabel1.setGeometry(50, 175, 845, 25)
                self.exp_bar.supportLabel1.setText(f"Reference Channel: {self.mainScr.referencePhase}" +
                                                f" - Function Type: {self.freqResp_scr2.freqResp_page2.functionTypeCB.currentText()}")
            self.exp_bar.supportLabel2.setText("Captured at: " + f"{datetimeText}")
        else: 
            if not self.screenName == "Freq Resp": 
                self.exp_bar.supportLabel1.setText(f"Canal de Referência: {self.mainScr.referencePhase}")
                self.exp_bar.supportLabel1.setGeometry(150, 175, 845, 25)
            else:
                self.exp_bar.supportLabel1.setGeometry(50, 175, 845, 25)
                self.exp_bar.supportLabel1.setText(f"Canal de Referência: {self.mainScr.referencePhase}" +
                                                f" - Tipo de Função: {self.freqResp_scr2.freqResp_page2.functionTypeCB.currentText()}")
            self.exp_bar.supportLabel2.setText("Capturado em: " + f"{datetimeText}")

        pixmap_bar = QPixmap(self.exp_bar.size())
        self.exp_bar.render(pixmap_bar)

        # Base
        sheet = QPixmap("images/baseExportImage_NEW.png")
        sheet_w = sheet.width()
        sheet_h = sheet.height()

        scaled_bar = pixmap_bar.scaledToWidth(
            int(sheet_w * 0.6),
            Qt.SmoothTransformation
        )

        # Centralizar horizontalmente
        x = (sheet_w - scaled_bar.width()) // 2

        # Ancorar no rodapé
        y = (sheet_h - scaled_bar.height() - int(sheet_h * 0.05)) + 100


        painter = QPainter(sheet)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(x, y, scaled_bar)
        painter.end()

        sheet.save("images/image_with_bar.png", "PNG")

        #Indo para as telas principais:
        
        #Preparando a tela principal para captura:
        self.mainScr.setBackground("white")
        self.FFTScr.setBackground("white")
        self.freqRespScr.magnitude.setBackground("white")
        self.freqRespScr.phase.setBackground("white")
        self.phasDiag_and_lissajScr.phasDiag.setBackground("white")
        self.phasDiag_and_lissajScr.lissaj.setBackground("white")
        if self.language == "Português":
            self.FFTScr.getPlotItem().setLabel(axis='bottom', text='Frequência (Hz)', color='black', **{'font-size':'8pt'})
            self.freqRespScr.magnitude.getPlotItem().setLabel(axis='bottom', text='Frequência (Hz)', color='black', **{'font-size':'8pt'})
            self.freqRespScr.phase.getPlotItem().setLabel(axis='bottom', text='Frequência (Hz)', color='black', **{'font-size':'8pt'})
            self.freqRespScr.phase.getPlotItem().setLabel(axis='left', text='Fase (graus)', color='black', **{'font-size':'8pt'})
        else:
            self.FFTScr.getPlotItem().setLabel(axis='bottom', text='Frequency (Hz)', color='black', **{'font-size':'8pt'})
            self.freqRespScr.magnitude.getPlotItem().setLabel(axis='bottom', text='Frequency (Hz)', color='black', **{'font-size':'8pt'})
            self.freqRespScr.phase.getPlotItem().setLabel(axis='bottom', text='Frequency (Hz)', color='black', **{'font-size':'8pt'})
            self.freqRespScr.phase.getPlotItem().setLabel(axis='left', text='Phase (degrees)', color='black', **{'font-size':'8pt'})
        self.FFTScr.getPlotItem().setLabel(axis='left', text='Amplitude (dB)', color='black', **{'font-size':'8pt'})
        self.freqRespScr.magnitude.getPlotItem().setLabel(axis='left', text='Magnitude (dB)', color='black', **{'font-size':'8pt'})

        if self.phasDiag_and_lissaj_scr2.page2.channelxAxisSelectCB.currentText() == "CH1":
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='CH1 (V)', color='black', **{'font-size':'8pt'})
        elif self.phasDiag_and_lissaj_scr2.page2.channelxAxisSelectCB.currentText() == "CH2":
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='CH2 (V)', color='black', **{'font-size':'8pt'})
        elif self.phasDiag_and_lissaj_scr2.page2.channelxAxisSelectCB.currentText() == "Math":
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='Math (V)', color='black', **{'font-size':'8pt'})

        
        if self.phasDiag_and_lissaj_scr2.page2.channelyAxisSelectCB.currentText() == "CH1":
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='CH1 (V)', color='black', **{'font-size':'8pt'})
        elif self.phasDiag_and_lissaj_scr2.page2.channelyAxisSelectCB.currentText() == "CH2":
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='CH2 (V)', color='black', **{'font-size':'8pt'})
        elif self.phasDiag_and_lissaj_scr2.page2.channelyAxisSelectCB.currentText() == "Math":
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='Math (V)', color='black', **{'font-size':'8pt'})
        
        self.backgroundLabel5.hide()
        self.whiteExportLabel.show()
        self.screen1.raise_()
        self.CH1Label.raise_()
        self.CH2Label.raise_()
        self.mathvDivLabel.raise_()
        self.timeLabel.setStyleSheet(""" color: "black"; 
                                            background-color: transparent""")
        self.timeLabel.raise_()
        self.blackLabel1.setStyleSheet("background-color: white")
        self.blackLabel2.setStyleSheet("background-color: white")
        self.blackLabel1.raise_()
        self.blackLabel2.raise_()
        self.posCH1Label.raise_()
        self.posCH2Label.raise_()
        self.mathPosLabel.raise_()
        if self.btTrigger.isOn: self.btTrigger.clicked.emit()
        if self.btCursor.isOn: self.btCursor.clicked.emit()
        if self.btMeas.isOn: self.btMeas.clicked.emit()

        if self.screenName == "Main" or self.screenName == "FFT":
            rect = QRect(int((self.p/0.8) * 5),  int((self.p/0.8) * 240), int((self.p/0.8) * 800), int((self.p/0.8) * 465))
            screenCapture = self.grab(rect)

            #constante para ajustar a ferramenta à opção do Windows: Change the size of text, apps, and other items:
            self.q = rect.width()/(screenCapture.width())

            #ajuste de screenCapture para se adequar aos valores de rect (nem sempre são equivalentes)
            screenCapture = screenCapture.scaled(
                int(screenCapture.width() * self.q/min(1, (self.p/0.8))),
                int(screenCapture.height() * self.q/min(1, (self.p/0.8))),  
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            #Caso os ajustes acima não sejam suficientes para padronizar o resultado para diferentes resoluções de tela:
            if not (abs(screenCapture.width() - 800)) <= 5:
                k = 800/screenCapture.width()
                screenCapture = screenCapture.scaled(
                int(screenCapture.width() * k),
                int(screenCapture.height() * k),  
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            #Amplificando as dimensões da captura - ajuste final
            target_width = int(screenCapture.width() * 3.4)
            target_height = int(screenCapture.height() * 3.4)


            screenCapture = screenCapture.scaled(
                target_width,
                target_height,  
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            
            baseArc = QPixmap("images/image_with_bar.png")

            capturePainter = QPainter(baseArc)

            # posição onde a imagem será inserida no PNG final
            dest_rect = QRect((sheet_w - screenCapture.width()) // 2, 380, screenCapture.width(), screenCapture.height())

            capturePainter.drawPixmap(dest_rect, screenCapture)
            capturePainter.end()

        elif self.screenName == "Freq Resp":
            self.freqResp_scr2.freqResp_page2.y_AxisCB.setCurrentIndex(0)
            rect = QRect(int((self.p/0.8) * 5),  int((self.p/0.8) * 240), int((self.p/0.8) * 800), int((self.p/0.8) * 465))
            screenCapture = self.grab(rect)

            #constante para ajustar a ferramenta à opção do Windows: Change the size of text, apps, and other items:
            self.q = rect.width()/(screenCapture.width())

            #ajuste de screenCapture para se adequar aos valores de rect (nem sempre são equivalentes)
            screenCapture = screenCapture.scaled(
                int(screenCapture.width() * self.q/min(1, (self.p/0.8))),
                int(screenCapture.height() * self.q/min(1, (self.p/0.8))),  
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            #Caso os ajustes acima não sejam suficientes para padronizar o resultado para diferentes resoluções de tela:
            if not (abs(screenCapture.width() - 800)) <= 5:
                k = 800/screenCapture.width()
                screenCapture = screenCapture.scaled(
                int(screenCapture.width() * k),
                int(screenCapture.height() * k),  
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            #Amplificando as dimensões da captura - ajuste final
            target_width = int(screenCapture.width() * 2.2)
            target_height = int(screenCapture.height() * 2.2)


            screenCapture = screenCapture.scaled(
                target_width,
                target_height,  
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            
            baseArc = QPixmap("images/image_with_bar.png")

            capturePainter = QPainter(baseArc)

            # posição onde a imagem será inserida no PNG final
            dest_rect = QRect(10, 700, screenCapture.width(), screenCapture.height())

            capturePainter.drawPixmap(dest_rect, screenCapture)
            capturePainter.end()

            baseArc.save(f"images/export_with_magnitude.png", "PNG")
            #Captura do gráfico de fase:
            self.freqResp_scr2.freqResp_page2.y_AxisCB.setCurrentIndex(1)

            rect = QRect(int((self.p/0.8) * 5),  int((self.p/0.8) * 240), int((self.p/0.8) * 800), int((self.p/0.8) * 465))
            screenCapture = self.grab(rect)

            #constante para ajustar a ferramenta à opção do Windows: Change the size of text, apps, and other items:
            self.q = rect.width()/(screenCapture.width())

            #ajuste de screenCapture para se adequar aos valores de rect (nem sempre são equivalentes)
            screenCapture = screenCapture.scaled(
                int(screenCapture.width() * self.q/min(1, (self.p/0.8))),
                int(screenCapture.height() * self.q/min(1, (self.p/0.8))),  
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            #Caso os ajustes acima não sejam suficientes para padronizar o resultado para diferentes resoluções de tela:
            if not (abs(screenCapture.width() - 800)) <= 5:
                k = 800/screenCapture.width()
                screenCapture = screenCapture.scaled(
                int(screenCapture.width() * k),
                int(screenCapture.height() * k),  
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            #Amplificando as dimensões da captura - ajuste final
            target_width = int(screenCapture.width() * 2.2)
            target_height = int(screenCapture.height() * 2.2)


            screenCapture = screenCapture.scaled(
                target_width,
                target_height,  
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            
            baseArc = QPixmap("images/export_with_magnitude.png")

            capturePainter = QPainter(baseArc)

            # posição onde a imagem será inserida no PNG final
            dest_rect = QRect(1800, 700, screenCapture.width(), screenCapture.height())

            capturePainter.drawPixmap(dest_rect, screenCapture)
            capturePainter.end()

        elif self.screenName == "Phas Diag":
            if not self.phasDiag_and_lissaj_scr2.page1.isolateScreen.isChecked() and not\
                self.phasDiag_and_lissaj_scr2.page2.isolateScreen.isChecked():

                #lissajous 
                rect = QRect(int(self.p/0.8 * 5), int(self.p/0.8 * 280), int(self.p/0.8 * 350), int(self.p/0.8 * 350))
                screenCapture = self.grab(rect)

                #constante para ajustar a ferramenta à opção do Windows: Change the size of text, apps, and other items:
                self.q = rect.width()/(screenCapture.width())

                #ajuste de screenCapture para se adequar aos valores de rect (nem sempre são equivalentes)
                screenCapture = screenCapture.scaled(
                    int(screenCapture.width() * self.q/min(1, (self.p/0.8))),
                    int(screenCapture.height() * self.q/min(1, (self.p/0.8))),  
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )

                #Caso os ajustes acima não sejam suficientes para padronizar o resultado para diferentes resoluções de tela:
                if not (abs(screenCapture.width() - 350)) <= 5:
                    k = 350/screenCapture.width()
                    screenCapture = screenCapture.scaled(
                    int(screenCapture.width() * k),
                    int(screenCapture.height() * k),  
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )

                #Amplificando as dimensões da captura - ajuste final
                target_width = int(screenCapture.width() * 4.5)
                target_height = int(screenCapture.height() * 4.5)


                screenCapture = screenCapture.scaled(
                    target_width,
                    target_height,  
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                
                baseArc = QPixmap("images/image_with_bar.png")

                capturePainter = QPainter(baseArc)

                # posição onde a imagem será inserida no PNG final
                dest_rect = QRect(20, 380, screenCapture.width(), screenCapture.height())

                capturePainter.drawPixmap(dest_rect, screenCapture)
                capturePainter.end()

                baseArc.save(f"images/export_with_lissajous.png", "PNG")

                #phas diag 
                rect = QRect(int(self.p/0.8 * 370), int(self.p/0.8 * 280), int(self.p/0.8 * 360), int(self.p/0.8 * 350))
                screenCapture = self.grab(rect)

                #constante para ajustar a ferramenta à opção do Windows: Change the size of text, apps, and other items:
                self.q = rect.width()/(screenCapture.width())

                #ajuste de screenCapture para se adequar aos valores de rect (nem sempre são equivalentes)
                screenCapture = screenCapture.scaled(
                    int(screenCapture.width() * self.q/min(1, (self.p/0.8))),
                    int(screenCapture.height() * self.q/min(1, (self.p/0.8))),  
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )

                #Caso os ajustes acima não sejam suficientes para padronizar o resultado para diferentes resoluções de tela:
                if not (abs(screenCapture.width() - 350)) <= 5:
                    k = 350/screenCapture.width()
                    screenCapture = screenCapture.scaled(
                    int(screenCapture.width() * k),
                    int(screenCapture.height() * k),  
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )

                #Amplificando as dimensões da captura - ajuste final
                target_width = int(screenCapture.width() * 4.5)
                target_height = int(screenCapture.height() * 4.5)


                screenCapture = screenCapture.scaled(
                    target_width,
                    target_height,  
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                
                baseArc = QPixmap("images/export_with_lissajous.png")

                capturePainter = QPainter(baseArc)

                # posição onde a imagem será inserida no PNG final
                dest_rect = QRect(1800, 380, screenCapture.width(), screenCapture.height())

                capturePainter.drawPixmap(dest_rect, screenCapture)
                capturePainter.end()

            else:
                rect = QRect(int(self.p/0.8 * 250), int(self.p/0.8 * 280), int(self.p/0.8 * 350), int(self.p/0.8 * 350))
                screenCapture = self.grab(rect)

                #constante para ajustar a ferramenta à opção do Windows: Change the size of text, apps, and other items:
                self.q = rect.width()/(screenCapture.width())

                #ajuste de screenCapture para se adequar aos valores de rect (nem sempre são equivalentes)
                screenCapture = screenCapture.scaled(
                    int(screenCapture.width() * self.q/min(1, (self.p/0.8))),
                    int(screenCapture.height() * self.q/min(1, (self.p/0.8))),  
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )

                #Caso os ajustes acima não sejam suficientes para padronizar o resultado para diferentes resoluções de tela:
                if not (abs(screenCapture.width() - 800)) <= 5:
                    k = 800/screenCapture.width()
                    screenCapture = screenCapture.scaled(
                    int(screenCapture.width() * k),
                    int(screenCapture.height() * k),  
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )

                #Amplificando as dimensões da captura - ajuste final
                target_width = int(screenCapture.width() * 1.8)
                target_height = int(screenCapture.height() * 1.8)


                screenCapture = screenCapture.scaled(
                    target_width,
                    target_height,  
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                
                baseArc = QPixmap("images/image_with_bar.png")

                capturePainter = QPainter(baseArc)

                # posição onde a imagem será inserida no PNG final
                dest_rect = QRect((sheet_w - screenCapture.width()) // 2, 380, screenCapture.width(), screenCapture.height())

                capturePainter.drawPixmap(dest_rect, screenCapture)
                capturePainter.end()



        # Salvar
        baseArc.save(finalOutput, "PNG")
        

        #Desfazendo os ajustes feitos para captura, tudo voltando ao normal:
        self.mainScr.setBackground((5, 5, 18))
        self.FFTScr.setBackground((16, 5, 5))
        self.freqRespScr.magnitude.setBackground((5, 16, 5))
        self.freqRespScr.phase.setBackground((5, 16, 5))
        self.phasDiag_and_lissajScr.phasDiag.setBackground((18, 18, 0))
        self.phasDiag_and_lissajScr.lissaj.setBackground((18, 18, 0))
        if self.language == "Português":
            self.FFTScr.getPlotItem().setLabel(axis='bottom', text='Frequência (Hz)', color='white', **{'font-size':'8pt'})
            self.freqRespScr.magnitude.getPlotItem().setLabel(axis='bottom', text='Frequência (Hz)', color='white', **{'font-size':'8pt'})
            self.freqRespScr.phase.getPlotItem().setLabel(axis='bottom', text='Frequência (Hz)', color='white', **{'font-size':'8pt'})
            self.freqRespScr.phase.getPlotItem().setLabel(axis='left', text='Fase (graus)', color='white', **{'font-size':'8pt'})
        else:
            self.FFTScr.getPlotItem().setLabel(axis='bottom', text='Frequency (Hz)', color='white', **{'font-size':'8pt'})
            self.freqRespScr.magnitude.getPlotItem().setLabel(axis='bottom', text='Frequency (Hz)', color='white', **{'font-size':'8pt'})
            self.freqRespScr.phase.getPlotItem().setLabel(axis='bottom', text='Frequency (Hz)', color='white', **{'font-size':'8pt'})
            self.freqRespScr.phase.getPlotItem().setLabel(axis='left', text='Phase (degrees)', color='white', **{'font-size':'8pt'})
        self.FFTScr.getPlotItem().setLabel(axis='left', text='Amplitude (dB)', color='white', **{'font-size':'8pt'})
        self.freqRespScr.magnitude.getPlotItem().setLabel(axis='left', text='Magnitude (dB)', color='white', **{'font-size':'8pt'})
        self.blackLabel1.setStyleSheet("background-color: black")
        self.blackLabel2.setStyleSheet("background-color: black")
        self.timeLabel.setStyleSheet(""" color: "white"; 
                                            background-color: transparent""")
        
        if self.phasDiag_and_lissaj_scr2.page2.channelxAxisSelectCB.currentText() == "CH1":
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='CH1 (V)', color='white', **{'font-size':'8pt'})
        elif self.phasDiag_and_lissaj_scr2.page2.channelxAxisSelectCB.currentText() == "CH2":
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='CH2 (V)', color='white', **{'font-size':'8pt'})
        elif self.phasDiag_and_lissaj_scr2.page2.channelxAxisSelectCB.currentText() == "Math":
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='bottom', text='Math (V)', color='white', **{'font-size':'8pt'})

        
        if self.phasDiag_and_lissaj_scr2.page2.channelyAxisSelectCB.currentText() == "CH1":
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='CH1 (V)', color='white', **{'font-size':'8pt'})
        elif self.phasDiag_and_lissaj_scr2.page2.channelyAxisSelectCB.currentText() == "CH2":
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='CH2 (V)', color='white', **{'font-size':'8pt'})
        elif self.phasDiag_and_lissaj_scr2.page2.channelyAxisSelectCB.currentText() == "Math":
            self.phasDiag_and_lissajScr.lissaj.getPlotItem().setLabel(axis='left', text='Math (V)', color='white', **{'font-size':'8pt'})

        self.whiteExportLabel.hide()
        self.backgroundLabel5.show()

         
        if os.path.exists("images/export_with_lissajous.png"): os.remove("images/export_with_lissajous.png")
        if os.path.exists("images/export_with_magnitude.png"): os.remove("images/export_with_magnitude.png")
        if os.path.exists("images/image_with_bar.png"): os.remove("images/image_with_bar.png")

        self.captureScreen = CaptureScreen(self.language, datetimeText, finalOutput, "Image")
        self.captureScreen.exec()