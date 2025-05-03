# This tells Python who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

"""
This code instructs Karel to start at one dead end, 
move forwards through the labyrinth, 
and will eventually end up at the other dead end.
"""

def main():
    # Solves labyrinth.
    while front_is_clear(): # Move until there is nowhere to go (see what find_direction() does!)
        move_to_wall()
        find_direction()


def move_to_wall():
    while front_is_clear():
        move()


def find_direction():
    """
    Turns Karel to the unblocked direction, if an unblocked direction exists. 
    If both left and right are blocked, Karel will not turn.
    
    Pre: There is a wall in front of Karel.
    Post: Karel has turned into an unblocked direction if one exists.
    """
    if left_is_clear():
        turn_left()
    if right_is_clear():
        turn_right()


def turn_right():
    for i in range(3):
        turn_left()


# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()
