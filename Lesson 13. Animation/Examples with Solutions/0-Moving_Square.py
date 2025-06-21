"""
File: Moving_Square.py
-----------------------
This program demonstrates animation of a square 
that starts in the left of the screen and moves to the middle.
"""

from graphics import Canvas
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SQUARE_SIZE = 40
VELOCITY = 2
DELAY = 0.01

def main():
    # Initial Setup - making all the variables we need
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    start_x = 0
    start_y = CANVAS_HEIGHT / 2 - SQUARE_SIZE / 2
    square = canvas.create_rectangle(start_x, start_y,
                    SQUARE_SIZE,
                    start_y + SQUARE_SIZE)

    # A Animation Loop that is true - this is repetition of heartbeats         
    while (start_x + SQUARE_SIZE / 2) < (CANVAS_WIDTH / 2):
        # Update World - each heartbeat update the world forward one frame
        start_x += VELOCITY
        print("x:", start_x)
        canvas.moveto(square, start_x, start_y)
        # Pause - without pause, human won't be able to see it
        time.sleep(DELAY)

    print("Done!")



"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
  
