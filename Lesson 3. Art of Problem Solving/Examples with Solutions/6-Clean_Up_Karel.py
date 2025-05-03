# This tells Python who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

"""
This code instructs Karel to clean up all the beepers been spread across her world. 
Note: The starter code was a solution, but it was messy! 
I was able to decompose it by looking at some of the comments for ideas.
"""

def main():
    # If we aren't at the top row (we use a while loop because we don't know how many rows there are)
    while left_is_clear():
        ### Pick up a row of beepers ###
        while front_is_clear():
            # Pick up a beeper if present
            if beepers_present():
                pick_beeper()
            move()
            
        if beepers_present():
            pick_beeper()
        
        ### Move back to the first column ###
        # Turn around
        for i in range(2):
            turn_left()
        
        # Move to wall
        while front_is_clear():
            move()
        
        ### Move up to the next row ###
        # Turn right
        for i in range(3):
            turn_left()
        move()
        
        ### Reset Karel for loop pre-conditions by turning right to face East ###
        for i in range(3):
            turn_left()
    
    ### Pick up the final row of beepers ###
    while front_is_clear():
        # Pick up a beeper if present
        if beepers_present():
            pick_beeper()
        move()
    
    if beepers_present():
        pick_beeper()
        

# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()
