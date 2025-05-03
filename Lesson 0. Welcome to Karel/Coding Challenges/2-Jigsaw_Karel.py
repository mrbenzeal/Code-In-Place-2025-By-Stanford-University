from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""

# this program executes in a special function called main
def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move_two_steps()
    pick_beeper()
    move()
    turn_left()
    move_two_steps()
    put_beeper()
    turn_left_twice()
    move_two_steps()
    turn_right()
    move_two_steps()
    move()
    turn_left_twice()

# this definition instructs Karel to move two steps
def move_two_steps():
    move()
    move()

# this definition instructs Karel to turn_left twice
def turn_left_twice():
    turn_left()
    turn_left()

# this definition instructs Karel turn right by turning left three times)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
