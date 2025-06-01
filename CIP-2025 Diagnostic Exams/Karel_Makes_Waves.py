"""
File: Draw_Flag.py
-------------------
This is a program that draws the flag of Indonesia using Python graphics.
To draw the Indonesian flag all we did was to draw a single red rectangle 
which covers the top half of the graphics canvas. 
We don't need to draw the white stripe, because the canvas is white by default.
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
  
