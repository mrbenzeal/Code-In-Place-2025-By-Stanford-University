from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
    turn_left()
    move_three_steps()
    turn_right()
    move_three_steps()
    turn_right()
    move_three_steps()
    turn_left()

# the definition the gets Karel to move three steps
def move_three_steps():
    move()
    move()
    move()

# the definition of turn_right (Karel turn right by turning left three times)
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
