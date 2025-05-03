from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
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
    turn_left()
    turn_left()
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


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
