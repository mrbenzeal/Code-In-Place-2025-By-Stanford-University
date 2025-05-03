# This tells Python who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *


"""
# Section 1: Karel the Robot
# Stone Mason Karel.
This code instructs karel to walk along the row,
building columns of stones (beepers), 
assumed to be of five (5) units high 
and exactly four squares apart, 
on the 1st, 5th, 9th, and 13th columns.
"""
def main():
    while front_is_clear():
        build_column()
        move_four_steps() 
        move_if_possible() 
    """
    fencepost problem! 
    One more column to build. 
    This last build_column() fixes it.
    """
    build_column() 
    

"""
#build_column()
Karel build columns of stones (beepers).
Pre-condition: Karel is at the left end of the
bottom row, facing east.
Post-condition: Karel is at the right end of the
bottom row, facing east.
"""
def build_column():
    turn_left()
    place_five_stones()
    return_to_base() 
    turn_left()


"""
#place_five_stones()
Karel puts 5 stones (beepers) on the columns.
Pre: Karel is at the base of the
unbuilt column, facing north.
Post: Karel is at the top of the
built column, facing north.
"""
def place_five_stones():
    for i in range(4):
        put_beeper()
        move()
    """
    fencepost problem! 
    One more stone (beeper) to put. 
    This last put_beeper() fixes it.
    """
    put_beeper() 


"""
#return_to_base()
Karel returns to the base of the built columns.
Pre: Karel is at the top of the
built column, facing north.
Post: Karel is at the base of the
built column, facing south.
"""
def return_to_base():
    turn_around() 
    move_to_wall() 


"""
#turn_around()
Karel turns around, facing south.
Pre: Karel is at the top of the
built column, facing north.
Post: Karel is at the top of the
built column, facing south.
"""
def turn_around():
    turn_left()
    turn_left()


"""
#move_to_wall()
Karel moves to the base of the built column, 
facing south.
Pre: Karel is at the top of the built column, 
facing south.
Post: Karel is at the base of the built column, 
facing south.
"""
def move_to_wall():
    while front_is_clear():
        move()


"""
#move_four_steps()
Karel moves along the bottom row, 
making a stop at every 4 steps.
"""
def move_four_steps():
    for i in range(3):
        move()


"""
#move_if_possible()
this function enables Karel to move along the row; 
the exclusion of it will cause Karel not to move.
"""
def move_if_possible():
    if front_is_clear():
        move()


"""
This is a boilerplate code which launches our code
when we hit the run button.
# There is no need to edit code beyond this point
"""
if __name__ == '__main__':
    main()
