"""
File: Obstacles.py
-------------------
This program gets Karel over the obstacles, 
puts beepers in the squares directly to the right of the walls, 
and moves Karel to the bottom right corner of the world.
"""

from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world 
    and ends facing East in the bottom right corner of the world.
    """
    move()
    turn_left()
    move()
    turn_right()
    move()
    go_in_put_beeper_and_leave()
    move()
    go_in_put_beeper_and_leave()
    move()
    turn_right()
    move()
    put_beeper()
    turn_left()
    move()
    move()


# the definition of turn_right (Karel turn right by turning left three times)
def turn_right():
    for i in range(3):
        turn_left()
    

# this definition gets Karel into the obstacle walls, put the beeper and leave 
def go_in_put_beeper_and_leave():
    turn_right()
    move()
    put_beeper()
    turn_left()
    turn_left()
    move()
    turn_right()


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
