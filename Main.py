import tkinter as tk

# mainWindow configurations
mainWindow = tk.Tk()    # initialized window in mainWindow variable
mainWindow.title("Speed Wheel")     # named the program Speed Wheel 
mainWindow.configure(background="#121212")      # made mainWindow have a black background


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
buttonFrame = tk.Frame (mainWindow)     # this adds a frame that contains the liquid and break type option buttons
buttonFrame.pack()      # This unpacked the buttonFrame

wheelFrame = tk.Frame (mainWindow)
wheelFrame.pack()

syringeFrame = tk.Frame (mainWindow)        #this is the frame that will contain the syringe model
syringeFrame.pack(anchor=tk.E)     # This unpacks the syringeFrame

mainWindow.mainloop()       # set the mainWindow on the loop