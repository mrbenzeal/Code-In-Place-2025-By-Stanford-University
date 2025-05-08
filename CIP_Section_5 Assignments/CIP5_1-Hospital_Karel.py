# This tells Python who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

"""
# Section 1: Karel the Robot
# Program: Hospital_Karel.py
This code instructs karel to walk along the row, 
picks up supplies from the places marked by each beeper
and build a new hospital in the places marked by each beeper. 
Each hospital will be of two columns of three beepers.
"""
def main():
    while front_is_clear():
        if beepers_present():
            build_hospital() 
        move_if_possible() 


#A
def build_hospital():
    """
    # Karel picks up supplies and builds a hospital.
    Pre-condition: Karel is on a beeper, representing a
    pile of supplies. facing east.
    Post-condition: Karel is standing at the base
    of the last column of the hospital, facing east.
    """
    # pick up supplies *
    pick_beeper()
    do_one_column()
    move()
    do_one_column()


#A.1
def do_one_column():
    """
    # Karel builds a single column of a hospital.
    Pre: Karel is at the base of where she is to build a column,
    facing east.
    Post: Karel is at the base of the column she just built, 
    facing east.
    """
    turn_left()
    put_three_beepers() 
    return_to_base() 
    turn_left()


#A.1.a
def put_three_beepers():
    """
    # Karel is at the top of the column 
    after placing three beepers in a row, facing north.
    Pre: Karel is on the spot where she is to place the first beeper, 
    facing north.
    Post: Karel is on the top of the column 
    where she placed the third beeper in a row, facing north.
    """
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()


#A.1.b
def return_to_base():
    """
    # Karel turns around and goes to the wall.
    Pre: Karel is at the top of the column she just built, facing north.
    Post: Karel has returned to the base of the built column, facing down (south).
    """
    turn_around() 
    move_to_wall() 


#A.1.b.i
def turn_around():
    """
    # Turn Karel turns around, facing down (south).
    Pre: Karel is at the top of the built column, facing up (north).
    Post: Karel is at the top of the built column, facing down (south).
    """
    turn_left()
    turn_left()


#A.1.b.ii
def move_to_wall():
    """
    # Move Karel to the base of the built column, facing down (south).
    Pre: Karel is at the top of the built column, facing down (south).
    Post: Karel is at the base of the built column, facing down (south).
    """
    while front_is_clear():
        move()


#B
def move_if_possible():
    """
    the function enables Karel to move along the row; 
    the exclusion of it will cause Karel not to move.
    """
    if front_is_clear():
        move()


"""
This is a boilerplate code which launches our code
when we hit the run button.
# There is no need to edit code beyond this point
"""
if __name__ == '__main__':
    main()
