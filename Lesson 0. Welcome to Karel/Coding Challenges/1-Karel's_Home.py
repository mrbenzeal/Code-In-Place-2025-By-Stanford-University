from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    move_two_steps()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move_two_steps()
    turn_around()


def move_two_steps():
    move()
    move() 


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
