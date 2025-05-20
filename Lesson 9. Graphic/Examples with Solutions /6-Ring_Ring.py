"""
File: Ring_Ring.py
-------------------
This is a program that combine shapes to make new ones like making a red ring.
This is done by drawing two overlapping ovals. we make one outer oval (in red), 
and then one smaller, inner oval (in white) inside of the first oval! 
Since the background is white, this gives the appearance of a ring.
"""

from graphics import Canvas

CANVAS_WIDTH = 150
CANVAS_HEIGHT = 150

# the diameter of the outer red circle
OUTER_DIAMETER = 50

# the left and top coordinates of the outer red circle
OUTER_LEFT_X = (CANVAS_WIDTH - OUTER_DIAMETER)/2
OUTER_TOP_Y = (CANVAS_HEIGHT - OUTER_DIAMETER)/2

# the size of the red band of the ring
# inner_left_x = outer_left_x + RING_WIDTH
RING_WIDTH = 10


def main():
    my_canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Calculate the top left corner position
    left_x = OUTER_LEFT_X - OUTER_DIAMETER/2
    top_y = OUTER_TOP_Y - OUTER_DIAMETER/2
    
    # Calculate the right and bottom of the square
    right_x = left_x + OUTER_DIAMETER
    bottom_y = top_y + OUTER_DIAMETER

	# drawing a red square and storing it in a variable 'red_square'
    my_canvas.create_oval(left_x, top_y, right_x, bottom_y, 'red')
    
    
"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
    
