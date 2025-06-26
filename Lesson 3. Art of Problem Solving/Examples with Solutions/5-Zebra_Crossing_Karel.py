"""
File: Zebra_Crossing_Karel.py
------------------------------
This program instructs Karel to make a Zebra crossing, 
defined as as a pattern of:
2-square wide column of beepers, 
followed by repeating pairs of a 3-square wide gap 
and a 2-square wide column of beepers. 
"""

# This tells Python who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

def main():
    draw_stripe()
    while front_is_clear():  # We don't know exactly how many stripes we will need, so use a while-loop.
        for i in range(4):  # We know that there are 3 squares between each stripe, so use a for-loop to go to the next stripe's starting location.
            move()
        draw_stripe()  # This while-loop assumes Karel starts and ends drawing a stripe facing East on row 1!


def draw_stripe():
    """
    Draws a two-column stripe as described in the prompt.
    Pre: Karel is on row 1 facing East.
    Post: Karel is on row 1 facing East, one column over.
    """

    # Place the stripe's first column of beepers.
    turn_left()  # Face North for beeper_column()'s pre-condition
    beeper_column()

    # Move to the next column
    turn_right()
    move()

    # Place the stripe's second column of beepers
    turn_right()  # Face South for beeper_column's pre-condition
    beeper_column()
    turn_left()  # Face East


def beeper_column():
    """
    Places one column of beepers.
    Pre: Karel is either:
           - On row 1 facing North or,
           - On the top-most row facing South
    Post: If Karel started on row 1, they are now on the top-most row facing North.
          If Karel started on the top-most row they are now on row 1 facing South.
    """
    put_beeper()  # Fencepost problem! This initial put_beeper() fixes it.
    while front_is_clear():  # We don't know how tall the column is, so use a while-loop to travel it
        move()
        put_beeper()


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
