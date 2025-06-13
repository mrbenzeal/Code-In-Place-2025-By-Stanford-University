"""
This is an all round worked example of a graphical program 
that create both objects and animations.
"""

from graphics import Canvas
import time
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
TRIANGLE_WIDTH = 100
TRIANGLE_HEIGHT = 100
SQUARE_SIZE = 50 
BALL_SIZE = 40 
DELAY = 0.001    # seconds to wait between each update


def main():
    # Create my canvas to draw on
    my_canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Point 1: Bottom Left
    x1 = (CANVAS_WIDTH - TRIANGLE_WIDTH)/2 # 150
    y1 = (CANVAS_HEIGHT + TRIANGLE_HEIGHT)/2 # 250
    
    # Point 2: Bottom Right
    x2 = (CANVAS_WIDTH + TRIANGLE_WIDTH)/2 # 250
    y2 = (CANVAS_HEIGHT + TRIANGLE_HEIGHT)/2 # 250
    
    # Point 3: Middle
    x3 = CANVAS_WIDTH/2 # 200
    y3 = (CANVAS_HEIGHT - TRIANGLE_HEIGHT)/2 # 150

    # set y coordinates for the square
    start_y = (CANVAS_WIDTH / 2) + (SQUARE_SIZE * 2) # 300
    end_y = start_y + SQUARE_SIZE # 350

    # change on the x and y cordinates for the ball
    change_x = 1
    change_y = 1

    # Creating Objects and saving them in variables
    # By default, all are drawn in black if you omit the color parameter.
    # Objects are drawn on the canvas in the order in which they are created by your code
    # the latter drawn object(s) can potentially cover (occlude) part of the the formerly drawn object(s).
    # This is sometimes referred to as the z-order of the objects

    # drawing black lines
    first_line = my_canvas.create_line(10, 10, 100, 10, 'black')
    second_line = my_canvas.create_line(10, 20, 100, 40)
    
    # drawing a rectangle
    yellow_rectangle = my_canvas.create_rectangle(5, 50, 100, 200, 'yellow')
    
    # drawing an oval
    red_oval = my_canvas.create_oval(5, 50, 100, 200, 'red')
    
    # drawing a triangle
    black_triangle = my_canvas.create_polygon(x1, y1, x2, y2, x3, y3)
    orange_triangle = my_canvas.create_polygon(110, 140, 170, 140, 140, 50, color='orange')
    
    # creating text on the canvas
    my_text = my_canvas.create_text(110, 10, font='Arial', font_size = 20, text="Mr. Obinna Ani's Graphics", color='blue')
    
    # drawing a brown line
    brown_line = my_canvas.create_line(120, 60, 160, 100, color='brown')
    
    # drawing a square
    blue_square = my_canvas.create_rectangle(0, start_y, SQUARE_SIZE, end_y, 'blue')
    
    # drawing a ball and storing it in a variable
    brown_ball = my_canvas.create_oval(0, 0, BALL_SIZE, BALL_SIZE, 'brown')

    # Note:
    # if we make a variable of an object: second_line = my_canvas.create_line(10, 20, 100, 40)
    # We can remove the object from the canvas by using: my_canvas.delete(second_line) 

    # Also note that deleting an object is permanent 
    # if you want to temporarily make an object hidden, 
    # we use set_hidden. 
    # We can pass in either True or False to set an object to be hidden or visible:
    # if: second_line = my_canvas.create_line(10, 20, 100, 40)
    # then: my_canvas.set_hidden(second_line, True)  # no longer visible
    # or: my_canvas.set_hidden(second_line, False) # visible again

    # We can change the colour of an object by: my_canvas.set_color(var_second_line, 'red')
    # We can also individually change the outline or fill of an object using the set_fill_color
    # and set_outline_color functions as follows: my_canvas.set_fill_color(second_line, 'green')
    # or: my_canvas.set_outline_color(second_line, 'blue')

    # We can get an object's dimensions via get_obj_width and get_obj_height: 
    
    """print(my_canvas.get_obj_width(second_line))  # prints 50
    print(my_canvas.get_obj_height(second_line)) # prints 100"""

    # We can also ask the canvas for information about an object's location
    print(my_canvas.get_left_x(red_oval))  # prints 5
    print(my_canvas.get_top_y(red_oval))   # prints 50

    # We can change the location (specify new x and y coordinates) of an object using 'moveto' or 'move'

    # animation loop for the blue square
    """while my_canvas.get_left_x(blue_square) < start_y:
        my_canvas.move(blue_square, 1, 0)
   
        # pause
        time.sleep(DELAY)"""

    # animation loop for the brown ball
    while(True):
        left_x = my_canvas.get_left_x(brown_ball)
        top_y = my_canvas.get_top_y(brown_ball)

        """# Here is a list of a few other helpful functions that can be used to make some super cool animated programs! 

        # get the coordinates of the mouse
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()

        # wait for a click
        canvas.wait_for_click()"""
        
        # change direction if ball reaches an edge
        if left_x < 0 or left_x + BALL_SIZE >= CANVAS_WIDTH:
            change_x = -change_x
        
        if top_y < 0 or top_y + BALL_SIZE >= CANVAS_HEIGHT:
            change_y = -change_y

        # update the ball
        my_canvas.move(brown_ball, change_x, change_y)
        
        # pause
        time.sleep(DELAY)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()  
