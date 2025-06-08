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
"""

from graphics import Canvas
import random
import os
import time

# --- Canvas Constants --- 
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400

# --- Constant Definitions ---
# --ToDo-- DISCOUNT_CODES = {"SAVE10": 10, "SAVE20": 20}
DISCOUNT_CHANCE = 0.2
BULK_DISCOUNT_THRESHOLD = 300
BULK_DISCOUNT = 50
TAX_RATE = 0.05
PAYMENT_OPTIONS = ["Cash", "Card", "Transfer"]
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40
START_X = 50
START_Y = 50
CART_PANEL_START_Y = 200
GAP_Y = 60
BALL_SIZE = 20
DELAY = 0.01    # seconds to wait between each update
MIN_STOCK = 5
MAX_STOCK = 20


# --- Main Entry ---
def main():
    # Initialize canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    print("  POS Shopping Cart System")
    print("<-------------------------->")

    # creating the canvas title line of text
    canvas_title = canvas.create_text(220, 5, "POS Shopping Cart System", color="blue", font="Courier", font_size=10)

    products = get_initial_products()
    cart = []
    loyalty_points = {}
    daily_sales = []
    payment_method = "Cash"
    customer_name = input("Enter customer name: ")
    total_price = 0
    user_discount = 0

    state = (cart, products, loyalty_points, daily_sales, payment_method, customer_name, total_price, user_discount)
    draw_buttons(canvas, products, cart, total_price, user_discount, payment_method)

    def handler(x, y):
        nonlocal state
        cart, products, loyalty_points, daily_sales, payment_method, customer_name, total_price, user_discount = state
        cart, total_price, user_discount = on_mouse_click(canvas, x, y, state)
        state = (cart, products, loyalty_points, daily_sales, payment_method, customer_name, total_price, user_discount)

    canvas.wait_for_click()

    while True:
        command = input("Command (barcode/restock/checkout/exit): ").strip().lower()
        if command == "barcode":
            code = input("Enter barcode: ")
            cart, total_price = simulate_barcode_scan(code, products, cart, total_price)
            draw_buttons(canvas, products, cart, total_price, user_discount, payment_method)
        elif command == "restock":
            restock(products)
            draw_buttons(canvas, products, cart, total_price, user_discount, payment_method)
        elif command == "checkout":
            try:
                payment_received = float(input("Enter amount paid: ₦"))
            except ValueError:
                print("❌ Invalid amount")
                continue
            cart = checkout(cart, customer_name, total_price, user_discount, payment_received, payment_method, loyalty_points, daily_sales)
            total_price = 0
            user_discount = 0
            draw_buttons(canvas, products, cart, total_price, user_discount, payment_method)
        elif command == "exit":
            print("👋 Exiting POS...")
            moving_objects(canvas)
            break


# --- Data Definitions ---
def get_initial_products():

    # Generate random stock numbers
    num1 = random.randint(MIN_STOCK, MAX_STOCK)
    num2 = random.randint(MIN_STOCK, MAX_STOCK)
    num3 = random.randint(MIN_STOCK, MAX_STOCK)

    return {
        "Apple": {"price": 100, "image": "🍎", "stock": num1, "barcode": "111"},
        "Banana": {"price": 50, "image": "🍌", "stock": num2, "barcode": "222"},
        "Orange": {"price": 80, "image": "🍊", "stock": num3, "barcode": "333"}
    }


# --- Event Handling ---
def on_mouse_click(canvas, x, y, state):
    cart, products, loyalty_points, daily_sales, payment_method, customer_name, total_price, user_discount = state

    for rect, item in draw_buttons(canvas, products, cart, total_price, user_discount, payment_method):
        if canvas.get_object_at(x, y) == rect:
            if products[item]["stock"] > 0:
                products[item]["stock"] -= 1
                cart.append((item, products[item]["price"]))
                total_price += products[item]["price"]
                if total_price > BULK_DISCOUNT_THRESHOLD and random.random() < DISCOUNT_CHANCE:
                    user_discount += BULK_DISCOUNT
                    print(f"🎉 Bulk discount applied: ₦{BULK_DISCOUNT}")
            else:
                print(f"⚠️ {item} is out of stock!")
            break

    draw_buttons(canvas, products, cart, total_price, user_discount, payment_method)
    return cart, total_price, user_discount


# --- Command Handlers ---
def simulate_barcode_scan(barcode, products, cart, total_price):
    for name, info in products.items():
        if info["barcode"] == barcode:
            if info["stock"] > 0:
                info["stock"] -= 1
                cart.append((name, info["price"]))
                total_price += info["price"]
                print(f"🔍 Scanned {name}, added to cart.")
            else:
                print(f"⚠️ {name} is out of stock!")
            break
    else:
        print("❌ Unknown barcode")
    return cart, total_price


def restock(products):
    for item in products:
        products[item]["stock"] += 5
    print("✅ Products restocked.")


def calculate_final_total(total_price, user_discount):
    tax = total_price * TAX_RATE
    final_total = total_price + tax - user_discount
    return final_total, tax


def checkout(cart, customer_name, total_price, user_discount, payment_received, payment_method, loyalty_points, daily_sales):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"receipt_{customer_name}_{timestamp}.txt"
    final_total, tax = calculate_final_total(total_price, user_discount)
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
    points = int(final_total / 100)
    if customer_name not in loyalty_points:
        loyalty_points[customer_name] = 0
    loyalty_points[customer_name] += points
    print(f"🌟 {customer_name} earned {points} points. Total: {loyalty_points[customer_name]}")
    daily_sales.append((timestamp, customer_name, final_total))
    return []


# --- GUI Drawing Functions ---
def draw_buttons(canvas, products, cart, total_price, user_discount, payment_method):
    canvas.clear()
    # --error-- canvas.set_outline_color(color="lightgray")
    canvas.create_text(80, 10, "Click a product or scan barcode to add to cart", color="red", font="Courier", font_size=15)

    product_buttons = []
    for i, (item, info) in enumerate(products.items()):
        x = START_X
        y = START_Y + i * GAP_Y
        rect = canvas.create_rectangle(x, y, x + BUTTON_WIDTH, y + BUTTON_HEIGHT)
        # --error-- canvas.set_fill_color("white")
        canvas.create_rectangle(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
        # --error-- canvas.set_fill_color("black")
        stock = info["stock"]
        canvas.create_text(x + 5, y + 25, f"{info['image']} {item} - ₦{info['price']} ({stock})", color="brown", font="Courier", font_size=14)
        product_buttons.append((rect, item))

    # --error-- canvas.set_fill_color("blue")
    canvas.create_text(400, 130, f"Total: ₦{total_price:,.2f}", color="blue", font="Courier", font_size=18)

    draw_cart_panel(canvas, cart)
    draw_payment_selector(canvas, payment_method)
    return product_buttons


def draw_cart_panel(canvas, cart):
    # --error-- canvas.set_fill_color("black")
    canvas.create_text(400, CART_PANEL_START_Y - 20, "Cart:", color="blue", font="Courier", font_size=16)
    y = CART_PANEL_START_Y
    cart_summary = {}
    for item, price in cart:
        if item in cart_summary:
            cart_summary[item]["qty"] += 1
            cart_summary[item]["total"] += price
        else:
            cart_summary[item] = {"qty": 1, "total": price}

    for item, data in cart_summary.items():
        canvas.create_text(400, y, f"{item} x{data['qty']} - ₦{data['total']:,.2f}", color="blue", font="Courier", font_size=14)
        y += 20


def draw_payment_selector(canvas, payment_method):
    # --error-- canvas.set_fill_color("black")
    canvas.create_text(50, 280, "Payment Method:", color="violet", font="Courier", font_size=14)
    for i, method in enumerate(PAYMENT_OPTIONS):
        x = 50 + i * 110
        y = 300
        canvas.create_rectangle(x, y, x + 100, y + 30)
        # --error-- canvas.set_fill_color("white")
        canvas.create_rectangle(x, y, 100, 30)
        # --error-- canvas.set_fill_color("black")
        canvas.create_text(x + 10, y + 20, method, color="violet", font="Courier", font_size=12)
        if method == payment_method:
            # --error-- canvas.set_fill_color("blue")
            canvas.create_text(x + 80, y + 20, "✓", color="yellow", font="Courier", font_size=14)


def moving_objects(canvas):
    # creating brown_ball and my_image; and storing them in variables
    brown_ball = canvas.create_oval(0, 370, BALL_SIZE, BALL_SIZE + 370, 'brown')
    # --ToDo-- my_image = canvas.create_image(x, y, 'image')
    
    # change on the x and y cordinates for the ball
    change_x = 2
    change_y = 1

    # animation loop for the brown ball
    while(True):
        left_x = canvas.get_left_x(brown_ball)
        top_y = canvas.get_top_y(brown_ball)

        # change direction if ball reaches an edge
        if left_x < 0 or left_x + BALL_SIZE >= CANVAS_WIDTH:
            change_x = -change_x
        
        if top_y < 370 or top_y + BALL_SIZE >= CANVAS_HEIGHT:
            change_y = -change_y

        # update the ball
        canvas.move(brown_ball, change_x, change_y)
        
        # pause
        time.sleep(DELAY)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == "__main__":
    main()
