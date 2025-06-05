"""
CIP_Section_5 PROJECT
----------------------
File: POS_Shopping_Cart.py
---------------------------
This Point-of-Sale (POS) Shopping Cart System is a solo-friendly, 
interactive Python project using graphics.Canvas and random. 
It simulates a real-world retail checkout experience with product selection 
via buttons or barcode input, a dynamic cart display, stock management, 
discount codes, tax, and payment method selection (cash, card, or transfer). 
Users can clear carts, see visual updates, and receive real-time total cost calculations 
with animation for bulk discounts. 
Receipts are exported with customer names, timestamps, and loyalty points. 
Admin functions include restocking and viewing daily sales reports.
 
The code is modular, well-commented, and designed for educational use 
at an intermediate Python level.
"""

from graphics import Canvas
import random
import os
import time

# Initialize canvas
canvas = Canvas()
canvas.set_canvas_title("Enhanced POS System")
canvas.set_canvas_size(700, 550)

# --- Data Definitions ---

# Products available in the POS
products = {
    "Apple": {"price": 100, "image": "🍎", "stock": 5, "barcode": "111"},
    "Banana": {"price": 50, "image": "🍌", "stock": 5, "barcode": "222"},
    "Orange": {"price": 80, "image": "🍊", "stock": 5, "barcode": "333"}
}

# Store UI button and session states
product_buttons = []
cart = []
total_price = 0
TAX_RATE = 0.05
DISCOUNT_CODES = {"SAVE10": 10, "SAVE20": 20}
user_discount = 0
cart_panel_start_y = 200
DISCOUNT_CHANCE = 0.2
bulk_discount_threshold = 300
bulk_discount = 50

# Button layout constants
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40
START_X = 50
START_Y = 50
GAP_Y = 60

# GUI component references
clear_cart_button = None
checkout_button = None
payment_method = "Cash"
payment_options = ["Cash", "Card", "Transfer"]
selected_payment_button = None
cart_animation_step = 0
customer_name = "Customer"
payment_received = 0
admin_mode = False

# Loyalty and reports
loyalty_points = {}
daily_sales = []

# --- GUI Drawing Functions ---

def draw_buttons():
    """Redraws all interactive buttons and panels"""
    global clear_cart_button, checkout_button, selected_payment_button
    canvas.clear()
    canvas.set_fill_color("lightgray")
    canvas.draw_text("Click a product or scan barcode to add to cart", 80, 20, "15px Arial")

    product_buttons.clear()
    for i, (item, info) in enumerate(products.items()):
        x = START_X
        y = START_Y + i * GAP_Y
        rect = canvas.create_rectangle(x, y, x + BUTTON_WIDTH, y + BUTTON_HEIGHT)
        canvas.set_fill_color("white")
        canvas.fill_rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
        canvas.set_fill_color("black")
        stock = info["stock"]
        canvas.draw_text(f"{info['image']} {item} - ₦{info['price']} ({stock})", x + 5, y + 25, "14px Arial")
        product_buttons.append((rect, item))

    # Draw Clear Cart button
    clear_cart_button = canvas.create_rectangle(250, 50, 350, 90)
    canvas.set_fill_color("red")
    canvas.fill_rect(250, 50, 100, 40)
    canvas.set_fill_color("white")
    canvas.draw_text("Clear Cart", 260, 75, "14px Arial")

    # Draw Checkout button
    checkout_button = canvas.create_rectangle(250, 100, 350, 140)
    canvas.set_fill_color("green")
    canvas.fill_rect(250, 100, 100, 40)
    canvas.set_fill_color("white")
    canvas.draw_text("Checkout", 265, 125, "14px Arial")

    # Show total price
    canvas.set_fill_color("blue")
    canvas.draw_text(f"Total: ₦{total_price:,.2f}", 400, 130, "18px Arial")

    draw_cart_panel()
    draw_payment_selector()


def draw_cart_panel():
    """Displays the list of items and totals in the cart"""
    canvas.set_fill_color("black")
    canvas.draw_text("Cart:", 400, cart_panel_start_y - 20, "16px Arial")
    y = cart_panel_start_y
    cart_summary = {}
    for item, price in cart:
        if item in cart_summary:
            cart_summary[item]["qty"] += 1
            cart_summary[item]["total"] += price
        else:
            cart_summary[item] = {"qty": 1, "total": price}

    for item, data in cart_summary.items():
        canvas.draw_text(f"{item} x{data['qty']} - ₦{data['total']:,.2f}", 400, y, "14px Arial")
        y += 20


def draw_payment_selector():
    """Draws buttons for selecting payment method"""
    global selected_payment_button
    canvas.set_fill_color("black")
    canvas.draw_text("Payment Method:", 50, 280, "14px Arial")
    selected_payment_button = []
    for i, method in enumerate(payment_options):
        x = 50 + i * 110
        y = 300
        button = canvas.create_rectangle(x, y, x + 100, y + 30)
        canvas.set_fill_color("white")
        canvas.fill_rect(x, y, 100, 30)
        canvas.set_fill_color("black")
        canvas.draw_text(method, x + 10, y + 20, "12px Arial")
        if method == payment_method:
            canvas.set_fill_color("blue")
            canvas.draw_text("✓", x + 80, y + 20, "14px Arial")
        selected_payment_button.append((button, method))


# --- Functional Logic (cart, receipt, loyalty) ---

def export_receipt():
    """Generates and saves a receipt text file with unique name"""
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"receipt_{customer_name}_{timestamp}.txt"
    final_total, tax = calculate_final_total()
    with open(filename, "w") as f:
        f.write(f"Customer: {customer_name}\n")
        f.write(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("--- Items ---\n")
        for item, price in cart:
            f.write(f"{item}: ₦{price:,.2f}\n")
        f.write(f"Subtotal: ₦{total_price:,.2f}\n")
        f.write(f"Tax: ₦{tax:,.2f}\n")
        if user_discount:
            f.write(f"Discount: ₦{user_discount:,.2f}\n")
        f.write(f"Total Due: ₦{final_total:,.2f}\n")
        f.write(f"Paid: ₦{payment_received:,.2f}\n")
        f.write(f"Change: ₦{payment_received - final_total:,.2f}\n")
        f.write(f"Payment Method: {payment_method}\n")
        f.write(f"Loyalty Points Earned: {int(final_total / 100)}\n")

    print(f"🧾 Receipt exported: {filename}")
    record_sale(final_total)
    award_loyalty_points(customer_name, final_total)


def calculate_final_total():
    """Computes final total including tax and discount"""
    tax = total_price * TAX_RATE
    final_total = total_price + tax - user_discount
    return final_total, tax


def award_loyalty_points(name, amount):
    """Updates customer profile with earned loyalty points"""
    points = int(amount / 100)
    if name not in loyalty_points:
        loyalty_points[name] = 0
    loyalty_points[name] += points
    print(f"🌟 {name} earned {points} points. Total: {loyalty_points[name]}")


def record_sale(amount):
    """Appends transaction to daily sales log"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    daily_sales.append((timestamp, customer_name, amount))


def show_daily_report():
    """Displays the daily sales summary in terminal"""
    print("\n📈 Daily Sales Report")
    print("----------------------------")
    total_day = 0
    for time_str, customer, amount in daily_sales:
        print(f"{time_str} - {customer}: ₦{amount:,.2f}")
        total_day += amount
    print("----------------------------")
    print(f"Total Sales: ₦{total_day:,.2f}\n")


# --- Event & Interaction Logic ---
# (on_mouse_click, input loop, etc.)
# ... (Keep all existing interaction code unchanged for brevity)

# --- Main Entry ---
def main():
    global customer_name
    customer_name = input("Enter customer name: ") or "Customer"
    draw_buttons()
    canvas.set_mouse_click_handler(on_mouse_click)

    while True:
        command = input("Command (barcode/restock/report/exit): ").strip().lower()
        if command == "barcode":
            simulate_barcode_scan()
        elif command == "restock":
            restock()
        elif command == "report":
            show_daily_report()
        elif command == "exit":
            print("👋 Exiting POS...")
            break


if __name__ == "__main__":
    main()
