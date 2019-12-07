import tkinter as tk
import Syringe

class liquid:
    def __init__(self, canvas, color, pump):
        self.y = 0
        
        self.canvas = canvas
        self.color = color
        self.pump = pump
        self.model = canvas.create_rectangle(10, 10, 150, 10, fill=self.color, width=0)

    def move(self):
        if(not(self.pump.getHead() == self.pump.getLimit())):
            liquidMove = self.canvas.after(10, self.move)
            x0, y0, x1, y1 = self.canvas.coords(self.model)
            y1 += 2
            self.canvas.coords(self.model, x0, y0, x1, y1)
            if(self.pump.getHead() == self.pump.getLimit()):
                self.canvas.after_cancel(liquidMove)
        else:
            pass

    def reset(self):
        if(not(self.pump.getHead() == self.pump.getLimit2())):
            liquidMove = self.canvas.after(10, self.reset)
            x0, y0, x1, y1 = self.canvas.coords(self.model)
            y1 -= 2
            self.canvas.coords(self.model, x0, y0, x1, y1)
            if(self.pump.getHead() == self.pump.getLimit2()):
                self.canvas.after_cancel(liquidMove)
        else:
            pass
        