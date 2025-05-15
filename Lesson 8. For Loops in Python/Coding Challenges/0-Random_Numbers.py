"""
File: Random_Numbers.py
------------------------
This program prints a series of 10 random numbers in the
range from 1 to 100.
"""

import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    """
    this code is printing a random number in a loop, 
    repeating this action ten times. 
    And each number is independently randomly selected between 1 and 100.
    """
    for i in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE))


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
