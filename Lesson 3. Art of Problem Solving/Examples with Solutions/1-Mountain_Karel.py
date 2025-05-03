# This tells Python who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

"""
# The mountain karel example from the video!
This program instructs karel to climb up the mountain top, 
plant a flag (beeper) 
and climb down the mountain.
"""

def main():
    # go up the mountain, place flag and come down the mountain.
    climb_up_mountain()
    plant_flag()
    climb_down_mountain()
    

#A
def climb_up_mountain():
    """
    Pre: Karel is at the base of a mountain
    Post: Karel is standing at the top.
    Karel's front will only be clear when karel
    is at the top
    """
    while front_is_blocked():
        step_up()
        

#A1
def step_up():
    # Karel takes one step up the mountain
    # In both Pre/Post condition, Karel is facing right (East)
    turn_left()
    move()
    turn_right()
    move()


#A1a
def turn_right():
    # Makes karel turn in the clock-wise direction.
    # Works in any pre-condition state!
    for i in range(3):
        turn_left()


#B
def plant_flag():
    # a beeper, the national flag of karel land
    put_beeper()


#C
def climb_down_mountain():
    """
    Pre: Karel is at the top of the mountain, facing right
    Post: Karel is at the bottom (base) of the mountain, facing right
    Karel's front will only be blocked when
    Karel is at the base, facing the far right wall
    """
    while front_is_clear():
        step_down()
    

#C1
def step_down():
    """
    Take one step down. In both Pre/Post Karel is 
    facing right (East)
    """
    move()
    turn_right()
    move()
    turn_left()


# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()
