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

    # Getting the middle of the canvas
    middle_x = CANVAS_WIDTH/2
    middle_y = CANVAS_HEIGHT/2
    
    # Calculating the top left corner position of the outer red circle
    left_x_1 = middle_x - OUTER_DIAMETER/2
    top_y_1 = middle_y - OUTER_DIAMETER/2
    
    # Calculating the right and bottom of the outer red circle
    right_x_1 = left_x_1 + OUTER_DIAMETER
    bottom_y_1 = top_y_1 + OUTER_DIAMETER

    # Calculating the top left corner position of the white inner circle
    left_x_2 = OUTER_LEFT_X + RING_WIDTH
    top_y_2 = OUTER_TOP_Y + RING_WIDTH
    
    # Calculating the right and bottom of the white inner circle
    right_x_2 = OUTER_LEFT_X + OUTER_DIAMETER - RING_WIDTH
    bottom_y_2 = OUTER_TOP_Y + OUTER_DIAMETER - RING_WIDTH

	# drawing a red outer circle 
    my_canvas.create_oval(left_x_1, top_y_1, right_x_1, bottom_y_1, 'red')

    # drawing a white inner circle
    my_canvas.create_oval(left_x_2, top_y_2, right_x_2, bottom_y_2, 'white')
    
    
"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
    
