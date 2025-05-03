from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    # pass
  
    put_beeper()

    while(front_is_clear()):
        move()

    put_beeper()
    turn_around()

    while(front_is_clear()):
        move()

    turn_around()

    move()
    while(no_beepers_present()):
        # move()
        turn_around()
        move()
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        move()
        
        while(no_beepers_present()):
            move()

    
        turn_around()
        move()
            
    if(facing_east()):
      pick_beeper()
      turn_around()
      move()
      turn_around()

    if(facing_west()):
      turn_around()
      move()
      pick_beeper()
      turn_around()
      move()
      turn_around()


def turn_around():
    for i in range(2):
        turn_left()
  

if __name__ == '__main__':
    main()
