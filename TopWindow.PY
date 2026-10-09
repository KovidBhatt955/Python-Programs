# Import necessary libraries
from tkinter import *

# Setting up main window
root = Tk()
root.geometry("400x300")
root.title("main")

# Function to open New (Top Level) Window
def top_win():
    # Setting up Top Window
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    # Adding a label widget to Top Window
    l2 = Label(top, text="This is toplevel window")
    l2.pack()

    top.mainloop()

# Adding a label and button Widget to Root (Main) Window
l = Label(root, text="This is a root window")
btn = Button(root, text="Click here to open another window", command=top_win)

# Arranging widgets
l.pack()
btn.pack()

root.mainloop()