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
            y1 += 5
            self.canvas.coords(self.model, x0, y0, x1, y1)
            if(self.pump.getHead() == self.pump.getLimit()):
                self.canvas.after_cancel(liquidMove)
        else:
            pass

    def reset(self):
        if(not(self.pump.getHead() == self.pump.getLimit2())):
            liquidMove = self.canvas.after(10, self.reset)
            x0, y0, x1, y1 = self.canvas.coords(self.model)
            y1 -= 5
            self.canvas.coords(self.model, x0, y0, x1, y1)
            if(self.pump.getHead() == self.pump.getLimit2()):
                self.canvas.after_cancel(liquidMove)
        else:
            pass


# BELOW ARE THE LIQUIDS WHICH TRANSCEND TO THE SLOWEST SPEED

# This is an oil subclass which inherits, methods and init, everything from liquid
class oilLiquid(liquid):
    def move(self):
        # This oil liquid will move faster than liquid
        if(not(self.pump.getHead() == self.pump.getLimit())):
            liquidMove = self.canvas.after(10, self.move)
            x0, y0, x1, y1 = self.canvas.coords(self.model)
            y1 += 8
            if(self.pump.getHead() == self.pump.getLimit()):
                self.canvas.after_cancel(liquidMove)
        else:
            pass

    def reset(self):
        if(not(self.pump.getHead() == self.pump.getLimit2())):
            liquidMove = self.canvas.after(10, self.reset)
            x0, y0, x1, y1 = self.canvas.coords(self.model)
            y1 -= 8
            self.canvas.coords(self.model, x0, y0, x1, y1)
            if(self.pump.getHead() == self.pump.getLimit2()):
                self.canvas.after_cancel(liquidMove)
        else:
            pass

# This is a water subclass which inherits, methods and init, everything from liquid
class waterLiquid(liquid):
    def move(self):
        # This oil liquid will move slower
        if(not(self.pump.getHead() == self.pump.getLimit())):
            liquidMove = self.canvas.after(10, self.move)
            x0, y0, x1, y1 = self.canvas.coords(self.model)
            y1 += 7
            if(self.pump.getHead() == self.pump.getLimit()):
                self.canvas.after_cancel(liquidMove)
        else:
            pass

    def reset(self):
        if(not(self.pump.getHead() == self.pump.getLimit2())):
            liquidMove = self.canvas.after(10, self.reset)
            x0, y0, x1, y1 = self.canvas.coords(self.model)
            y1 -= 7
            self.canvas.coords(self.model, x0, y0, x1, y1)
            if(self.pump.getHead() == self.pump.getLimit2()):
                self.canvas.after_cancel(liquidMove)
        else:
            pass

# This is a water subclass which inherits, methods and init, everything from liquid
class alcoholLiquid(liquid):
    def move(self):
        # This oil liquid will move slower
        if(not(self.pump.getHead() == self.pump.getLimit())):
            liquidMove = self.canvas.after(10, self.move)
            x0, y0, x1, y1 = self.canvas.coords(self.model)
            y1 += 6
            if(self.pump.getHead() == self.pump.getLimit()):
                self.canvas.after_cancel(liquidMove)
        else:
            pass

    def reset(self):
        if(not(self.pump.getHead() == self.pump.getLimit2())):
            liquidMove = self.canvas.after(10, self.reset)
            x0, y0, x1, y1 = self.canvas.coords(self.model)
            y1 -= 6
            self.canvas.coords(self.model, x0, y0, x1, y1)
            if(self.pump.getHead() == self.pump.getLimit2()):
                self.canvas.after_cancel(liquidMove)
        else:
            pass


# This is a syrup subclass which inherits everything, methods and init, from liquid
class syrupLiquid(liquid):
    def move(self):
        # This oil liquid will move slower
        if(not(self.pump.getHead() == self.pump.getLimit())):
            liquidMove = self.canvas.after(10, self.move)
            x0, y0, x1, y1 = self.canvas.coords(self.model)
            y1 += 3
            if(self.pump.getHead() == self.pump.getLimit()):
                self.canvas.after_cancel(liquidMove)
        else:
            pass

    def reset(self):
        if(not(self.pump.getHead() == self.pump.getLimit2())):
            liquidMove = self.canvas.after(10, self.reset)
            x0, y0, x1, y1 = self.canvas.coords(self.model)
            y1 -= 3
            self.canvas.coords(self.model, x0, y0, x1, y1)
            if(self.pump.getHead() == self.pump.getLimit2()):
                self.canvas.after_cancel(liquidMove)
        else:
            pass
