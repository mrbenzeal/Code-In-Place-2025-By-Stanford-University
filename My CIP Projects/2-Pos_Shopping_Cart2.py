import tkinter as tk
from tkinter import messagebox
import random

# --- Product Inventory ---
products = {
    "Apple": 100,
    "Banana": 50,
    "Orange": 70,
    "Milk": 200,
    "Bread": 150,
    "Eggs": 30
}

# --- Daily Special ---
daily_special = random.choice(list(products.keys()))
discount_rate = 0.2  # 20% off

# --- POS Application ---
class POSApp:
    def __init__(self, master):
        self.master = master
        master.title("Python POS System")

        self.cart = []

        # Input fields
        self.item_label = tk.Label(master, text="Item Name:")
        self.item_label.grid(row=0, column=0)
        self.item_entry = tk.Entry(master)
        self.item_entry.grid(row=0, column=1)

        self.qty_label = tk.Label(master, text="Quantity:")
        self.qty_label.grid(row=1, column=0)
        self.qty_entry = tk.Entry(master)
        self.qty_entry.grid(row=1, column=1)

        self.add_button = tk.Button(master, text="Add to Cart", command=self.add_to_cart)
        self.add_button.grid(row=2, column=0, columnspan=2)

        # Display area
        self.cart_display = tk.Text(master, height=15, width=50)
        self.cart_display.grid(row=3, column=0, columnspan=2)

        # Buttons
        self.total_button = tk.Button(master, text="Checkout", command=self.checkout)
        self.total_button.grid(row=4, column=0)

        self.clear_button = tk.Button(master, text="Clear Cart", command=self.clear_cart)
        self.clear_button.grid(row=4, column=1)

        self.update_cart_display("Today's Special: {} ({}% OFF!)\n".format(
            daily_special, int(discount_rate * 100)))

    def add_to_cart(self):
        item = self.item_entry.get().strip().title()
        qty = self.qty_entry.get().strip()

        if not item or not qty:
            messagebox.showwarning("Input Error", "Please enter both item name and quantity.")
            return

        if item not in products:
            messagebox.showwarning("Product Not Found", f"{item} is not available in inventory.")
            return

        try:
            qty = int(qty)
            if qty <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Input Error", "Quantity must be a positive integer.")
            return

        price = products[item]
        if item == daily_special:
            price = int(price * (1 - discount_rate))

        self.cart.append((item, price, qty))
        self.update_cart_display(f"Added: {item} x {qty} = ₦{price * qty}\n")

        self.item_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)

    def update_cart_display(self, text):
        self.cart_display.insert(tk.END, text)
        self.cart_display.see(tk.END)

    def checkout(self):
        if not self.cart:
            messagebox.showinfo("Cart Empty", "Please add items to the cart first.")
            return

        total = sum(price * qty for _, price, qty in self.cart)
        summary = "\n".join([f"{item} x {qty} = ₦{price * qty}" for item, price, qty in self.cart])
        summary += f"\n\nTotal Amount: ₦{total}"

        messagebox.showinfo("Checkout Summary", summary)
        self.clear_cart()

    def clear_cart(self):
        self.cart = []
        self.cart_display.delete(1.0, tk.END)
        self.update_cart_display("Cart cleared.\n")
        self.update_cart_display("Today's Special: {} ({}% OFF!)\n".format(
            daily_special, int(discount_rate * 100)))


if __name__ == "__main__":
    root = tk.Tk()
    app = POSApp(root)
    root.mainloop()
