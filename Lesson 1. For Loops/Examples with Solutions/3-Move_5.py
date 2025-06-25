"""
File: Move_5.py
----------------
This program has Karel move forward 5 times
"""

from karel.stanfordkarel import *

def main():
    """
    Moves forward 5 times
    """
    for i in range(5):
        move()


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
