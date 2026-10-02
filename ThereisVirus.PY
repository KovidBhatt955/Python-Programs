# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup tkinter window
root = Tk()
root.geometry("500x500")

# Function for Displaying Warning Message
# This will be called one the button is clicked
# messagebox.showwarning("Window Name", "Text to be Displayed")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found. Now time to explode while scanning")

# Adding Button Widget to Window
button = Button(root, text="Scan for Virus which is Virusing", command=msg)
button.place(x=40, y=80)

# Entering the main loop
root.mainloop()