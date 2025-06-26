"""
File: Spring_Flowers.py
------------------------
This program instructs Karel to start in the bottom left corner of a world 
with 2 empty flower stems, facing East.
Karel will bloom both flowers with beepers 
and end in the bottom right corner of the world facing East.
"""

# This tells Python who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

def main():
    # Karel makes springtime happen by blooming both flower stems in the world!
    for i in range(2):  # We know there will be exactly two stems, so we can use a for-loop to bloom them!
        move_to_wall()  # Move to the next stem
        bloom_flower()
    move_to_wall()  # Fencepost problem! This fixes it. :)


def bloom_flower():
    """
    Karel places a bloom on top of the stem she is facing.
    Pre: Karel is on row 1 to the immediate left of a stem facing East.
    Post: Karel is on row 1 to the immediate right of a stem facing East.
    """
    climb_stem()
    make_bloom()
    move_to_wall()
    turn_left()


def climb_stem():
    """
    Karel climbs the stem until the top, at the bottom left corner of where the bloom will go.
    Pre: Karel is at the base of the stem facing East.
    Post: Karel is at the bottom left corner of the bloom facing North.
    """
    turn_left()
    while right_is_blocked():
        move()


def make_bloom():
    """
    Karel makes the flower bloom with beepers!
    Pre: Karel is on the bottom left corner of the bloom facing North
    Post: Karel is on the bottom right corner of the bloom facing South
    """
    # Makes a square of beepers
    put_beeper()
    move()
    for i in range(2):
        put_beeper()
        turn_right()
        move()
    put_beeper()


def move_to_wall():
    # Karel moves until blocked.
    while front_is_clear():
        move()


def turn_right():
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
