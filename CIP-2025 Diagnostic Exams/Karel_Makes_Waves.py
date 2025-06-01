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
  
