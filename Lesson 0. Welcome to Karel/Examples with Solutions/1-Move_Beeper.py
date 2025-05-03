from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
    move()
    pick_beeper()
    turn_left()
    move()
    move()
    put_beeper()
    turn_right()
    move()

# the definition of turn_right (Karel turn right by turning left three times)
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()
