"""
File: Chess_Board.py
---------------------
This program writes a code that draws a chessboard on the canvas.
"""

from graphics import Canvas
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = CANVAS_WIDTH
N_ROWS = 8
N_COLS = N_ROWS
SIZE = CANVAS_WIDTH / N_ROWS


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # For each row and column, draw a square
    for r in range(N_ROWS):
        for c in range(N_COLS):
            draw_square(canvas, r, c)


def draw_square(canvas, r, c):
    """
    Draws a square at row r, column c. Also prints out the row and column.
    """
    print(r, c)
    
    color = get_color(r, c)  # Get the square's color based on the row and column  

    x = c * SIZE  # Calculate left_x
    y = r * SIZE  # Calculate top_y
    end_x = x + SIZE  # Calculate right_x
    end_y = y + SIZE  # Calculate bottom_y
    
    canvas.create_rectangle(x, y, end_x, end_y, color, 'black')  # Draw the rectangle
            
        
def get_color(r, c):
    """
    Get's the color of the checkerboard square at row r column c.
    """
    if is_even(r + c):
        return "black"
    else:
        return "white"


def is_even(value):
    """
    Returns whether or not a number is even.
    """
    return value % 2 == 0


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
