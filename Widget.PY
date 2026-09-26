import tkinter as tk
from datetime import datetime


def handle_check_in():
  # Read the typed name from the Entry widget
  name = name_entry.get().strip()

  # Get current date or workshop date
  workshop_date = datetime.now().strftime("%B %d, %Y")

  # Create the multi-line welcome message
  if name:
    message = (
        f"Hello, {name}!\nWelcome to the Python & Tkinter"
        f" Workshop.\nDate: {workshop_date}\nWe are glad to have you here!"
    )
  else:
    message = (
        f"Hello, Guest!\nWelcome to the Python & Tkinter"
        f" Workshop.\nDate: {workshop_date}\nPlease enter your name."
    )

  # Update the Text widget (enable state, insert text, disable state)
  output_text.config(state=tk.NORMAL)
  output_text.delete("1.0", tk.END)
  output_text.insert(tk.END, message)
  output_text.config(state=tk.DISABLED)


# Create the main window
root = tk.Tk()
root.title("Workshop Participant Greeting")
root.geometry("400x350")

# Instruction Label
instruction_label = tk.Label(
    root, text="Please enter your name below:", font=("Arial", 11)
)
instruction_label.pack(pady=10)

# Entry Widget for Name
name_entry = tk.Entry(root, font=("Arial", 12), width=25)
name_entry.pack(pady=5)

# Check In Button
check_in_button = tk.Button(
    root,
    text="Check In",
    command=handle_check_in,
    font=("Arial", 11),
    bg="#4CAF50",
    fg="white",
)
check_in_button.pack(pady=10)

# Output Text Widget for multi-line message
output_text = tk.Text(root, height=6, width=35, font=("Arial", 10))
output_text.pack(pady=10)
output_text.config(state=tk.DISABLED)  # Make it read-only by default

# Run the application
root.mainloop()
