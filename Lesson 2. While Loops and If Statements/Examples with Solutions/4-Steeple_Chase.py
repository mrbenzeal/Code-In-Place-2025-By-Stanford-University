"""
File: Steeple_Chase.py
-----------------------
This program has Karel runs a steeple chase that is 9 avenues long.
Hurdles are of arbitrary height and placement.
"""

from karel.stanfordkarel import *

def main():
    """
    To run a race that is 9 avenues long, we need to move
    forward or jump hurdles 8 times. Let's use a for-loop for this!
    """
    for i in range(8):
        if front_is_clear():  # If there is no hurdle to jump, move
            move()
        else:  # If there is a hurdle (the front is blocked)
            jump_hurdle()


def jump_hurdle():
    """
    Pre-condition:  Facing East at bottom of hurdle
    Post-condition: Facing East at bottom in next avenue after hurdle
    """
    ascend_hurdle()
    move()
    descend_hurdle()


def ascend_hurdle():
    """
    Pre-condition:  Facing East at bottom of hurdle
    Post-condition: Facing East immediately above hurdle
    """
    turn_left()  # Face North
    
    # While there is a wall on the Eastern side of Karel, move up a row
    while right_is_blocked():
        move()
        
    turn_right()  # Face East


def descend_hurdle():
    """
    Pre-condition:  Facing East above and immediately after hurdle
    Post-condition: Facing East at bottom of hurdle
    """
    turn_right()  # Face South
    move_to_wall()  # Move to row 1
    turn_left()  # Face East


def move_to_wall():
    """
    Pre-condition:  None
    Post-condition: Facing first wall in whichever direction
                    Karel was facing previously
    """
    while front_is_clear():
        move()


def turn_right():
    """
    Pre-condition:  None
    Post-condition: Karel is facing to the right of whichever
                    direction Karel was facing previously
    """
    for i in range(3):
        turn_left()


"""
# This is "boilerplate" code which launches your code
  when you hit the run button
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
