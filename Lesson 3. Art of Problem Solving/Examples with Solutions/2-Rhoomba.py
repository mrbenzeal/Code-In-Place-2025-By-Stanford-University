"""
File: Rhoomba.py
-----------------
This program instructs karel to clear every beepers in her world 
and stay at the end of the top most row.
"""

# This tells PyCharm who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

def main():
    """
    Clear the world, row by row. Each time a row is
    cleared, reset to the start of the row to create
    a consistent pre/post of the while loop
    Left is clear until you are on the top row
    """
    while left_is_clear():  # While there is nothing to the North of Karel, clear a row
        # Note: the while-loop always assumes that Karel is facing right (east)
        clear_row()
        reset_to_next_row()
    # Fencepost problem! This last clear_row() fixes it.
    clear_row()
    
    
def clear_row():
    """
    Clear an entire row
    Pre: Karel is either facing East in column 1, or facing West in the last column
    Post: If Karel started in column 1 they are now in the last column.
          If Karel started in the last column they are now in column 1.
          The row Karel is on has no beepers in it.
    """
    while front_is_clear():  # We don't know for sure how large the world may be, so use a while loop!
        clear_corner()  
        move()
    # Fencepost problem! This last clear_corner() fixes it.
    clear_corner()
    
    
def clear_corner():
    """
    Cleans a corner so that there are no beepers on it.
    Pre: The corner Karel is on has zero or one beepers present.
    Post: The corner Karel is on has zero beepers present.
    """
    if beepers_present():
        pick_beeper()
        
        
def reset_to_next_row():
    """
    Pre: Karel is at the end of a row, facing right (East)
    Post: Karel is at the start of the next row, facing right (East)
    """
    turn_around()
    move_to_wall()
    turn_right()
    move()
    turn_right()
    

def move_to_wall():
    """
    Move Karel back to her initial start position, facing left (West).
    Pre: Karel is at the end of a row, facing left (West).
    Post: Karel is at the initial start of a row, facing left (West).
    """
    while front_is_clear():
        move()
    
    
def turn_right():
    """
    Make Karel to turn thrice (3), facing upwards (North).
    Pre: Karel is at the initial start of a row, facing left (West).
    Post: Karel is at the initial start of a row, facing upwards (North).
    """
    for i in range(3):
        turn_left()
        
        
def turn_around():
    """
    Turn Karel around, facing left (West).
    Pre: Karel is at the end of a row, facing right (East).
    Post: Karel is at the end of a row, facing left (West).
    """
    turn_left()
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
