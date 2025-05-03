# This tells Python who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

"""

"""
def main():
    turn_left() # karel faces north/up
    two_step_up()
    climb_down()
    plant_beeper()


def two_step_up():
    """
    this function will help karel to find the midpoint 
    by going two step up and one step to the right
    pre: karel is facing north
    post: karel is at top row facing north
    """
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            turn_right()
            move()
            turn_left()


def climb_down():
    """
    karel will climb down from the midpoint on top row to
    the midpoint on bottom row
    pre: karel is at top row facing north
    post: karel is at bottom row facing south
    """
    turn_around()
    move_to_wall()


def plant_beeper():
    """
    karel puts the beeper and set to end position
    pre: karel at bottom row faces south
    post: karel sits on a beeper and faces east
    """
    put_beeper()
    turn_left()


def move_to_wall():
    """
    pre: karel will move forward until blocked by wall
    post: karel is facing wall 
    """
    while front_is_clear():
            move()


def turn_right():
    for i in range (3):
        turn_left()

        
def turn_around():
    for i in range (2):
        turn_left()


"""
This is a boilerplate code which launches our code
when we hit the run button.
# There is no need to edit code beyond this point
"""
if __name__ == '__main__':
    main()
