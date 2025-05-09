"""
File: Weighted_Coin.py
------------------
Simulate flip a weighted coin. this  is a coin where the probability of heads isn't 50%.
This program uses the random module to "flip" coin where the probability of heads is 70% 
and print the outcome (heads or tails).
"""

# Import the random library which lets us simulate random things like dice!
import random

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality 
of printing to the console.
"""
def main():
    flip = random.randint(0,1)
    if flip < HEAD_PROBABILITY:
        print("Heads")
    else:
        print("Tails")


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
