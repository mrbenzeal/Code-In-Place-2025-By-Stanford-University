"""
File: Square.py
----------------
This program has Karel place beepers in a square (4 beepers total) 
and end in the same position Karel starts in.
"""

from karel.stanfordkarel import *

def main():
    """
    this function instructs Karel to place beepers in a square 
    (4 beepers total) and end in the same position Karel starts in.
    """
    for i in range(4):
        put_beeper()
        move()
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
