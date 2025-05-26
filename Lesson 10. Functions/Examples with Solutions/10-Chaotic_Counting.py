"""
File: Chaotic_Counting.py
--------------------------
This program writes a code that .
"""

import random

# Probability that counting will stop at any given number
DONE_LIKELIHOOD = 0.3  # 30% chance to stop at each number

def chaotic_counting():
    """
    Counts from 1 to 10, but may stop early based on random chance.
    At each number, there's a probability the counting will stop.
    """
    for i in range(1, 11):  # Count from 1 to 10
        if done():
            return  # Exit function early if done() returns True
        print(i)


def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False


def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == "__main__":
    main()
