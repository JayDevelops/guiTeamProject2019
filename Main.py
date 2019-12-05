import tkinter as tk
import time
import Syringe

# Simple function that switches the button menu from Liqud buttons and Brake buttons (command located in switchButton)
def switchB():
    brakeButtonFrame.tkraise()

def switchL():
    liquidButtonFrame.tkraise()

# mainWindow configurations
mainWindow = tk.Tk()    # initialized window in mainWindow variable
mainWindow.title("Speed Wheel")     # named the program Speed Wheel 
mainWindow.configure(background="#121212")      # made mainWindow have a black background
mainWindow.geometry("1280x720") # This sets the window to be 720p
mainWindow.resizable(0, 0) # This makes the window not resizable 

# mainMenu configurations
mainMenu = tk.Menu (mainWindow)     # set a new menu tab named mainMenu to mainWindow
mainWindow.config(menu=mainMenu)    # added the mainMenu to the mainWindow
optionMenu = tk.Menu (mainMenu)     # added another a menu in the mainMenu stored in optionMenu (This works a lot like frames)
mainMenu.add_cascade(label="Options", menu=optionMenu)      # adds button group called Options in mainMenu
optionMenu.add_command(label="Option 1")        # adds a menu button called Option 1 (this can be changed later)
optionMenu.add_command(label="Option 2")        # adds a menu button called Option 2 (this can be changed later)
optionMenu.add_separator()      # this adds a line separator to the option menu
optionMenu.add_command(label='Exit', command=mainWindow.destroy)        # This adds a button in the menu that exits the program


# Frame configurations

syringeFrame = tk.Frame (mainWindow)    # This frame contains the syringe model
syringeFrame.pack(side=tk.RIGHT)    # This unpacks the main syringe frame

interactFrame = tk.Frame(mainWindow)    # This frame is a parent frame and contains the buttons and the wheel model
interactFrame.pack(side=tk.RIGHT)   # This unpacks the interact parent frame

buttonFrame = tk.Frame (interactFrame)  # This frame is a child frame and it contains the buttons
buttonFrame.pack()  # This unpacks the button frame

brakeButtonFrame = tk.Frame (buttonFrame)   # This frame contains the buttons for the brake feature
brakeButtonFrame.grid(row=0, column=0)  # This unpacks the brake button frame 

liquidButtonFrame = tk.Frame (buttonFrame)  # This frame contains the buttons for the iquids
liquidButtonFrame.grid(row=0, column=0) # This unpacks the liquid button frame


wheelFrame = tk.Frame (interactFrame)   # This frame contains the wheel model
wheelFrame.pack()   # This unpacks the wheel model frame

syringeCanvas = tk.Canvas(syringeFrame, height=700, width=400, bd=0)     # This creates a new canvas that contains the syringe model
syringeCanvas.pack()        # This unpacks the syringe model

wheelCanvas = tk.Canvas (wheelFrame, height=650, width=900)
wheelCanvas.pack()


# This is the limit that the pump will go up to but not pass
backLimit = syringeCanvas.create_rectangle(10, 365, 150, 385, width=1, outline= "white", fill="white")
frontLimit = syringeCanvas.create_rectangle(10, 10, 150, 30, width=1, outline= "white", fill="white")

# Class properties
pump = Syringe.pump(syringeCanvas, backLimit, frontLimit)   # This creates a pump object and stores it into pump 

syringe = Syringe.syringe(syringeCanvas)      # This calls the syringe class through the Syringe.py file and creates the syringe model in the syringeCanvas


# user defined functions for the tkinter buttons
def pumpMove():
    pump.move()

def reset():
    pump.reset()

# limit cordinate [10.0, 365.0, 150.0, 385.0]

# Liquid Button Properties
pumpResetButtonL = tk.Button (liquidButtonFrame, width=10, text="Reset", command=reset)
pumpResetButtonL.pack(side=tk.LEFT)

pumpButtonL = tk.Button (liquidButtonFrame, width=10, text="Pump", command=pumpMove)
pumpButtonL.pack(side=tk.LEFT)

syrupButton = tk.Button (liquidButtonFrame, width=10, text="Syrup")
syrupButton.pack(side=tk.LEFT)

oilButton = tk.Button (liquidButtonFrame, width=10, text="Motor Oil")
oilButton.pack(side=tk.LEFT)

waterButton = tk.Button (liquidButtonFrame, width=10, text="Water")
waterButton.pack(side=tk.LEFT)

alcoholButton = tk.Button (liquidButtonFrame, width=10, text="Alcohol")
alcoholButton.pack(side=tk.LEFT)

switchButtonL = tk.Button (liquidButtonFrame, width=10, text="Switch", command=switchB)
switchButtonL.pack(side=tk.LEFT)


# Brake Button Properties
pumpResetButtonB = tk.Button (brakeButtonFrame, width=10, text="Reset", command=reset)
pumpResetButtonB.pack(side=tk.LEFT)

pumpButtonB = tk.Button (brakeButtonFrame, width=10, text="Pump", command=pumpMove)
pumpButtonB.pack(side=tk.LEFT)

sandpaperButton = tk.Button (brakeButtonFrame, width=10, text="Sand Paper")
sandpaperButton.pack(side=tk.LEFT)

towelButton = tk.Button (brakeButtonFrame, width=10, text="Towel")
towelButton.pack(side=tk.LEFT)

spongeButton = tk.Button (brakeButtonFrame, width=10, text="Sponge")
spongeButton.pack(side=tk.LEFT)

foilButton = tk.Button (brakeButtonFrame, width=10, text="Aluminum Foil")
foilButton.pack(side=tk.LEFT)

switchButtonB = tk.Button (brakeButtonFrame, width=10, text="Switch", command=switchL)
switchButtonB.pack(side=tk.LEFT)



mainWindow.mainloop()       # set the mainWindow on the loop