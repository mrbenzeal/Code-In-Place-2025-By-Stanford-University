"""
File: Weighted_Coin.py
------------------
Simulate flip a weighted coin. this  is a coin where the probability of heads isn't 50%.
This program uses the random module to "flip" coin where the probability of heads is 70% 
and print the outcome (heads or tails).
"""

# Import the random library which lets us simulate random things like dice!
import random

# define CONSTANT
HEAD_PROBABILITY = 0.7 # 70% chance of heads

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
def main():
    if random.random() < HEADS_WEIGHT:  # random.random() returns a random floating num between 0 and 1
        print("Heads!")  # 70% of heads
    else:
        print("Tails!")  # 30% of tails
"""

"""
def main():
    #for i in range(20):
    #    print(f'Coin flip {i} is: {flip_coin()}')
    print('Coin is flipped....\n...\n...')
    print(f'The result is {flip_coin()}')

def flip_coin()->str:
    toss = random.randint(1,10)
    if toss < 8:
        return 'heads'
    else:
        return 'tails'
"""

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
