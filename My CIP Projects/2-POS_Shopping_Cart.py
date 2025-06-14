"""
CIP_Section_5 PROJECT - Obinna Ani
-----------------------------------
File: POS_Shopping_Cart.py
---------------------------
This is a Nigerian Fruit Shop's Point-of-Sale (POS) Shopping Cart System.
- It is a solo-friendly, interactive Python project using Python graphics canvas, time, os and random imports. 
- It simulates a real-world retail checkout experience with product selection 
  via barcode input, a dynamic cart display, stock management, and tax. 
- Users can clear carts, see visual updates, and receive real-time total cost calculations. 
- Receipts can be exported, saved, and viewed on the terminal and canvas using the customer's name, timestamps, and loyalty points. 
- Admin functions also include restocking.

NOTE:
-----
This project is subject to more improved functionalities like:
- Click buttons effectively for objects on the canvas.
- Improved graphical animations.
- A better-decomposited program.
- And more.

VOTE OF THANKS:
---------------
I wish to thank:
- My Section Leader: Anna Q
- My 2025 Code In Place Section Members
- Professor Chris Piech & Mehran Sahami
- Stanford University's Code in Place 2025 staff
For making my Python learning journey pleasurable.
"""

from graphics import Canvas
import random
import os
import time
from datetime import datetime

# --- Canvas Constants --- #
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400

# --- Constant Definitions --- #
DISCOUNT_CHANCE = 0.2
BULK_DISCOUNT_THRESHOLD = 300
BULK_DISCOUNT = 50
TAX_RATE = 0.0005
PAYMENT_OPTIONS = ["Cash", "Card", "Transfer"]
MIN_STOCK = 5
MAX_STOCK = 20
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 20
START_X = 50
START_Y = 45
CART_PANEL_START_Y = 140
GAP_Y = 30
RECT_SIZE = 50
BALL_SIZE = 20
DELAY = 0.01    # seconds to wait between each update


""" Project Main Function """

# --- Main Entry --- #
def main():
    # Initializing canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Print to terminal
    print(" POS Shopping Cart System")
    print("**************************")

    # The welcome home page design
    welcome_home_page(canvas)
    draw_welcome_button(canvas)
    draw_enter_name_button(canvas) 

    # Initializing the canvas' local variables
    products = get_initial_products()
    cart = []
    loyalty_points = {}
    daily_sales = []
    selected_payment_button = []
    payment_method = "Cash"
    customer_name = input("Enter customer name: ") # print to terminal
    total_price = 0
    user_discount = 0

    # the POS interactive page
    draw_buttons(canvas, products, cart, total_price, user_discount, selected_payment_button, payment_method)
    draw_click_here_button(canvas)
    canvas.wait_for_click()
    pos_system_option_panel(canvas, cart, products, loyalty_points, daily_sales, selected_payment_button, payment_method, customer_name, total_price, user_discount)


""" Project Helper Functions """

# --- The Home Pages --- #
def welcome_home_page(canvas):
    # Creating the canvas title line of text "POS Shopping Cart System" and screen saver.
    canvas_title = canvas.create_text(220, 5, "POS Shopping Cart System", color="blue", font="Courier", font_size=10)
    #screen_saver = canvas.create_image(5, 15, "fruit_shop.png")


def goodbye_home_page(canvas):
    # Creating the canvas title line of text "POS Shopping Cart System" and screen saver.
    canvas_title = canvas.create_text(220, 5, "POS Shopping Cart System", color="blue", font="Courier", font_size=10)
    #screen_saver = canvas.create_image(5, 15, "CodeInPlace.png")


# --- Data Definitions --- #
def get_initial_products():
    # Generate random stock numbers
    nums = [random.randint(MIN_STOCK, MAX_STOCK) for num in range(8)]
    return {
        "Apple": {"price": 500, "image": "🍎", "stock": nums[0], "barcode": "111"},
        "Banana": {"price": 800, "image": "🍌", "stock": nums[1], "barcode": "222"},
        "Orange": {"price": 200, "image": "🍊", "stock": nums[2], "barcode": "333"},
        "Lemon": {"price": 150, "image": "🍋", "stock": nums[3], "barcode": "444"},
        "Mango": {"price": 200, "image": "🥭", "stock": nums[4], "barcode": "555"},
        "Cucumber": {"price": 300, "image": "🥒", "stock": nums[5], "barcode": "666"},
        "Carrot": {"price": 100, "image": "🥕", "stock": nums[6], "barcode": "777"},
        "Avacado": {"price": 550, "image": "🥑", "stock": nums[7], "barcode": "888"}
    }


# --- User Interface Refresh Helper --- #
def refresh_user_interface(canvas, products, cart, total_price, user_discount, selected_payment_button, payment_method):
    draw_buttons(canvas, products, cart, total_price, user_discount, selected_payment_button, payment_method)


# --- Option Handlers --- #
def pos_system_option_panel(canvas, cart, products, loyalty_points, daily_sales, selected_payment_button, payment_method, customer_name, total_price, user_discount):
    
    while True:
        option = input("Option (barcode/restock/checkout/view/exit): ").strip().lower()
        if option == "barcode":
            refresh_user_interface(canvas, products, cart, total_price, user_discount, selected_payment_button, payment_method)
            barcode = input("Enter barcode: ")
            cart, total_price = simulate_barcode_scan(barcode, products, cart, total_price)
            draw_buttons(canvas, products, cart, total_price, user_discount, selected_payment_button, payment_method)
          
        elif option == "restock":
            refresh_user_interface(canvas, products, cart, total_price, user_discount, selected_payment_button, payment_method)
            restock(products)
            print("✅ Products restocked.")
            draw_buttons(canvas, products, cart, total_price, user_discount, selected_payment_button, payment_method)
          
        elif option == "checkout":
            refresh_user_interface(canvas, products, cart, total_price, user_discount, selected_payment_button, payment_method)
            draw_payment_selector_buttons(canvas, selected_payment_button, payment_method)
            canvas.wait_for_click()
            try:
                payment_received = float(input("Enter amount paid: ₦"))
            except ValueError:
                print("❌ Invalid amount")
                continue
            cart = checkout(cart, customer_name, total_price, user_discount, payment_received, payment_method, loyalty_points, daily_sales)
            total_price = 0
            user_discount = 0
            draw_buttons(canvas, products, cart, total_price, user_discount, selected_payment_button, payment_method)
          
        elif option == "view":
            # Display the latest receipt on the terminal
            display_latest_receipt(canvas)
            # List all available receipts
            receipts = list_receipts(canvas)
            if not receipts:
                # Display "❌ No receipts available." on the terminal & canvas
                print("❌ No receipts available.")
                canvas.create_text(200, 200, "❌ No receipts available.", color="red", font="Courier", font_size=18)
                continue
            # Display all available receipts list on the terminal
            print("\nAvailable Receipts:")
            for idx, r in enumerate(receipts):
                print(f"{idx + 1}. {r}")
            # Prompt for receipt to view, choose & display on canvas
            y = 60
            try:
                choice = int(input("Select receipt number to view: "))
                if 1 <= choice <= len(receipts):
                    selected_receipt = receipts[choice - 1]
                    display_receipt_on_canvas(canvas, selected_receipt)
                else:
                    # Display "❌ Invalid selection." on the terminal & canvas
                    print("❌ Invalid selection.")
                    canvas.create_text(200, y + 20, "❌ Invalid selection.", color="red", font="Courier", font_size=18)
            except ValueError:
                # Display "❌ Invalid input." on the terminal & canvas
                print("❌ Invalid input.")
                canvas.create_text(200, y + 20, "❌ Invalid input.", color="red", font="Courier", font_size=18)
              
        elif option == "exit":
            print("👋 Exiting POS...")
            canvas.clear()
            # goodbye home page design
            goodbye_home_page(canvas)
            draw_goodbye_button(canvas)
            draw_moving_ball(canvas)
            break


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
        products[item]["stock"] += random.randint(MIN_STOCK, MAX_STOCK)
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
        f.write(f"Customer Name: {customer_name}\n")
        f.write(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("--- Items ---\n")
        for item, price in cart:
            f.write(f"{item}: ₦{price:,.2f}\n") # 
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


def display_latest_receipt(canvas):
    receipts = [f for f in os.listdir() if f.startswith("receipt_") and f.endswith(".txt")]
    if not receipts:
        print("❌ No receipts found.")
        return
    latest = max(receipts, key=os.path.getctime)
    print(f"\n📄 Displaying latest receipt: {latest}\n" + "-"*29)
    with open(latest, "r") as f:
        print(f.read())


def list_receipts(canvas):
    receipts = [f for f in os.listdir() if f.startswith("receipt_") and f.endswith(".txt")]
    receipts.sort(reverse=True, key=os.path.getctime)
    return receipts


def display_receipt_on_canvas(canvas, filename):
    canvas.clear()
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "white")
    canvas.create_text(20, 20, f"📄 Viewing: {filename}", color="black", font="Courier", font_size=16)
    
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        canvas.create_text(200, 100, "❌ Receipt file not found.", color="red", font="Courier", font_size=18)
        return

    y = 40
    print(f"\n📄 Displaying receipt: {filename}\n" + "-"*22)
    for line in lines:
        print(line.strip())
        if y < CANVAS_HEIGHT - 15:
            canvas.create_text(20, y, line.strip(), color="black", font="Courier", font_size=12)
            y += 15
        else:
            break  # avoid drawing off-screen


# --- GUI Drawing Functions --- #
def draw_welcome_button(canvas):
    # draw the rectangles  
    black_rect = canvas.create_rectangle(0, 310, RECT_SIZE, 330, 'black', 'red')
    white_rect = canvas.create_rectangle(CANVAS_WIDTH, 310, CANVAS_WIDTH - RECT_SIZE, 330, 'white', 'red')
    
    # animation loop YOU ARE WELCOME
    while canvas.get_left_x(black_rect) < (CANVAS_WIDTH / 2):
        canvas.move(black_rect, 1, 0)
        canvas.move(white_rect, -1, 0)
   
        # pause
        time.sleep(DELAY)
    canvas.create_text(252, 315, "YOU ARE", color="black", font="Courier", font_size=11)
    canvas.create_text(303, 315, "WELCOME", color="white", font="Courier", font_size=11)


def draw_enter_name_button(canvas):
    canvas.create_rectangle(225, 330, 375, 350, "violet", "black")
    canvas.create_text(232, 335, "ENTER COSTOMER NAME", color="blue", font="Courier", font_size=12)


def draw_click_here_button(canvas):
    click_here_button = canvas.create_rectangle(260, 45, 340, 65, "white", "black")    
    canvas.create_text(265, 50, "CLICK HERE", color="black", font="Courier", font_size=12)
    canvas.create_text(260, 70, "For Options", color="red", font="Courier", font_size=12)


def draw_buttons(canvas, products, cart, total_price, user_discount, selected_payment_button, payment_method):
    # This clears every object on the canvas
    canvas.clear()

    # Making the background colour of my canvas light-green
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, 'lightgreen')

    # This creates the "Input a product barcode to add to cart" text instruction on the canvas
    canvas.create_text(5, 30, "Input a barcode to add product to cart", color="red", font="Courier", font_size=11)

    # Creating the buttons for the products on the canvas
    product_buttons = []
    for i, (item, info) in enumerate(products.items()):
        x = START_X
        y = START_Y + i * GAP_Y
        product_rect = canvas.create_rectangle(x, y, x + BUTTON_WIDTH, y + BUTTON_HEIGHT, "violet", "black")
        
        stock = info["stock"]
        canvas.create_text(x + 5, y + 5, f"{info['image']} {item} - ₦{info['price']} ({stock})", color="blue", font="Courier", font_size=14)

        # Creating the buttons for the barcodes on the canvas
        barcode_button = canvas.create_rectangle(x - 45, y, x - 5, y + BUTTON_HEIGHT, "white", "black")
        canvas.create_text(x - 40, y + 5, f"{info['barcode']}", color="black", font="Courier", font_size=14)

        product_buttons.append((product_rect, item))

    # Creating the text "Total: ₦", which is the total cost of the products on the canvas
    canvas.create_text(400, 70, f"Total: ₦{total_price:,.2f}", color="blue", font="Courier", font_size=18)

    draw_cart_panel(canvas, cart)

    return product_buttons


def draw_cart_panel(canvas, cart):
    # Creating the text "Cart 🛒:" on the canvas 
    canvas.create_text(400, CART_PANEL_START_Y - 20, "Cart 🛒:", color="blue", font="Courier", font_size=16)
    
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


def draw_payment_selector_buttons(canvas, selected_payment_button, payment_method):
    selected_payment_button.clear()

    # Creating the text "Payment Method:" on the canvas
    canvas.create_text(50, 280, "Payment Method:", color="red", font="Courier", font_size=14)
    
    for i, method in enumerate(PAYMENT_OPTIONS):
        x = 50 + i * 110
        y = 300
        button = canvas.create_rectangle(x, y, x + 85, y + 20, "violet", "black")
        
        canvas.create_text(x + 5, y + 5, method, color="blue", font="Courier", font_size=12)

    selected_payment_button.append((button, payment_method))


def draw_goodbye_button(canvas):
    # draw the rectangles  
    black_rect = canvas.create_rectangle(0, 330, RECT_SIZE, 350, 'black', 'blue')
    white_rect = canvas.create_rectangle(CANVAS_WIDTH, 330, CANVAS_WIDTH - RECT_SIZE, 350, 'white', 'blue')
    
    # animation loop YOU ARE WELCOME
    while canvas.get_left_x(black_rect) < (CANVAS_WIDTH / 2):
        canvas.move(black_rect, 1, 0)
        canvas.move(white_rect, -1, 0)
   
        # pause
        time.sleep(DELAY)
    canvas.create_text(260, 335, "GOOD", color="black", font="Courier", font_size=11)
    canvas.create_text(315, 335, "BYE", color="white", font="Courier", font_size=11)


def draw_moving_ball(canvas):
    # creating brown_ball and my_image; and storing them in variables
    brown_ball = canvas.create_oval(0, 370, BALL_SIZE, BALL_SIZE + 370, 'brown')
    # --ToDo-- my_image = canvas.create_image(x, y, 'image')
    
    # change on the x and y coordinates for the ball
    change_x = 2
    change_y = 1

    # animation loop for the brown ball
    while(True):
        left_x = canvas.get_left_x(brown_ball)
        top_y = canvas.get_top_y(brown_ball)

        # change direction if the ball reaches an edge
        if left_x < 0 or left_x + BALL_SIZE >= CANVAS_WIDTH:
            change_x = -change_x
        
        if top_y < 370 or top_y + BALL_SIZE >= CANVAS_HEIGHT:
            change_y = -change_y

        # update the ball
        canvas.move(brown_ball, change_x, change_y)
        
        # pause
        time.sleep(DELAY)


"""
# This provided line is required at the end of the Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == "__main__":
    main()
