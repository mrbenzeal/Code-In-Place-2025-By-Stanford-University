"""
File: Move_Beeper.py
---------------------
This program has Karel pick up the beeper, 
move to the top of the world, 
put the beeper down at the top of column 2, 
and then end up in the top right corner.
"""

from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world 
    and ends facing East in the bottom right corner of the world.
    """
    move()
    pick_beeper()
    turn_left()
    move()
    move()
    put_beeper()
    turn_right()
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
