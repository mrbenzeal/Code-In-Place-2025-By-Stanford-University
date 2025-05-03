"""
This is a worked example. It shows an example of Karel
using a while loop to place a row of beepers
"""

from karel.stanfordkarel import *

"""
this whole main function instructs karel to: 
place 10 beepers in each position in the bottom row, 
and end in the bottom right corner of the world.
"""
def main():
    while front_is_clear():
        put_beeper_ten_times()
        move()
    # this is a fence-post bug correction
    put_beeper_ten_times()

# this function instruct karel to place 10 beepers in each position in the bottom row
def put_beeper_ten_times():
    for i in range(10):
        put_beeper()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
