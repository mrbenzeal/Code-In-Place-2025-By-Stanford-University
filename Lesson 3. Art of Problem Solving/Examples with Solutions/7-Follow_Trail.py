"""
File: Follow_Trail.py
----------------------
This program instructs Karel to follow the trail of beepers 
(picking up beepers as she goes) until the end!
Karel will end up in the third cell down from the top right corner, facing East.
"""

# This tells Python who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

def main():
    while beepers_present():
        follow_straight_trail()
        step_backwards()
        # Check left
        turn_left()
        move()
        if no_beepers_present():
            # Trail doesn't continue to the left;
            # Go right
            step_backwards()
            turn_around()
            move()
            # Here the next iteration of the loop will check if there is a beeper; if there is we will keep going and if not we will stop!


def follow_straight_trail():
    while beepers_present():
        pick_beeper()
        move()


def step_backwards():
    """
    Turn around and go back one step, 
    then face the same way you were when you started
    """
    turn_around()
    move()
    turn_around()


def turn_around():
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
