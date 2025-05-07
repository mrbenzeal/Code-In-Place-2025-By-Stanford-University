"""
Program: How_Old_Are_They?.py
------------------------------
This is a python program that solves an age-related riddle 
of five friends: Anton, Beth, Chen, Drew, and Ethan.
This code stores each person's age to a variable 
and print their names and ages at the end. 
"""

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality 
of printing to the console.
"""
def main():
    # The ages of each friend is stored in constant variables as follow:
    ASTON_AGE = 21
    BETH_AGE = ASTON_AGE + 6 # Beth is 6 years older than Aston
    CHEN_AGE = BETH_AGE + 20 # Chen is 20 years older than Beth
    DREW_AGE = CHEN_AGE + ASTON_AGE # Drew's age is the sum of Chen's & Aston's age
    ETHAN_AGE = CHEN_AGE # Ethan and Aston are age mates

    # The names and ages of each friend is printed to the terminal
    print("Anton is " + str(ASTON_AGE))
    print("Beth is " + str(BETH_AGE))
    print("Chen is " + str(CHEN_AGE))
    print("Drew is " + str(DREW_AGE))
    print("Ethan is " + str(ETHAN_AGE))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
