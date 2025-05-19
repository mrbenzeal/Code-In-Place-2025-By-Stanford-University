"""
File: THIS_BIG.py
-------------------------
This project draws a square which has dimensions THIS_BIG by THIS_BIG 
(each side of the square is THIS_BIG pixels long) centered at CENTER_X, CENTER_Y.
"""

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
THIS_BIG = 144
CENTER_X = 160
CENTER_Y = 160

def main():
    # Create my canvas to draw on
    my_canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Calculate the top left corner position
    left_x = CENTER_X - THIS_BIG/2
    top_y = CENTER_Y - THIS_BIG/2
    
    # Calculate the right and bottom of the square
    right_x = left_x + THIS_BIG
    bottom_y = top_y + THIS_BIG

	# drawing a red square and storing it in a variable 'red_square'
    my_canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'red')
    red_square = my_canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'red')
    

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
