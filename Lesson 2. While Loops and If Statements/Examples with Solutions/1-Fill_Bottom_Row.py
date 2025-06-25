"""
File: Fill_Bottom_Row.py
-------------------------
This program has Karel use a while loop to place a row of beepers.
"""

from karel.stanfordkarel import *

def main():
    """
    this main function fills entire bottom row of any sized world with beepers.
    """
    while front_is_clear():
        put_beeper()
        move()
    # this is a fence-post bug correction
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
