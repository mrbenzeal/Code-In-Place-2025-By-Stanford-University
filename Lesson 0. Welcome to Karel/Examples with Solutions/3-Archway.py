"""
File: Archway.py
-----------------
This program has Karel move up and over the archway, 
so Karel ends up on the right side of it, facing East.
"""

from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world 
    and ends facing East in the bottom right corner of the world.
    """
    turn_left()
    move_thrice()
    turn_right()
    move_thrice()
    turn_right()
    move_thrice()
    turn_left()


# the definition the gets Karel to move three steps
def move_thrice():
    for i in range(3):
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
    
