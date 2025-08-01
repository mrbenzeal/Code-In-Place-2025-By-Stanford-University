"""
This is an example of a program that has Karel 
place a square of beepers. It uses a for loop
that has multiple lines in the loop.
"""

# This tells python who Karel is!
from karel.stanfordkarel import *

# this program executes in a special function called main
def main():
    for i in range(4):
        move()
        put_beeper()
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
