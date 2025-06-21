"""
File: Mouse_Tracker.py
-----------------------
This program tracks the mouse's position and prints the mouse's (x, y) location in the graphics canvas.
Some extra functions that you can use in the graphics are commented out below.
"""

from graphics import Canvas
import time

CANVAS_SIZE = 400
PAUSE_TIME = 1/50

def main():
    canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)
    while True:
        # Get the x & y location of the mouse
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        # Pause time 
        time.sleep(PAUSE_TIME)
        print("Mouse location: (" + str(mouse_x) + ", " + str(mouse_y) + ")")
    
    # Move shape to some new coordinates (absolute coordinate)
    # canvas.moveto(shape, new_x, new_y)

    # Move shape by a given change_x & change_y (relative coordinate)
    # canvas.move(shape, change_x, change_y)

    # Get the coordinates of a shape
    # top_y = canvas.get_top_y(shape)
    # left_x = canvas.get_left_x(shape)

    # Return a list of elements in a rectangle area
    # return = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main() 
