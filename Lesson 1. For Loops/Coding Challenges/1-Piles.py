from karel.stanfordkarel import *

# File: piles.py
# -----------------------------

"""
this is a function that instructs Karel
to pick up all the beepers in the world.
"""
def main():
    move()
    pick_beepers_and_move()
    move()
    pick_beepers_and_move()
    move()
    pick_beepers_and_move()

# this definition instruct karel to pick up 10 beepers and move one step.
def pick_beepers_and_move():
    for i in range(10):
        pick_beeper()
    move()
   
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
