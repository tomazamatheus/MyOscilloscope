import math
import numpy as np

        

def FFT_xBotLimLE_Changed(self):
    text = self.FFT_scr2.page1.x_botLim_LE.text()

    try:
        minor_ticks = []
        for decade in range(1, 6):  
            for k in range(2, 10):
                pos = decade + math.log10(k)
                minor_ticks.append((pos, "")) 

        self.FFTScr.xBotLim = float(text) 
        if self.FFTScr.xBotLim >= self.FFTScr.xTopLim:
            self.FFTScr.xBotLim = self.FFTScr.xTopLim
            self.FFT_scr2.page1.x_botLim_LE.setText(f"{self.FFTScr.xBotLim:.0f}")
            self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}")]
            self.FFTScr.setXRange(self.FFTScr.xBotLim, self.FFTScr.xBotLim)

        else:
            if self.FFTScr.xBotLim < 10:
                self.FFT_scr2.page1.x_botLim_LE.setText("10")
                if self.FFTScr.xTopLim < 100: 
                    self.FFTScr.ticksX = [(1, "10"), (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                elif self.FFTScr.xTopLim < 1000: 
                    self.FFTScr.ticksX = [(1, "10"), (2, "100"), (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                elif self.FFTScr.xTopLim < 10000:
                    self.FFTScr.ticksX = [(1, "10"), (2, "100"), (3, "1000"), (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                elif self.FFTScr.xTopLim < 100000:
                    self.FFTScr.ticksX = [(1, "10"), (2, "100"), (3, "1000"), (4, "10000"), (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                else:
                    self.FFTScr.ticksX = [(1, "10"), (2, "100"), (3, "1000"), (4, "10000"), (5, "100000"), (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                
                self.FFTScr.setXRange(1, math.log10(self.FFTScr.xTopLim))
                self.FFTScr.getPlotItem().getAxis('bottom').setTicks([self.FFTScr.ticksX, minor_ticks])
            
            elif self.FFTScr.xBotLim >= 500000:
                self.FFT_scr2.page1.x_botLim_LE.setText("500000")
                self.FFTScr.ticksX = [(math.log10(500000), "500000")]
                self.FFTScr.setXRange(4, 6) 
                self.FFTScr.getPlotItem().getAxis('bottom').setTicks([self.FFTScr.ticksX, minor_ticks])

            else:
                self.FFT_scr2.page1.x_botLim_LE.setText(f"{self.FFTScr.xBotLim:.0f}")
                if self.FFTScr.xBotLim < 100:
                    if self.FFTScr.xTopLim < 100:     
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                        
                    elif self.FFTScr.xTopLim < 1000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"),
                                            (2, "100"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                    elif self.FFTScr.xTopLim < 10000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"),
                                            (2, "100"),
                                            (3, "1000"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                        
                    elif self.FFTScr.xTopLim < 100000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"),
                                            (2, "100"),
                                            (3, "1000"),
                                            (4, "10000"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                    
                    else:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"),
                                            (2, "100"),
                                            (3, "1000"),
                                            (4, "10000"), 
                                            (5, "100000"),
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                        
                elif self.FFTScr.xBotLim < 1000:
                    if self.FFTScr.xTopLim < 1000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                        
                    elif self.FFTScr.xTopLim < 10000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"),
                                            (3, "1000"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                        
                    elif self.FFTScr.xTopLim < 100000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"),
                                            (3, "1000"),
                                            (4, "10000"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                    
                    else:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"),
                                            (3, "1000"),
                                            (4, "10000"), 
                                            (5, "100000"),
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                        
                elif self.FFTScr.xBotLim < 10000:
                    if self.FFTScr.xTopLim < 10000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                        
                        
                    elif self.FFTScr.xTopLim < 100000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"),
                                            (4, "10000"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                    
                    else:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"),
                                            (4, "10000"), 
                                            (5, "100000"),
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                    
                
                elif self.FFTScr.xBotLim < 100000:
                    if self.FFTScr.xTopLim < 100000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"),
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                    
                    else:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"),
                                            (5, "100000"),
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                    
                    
                else: #500000
                    self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"),
                                        (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                    self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                self.FFTScr.getPlotItem().getAxis('bottom').setTicks([self.FFTScr.ticksX, minor_ticks])

    except ValueError:
        self.FFT_scr2.page1.x_botLim_LE.setText("10")
        if self.FFTScr.xTopLim < 100: 
            self.FFTScr.ticksX = [(1, "10"), (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
        elif self.FFTScr.xTopLim < 1000: 
            self.FFTScr.ticksX = [(1, "10"), (2, "100"), (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
        elif self.FFTScr.xTopLim < 10000:
            self.FFTScr.ticksX = [(1, "10"), (2, "100"), (3, "1000"), (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
        elif self.FFTScr.xTopLim < 100000:
            self.FFTScr.ticksX = [(1, "10"), (2, "100"), (3, "1000"), (4, "10000"), (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
        else:
            self.FFTScr.ticksX = [(1, "10"), (2, "100"), (3, "1000"), (4, "10000"), (5, "100000"), (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
        self.FFTScr.setXRange(1, math.log10(self.FFTScr.xTopLim))
        self.FFTScr.getPlotItem().getAxis('bottom').setTicks([self.FFTScr.ticksX, minor_ticks])

def FFT_xTopLimLE_Changed(self):
    text = self.FFT_scr2.page1.x_topLim_LE.text()

    try:
        minor_ticks = []
        for decade in range(1, 6):  
            for k in range(2, 10):
                pos = decade + math.log10(k)
                minor_ticks.append((pos, "")) 
                
        self.FFTScr.xTopLim = float(text) 
        if self.FFTScr.xTopLim <= self.FFTScr.xBotLim:
            self.FFTScr.xTopLim = self.FFTScr.xBotLim
            self.FFT_scr2.page1.x_topLim_LE.setText(f"{self.FFTScr.xTopLim:.0f}")
            self.FFTScr.ticksX = [(math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
            self.FFTScr.setXRange(self.FFTScr.xTopLim, self.FFTScr.xTopLim)

        else:
            if self.FFTScr.xTopLim >= 500000:
                self.FFTScr.xTopLim = 500000
                self.FFT_scr2.page1.x_topLim_LE.setText("500000")

                if self.FFTScr.xBotLim < 100:
                    self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (2, "100"), (3, "1000"), (4, "10000"), 
                                            (5, "100000"), (math.log10(500000), "500000")]
                    self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                    
                elif self.FFTScr.xBotLim < 1000:
                    self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (3, "1000"), (4, "10000"), 
                                            (5, "100000"), (math.log10(500000), "500000")]
                    self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                    
                elif self.FFTScr.xBotLim < 10000:
                    self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (4, "10000"), 
                                            (5, "100000"), (math.log10(500000), "500000")]
                    self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                    
                elif self.FFTScr.xBotLim < 100000:
                    self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), 
                                            (5, "100000"), (math.log10(500000), "500000")]
                    self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                    
                elif self.FFTScr.xBotLim < 500000:
                    self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), 
                                          (math.log10(500000), "500000")]
                    self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                else:
                    self.FFTScr.ticksX = [(math.log10(500000), "500000")]
                    self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
            
            elif self.FFTScr.xTopLim < 10:
                self.FFTScr.xTopLim = 10
                self.FFT_scr2.page1.x_topLim_LE.setText("10")
                self.FFTScr.ticksX = [(1, "10")]
                self.FFTScr.setXRange(0.8, 1.2)
                self.FFTScr.getPlotItem().getAxis('bottom').setTicks([self.FFTScr.ticksX, minor_ticks])

            else:
                self.FFT_scr2.page1.x_topLim_LE.setText(f"{self.FFTScr.xTopLim:.0f}")
                if self.FFTScr.xTopLim > 100000:
                    if self.FFTScr.xBotLim < 100:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (2, "100"), (3, "1000"), (4, "10000"), (5, "100000"),
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                    elif self.FFTScr.xBotLim < 1000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (3, "1000"), (4, "10000"), (5, "100000"),
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                    elif self.FFTScr.xBotLim < 10000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (4, "10000"), (5, "100000"),
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                    elif self.FFTScr.xBotLim < 10000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (4, "10000"), (5, "100000"),
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                    elif self.FFTScr.xBotLim < 100000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (5, "100000"),
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                    else:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"),
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                elif self.FFTScr.xTopLim > 10000:
                    if self.FFTScr.xBotLim < 100:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (2, "100"), (3, "1000"), (4, "10000"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                    elif self.FFTScr.xBotLim < 1000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (3, "1000"), (4, "10000"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                    elif self.FFTScr.xBotLim < 10000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (4, "10000"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                    elif self.FFTScr.xBotLim < 10000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (4, "10000"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                    elif self.FFTScr.xBotLim < 100000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"),
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                
                elif self.FFTScr.xTopLim > 1000:
                    if self.FFTScr.xBotLim < 100:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (2, "100"), (3, "1000"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                    elif self.FFTScr.xBotLim < 1000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (3, "1000"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                    elif self.FFTScr.xBotLim < 10000:
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                
                elif self.FFTScr.xTopLim > 100:
                    if self.FFTScr.xBotLim < 100:
                        
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (2, "100"),  
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                    elif self.FFTScr.xBotLim < 1000:
                        
                        self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                        self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
                        

                else:
                    self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), 
                                            (math.log10(self.FFTScr.xTopLim), f"{self.FFTScr.xTopLim:.0f}")]
                    self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))

                self.FFTScr.getPlotItem().getAxis('bottom').setTicks([self.FFTScr.ticksX, minor_ticks])
                

    except ValueError:
        self.FFTScr.xTopLim = 500000
        self.FFT_scr2.page1.x_topLim_LE.setText("500000")

        if self.FFTScr.xBotLim < 100:
            self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (2, "100"), (3, "1000"), (4, "10000"), 
                                    (5, "100000"), (math.log10(500000), "500000")]
            self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
            
        elif self.FFTScr.xBotLim < 1000:
            self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (3, "1000"), (4, "10000"), 
                                    (5, "100000"), (math.log10(500000), "500000")]
            self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
            
        elif self.FFTScr.xBotLim < 10000:
            self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), (4, "10000"), 
                                    (5, "100000"), (math.log10(500000), "500000")]
            self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
            
        elif self.FFTScr.xBotLim < 100000:
            self.FFTScr.ticksX = [(math.log10(self.FFTScr.xBotLim), f"{self.FFTScr.xBotLim:.0f}"), 
                                    (5, "100000"), (math.log10(500000), "500000")]
            self.FFTScr.setXRange(math.log10(self.FFTScr.xBotLim), math.log10(self.FFTScr.xTopLim))
            
        else:
            self.FFTScr.ticksX = [(5, "100000"), (math.log10(500000), "500000")]
            self.FFTScr.setXRange(4.9, math.log10(600000))

def FFT_yBotLimLE_Changed(self):
    try:
        text = self.FFT_scr2.page1.y_botLim_LE.text()
        self.FFTScr.yBotLim = float(text)

        if self.FFTScr.yBotLim < -1000:
            self.FFTScr.yBotLim = -1000
        
        elif self.FFTScr.yBotLim > 1000:
            self.FFTScr.yBotLim = 1000

        self.FFTScr.setYRange(self.FFTScr.yBotLim, self.FFTScr.yTopLim)

    except ValueError:
        self.FFTScr.yBotLim = -60
        self.FFTScr.setYRange(self.FFTScr.yBotLim, self.FFTScr.yTopLim)

def FFT_yTopLimLE_Changed(self):
    try:
        text = self.FFT_scr2.page1.y_topLim_LE.text()
        self.FFTScr.yTopLim = float(text)

        if self.FFTScr.yTopLim < -1000:
            self.FFTScr.yTopLim = -1000
        
        elif self.FFTScr.yTopLim > 1000:
            self.FFTScr.yTopLim = 1000

        self.FFTScr.setYRange(self.FFTScr.yBotLim, self.FFTScr.yTopLim)

    except ValueError:
        self.FFTScr.yTopLim = 30
        self.FFTScr.setYRange(self.FFTScr.yBotLim, self.FFTScr.yTopLim)

def FFT_restoreDefault(self):
    self.FFT_scr2.page1.x_botLim_LE.setText("10")
    self.FFTScr.xBotLim = float(self.FFT_scr2.page1.x_botLim_LE.text())
    self.FFT_scr2.page1.x_topLim_LE.setText("250000")
    self.FFTScr.xTopLim = float(self.FFT_scr2.page1.x_topLim_LE.text())
    self.FFT_scr2.page1.y_botLim_LE.setText("-65")
    self.FFTScr.yBotLim = float(self.FFT_scr2.page1.y_botLim_LE.text())
    self.FFT_scr2.page1.y_topLim_LE.setText("15")
    self.FFTScr.yTopLim = float(self.FFT_scr2.page1.y_topLim_LE.text())

    self.FFT_scr2.page1.x_botLim_LE.returnPressed.emit()
    self.FFT_scr2.page1.x_topLim_LE.returnPressed.emit()
    self.FFT_scr2.page1.y_botLim_LE.returnPressed.emit()
    self.FFT_scr2.page1.y_topLim_LE.returnPressed.emit()