"""
File: Random_Circles.py
------------------------
This program writes a code that draws 20 circles at random positions with random colors on the canvas
"""

from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20


def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_random_circles(canvas)


def draw_random_circles(canvas):
    for i in range(N_CIRCLES):
        x = random.randint(0, CANVAS_HEIGHT-CIRCLE_SIZE)
        y = random.randint(0, CANVAS_WIDTH-CIRCLE_SIZE)
        color = random_color()

        print(x,y,color)
        canvas.create_oval(x, y, x + CIRCLE_SIZE, y + CIRCLE_SIZE, random_color())


def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
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
