"""
File: Mirror_Mirror.py
--------------------------
This is a program that draws a blue rectangle on the other side of the canvas 
which is the mirror image of the red rectangle. 
(That is, the left edge of the blue rectangle is the same distance 
from the line in the middle as the right edge of the red rectangle, 
and the left edge of the red rectangle is the same distance 
from the left edge of the canvas as the right edge of the blue rectangle is 
from the right edge of the canvas!). 
"""

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Create mirror line
    canvas.create_line(
        CANVAS_WIDTH // 2, 
        0, 
        CANVAS_WIDTH // 2, 
        CANVAS_HEIGHT)
    
    # Create red rectangle
    rect_left_x = 20
    rect_top_y = 50
    rect_width = 100
    rect_height = 200
    canvas.create_rectangle(
        rect_left_x, 
        rect_top_y, 
        rect_left_x + rect_width, 
        rect_top_y + rect_height, 
        'red')
    
    pass # Delete this line and write your code here! :)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
