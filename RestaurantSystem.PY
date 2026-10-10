# Import tkinter for GUI and ttk for improved widgets
import tkinter as tk
from tkinter import ttk, messagebox
import os
from PIL import Image, ImageTk


# Define the RestaurantOrderMangementApp class
class RestaurantOrderMangement:
    # Initialize the application
    def __init__(self, root):
        self.root = root # The main window of the app
        self.root.title("Restaurant Management App") # Set the title of the window

        # A dictionary to store the new items and their prices
        self.menu_items = {"FRIES MEAL": 2,
                           "LUNCH MEAL": 2,
                           "BURGER MEAL": 3,
                           "PIZZA MEAL": 4,
                           "CHEESE BURGER": 2.5,
                           "DRINKS": 1
        }

        self.exchange_rate = 96 # E xchange rate for currency conversion

        self.setup_background(root) # Set up the background image


        # Create a frame to hold the widgets
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Heading label
        ttk.Label (
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels = {}   # To store references to menu item labels

        self.menu_quantities = {}   # To store references to quantity entry widget

        # Create labels and entry widgets for each new menu items
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item}  (${price}):",
                font=("Arial", 12)
            )
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        # Curreny Selection
        self.currency_var = tk.StringVar()
        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(
            row=len(self.menu_items) + 1,
            column=0,
            padx=10,
            pady=5
        )

        # Dropdown for currency selection
        curreny_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="Readonly",
            width=18,
            values=("USD", "INR")
        )
        curreny_dropdown.grid(
            row=len(self.menu_items) + 1,
            column=1,
            padx=10,
            pady=5
        )
        curreny_dropdown.current(0)  # Set default currency
        self.currency_var.trace("w", self.update_menu_prices)

        # Button to place the order
        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )
        order_button.grid(
            row=len(self.menu_items) + 2,
            columnspan=3,
            padx=10,
            pady=10
        )

    # Method to set up the background image
    def setup_background(self, root):

                    bg_width, bg_height = 800, 600

                    image_path = os.path.join(
                        os.path.dirname(os.path.abspath(__file__)),
                        "terrace-graden.jpg"
                    )

                    if not os.path.exists(image_path):
                        messagebox.showerror(
                            "Image Error",
                            f"Image not found:\n{image_path}"
                        )
                        return

                    # Open and resize the image
                    image = Image.open(terrace-garden.jpg)
                    image = image.resize((bg_width, bg_height))

                    self.background_image = ImageTk.PhotoImage(image)

                    # Create the background canvas
                    canvas = tk.Canvas(
                        root,
                        width=bg_width,
                        height=bg_height,
                        highlightthickness=0
                    )
                    canvas.pack(fill="both", expand=True)

                    canvas.create_image(
                        0, 0,
                        anchor=tk.NW,
                        image=self.background_image
                    )

                    # Keep the canvas behind other widgets
                    canvas.lower()


    # Method to update the menu prices based on the selected currency
    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price}):")

    # Method to place an order
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost

                if quantity > 0:
                    order_summary += (
                        f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
                    )

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")

# Main block to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderMangement(root)
    root.geometry("800x600")  # Set the size of the window
    root.mainloop()           # Start the GUI loop