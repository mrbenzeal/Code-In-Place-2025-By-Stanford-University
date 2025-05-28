"""
File: Box_Row.py
-----------------
This is a program that draws a line of 5 boxes perfectly in line with one another, 
such that the boxes fill the bottom of the canvas.
"""

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    # Create my canvas to draw on
    my_canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Calculate the top left corner position
    left_x = 0
    top_y = CANVAS_HEIGHT - BOX_SIZE
    
    # Calculate the right and bottom of the square
    right_x = BOX_SIZE
    bottom_y = top_y + BOX_SIZE

    # Using the for loop to make a total of 5 boxes perfectly in line with one another
    for i in range(N_BOXES):
        # Creates a white rectangle 
        # with a black outline
        my_canvas.create_rectangle(
            left_x, 
            top_y, 
            (i+1)*BOX_SIZE, 
            bottom_y, 
            "white", 
            "black"
        )
        left_x += BOX_SIZE
        # right_x = right_x * (i+1)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
    
