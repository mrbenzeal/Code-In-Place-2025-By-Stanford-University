"""
File: Centered_Square.py
-------------------------
This program that draws a square, 
200 pixels wide, by 200 pixels high, 
right in the center of the canvas.
"""

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
SQUARE_SIZE = 100

def main():
    # Create my canvas to draw on
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Get the middle of the canvas
    middle_x = CANVAS_WIDTH/2
    middle_y = CANVAS_HEIGHT/2
    
    # Calculate the top left corner position
    left_x = middle_x - SQUARE_SIZE/2
    top_y = middle_y - SQUARE_SIZE/2
    
    # Calculate the right and bottom of the square
    right_x = left_x + SQUARE_SIZE
    bottom_y = top_y + SQUARE_SIZE
    
    # Draw the square
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
