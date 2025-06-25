"""
File: Backflip.py
-----------------
This program has Karel to do a cool backflip by turning left 4 times.
"""

from karel.stanfordkarel import *

def main():
    """
    Making Karel do a sick backflip by turning left 4 times.
    """
    for i in range(4):
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
