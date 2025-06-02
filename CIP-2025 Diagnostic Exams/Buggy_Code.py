"""
DIAGNOSTIC_EXAM
----------------
File: Buggy_Code.py
---------------------
Consider the following buggy code:

from graphics import Canvas

def main():
    # draws two cars
    canvas = Canvas(400, 400)
    x = 10
    y = 10
    draw_car()

    x = 100
    y = 100
    draw_car()

def draw_car():
    # draws a car at the location x, y
    # you can assume that math offsets for the rectangles are correct
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()

The programmer wants to draw two cars, one at location (10, 10) and another at location (100, 100). 
When they run their program they get a "NameError" 
and the IDE complains that inside draw_car it doesn't know what canvas, x, or y mean.

Fix this program so that the location information is correctly given to draw_car. 
You can make changes to both draw_car and main. Write a comments for each line you changed.

Note that you should assume that the offsets in draw_car are correct. 
You are not meant to be worrying about the canvas coordinates, rather the control flow of the program.
"""

from graphics import Canvas

def main():
    # Create a canvas of size 400x400
    canvas = Canvas(400, 400)
    
    # Draw the first car at position (10, 10)
    x = 10
    y = 10
    draw_car(canvas, x, y)  # Pass canvas, x, and y to draw_car

    # Draw the second car at position (100, 100)
    x = 100
    y = 100
    draw_car(canvas, x, y)  # Pass canvas, x, and y to draw_car

def draw_car(canvas, x, y):
    # Draws a car at the given (x, y) location
    # The offsets for the rectangles are assumed to be correct
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()
  
