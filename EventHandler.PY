# Import necessary libraries
from tkinter import *

# Create window
window = Tk()
window.title("Event Handler")
window.geometry("100x100")

# Event handler for Keypresses
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

# Event Handler for button click
def handle_click(event):
    print("\nThe button was Clicked! me go boom boom!!!")

button = Button(text="Click me!")
button.pack()

# Bind click event to handle_click()'
button.bind("<Button-1>", handle_click)

# Start the GUI event loop
window.mainloop()