"""
File: Step_Up.py
-----------------
This program has Karel pick up the beeper and put it on the ledge.
"""

# This tells PyCharm who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

# this program executes in a special function called main
def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
    move()

# the definition of turn_right (Karel turn right by turning left three times)
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
