"""
File: Draw_Flag.py
-------------------
This is a program that draws the flag of Indonesia using Python graphics.
To draw the Indonesian flag all we did was to draw a single red rectangle 
which covers the top half of the graphics canvas. 
We don't need to draw the white stripe, because the canvas is white by default.
"""

from graphics import Canvas
import random

# The width of my canvas
CANVAS_WIDTH = 450
# The height of my canvas
CANVAS_HEIGHT = 300

def main():
    # Create my canvas to draw on
    my_canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Calculate the top left corner position
    left_x = 0
    top_y = 0
    
    # Calculate the right and bottom of the square
    right_x = CANVAS_WIDTH
    bottom_y = CANVAS_HEIGHT/2

    # Draws a rectangle with specified color
    Indonesian_flag = my_canvas.create_rectangle(
        left_x, 
        top_y, 
        right_x, 
        bottom_y,
        color="red"
    )
    

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
