import tkinter as tk

class syringe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.model = canvas.create_rectangle(10, 10, 150, 400, width=4)
        self.line1 = canvas.create_line(70, 80, 150, 80, width=3)
        self.line2 = canvas.create_line(70, 160, 150, 160, width=3)
        self.line3 = canvas.create_line(70, 240, 150, 240, width=3)
        self.line4 = canvas.create_line(70, 320, 150, 320, width=3)

class pump:
    def __init__(self, canvas, limit):
        self.canvas = canvas
        self.limit = limit
        self.head = canvas.create_rectangle(10, 10, 150, 30, width=1, fill="white")
        self.arm = canvas.create_rectangle(70, 30, 90, 404, width=1, fill="white")
        self.handle = canvas.create_rectangle(10, 404, 150, 424, width=1, fill="white")
    def move(self):
        if (not(self.canvas.coords(self.head) == self.canvas.coords(self.limit))):
            pumpMove = self.canvas.after(10,self.move)
            self.canvas.move(self.head, 0, 5)
            self.canvas.move(self.arm, 0, 5)
            self.canvas.move(self.handle, 0, 5)
            startPosition = self.canvas.coords(self.head)
            endPosition = self.canvas.coords(self.limit)
            if (startPosition == endPosition):
                self.canvas.after_cancel(pumpMove)
        else:
            pass

