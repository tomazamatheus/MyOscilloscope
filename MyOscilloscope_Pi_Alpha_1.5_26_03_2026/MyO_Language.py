from PySide6.QtGui import QFont


def saveLanguage(self, lang : str):
    filepath = self.PARAMETERS_FILE
    key = "language"
    val = lang

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    key_written = False


    for i, line in enumerate(lines):
        if line.strip().startswith(f"{key} ="):
            lines[i] = f"{key} = {val}\n"
            key_written = True
            break


    if not key_written:
        lines.append(f"{key} = {val}\n")

    
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)

    self.loadLanguage()

def loadLanguage(self):
    filepath = self.PARAMETERS_FILE
    params = {
        "offs_CH1": 1.500,
        "offs_CH2": 1.500,
        "attn_CH1": 1.500,
        "attn_CH2": 1.500,
        "phase_corr": 0.00000,
        "samplingRate": 19232,
        "show_welcome": True,
        "language": "English",
    }

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()


                if not line or line.startswith("#"):
                    continue

                if "=" not in line:
                    continue

                key, value = map(str.strip, line.split("=", 1))

                if key not in params:
                    continue

                if key == "language": params[key] = value
                    
            self.language = params["language"]
            self.changeSystemLanguage(self.language)
                                    
    except FileNotFoundError:
        pass

def changeSystemLanguage(self, lang):

    #tela de créditos
    self.creditsScreen.language = lang
    self.creditsScreen.setLanguage()

    #tela de apoio do WFM Generator
    self.WFM_supportScreen.language = lang
    self.WFM_supportScreen.setLanguage()

    #tela aviso COM Port
    self.COMPortScr.language = lang
    self.COMPortScr.setLanguage()

    #tela save calib
    self.savedCalibScr.language = lang
    self.savedCalibScr.setLanguage()

    #NOTA: o ajuste para a tela de calibration wizard ocorre em calibWizardIsOn()

    self.FFT_scr2.language = lang
    #Measure scr2
    if self.language == "Português":
        self.measure.channelSelectLabel.setText("Canal:")
        self.measure.frequencyLabel.setText("Frequência:")
        self.measure.periodLabel.setText("Período:")
        self.measure.meanLabel.setText("Valor Médio - DC:")
        self.measure.vppLabel.setText("Pico-a-Pico:")
        self.measure.vrmsLabel.setText("RMS:")
        self.measure.minLabel.setText("Mín:")
        self.measure.maxLabel.setText("Máx:")
        self.measure.phaseLabel.setText("Defasagem:")

        self.mainScr2_1.attnFactorLabel_CH1.setText("Fator de Aten. (CH1)")
        self.mainScr2_1.attnFactorLabel_CH2.setText("Fator de Aten. (CH2)")
        self.mainScr2_1.refChannelLabel.setText("Canal de Referência:")
        self.mainScr2_1.customTimeScaleLabel.setWordWrap(True)
        self.mainScr2_1.customTimeScaleLabel.setText("Definir escala customizada para Time (ms):")
        self.mainScr2_2.currentInVerticalScaleLabel.setText("Trocar V/div por A/div na escala vertical:")
        self.mainScr2_2.currentInVerticalScaleLabel.setWordWrap(True)

        self.cursor.cursorSelectLabel.setText("Altere um cursor via Cursor Knob ou pela sua caixa de texto." \
        " Cursor Knob associado ao cursor:")
        self.cursor.cursorSelectLabel.setWordWrap(True)

        self.cursorFFT.cursorSelectLabel.setText("Altere um cursor via Cursor Knob ou pela sua caixa de texto." \
        " Cursor Knob associado ao cursor:")
        self.cursorFFT.cursorSelectLabel.setWordWrap(True)

        self.cursorFreqResp_Magn.cursorSelectLabel.setText("Altere um cursor via Cursor Knob ou pela sua caixa de texto." \
        " Cursor Knob associado ao cursor:")
        self.cursorFreqResp_Magn.cursorSelectLabel.setWordWrap(True)

        self.cursorFreqResp_Phase.cursorSelectLabel.setText("Altere um cursor via Cursor Knob ou pela sua caixa de texto." \
        " Cursor Knob associado ao cursor:")
        self.cursorFreqResp_Phase.cursorSelectLabel.setWordWrap(True)

        self.trigger.trigChannelLabel.setText("Canal associado:")
        self.trigger.trigTypeCBLabel.setText("Tipo de Captura:")
        self.trigger.trigModeCBLabel.setText("Modo de operação:")
        self.trigger.trigChannelLabel2.setText("Para alterar o canal associado, mude o canal de referência na aba Main.")

        if self.FFT_scr2.stack.currentIndex() == 0: self.FFT_scr2.secondaryLabel.setText("Pág. 1: Ajuste dos limites visíveis")
        self.FFT_scr2.secondaryLabel.setWordWrap(True)

        self.FFT_scr2.page1.x_botLim_Label.setText("Lim. Inf. (Freq.) \n(Hz): ")
        self.FFT_scr2.page1.x_topLim_Label.setText("Lim. Sup. (Freq.) \n(Hz): ")
        self.FFT_scr2.page1.y_botLim_Label.setText("Lim. Inf. (Ampl.) \n(dB): ")
        self.FFT_scr2.page1.y_topLim_Label.setText("Lim. Sup. (Ampl.) \n(dB): ")
        self.FFT_scr2.page1.btRestoreDefault.setText("Restaurar\nPadrão")


        if self.FFT_scr2.stack.currentIndex() == 1: self.FFT_scr2.secondaryLabel.setText("Pág. 2: Maiores frequências")
        self.FFT_scr2.page2.channelLabel.setText("Canal:")

        self.FFTScr.getPlotItem().setLabel(axis='bottom', text='Frequência (Hz)', color='white', **{'font-size':'8pt'})

        self.freqResp_scr2.freqResp_page1.numberPointsLabel.setText("Número de pontos:")
        self.freqResp_scr2.freqResp_page1.initialFreqLabel.setText("Freq. Inicial (Hz):")
        self.freqResp_scr2.freqResp_page1.finalFreqLabel.setText("Freq. Final (Hz):")
        self.freqResp_scr2.freqResp_page1.btSweepLabel.setText("Controle do Sweep:")

        self.freqResp_scr2.freqResp_page2.functionTypeLabel.setText("Função do Sweep:")
        self.freqResp_scr2.freqResp_page2.y_AxisLabel.setText("Eixo Y:")
        self.freqResp_scr2.freqResp_page2.plotColorLabel.setText("Cor do Plot:")
        self.freqResp_scr2.freqResp_page2.btclearScreen.setText("Limpar\nTela")
        self.freqResp_scr2.freqResp_page2.clearScreenPartialCheckBox.setText("Manter o plot mais\nrecente ao limpar.")
    
        self.freqResp_scr2.freqResp_page3.x_botLim_Label.setText("Lim. Inf. (Freq.) \n(Hz): ")
        
        self.freqResp_scr2.freqResp_page3.x_topLim_Label.setText("Lim. Sup. (Freq.) \n(Hz): ")

        self.freqResp_scr2.freqResp_page3.y_botLim_Label.setText("Lim. Inf.\n(Magn.) (dB): ")

        self.freqResp_scr2.freqResp_page3.y_topLim_Label.setText("Lim. Sup.\n(Magn.) (dB): ")

        self.freqResp_scr2.freqResp_page3.y_botLim_Label_phase.setText("Lim. Inf.\n(Fase) (graus): ")

        self.freqResp_scr2.freqResp_page3.y_topLim_Label_phase.setText("Lim. Sup.\n(Fase) (graus): ")

        self.freqRespScr.magnitude.getPlotItem().setLabel(axis='bottom', text='Frequência (Hz)', color='white', **{'font-size':'8pt'})
        self.freqRespScr.phase.getPlotItem().setLabel(axis='bottom', text='Frequência (Hz)', color='white', **{'font-size':'8pt'})
        self.freqRespScr.phase.getPlotItem().setLabel(axis='left', text='Fase (graus)', color='white', **{'font-size':'8pt'})

        self.phasDiag_and_lissaj_scr2.page1.CH1PhaseLabel.setText("Fase\n(graus):")
        self.phasDiag_and_lissaj_scr2.page1.CH2PhaseLabel.setText("Fase\n(graus):")
        self.phasDiag_and_lissaj_scr2.page1.MathPhaseLabel.setText("Fase\n(graus):")
        self.phasDiag_and_lissaj_scr2.page1.isolateScreen.setText("Isolar")
        self.phasDiag_and_lissaj_scr2.page1.magnitudeVoltageLabel.setText("Tensão da\nMagnitude:")

        self.phasDiag_and_lissaj_scr2.page2.isolateScreen.setText("Isolar")
        self.phasDiag_and_lissaj_scr2.page2.choosexAxisChannelLabel.setText("Canal do\nEixo X:")
        self.phasDiag_and_lissaj_scr2.page2.chooseyAxisChannelLabel.setText("Canal do\nEixo Y:")

        self.calib_scr2.LPF_CheckBox.setText("Habilitar Filtro\nPassa-Baixa (DSP)")
        self.calib_scr2.LPF_label.setText("Freq. de Corte (Hz):")
        self.calib_scr2.phaseCorr_label.setText("O ajuste de Correção de Fase e o Filtro Passa-Baixa podem causar leve distorção nos dois canais.")
        self.calib_scr2.phaseCorr_CheckBox.setText("Habilitar ajuste de\nCorreção de Fase")


        self.WFMgeneratorScr.signalTypeLabel.setText("Tipo de Sinal:")
        self.WFMgeneratorScr.freqLabel.setText("Frequência (Hz):")

        self.calibrationScr.mainLabel.setText("Opções de calibração:")
        self.exportScr.mainLabel.setText("Exportar como:")
        self.mathPlusScr.mainLabel.setText("Escolha a operação\nassociada ao Canal Math:")
        #self.mathPlusScr.additionalLabel.setText("ou")
        self.cursorFFTLabel.setText("Os cursores X1 e X2 estão em\nescala logarítmica")

    else:
        self.measure.channelSelectLabel.setText("Channel:")
        self.measure.frequencyLabel.setText("Frequency:")
        self.measure.periodLabel.setText("Period:")
        self.measure.meanLabel.setText("DC - Mean:")
        self.measure.vppLabel.setText("Peak-to-Peak:")
        self.measure.vrmsLabel.setText("RMS:")
        self.measure.minLabel.setText("Min:")
        self.measure.maxLabel.setText("Max:")
        self.measure.phaseLabel.setText("Phase Shift:")

        self.mainScr2_1.attnFactorLabel_CH1.setText("Attn. Factor (CH1)")
        self.mainScr2_1.attnFactorLabel_CH2.setText("Attn. Factor (CH2)")
        self.mainScr2_1.refChannelLabel.setText("Reference Channel:")
        self.mainScr2_1.customTimeScaleLabel.setWordWrap(True)
        self.mainScr2_1.customTimeScaleLabel.setText("Custom Time Scale value (ms):")
        self.mainScr2_2.currentInVerticalScaleLabel.setText("Replace V/div with A/div on vertical scale:")
        self.mainScr2_2.currentInVerticalScaleLabel.setWordWrap(True)

        self.cursor.cursorSelectLabel.setText("Change the cursor value either using the Cursor Knob or its box. " +
                                                "Cursor knob is assigned to:")
        self.cursor.cursorSelectLabel.setWordWrap(True)

        self.cursorFFT.cursorSelectLabel.setText("Change the cursor value either using the Cursor Knob or its box. " +
                                                "Cursor knob is assigned to:")
        self.cursorFFT.cursorSelectLabel.setWordWrap(True)

        self.cursorFreqResp_Magn.cursorSelectLabel.setText("Change the cursor value either using the Cursor Knob or its box. " +
                                                "Cursor knob is assigned to:")
        self.cursorFreqResp_Magn.cursorSelectLabel.setWordWrap(True)

        self.cursorFreqResp_Phase.cursorSelectLabel.setText("Change the cursor value either using the Cursor Knob or its box. " +
                                                "Cursor knob is assigned to:")
        self.cursorFreqResp_Phase.cursorSelectLabel.setWordWrap(True)

        self.trigger.trigChannelLabel.setText("Trigger Channel:")
        self.trigger.trigTypeCBLabel.setText("Trigger Type:")
        self.trigger.trigModeCBLabel.setText("Trigger Mode:")

        self.FFT_scr2.page1.x_botLim_Label.setText("Bot Lim (Freq.) \n(Hz): ")
        self.FFT_scr2.page1.x_topLim_Label.setText("Top Lim (Freq.) \n(Hz): ")
        self.FFT_scr2.page1.y_botLim_Label.setText("Bot Lim (Ampl.) \n(dB): ")
        self.FFT_scr2.page1.y_topLim_Label.setText("Top Lim (Ampl.) \n(dB): ")

        self.FFT_scr2.secondaryLabel.setText("Screen 1: adjust\nthe visible limits\n")
        self.FFT_scr2.secondaryLabel.setWordWrap(True)
        self.FFT_scr2.page2.channelLabel.setText("Channel:")

        self.FFT_scr2.page1.btRestoreDefault.setText("Restore\nDefault")
        self.FFTScr.getPlotItem().setLabel(axis='bottom', text='Frequency (Hz)', color='white', **{'font-size':'8pt'})

        self.freqResp_scr2.freqResp_page1.numberPointsLabel.setText("Number of points:")
        self.freqResp_scr2.freqResp_page1.initialFreqLabel.setText("Initial Freq. (Hz):")
        self.freqResp_scr2.freqResp_page1.finalFreqLabel.setText("Final Freq. (Hz):")
        self.freqResp_scr2.freqResp_page1.btSweepLabel.setText("Sweep Control:")

        self.freqResp_scr2.freqResp_page2.functionTypeLabel.setText("Sweep Function:")
        self.freqResp_scr2.freqResp_page2.y_AxisLabel.setText("Y-Axis:")
        self.freqResp_scr2.freqResp_page2.plotColorLabel.setText("Plot Color:")
        self.freqResp_scr2.freqResp_page2.btclearScreen.setText("Clear\nScreen")
        self.freqResp_scr2.freqResp_page2.clearScreenPartialCheckBox.setText("Keep the last plot\nwhen cleaning.")
    
        self.freqResp_scr2.freqResp_page3.x_botLim_Label.setText("Bot. lim. (Freq.) \n(Hz): ")
        
        self.freqResp_scr2.freqResp_page3.x_topLim_Label.setText("Top. lim. (Freq.) \n(Hz): ")

        self.freqResp_scr2.freqResp_page3.y_botLim_Label.setText("Bot. lim.\n(Magn.) (dB): ")

        self.freqResp_scr2.freqResp_page3.y_topLim_Label.setText("Top. lim.\n(Magn.) (dB): ")

        self.freqResp_scr2.freqResp_page3.y_botLim_Label_phase.setText("Bot. lim.\n(Phase) (deg.): ")

        self.freqResp_scr2.freqResp_page3.y_topLim_Label_phase.setText("Top. lim.\n(Phase) (deg.): ")

        self.freqRespScr.magnitude.getPlotItem().setLabel(axis='bottom', text='Frequency (Hz)', color='white', **{'font-size':'8pt'})
        self.freqRespScr.phase.getPlotItem().setLabel(axis='bottom', text='Frequency (Hz)', color='white', **{'font-size':'8pt'})
        self.freqRespScr.phase.getPlotItem().setLabel(axis='left', text='Phase (degrees)', color='white', **{'font-size':'8pt'})
        

        self.freqResp_scr2.freqResp_page3.btRestoreDefault.setText("Restore\nDefault")

        self.phasDiag_and_lissaj_scr2.page1.CH1PhaseLabel.setText("Phase\n(deg.):")
        self.phasDiag_and_lissaj_scr2.page1.CH2PhaseLabel.setText("Phase\n(deg.):")
        self.phasDiag_and_lissaj_scr2.page1.MathPhaseLabel.setText("Phase\n(deg.):")
        self.phasDiag_and_lissaj_scr2.page1.isolateScreen.setText("Isolate")
        self.phasDiag_and_lissaj_scr2.page1.magnitudeVoltageLabel.setText("Magnitude\nVoltage:")

        self.phasDiag_and_lissaj_scr2.page2.isolateScreen.setText("Isolate")
        self.phasDiag_and_lissaj_scr2.page2.choosexAxisChannelLabel.setText("X-Axis\nChannel:")
        self.phasDiag_and_lissaj_scr2.page2.chooseyAxisChannelLabel.setText("Y-Axis\nChannel:")

        if self.screen2.width() <= 128:
            self.calib_scr2.mainLabel.setFont(QFont("Microsoft Sans Serif", 18))
            self.calib_scr2.LPF_CheckBox.setText("Enable Low-Pass\nFilter")

        self.WFMgeneratorScr.signalTypeLabel.setText("Signal Type:")
        self.WFMgeneratorScr.freqLabel.setText("Frequency (Hz):")

        self.calibrationScr.mainLabel.setText("Calibration options:")
        self.exportScr.mainLabel.setText("Export as:")
        self.mathPlusScr.mainLabel.setText("Choose the operation for \nMath Channel:")
        # self.mathPlusScr.additionalLabel.setText("or")
        self.cursorFFTLabel.setText("Cursor lines X1 and X2 are in \nlogarithmic scale")

        self.helpScrLangEnglish()

def helpScrLangEnglish(self):
    self.helpScr.sectionLabel.setText("Go to section:")
    self.helpScr.page1.label1.setText("Welcome to the MyOscilloscope User Help section! Browse the following pages " + 
                                        "to find instructions on how to use the kit and the graphical interface. ")
    
    self.helpScr.sectionCB.clear()
    self.helpScr.sectionCBItems = ["First Page", "Introduction", "DC and AC Coupling", "Circuit Connection", "Voltage Source", "Calibration", "Main Functionalities",
                            "Support Functionalities", "Last Pages"]

    self.helpScr.sectionCB.addItems(self.helpScr.sectionCBItems)

    #page2
    self.helpScr.page2.titleLabel.setText("Introduction")
    self.helpScr.page2.label1.setText("MyOscilloscope is a project designed to assist students and enthusiasts in learning " + 
                                        "Electric Circuits. To achieve this, the kit and the graphical interface work together " + 
                                        "as an integrated system.")

    #page3
    self.helpScr.page3.titleLabel.setText("Introduction")
    self.helpScr.page3.label1.setText("The MyOscilloscope kit includes a shield, which is a board that works together " + 
                                        "with a microcontroller to receive the signals to be measured and observed. ")

                                
    #page4
    self.helpScr.page4.titleLabel.setText("Introduction")
    self.helpScr.page4.label1.setText("The kit also includes jumper wires, a breadboard, and components for circuit " + 
                                        "assembly, allowing experimental setups to be built just as they would be in a " + 
                                        "teaching laboratory.")
                                
    #page5
    self.helpScr.page5.titleLabel.setText("Introduction")
    self.helpScr.page5.label1.setText("First, connect the USB cable between your PC and the microcontroller. " + 
                                        "If the interface does not detect the shield on any COM port, click Search " + 
                                        "(on the “COM Port” screen) to perform a new search.")
                                
    #page6
    self.helpScr.page6.titleLabel.setText("Introduction")
    self.helpScr.page6.label1.setText("Assemble the circuit you wish to study on the breadboard. Define one of the circuit " + 
                                        "nodes as the reference node (GND). Also define the node whose voltage you want to " + 
                                        "observe on oscilloscope CH1, and the node whose voltage will be observed " + 
                                        "on CH2. ")
                                
    self.helpScr.page6.sourceLabel.setText("Source: [1]")

    #page7
    self.helpScr.page7.titleLabel.setText("DC and AC Coupling")
    self.helpScr.page7.label1.setText("As will be discussed later, the signals under study can be decomposed into components; in other words, the sum of the components is equal to the observed signal. " +
                                        "\nAmong all signal components, one has zero frequency and is known as the DC component. All the others have non-zero frequency.")
    self.helpScr.page7.sourceLabel.setText("Source: [2]")
                                
    #page8
    self.helpScr.page8.titleLabel.setText("DC and AC Coupling")
    self.helpScr.page8.label1.setText("Oscilloscopes generally provide a way to either include or reject the DC component of a signal. In MyOscilloscope, this is determined by the input to which the probe is connected. " +
                                        "\nCH1 provides AC1 and DC1 inputs. The first rejects the DC component, while the second preserves it. The equivalent inputs for CH2 are AC2 and DC2.")
    self.helpScr.page8.label2.setText("A jumper must be connected between the reference node of the assembled circuit and the GND inputs of the shield, as indicated in the image.")
                                
    #page9
    self.helpScr.page9.titleLabel.setText("Connection of Breadboard\nCircuit to Shield")
    self.helpScr.page9.label1.setText("The following image shows a schematic illustrating how the breadboard circuit should be connected to the shield, with both channels set to DC coupling.")
                                
    #page10
    self.helpScr.page10.titleLabel.setText("Connection of Breadboard\nCircuit to Shield")
    self.helpScr.page10.label1.setText("The following image shows a schematic illustrating how the breadboard circuit should be connected to the shield, with both channels set to AC coupling.")
                                
    #page11
    self.helpScr.page11.titleLabel.setText("Connection of Breadboard\nCircuit to Shield")
    self.helpScr.page11.label1.setText("• It is not necessary for both channels to operate in AC mode or both in DC mode. " + 
                                        "\n•The observed voltage is measured with respect to the reference node connected to the shield’s GND inputs. This means that changing the reference node may produce different results, since the voltage reference is altered.")

    #page12
    self.helpScr.page12.titleLabel.setText("The MyOscilloscope Voltage Source")
    self.helpScr.page12.label1.setText("To power the circuit under study, MyOscilloscope includes a special cable that operates in conjunction with the interface’s Waveform Generator.")
                                
    #page13
    self.helpScr.page13.titleLabel.setText("The MyOscilloscope Voltage Source")
    self.helpScr.page13.label1.setText("This special cable features, at one end, a 3.5 mm (P2) audio connector to be connected to the PC’s audio output. At the other end, there are three jumper wires. Two of them are colored, and the third one is black.")
                                
    #page14
    self.helpScr.page14.titleLabel.setText("The MyOscilloscope Voltage Source")
    self.helpScr.page14.label1.setText("The two colored jumpers represent the higher-voltage terminal (typically associated with red in laboratory settings) of the voltage source, while the black jumper represents the lower-voltage terminal (typically associated with black).")

    #page15
    self.helpScr.page15.titleLabel.setText("The MyOscilloscope Voltage Source")
    self.helpScr.page15.label1.setText("Some applications may require the use of both colored jumpers. Under no circumstances should they be short-circuited. With the Waveform Generator enabled, a short circuit may occur, potentially causing damage to the kit, the assembled circuit, and the user’s PC. Unless otherwise specified, use only one of the colored jumpers and leave the other unconnected. " +
                                        "\n\nAs in a laboratory environment, never short-circuit the two terminals of the voltage source. In other words, never connect the jumpers of the cable shown in the image to each other.")
                                
    #page16
    self.helpScr.page16.titleLabel.setText("The MyOscilloscope Voltage Source")
    self.helpScr.page16.label1.setText("The following schematic illustrates how the circuit components should be connected when the power cable is added.")
                                
    #page17
    self.helpScr.page17.titleLabel.setText("Waveform Generator")
    self.helpScr.page17.label1.setText("• MyOscilloscope includes a built-in Waveform Generator. It allows adjustment of the waveform type, frequency, and amplitude. " +
                                "\n\n\n\n\n\n\n\n\n\n" + 
                                "• The button marked with a “?” provides additional instructions on how the Waveform Generator operates. It is worth reviewing.")

    #page18
    self.helpScr.page18.titleLabel.setText("Calibration")
    self.helpScr.page18.label1.setText("•Before performing measurements with MyOscilloscope, it is important to calibrate the kit with respect to the user’s PC. There are two ways to perform this procedure: " +
                                "\n\n1) Manual Calibration, intended for users familiar with the procedure;" + 
                                "\n\n2) Calibration Wizard, which provides step-by-step guidance for proper calibration.")

    #page19
    self.helpScr.page19.titleLabel.setText("Introduction to MyOscilloscope\nMain Functionalities")
    self.helpScr.page19.label1.setText("Below is a summary of the main functionalities of MyOscilloscope, associated with the buttons located in the upper-left section of the interface.")

    #page20
    self.helpScr.page20.titleLabel.setText("Main (Screen)")
    self.helpScr.page20.label1.setText("Allows signal display in the time domain. Using the knobs located on the right side of the interface, you can adjust the horizontal scale (Time), vertical scale (V/div or A/div), and the vertical position (Position) of each channel." + 
                                "\n\n\n\n\n\n\n\n\n\n\n\n\n" + 
                                "Its auxiliary screen has multiple applications and will be discussed shortly.")
                                
    #page21
    self.helpScr.page21.titleLabel.setText("FFT")
    self.helpScr.page21.label1.setText("FFT stands for Fast Fourier Transform. It is based on the concept that signals can be represented as sums of sinusoids with distinct amplitudes and frequencies, including zero frequency (the DC component). This section allows signal display in the frequency domain.")
    self.helpScr.page21.label2.setText("Its auxiliary screen contains two pages:" +
                                "\n\n• Page 1: Allows adjustment of the display limits for each axis. " +
                                "\n\n• Page 2: Displays the highest amplitudes among the frequency–amplitude pairs of each channel. ")
                                
    #page22
    self.helpScr.page22.titleLabel.setText("Frequency Response")
    self.helpScr.page22.label1.setText("Allows the definition of the frequency response curve of the circuit under study (sweep). In the auxiliary screens, it provides: \n" +
    "\n• Definition of the number of curve points and frequency limits;" + 
    "\n• Buttons to start, pause, and stop the sweep;"+
    "\n• Selection of the channels associated with the frequency response function;"+
    "\n• Switching between magnitude and phase plots;"+
    "\n• Selection of the curve color;"+
    "\n• Removal of curves from the screen;"+
    "\n• Adjustment of the displayed limits.")

    #page23
    self.helpScr.page23.titleLabel.setText("Phasor Diagram & Lissajous")
    self.helpScr.page23.label1.setText("The Phasor Diagram displays the phasors of each channel in the complex plane. Its auxiliary screen shows the phase and magnitude of each phasor. It is possible to adjust the type of voltage associated with the phasor magnitudes.")
    self.helpScr.page23.label2.setText("The Lissajous figure displays a parametric plot based on two selectable channels among CH1, CH2, and Math. Its auxiliary screen allows this selection. Both auxiliary screens can display their respective functionalities independently.")
                                
    #page24
    self.helpScr.page24.titleLabel.setText("Main Screen Auxiliary Functionalities:\nAttenuation Jumpers")
    self.helpScr.page24.label1.setText("The Arduino Uno microcontroller currently used in the kit supports, together with the shield, voltage inputs approximately between −3 V and +3 V. The shield includes attenuation jumpers which, when removed, allow measurement of signals with amplitudes up to five times higher. When these jumpers are disconnected, adjust the attenuation factor of the corresponding channel accordingly.")
                                
    #page25
    self.helpScr.page25.titleLabel.setText("Main Screen Auxiliary Functionalities:\nVertical Scale Change")
    self.helpScr.page25.label1.setText("If the voltage of a channel is associated with a resistor, Ohm’s Law can be used to configure the channel as a current meter. To do so, enable this functionality for the specific channel and enter the value of the associated resistor (shunt resistor). The displayed signal will then be indicated as current, and all measurements will be shown in current units.")
                                
    #page26
    self.helpScr.page26.titleLabel.setText("Main Screen Auxiliary Functionalities\n")
    self.helpScr.page26.label1.setText("Custom Time Scale: Allows setting any time scale value between 0.1 and 50 ms/div.")
    self.helpScr.page26.label2.setText("Reference Channel: Defines which channel represents the zero-phase (reference) signal. It also affects the Trigger, Cursors, Calibration Wizard, and Phasor Diagram features.")
    self.helpScr.page26.label3.setText("The following pages provide additional explanations on how the scales operate.")

                                
    #page27
    self.helpScr.page27.titleLabel.setText("Horizontal and Vertical Scales in Time Domain:\nExample 1")

    #page28
    self.helpScr.page28.titleLabel.setText("Horizontal and Vertical Scales in Time Domain:\nExample 2")
    self.helpScr.page28.label1.setText("The same signals for each channel are shown in both images, with different scale settings. Always adjust the scales properly for optimal visualization.")

    #page29
    self.helpScr.page29.titleLabel.setText("MyOscilloscope Support Functionalities")
    self.helpScr.page29.label1.setText("The following pages contain a summary of the support functions of MyOscilloscope, most of which are common to standard bench oscilloscopes.")
    self.helpScr.page29.label2.setText("• Trigger: Enables synchronization of signal acquisition and display, ensuring proper visualization.")
                                
    #page30
    self.helpScr.page30.titleLabel.setText("MyOscilloscope Support Functionalities")
    self.helpScr.page30.label1.setText("• Measure: Displays important signal measurements for each channel, such as frequency, period, average value, maximum and minimum values, among other parameters.")
    self.helpScr.page30.label2.setText("• Cursor: Displays cursors that assist in obtaining signal information directly from the graph by adjusting their positions.") 
    self.helpScr.page30.label3.setText("• Freeze: Stops the update of data on the oscilloscope display. ")

    #page31
    self.helpScr.page31.titleLabel.setText("MyOscilloscope Support Functionalities")
    self.helpScr.page31.label1.setText("• Export: Allows the creation of a .csv spreadsheet file containing the interface graph data (Export Data) or the creation of a .png file showing a copy of the information currently displayed on the screen, including the main screen active at the moment of capture (Export Image).")
    self.helpScr.page31.label2.setText("• Math: Allows configuration of the operation associated with the Math channel across all program functionalities. Simple operations between CH1 and CH2 can be selected, or more complex mathematical expressions can be created using the Math+ feature.")
                                
    #page32
    self.helpScr.page32.label1.setText("For more information, visit the MyOscilloscope website by clicking the button shown in the image.")
    self.helpScr.page32.label2.setText("The Credits screen can be accessed by clicking the Escola Politécnica da USP icon (Minerva).")

    #page33
    self.helpScr.page33.titleLabel.setText("References")
    self.helpScr.page33.label1.setText("• The information provided in this User Support section is based on the MyOscilloscope User Guide, available at: myoscilloscope.lme.usp.br. Accessed on Feb 17, 2026. " + 
                                "\n\n\n\n[1] Adapted from course material by Professor Elisabete Galeazzo, Ph.D., Escola Politécnica da USP." +
                                "\n\n\n[2] https://www.facom.ufu.br/~jamil/eletronica/sinais_eletricos/sinais_eletricos.htm (Adapted). Accessed on Feb 17, 2026.")