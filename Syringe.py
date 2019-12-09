import tkinter as tk

class syringe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.model = canvas.create_rectangle(10, 10, 150, 450, width=4)
        self.line1 = canvas.create_line(70, 80, 150, 80, width=3)
        self.line2 = canvas.create_line(70, 160, 150, 160, width=3)
        self.line3 = canvas.create_line(70, 240, 150, 240, width=3)
        self.line4 = canvas.create_line(70, 320, 150, 320, width=3)
        self.line5 = canvas.create_line(70, 400, 150, 400, width=3)

class pump:
    def __init__(self, canvas, limit, limit2):
        self.pumpSpeed = 2
        
        self.canvas = canvas
        self.limit = limit
        self.limit2 = limit2
        self.background = canvas.create_rectangle(10, 10, 150, 450, width=4, fill="white")
        self.head = canvas.create_rectangle(10, 10, 150, 30, width=1, fill="white")
        self.arm = canvas.create_rectangle(70, 30, 90, 454, width=1, fill="white")
        self.handle = canvas.create_rectangle(10, 454, 150, 474, width=1, fill="white")

    def move(self):
        if (not(self.canvas.coords(self.head) == self.canvas.coords(self.limit))):
            pumpMove = self.canvas.after(10,self.move)
            self.canvas.move(self.head, 0, self.pumpSpeed)
            self.canvas.move(self.arm, 0, self.pumpSpeed)
            self.canvas.move(self.handle, 0, self.pumpSpeed)
            startPosition = self.canvas.coords(self.head)
            endPosition = self.canvas.coords(self.limit)
            if (startPosition == endPosition):
                self.canvas.after_cancel(pumpMove)
        else:
            pass
    
    def reset(self):
        if (not(self.canvas.coords(self.head) == self.canvas.coords(self.limit2))):
            pumpMove = self.canvas.after(10,self.reset)
            self.canvas.move(self.head, 0, -self.pumpSpeed)
            self.canvas.move(self.arm, 0, -self.pumpSpeed)
            self.canvas.move(self.handle, 0, -self.pumpSpeed)
            startPosition = self.canvas.coords(self.head)
            endPosition = self.canvas.coords(self.limit2)
            if (startPosition == endPosition):
                self.canvas.after_cancel(pumpMove)
        else:
            pass
    
    def getHead(self):
        headPosition = self.canvas.coords(self.head)
        return headPosition

    def getLimit(self):
        limitPosition = self.canvas.coords(self.limit)
        return limitPosition

    def getLimit2(self):
        limit2Position = self.canvas.coords(self.limit2)
        return limit2Position

    def setPumpSpeed(self, speed):
        self.pumpSpeed = speed