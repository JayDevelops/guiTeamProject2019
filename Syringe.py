import tkinter as tk

class syringe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.model = canvas.create_rectangle(10, 10, 150, 550, fill="#121212")
