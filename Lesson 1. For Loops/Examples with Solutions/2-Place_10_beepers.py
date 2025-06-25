"""
File: Place_10_beepers.py
--------------------------
This program has Karel place 10 beepers on the spot Karel is currently standing on.
"""

from karel.stanfordkarel import *

def main():
    """
    Places 10 beepers in the spot that Karel is standing.
    """
    for i in range(10):
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
