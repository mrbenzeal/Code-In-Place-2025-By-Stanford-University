"""
File: Invert.py
----------------
This program has Karel "invert" each beeper in the first row. 
To invert a beeper: if there was a beeper pick it up. 
Otherwise, put one down.
"""

from karel.stanfordkarel import *

def main():
    """
    this main function inverts the pattern of beepers in a single row world.
    """
    while front_is_clear():
        invert_beeper()
        move()
    # this is a fence-post bug correction
    invert_beeper()


""" this function flips whether or not there is a beeper """
def invert_beeper():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()


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
