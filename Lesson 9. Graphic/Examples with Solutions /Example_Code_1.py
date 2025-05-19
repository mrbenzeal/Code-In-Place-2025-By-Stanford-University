"""
This is an example of a graphical program that uses a for loop
to place 5 diagonal balls from the top. If you change the value from 5 
to something like 10, it will place a different
number of balls diagonally.
"""

from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    # Create my canvas to draw on
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range(0, 5):
        canvas.create_oval(i*20, i*20, i*20+20, i*20+20)
    

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
