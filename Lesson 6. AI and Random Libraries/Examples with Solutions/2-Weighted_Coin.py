"""
File: Weighted_Coin.py
------------------
Simulate flip a weighted coin. this  is a coin where the probability of heads isn't 50%.
This program uses the random module to "flip" coin where the probability of heads is 70% 
and print the outcome (heads or tails).
"""

# Import the random library which lets us simulate the coin flip!
import random

PROBABILITY_OF_HEADS = 0.70 # 70% chance of heads

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality 
of printing to the console.
"""
def main():
    # geting the probability
    random_draw = random.random() # random.random() returns a random floating num between 0 and 1

    if random_draw < PROBABILITY_OF_HEADS: 
        print("Heads!")  # 70% of heads
    else:
        print("Tails!")  # 30% of tails
        

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
