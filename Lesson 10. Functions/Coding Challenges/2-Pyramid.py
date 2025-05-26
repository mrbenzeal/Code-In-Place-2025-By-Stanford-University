"""
File: Pyramid.py
-----------------
This program writes a code that draws a pyramid consisting of bricks arranged in horizontal rows, 
so that the number of bricks in each row decreases by one as we move up the pyramid.
"""

from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base
# COLORS = ["red", "orange", "yellow", "green", "blue", "violet", ] # Adding many colors
COLORS = ["yellow"] # Adding only yellow color


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO, your code here
    draw_base_brick_row (canvas, BRICKS_IN_BASE)
    # for next row, the number of bricks will be BRICKS_IN_BASE - 1
    #Count variable keeps track of the number of bricks that needs to be decreased while going up the rows in pyramid
    count = 1
    for bricks in range (BRICKS_IN_BASE-1):
        bricks_in_row = BRICKS_IN_BASE - count
        draw_next_brick_row (canvas, bricks_in_row, count)
        count +=1 


def draw_base_brick_row(canvas, BRICKS_IN_BASE):
    for i in range (BRICKS_IN_BASE): 
        start_x = CANVAS_WIDTH/2 - (BRICKS_IN_BASE/2)*BRICK_WIDTH + i*BRICK_WIDTH
        start_y = CANVAS_HEIGHT - BRICK_HEIGHT
        end_x = start_x + BRICK_WIDTH
        end_y = start_y + BRICK_HEIGHT
        color = random.choice(COLORS)

        canvas.create_rectangle(start_x, start_y, end_x, end_y, color, 'black')
        #canvas.wait_for_click()
        #time.sleep(0.02)
        

def draw_next_brick_row(canvas, bricks_in_row, count):
    for i in range (bricks_in_row): 
        start_x = CANVAS_WIDTH/2 - (bricks_in_row/2)*BRICK_WIDTH + i*BRICK_WIDTH
        start_y = CANVAS_HEIGHT - (count+1)*BRICK_HEIGHT
        end_x = start_x + BRICK_WIDTH
        end_y = start_y + BRICK_HEIGHT
        color = random.choice(COLORS)

        canvas.create_rectangle(start_x, start_y, end_x, end_y, color, 'black')
        #canvas.wait_for_click()
        #time.sleep(0.02)
    

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
