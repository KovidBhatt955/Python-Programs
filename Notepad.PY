import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Opens an old letter file and loads its text into the editor."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return  # If user cancels, do nothing
    
    # Clear the current text and insert the content from the file
    text_editor.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_editor.insert(tk.END, text)
        
    root.title(f"Letter Writing Application - {filepath}")

def save_file():
    """Saves the current letter under a new name."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return  # If user cancels, do nothing
    
    # Get all text from the widget and write it to the file
    with open(filepath, "w") as output_file:
        text = text_editor.get("1.0", tk.END)
        output_file.write(text)
        
    root.title(f"Letter Writing Application - {filepath}")

# 1. Create the main window
root = tk.Tk()
root.title("Letter Writing Application")

# 2. Create the widgets
btn_open = tk.Button(root, text="Open Letter", command=open_file)
btn_save = tk.Button(root, text="Save Letter As...", command=save_file)
text_editor = tk.Text(root, wrap="word")

# 3. Use grid() to lay it out
btn_open.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
btn_save.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
text_editor.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# 4. Configure window resizing behavior
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Start the application
root.mainloop()
