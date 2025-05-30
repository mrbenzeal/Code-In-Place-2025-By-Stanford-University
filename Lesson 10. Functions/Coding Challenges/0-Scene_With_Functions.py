"""
File: Scene_With_Functions.py
------------------------------
This program writes a code that: 
- Draw three different colored clouds at different x and y locations 
- Draw three trees with brown trunk and different colored leaves at different position.
"""

from graphics import Canvas
import math
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_cloud(canvas, 140, 10, 'salmon')
    # drawing two more clouds, and three trees
    draw_cloud(canvas, 260, 30, 'purple')
    draw_cloud(canvas, 20, 50, 'violet')
    draw_tree_1(canvas)
    draw_tree_2(canvas)
    draw_tree_3(canvas)


def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in 
    different values of x and y (the location of the cloud) and
    color (the color of the cloud). 
    """
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH

    # Bottom two puffs
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )
    """
    This function draws one cloud. You can call it and pass in 
    different values of x and y (the location of the cloud) and
    color (the color of the cloud). 
    """
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH

    # Bottom two puffs
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )


def draw_tree_1(canvas):
    """
    Draws a tree with a brown trunk and green leaves at a fixed position.
    """
    trunk_x = 50
    trunk_y_top = TREE_BOTTOM_Y - TRUNK_HEIGHT
    trunk_y_bottom = TREE_BOTTOM_Y
    # Draw trunk
    canvas.create_rectangle(
        trunk_x,
        trunk_y_top,
        trunk_x + TRUNK_WIDTH,
        trunk_y_bottom,
        'brown'
    )
    # Draw leaves as an oval centered above the trunk
    leaves_center_x = trunk_x + TRUNK_WIDTH / 2
    leaves_top = trunk_y_top - LEAVES_SIZE / 2
    leaves_bottom = trunk_y_top + LEAVES_SIZE / 2
    canvas.create_oval(
        leaves_center_x - LEAVES_SIZE / 2,
        leaves_top,
        leaves_center_x + LEAVES_SIZE / 2,
        leaves_bottom,
        'green'
    )


def draw_tree_2(canvas):
    """
    Draws a tree with a brown trunk and red leaves at a fixed position.
    """
    trunk_x = 130
    trunk_y_top = TREE_BOTTOM_Y - TRUNK_HEIGHT
    trunk_y_bottom = TREE_BOTTOM_Y
    # Draw trunk
    canvas.create_rectangle(
        trunk_x,
        trunk_y_top,
        trunk_x + TRUNK_WIDTH,
        trunk_y_bottom,
        'brown'
    )
    # Draw leaves as an oval centered above the trunk
    leaves_center_x = trunk_x + TRUNK_WIDTH / 2
    leaves_top = trunk_y_top - LEAVES_SIZE / 2
    leaves_bottom = trunk_y_top + LEAVES_SIZE / 2
    canvas.create_oval(
        leaves_center_x - LEAVES_SIZE / 2,
        leaves_top,
        leaves_center_x + LEAVES_SIZE / 2,
        leaves_bottom,
        'red'
    )
    

def draw_tree_3(canvas):
    """
    Draws a tree with a brown trunk and yellow leaves at a fixed position.
    """
    trunk_x = 310
    trunk_y_top = TREE_BOTTOM_Y - TRUNK_HEIGHT
    trunk_y_bottom = TREE_BOTTOM_Y
    # Draw trunk
    canvas.create_rectangle(
        trunk_x,
        trunk_y_top,
        trunk_x + TRUNK_WIDTH,
        trunk_y_bottom,
        'brown'
    )
    # Draw leaves as an oval centered above the trunk
    leaves_center_x = trunk_x + TRUNK_WIDTH / 2
    leaves_top = trunk_y_top - LEAVES_SIZE / 2
    leaves_bottom = trunk_y_top + LEAVES_SIZE / 2
    canvas.create_oval(
        leaves_center_x - LEAVES_SIZE / 2,
        leaves_top,
        leaves_center_x + LEAVES_SIZE / 2,
        leaves_bottom,
        'yellow'
    )
    

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main() 
