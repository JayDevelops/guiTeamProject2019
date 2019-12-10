import tkinter as tk
import Syringe

class liquid:
    def __init__(self, canvas, pump):
        self.y = 0
        self.liquidSpeed = 2

        self.canvas = canvas
        self.pump = pump
        self.model = canvas.create_rectangle(10, 10, 150, 10, fill="#ffffff", width=0)

    def move(self):
        if(not(self.pump.getHead() == self.pump.getLimit())):
            liquidMove = self.canvas.after(10, self.move)
            x0, y0, x1, y1 = self.canvas.coords(self.model)
            y1 += self.liquidSpeed
            self.canvas.coords(self.model, x0, y0, x1, y1)
            if(self.pump.getHead() == self.pump.getLimit()):
                self.canvas.after_cancel(liquidMove)
        else:
            pass

    def reset(self):
        if(not(self.pump.getHead() == self.pump.getLimit2())):
            liquidMove = self.canvas.after(10, self.reset)
            x0, y0, x1, y1 = self.canvas.coords(self.model)
            y1 -= self.liquidSpeed
            self.canvas.coords(self.model, x0, y0, x1, y1)
            if(self.pump.getHead() == self.pump.getLimit2()):
                self.canvas.after_cancel(liquidMove)
        else:
            pass

    def setLiquidSpeed(self, speed):
        self.liquidSpeed = speed

    def setLiquidColor(self, color):
        self.canvas.itemconfig(self.model, fill=color)

    def changeSpeed(self, newSpeed):
        self.liquidSpeed = newSpeed
