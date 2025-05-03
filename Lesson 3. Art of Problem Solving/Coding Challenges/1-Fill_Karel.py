# This tells Python who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *


"""
# Section 1: Karel the Robot
# Fill Karel.

This code instructs karel to walk along the rows,
full of blocking walls; filling it with beepers.

Pre: Karel is at the bottom-left corner, 
facing east.

Post: Karel is at the top-right corner, 
facing east.
"""
def main():
    while front_is_clear():
        if left_is_clear():
            fill_with_beepers()
            move_if_possible()
            return_to_first_column()
            move_to_next_row()
        else:
            fill_with_beepers()
            move_until_blocked()
    move_if_possible()


"""
#fill_with_beepers()

karel moves along the rows; 
filling it with beepers.

Pre: Karel is at the bottom-left corner, 
facing east.

Post: Karel is at the top-right corner, 
facing east.
"""
def fill_with_beepers():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


"""
#move_if_possible()

this function enables Karel to move along the rows; 
the exclusion of it will cause Karel not to move.
"""
def move_if_possible():
    if front_is_clear():
        move()


"""
#return_to_first_column()

Karel returns to the first column of each row.

Pre: Karel is at the right corner of the rows, 
facing east.

Post: Karel is at the left corner of the rows, 
facing west.
"""
def return_to_first_column():
    turn_around() 
    move_until_blocked() 


"""
#turn_around()

Karel turns around, facing west.

Pre: Karel is at the right corner of the rows, 
facing east.

Post: Karel is at the right corner of the rows, 
facing west.
"""
def turn_around():
    turn_left()
    turn_left()


"""
#move_until_blocked()

Karel moves to the first column of each row.

Pre: Karel is at the right corner of the rows, 
facing west.

Post: Karel is at the left corner of the rows, 
facing west.
"""
def move_until_blocked():
    while front_is_clear():
        move()


"""
#move_to_next_row()

Karel moves up the rows through the first column.

Pre: Karel is at the initial row of the first column,
facing west.

Post: Karel moves up the next row of the first column, 
facing east.
"""
def move_to_next_row():
    make_right_turn()
    move()
    make_right_turn()


"""
#make_right_turn()

Make Karel to turn left thrice (3), 
"""
def make_right_turn():
    for i in range(3):
        turn_left()


"""
This is a boilerplate code which launches our code
when we hit the run button.
# There is no need to edit code beyond this point
"""
if __name__ == '__main__':
    main()
