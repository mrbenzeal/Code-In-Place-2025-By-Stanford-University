"""
File: 10s_Across_The_Board.py
------------------------------
This program has Karel place 10 beepers in each position in the bottom row.
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

"""
# This is "boilerplate" code which launches your code
  when you hit the run button
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
