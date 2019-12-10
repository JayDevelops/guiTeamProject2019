import tkinter as tk
import Syringe
import Liquid


# colors for liquids and brake types
oilColor = "#663300"
syrupColor = "#331a00"
waterColor = "#ddffff"
alcoholColor = "#f2f2f2"

sandPaperColor = "#cc2900"
towelColor = "#ffffff"
spongeColor = "#e6e600"
foilColor = "#b3b3b3"


# Speed constants of the liquids
syrupSpeed = 2
oilSpeed = 4
waterSpeed = 6
alcoholSpeed = 8


# Simple function that switches the button menu from Liqud buttons and Brake buttons (command located in switchButton)
def switchB():
    brakeButtonFrame.tkraise()

def switchL():
    liquidButtonFrame.tkraise()


# MainWindow Configurations
mainWindow = tk.Tk()    # Initialized window in mainWindow variable
mainWindow.title("Speed Wheel")     # Named the program Speed Wheel
mainWindow.configure(background="#121212")   # Made mainWindow have a black background
mainWindow.geometry("1280x720")  # This sets the window to be 720p
mainWindow.resizable(0, 0)  # This makes the window not resizable

# mainMenu configurations
mainMenu = tk.Menu(mainWindow)   # Set a new menu tab named mainMenu to mainWindow
mainWindow.config(menu=mainMenu)   # Added the mainMenu to the mainWindow
optionMenu = tk.Menu(mainMenu)    # Added another a menu in the mainMenu stored in optionMenu (This works a lot like frames)
mainMenu.add_cascade(label="Options", menu=optionMenu)    # Adds button group called Options in mainMenu
optionMenu.add_command(label="Option 1")   # Adds a menu button called Option 1 (this can be changed later)
optionMenu.add_command(label="Option 2")   # Adds a menu button called Option 2 (this can be changed later)
optionMenu.add_separator()   # This adds a line separator to the option menu
optionMenu.add_command(label='Exit', command=mainWindow.destroy)    # This adds a button in the menu that exits the program


# Frame configurations
syringeFrame = tk.Frame(mainWindow)    # This frame contains the syringe model
syringeFrame.pack(side=tk.RIGHT)    # This unpacks the main syringe frame

interactFrame = tk.Frame(mainWindow)    # This frame is a parent frame and contains the buttons and the wheel model
interactFrame.pack(side=tk.RIGHT)   # This unpacks the interact parent frame

buttonFrame = tk.Frame(interactFrame)  # This frame is a child frame and it contains the buttons
buttonFrame.pack()  # This unpacks the button frame

brakeButtonFrame = tk.Frame(buttonFrame)   # This frame contains the buttons for the brake feature
brakeButtonFrame.grid(row=0, column=0)  # This unpacks the brake button frame

liquidButtonFrame = tk.Frame(buttonFrame)  # This frame contains the buttons for the iquids
liquidButtonFrame.grid(row=0, column=0)  # This unpacks the liquid button frame


wheelFrame = tk.Frame(interactFrame)   # This frame contains the wheel model
wheelFrame.pack()   # This unpacks the wheel model frame

syringeCanvas = tk.Canvas(syringeFrame, height=700, width=400, bd=0, bg="#121212")   # This creates a new canvas that contains the syringe model
syringeCanvas.pack()   # This unpacks the syringe model

wheelCanvas = tk.Canvas(wheelFrame, height=650, width=900, bg="#121212")
wheelCanvas.pack()


# This is the limit that the pump will go up to but not pass
backLimit = syringeCanvas.create_rectangle(10, 418, 150, 438, width=1, outline="#121212", fill="#121212")
frontLimit = syringeCanvas.create_rectangle(10, 10, 150, 30, width=1, outline="#121212", fill="#121212")

# Class properties

pump = Syringe.pump(syringeCanvas, backLimit, frontLimit)  # This creates a pump object and stores it into pump


liquid = Liquid.liquid(syringeCanvas, pump)


syringe = Syringe.syringe(syringeCanvas)  # This calls the syringe class through the Syringe.py file and creates the syringe model in the syringeCanvas


# User defined functions for the tkinter buttons
def pumpMove():
    pump.move()
    liquid.move()

def reset():
    pump.reset()
    liquid.reset()


# Liquid button functions (chooses the color)
def syrup():
    liquid.setLiquidColor(syrupColor)
    liquid.setLiquidSpeed(syrupSpeed)
    pump.setPumpSpeed(syrupSpeed)

def oil():
    liquid.setLiquidColor(oilColor)
    liquid.setLiquidSpeed(oilSpeed)
    pump.setPumpSpeed(oilSpeed)

def water():
    liquid.setLiquidColor(waterColor)
    liquid.setLiquidSpeed(waterSpeed)
    pump.setPumpSpeed(waterSpeed)

def alcohol():
    liquid.setLiquidColor(alcoholColor)
    liquid.setLiquidSpeed(alcoholSpeed)
    pump.setPumpSpeed(alcoholSpeed)


# limit cordinate [10.0, 365.0, 150.0, 385.0]


# Liquid Button Properties
pumpResetButtonL = tk.Button(liquidButtonFrame, width=10, text="Reset", command=reset)
pumpResetButtonL.pack(side=tk.LEFT)

pumpButtonL = tk.Button(liquidButtonFrame, width=10, text="Pump", command=pumpMove)
pumpButtonL.pack(side=tk.LEFT)

syrupButton = tk.Button(liquidButtonFrame, width=10, text="Syrup", command=syrup)
syrupButton.pack(side=tk.LEFT)

oilButton = tk.Button(liquidButtonFrame, width=10, text="Motor Oil", command=oil)
oilButton.pack(side=tk.LEFT)

waterButton = tk.Button(liquidButtonFrame, width=10, text="Water", command=water)
waterButton.pack(side=tk.LEFT)

alcoholButton = tk.Button(liquidButtonFrame, width=10, text="Alcohol", command=alcohol)
alcoholButton.pack(side=tk.LEFT)

switchButtonL = tk.Button(liquidButtonFrame, width=10, text="Switch", command=switchB)
switchButtonL.pack(side=tk.LEFT)


# TODO: Brakers Functions and Brake Button Properties

# Brakers Functions here
def sandPaperBraker():
    liquid.changeSpeed(-2)

def towelBraker():
    liquid.changeSpeed(-4)

def spongeBraker():
    liquid.changeSpeed(-6)

def aluminumBraker():
    liquid.changeSpeed(-8)

pumpResetButtonB = tk.Button(brakeButtonFrame, width=10, text="Reset", command=reset)
pumpResetButtonB.pack(side=tk.LEFT)

pumpButtonB = tk.Button(brakeButtonFrame, width=10, text="Pump", command=pumpMove)
pumpButtonB.pack(side=tk.LEFT)

sandpaperButton = tk.Button(brakeButtonFrame, width=10, text="Sand Paper", command=sandPaperBraker)
sandpaperButton.pack(side=tk.LEFT)

towelButton = tk.Button(brakeButtonFrame, width=10, text="Towel", command=towelBraker)
towelButton.pack(side=tk.LEFT)

spongeButton = tk.Button(brakeButtonFrame, width=10, text="Sponge", command=spongeBraker)
spongeButton.pack(side=tk.LEFT)

foilButton = tk.Button(brakeButtonFrame, width=10, text="Aluminum Foil", command=aluminumBraker)
foilButton.pack(side=tk.LEFT)

switchButtonB = tk.Button(brakeButtonFrame, width=10, text="Switch", command=switchL)
switchButtonB.pack(side=tk.LEFT)


mainWindow.mainloop()     # Set the mainWindow on the loop
