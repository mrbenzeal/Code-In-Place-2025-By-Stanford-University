"""
DIAGNOSTIC_EXAM
----------------
File: Karel_Makes_Waves.py
---------------------------
Write a program that has Karel draw four small "waves". Each wave is a triangle made up of three beepers. 
There is a gap between each wave.

A few notes:
- Karel always begins at the bottom left corner of the world, facing East
- Karel's bag has infinite beepers.
- It does not matter which direction Karel ends up facing.
- You may assume that the world is always exactly 11 columns wide and 5 columns tall. 
- Your program only needs to work for this sized world.
- You must not use any non-Karel features like variables, return or break. 
- You may use any Karel features described in the course reader.
"""

from karel.stanfordkarel import *

def main():
    while front_is_clear():
        put_beeper()
        move()
        turn_left()
        put_beeper()
        move()
        put_beeper()
        turn_around()
        move()
        turn_left()
        if front_is_clear():
            move()
            move()


def turn_around():
    for i in range(2):
        turn_left()  
   

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
  
