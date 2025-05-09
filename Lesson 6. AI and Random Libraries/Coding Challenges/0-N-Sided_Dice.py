"""
File: N-Sided_Dice.py
------------------
This is a program which takes as input the number of sides on a dice. 
Then, simulates rolling a dice with that many sides. 
And prints the outcome of the roll.
# Note: not all dice have 6 sides! Some have multiple (e.g., 8, 20, etc.)
"""

# Import the random library which lets us simulate random things like dice!
import random

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality 
of printing to the console.
"""
def main():
    sides = input("How many sides does your dice have? ")
    sides = int(sides)
    roll = random.randint(1, sides)
    print(f"Your roll is {roll}")


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
