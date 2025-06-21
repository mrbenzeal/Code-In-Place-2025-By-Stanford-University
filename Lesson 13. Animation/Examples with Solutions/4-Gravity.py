"""
File: Gravity.py
-----------------
This program initialize a square at a random X, Y position on the canvas. 
It implements gravity: no matter where the square starts out, 
it should fall down until its bottom edge reaches the bottom of the canvas.
"""

from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SQUARE_SIZE = 40
VELOCITY = 2
DELAY = 0.01

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    start_x = random.random() * CANVAS_WIDTH
    start_y = random.random() * CANVAS_HEIGHT
    square = canvas.create_rectangle(start_x, start_y,
                    start_x + SQUARE_SIZE,
                    start_y + SQUARE_SIZE)
    
    while (start_y + SQUARE_SIZE < CANVAS_HEIGHT):
        start_y += VELOCITY
        canvas.moveto(square, start_x, start_y)
        time.sleep(DELAY) 


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
