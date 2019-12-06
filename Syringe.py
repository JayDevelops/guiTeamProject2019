import math
class Syringe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.model = canvas.create_rectangle(10, 10, 150, 400, width=4)
        self.line1 = canvas.create_line(70, 80, 150, 80, width=3)
        self.line2 = canvas.create_line(70, 160, 150, 160, width=3)
        self.line3 = canvas.create_line(70, 240, 150, 240, width=3)
        self.line4 = canvas.create_line(70, 320, 150, 320, width=3)

class Pump:
    def __init__(self, canvas):
        # Initializes the canvas object here
        self.canvas = canvas
        self.head = canvas.create_rectangle(10, 10, 150, 30, width=1, fill="white")

def calculateDistance(firstXPoint, secondXPoint, firstYPoint, secondYPoint):
    xOne = firstXPoint
    xTwo = secondXPoint

    yOne = firstYPoint
    yTwo = secondXPoint
    firstMath = ((xTwo - xOne)**2) + ((yTwo - yOne)**2)
    distance = math.sqrt(firstMath)
    roundedDistance = round(distance, 2)
    print(roundedDistance)

calculateDistance(8, 15, 10, 12)
