"""
File: Let_It_Grow.py
---------------------
This program demonstrates .
"""

from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
DELAY = 1/3
GROWTH_FACTOR = 10

def grow_leaves(canvas, leaves):
    curr_coordinates = get_corner_coordinates(canvas, leaves)
    canvas.delete(leaves)
    return canvas.create_oval(curr_coordinates[0] - GROWTH_FACTOR,
                              curr_coordinates[1] - GROWTH_FACTOR,
                              curr_coordinates[2] + GROWTH_FACTOR,
                              curr_coordinates[3] + GROWTH_FACTOR,
                              color="green")

################### No need to edit code beyond this point :) ###################

def get_corner_coordinates(canvas, canvas_obj):
    """
    Takes a canvas object and returns the coordinates as a tuple in the form of
    (left_x, top_y, right_x, bottom_y).
    """
    
    left_x, top_y = canvas.coords(canvas_obj)
    right_x = left_x + canvas.get_object_width(canvas_obj)
    bottom_y = top_y + canvas.get_object_height(canvas_obj)
    
    return left_x, top_y, right_x, bottom_y

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    leaves = make_tree(canvas)
    grow(canvas, leaves)

def make_tree(canvas):
    canvas.create_rectangle(CANVAS_WIDTH/2 - 20,
                            CANVAS_HEIGHT/4 + 20,
                            CANVAS_WIDTH/2 + 20,
                            CANVAS_HEIGHT,
                            color="#402F1D")
    
    canvas.create_line(CANVAS_WIDTH/2 - 100,
                       CANVAS_HEIGHT/4 + 60,
                       CANVAS_WIDTH/2 + 20,
                       CANVAS_HEIGHT/4 + 80,
                       color="#402F1D")
    
    canvas.create_line(CANVAS_WIDTH/2 + 80,
                       CANVAS_HEIGHT/4 + 120,
                       CANVAS_WIDTH/2 + 20,
                       CANVAS_HEIGHT/4 + 130,
                       color="#402F1D")
    
    leaves = []
    
    leaves.append(
        canvas.create_oval(CANVAS_WIDTH/2 - 20,
                           CANVAS_HEIGHT/4 - 20,
                           CANVAS_WIDTH/2 + 20,
                           CANVAS_HEIGHT/4 + 20,
                           color="green")
    )
    
    leaves.append(                   
        canvas.create_oval(CANVAS_WIDTH/2 - 100,
                           CANVAS_HEIGHT/4 + 40,
                           CANVAS_WIDTH/2 - 60,
                           CANVAS_HEIGHT/4 + 80,
                           color="green")
    )
    
    leaves.append(
        canvas.create_oval(CANVAS_WIDTH/2 + 80,
                           CANVAS_HEIGHT/4 + 100,
                           CANVAS_WIDTH/2 + 120,
                           CANVAS_HEIGHT/4 + 140,
                           color="green")
    )
    
    return leaves                 

def grow(canvas, leaves_list):
    for _ in range(8):
        for i in range(len(leaves_list)):
            leaves = leaves_list[i]
            leaves_list[i] = grow_leaves(canvas, leaves)
        
        time.sleep(DELAY)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
