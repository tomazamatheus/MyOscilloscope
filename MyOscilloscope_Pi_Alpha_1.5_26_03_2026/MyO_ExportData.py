import os
import datetime
import pandas as pd
from PIL import Image
from PySide6.QtGui import QPixmap, QPainter, QIcon, QFont, QDesktopServices
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QFileDialog
from PySide6.QtCore import Qt, QRect, QUrl
from MyO_PopUpWindows import *
from Main_Screen1 import *
from screen2 import *

def exportData(self):

    if self.language == "English": popUpWindowTitle = "Create .csv archive"
    else:                          popUpWindowTitle = "Criar arquivo .csv"
    finalOutput, _ = QFileDialog.getSaveFileName(
        self,
        popUpWindowTitle,
        "",
        "CSV Files (*.csv);;All Files (*)"
    )

    if not finalOutput:
        return

    data = {}

    if self.screenName == "Main":
        if self.btCH1.isOn:
            data['x_CH1'] = self.mainScr.x_plot
            data['y_CH1'] = self.mainScr.y_CH1_pure

        if self.btCH2.isOn:
            data['x_CH2'] = self.mainScr.x_plot
            data['y_CH2'] = self.mainScr.y_CH2_pure

        if self.btMath.isOn:
            data['x_Math'] = self.mainScr.x_plot
            data['y_Math'] = self.mainScr.y_Math_pure

        dataframe = pd.DataFrame(data)

        # escreve a primeira linha
        with open(finalOutput, "w", encoding="utf-8") as f:
            f.write(f"MyOscilloscope - Data from Main\n")

        # adiciona o dataframe abaixo
        dataframe.to_csv(finalOutput, mode="a", index=False)

    elif self.screenName == "FFT":
        if self.btCH1.isOn:
            data['x_CH1'] = self.FFTScr.FFT_freqs_CH1
            data['y_CH1'] = self.FFTScr.FFT_amplits_CH1_dB

        if self.btCH2.isOn:
            data['x_CH2'] = self.FFTScr.FFT_freqs_CH2
            data['y_CH2'] = self.FFTScr.FFT_amplits_CH2_dB

        if self.btMath.isOn:
            data['x_Math'] = self.FFTScr.FFT_freqs_Math
            data['y_Math'] = self.FFTScr.FFT_amplits_Math_dB

        dataframe = pd.DataFrame(data)

        # escreve a primeira linha
        with open(finalOutput, "w", encoding="utf-8") as f:
            f.write(f"MyOscilloscope - Data from FFT\n")

        # adiciona o dataframe abaixo
        dataframe.to_csv(finalOutput, mode="a", index=False)

    elif self.screenName == "Freq Resp":
        if not finalOutput:
            return

        all_data = []
        try:
            for i, (curve, curve_phase) in enumerate(
                zip(self.freqRespCurves, self.freqRespCurves_phase), start=1):
                x, y_mag = curve.getData()
                _, y_phase = curve_phase.getData()

                if curve.curveColor == 'w': color = "white"
                elif curve.curveColor == 'b': color = "blue"
                elif curve.curveColor == 'r': color = "red"
                elif curve.curveColor == 'y': color = "yellow"
                elif curve.curveColor == 'c': color = "cyan"
                elif curve.curveColor == 'purple': color = "purple"
                elif curve.curveColor == 'orange': color = "orange"

                df = pd.DataFrame({
                    "curve": f"curve{i}",
                    "color": str(color),
                    "frequency_Hz": 10**x,
                    "magnitude_dB": y_mag,
                    "phase_deg": y_phase
                })

                all_data.append(df)

            dataframe = pd.concat(all_data, ignore_index=True)

            # escreve cabeçalho informativo
            with open(finalOutput, "w", encoding="utf-8") as f:
                f.write("MyOscilloscope - Data from Frequency Response\n")
                f.write("curve,color,frequency_Hz,magnitude_dB, phase_dB\n")

            dataframe.to_csv(finalOutput, mode="a", index=False, header=False)
        except ValueError:
            pass

        except UnboundLocalError:
            pass

        
    elif self.screenName == "Phas Diag":

        with open(finalOutput, "w", encoding="utf-8", newline="") as f:

            if not self.phasDiag_and_lissaj_scr2.page2.isolateScreen.isChecked():

                rows = []

                if self.phasDiagMagnitVoltage == "RMS":
                    magn_CH1 = self.CH1VRMSValue
                    magn_CH2 = self.CH2VRMSValue
                    magn_math = self.mathVRMSValue

                elif self.phasDiagMagnitVoltage == "Pk-to-Pk":
                    magn_CH1 = self.CH1VppValue
                    magn_CH2 = self.CH2VppValue
                    magn_math = self.mathVppValue

                else:
                    magn_CH1 = self.CH1VppValue/2
                    magn_CH2 = self.CH2VppValue/2
                    magn_math = self.mathVppValue/2

                if self.btCH1.isOn:
                    rows.append({"channel": "CH1", "magnitude": magn_CH1, "phase": self.CH1Phase})

                if self.btCH2.isOn:
                    rows.append({"channel": "CH2", "magnitude": magn_CH2, "phase": self.CH2Phase})

                if self.btMath.isOn:
                    rows.append({"channel": "Math", "magnitude": magn_math, "phase": self.mathPhase})

                dataframe = pd.DataFrame(rows)

                f.write("MyOscilloscope - Data from Phasor Diagram\n")
                dataframe.to_csv(f, index=False)

                f.write("\n")  # separador


            if not self.phasDiag_and_lissaj_scr2.page1.isolateScreen.isChecked():

                data = {
                    "xAxis": self.phasDiag_and_lissajScr.lissaj.xAxis,
                    "yAxis": self.phasDiag_and_lissajScr.lissaj.yAxis
                }

                dataframe = pd.DataFrame(data)

                f.write("MyOscilloscope - Data from Lissajous\n")
                dataframe.to_csv(f, index=False)
                

    capturedTime = f"{datetime.date.today()} {datetime.datetime.now().time()}."
    self.captureScreen = CaptureScreen(self.language, capturedTime, finalOutput, "Data")
    self.captureScreen.exec()