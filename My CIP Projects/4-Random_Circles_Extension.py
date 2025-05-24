"""
File: Random_Circles_Extension.py
-----------------------------------
This program writes a code that 
- Draw a random number of circles between 1 and 20
- Draw circles of a random size 
- Draw the circles such that all parts of the circle are within my canvas. 
"""

from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = random.randint(10,50)
N_CIRCLES = random.randint(1,20)


"""The main function calls the function draw_random_circles to start the drawing"""
def main():
    # Print to the console a random colored circles
    print('Random Circles')

    # Create my canvas to draw on
    my_canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Draw a random number of circles between 1 and 20
    draw_random_circles(my_canvas)


"""
This function starts the drawing of 20 random colored circles, 
and calls the function random_color to start the random coloring for each circle.
"""
def draw_random_circles(my_canvas):
    # Ensuring that all parts of the circle are within my canvas width and height.
    a = CANVAS_HEIGHT - 1
    b = CANVAS_WIDTH - 1

    if a < CANVAS_HEIGHT and b < CANVAS_WIDTH:
        # A for loop used to draw random colored circles
        for i in range(N_CIRCLES):
            x = random.randint(1, a - CIRCLE_SIZE)
            y = random.randint(1, b - CIRCLE_SIZE)
            color = random_color()

            print(x,y,color)
            my_canvas.create_oval(x, y, x + CIRCLE_SIZE, y + CIRCLE_SIZE, random_color())


"""
This is a function to use to get a random color for each circle. 
It was predefined for me in my program. 
"""
def random_color():
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == "__main__":
    main()
