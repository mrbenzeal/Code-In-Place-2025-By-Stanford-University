from graphics import Canvas
import random

canvas = Canvas()
canvas.set_canvas_title("Simple POS Shopping System")
canvas.set_canvas_size(400, 500)

# Product definitions
products = {
    "Apple": 100,
    "Banana": 50,
    "Orange": 80
}

product_buttons = []
cart = []
total_price = 0

# Constants
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40
START_X = 50
START_Y = 50
GAP_Y = 60
DISCOUNT_CHANCE = 0.2  # 20%

def draw_buttons():
    canvas.clear()
    canvas.set_fill_color("lightgray")
    canvas.draw_text("Click on a product to add to cart", 100, 20, "15px Arial")

    for i, (item, price) in enumerate(products.items()):
        x = START_X
        y = START_Y + i * GAP_Y
        rect = canvas.create_rectangle(x, y, x + BUTTON_WIDTH, y + BUTTON_HEIGHT)
        canvas.set_fill_color("white")
        canvas.fill_rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
        canvas.set_fill_color("black")
        canvas.draw_text(f"{item} - ₦{price}", x + 10, y + 25, "14px Arial")
        product_buttons.append((rect, item))

    # Show total
    canvas.set_fill_color("blue")
    canvas.draw_text(f"Total: ₦{total_price}", 100, 400, "18px Arial")

def is_inside(x, y, rect_coords):
    x1, y1, x2, y2 = rect_coords
    return x1 <= x <= x2 and y1 <= y <= y2

def on_mouse_click(x, y):
    global total_price
    for rect, item in product_buttons:
        coords = canvas.get_coords(rect)
        if is_inside(x, y, coords):
            price = products[item]
            discount = 0
            if random.random() < DISCOUNT_CHANCE:
                discount = random.randint(10, 30)  # ₦10–₦30 off
                print(f"🎉 Discount on {item}: ₦{discount} OFF!")

            final_price = max(0, price - discount)
            cart.append((item, final_price))
            total_price += final_price
            print(f"🛒 Added {item}: ₦{final_price} (Discount: ₦{discount})")
            draw_buttons()
            break

# Setup
draw_buttons()
canvas.set_mouse_click_handler(on_mouse_click)
