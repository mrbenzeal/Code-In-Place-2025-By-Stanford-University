"""
File: Khansole_Academy_Extension.py
---------------------------------------------
This program randomly generates simple addition problems for the user,
(2-digit integers (i.e., the numbers 10 through 99))
reads in the answer from the user, and then checks to see
if they got it right or wrong, until the user appears to
have mastered the material.
(The program keeps giving the user problems until the user
has gotten 3 problems correct in a row)
"""

import random

# Define constants
CONSECUTIVE_CORRECT_ANSWERS_NEEDED = 3
SUM_RANGE_MIN = 10
SUM_RANGE_MAX = 99


def main():
    # Initialise the Khansole
    print("Khansole Academy")
    number_of_consecutive_correct_solutions = 0
    
    # Repeat questions until defined number of constants reached
    while number_of_consecutive_correct_solutions < CONSECUTIVE_CORRECT_ANSWERS_NEEDED:
        
        # Generate random 2-digit numbers
        num1 = random.randint(SUM_RANGE_MIN, SUM_RANGE_MAX)
        num2 = random.randint(SUM_RANGE_MIN, SUM_RANGE_MAX)
        
        # Print question
        print(f"What is {num1} + {num2}?")
        sum_solution = num1 + num2
        
        # Capture user input
        sum_user = int(input("Your answer: "))
        
        # Check if solution correct or not
        if sum_user == sum_solution:  # correct
            # Increment number of correct solutions by 1
            number_of_consecutive_correct_solutions += 1
            
            # Print message
            print("Correct!\nYou've gotten {} correct in a row.".format(
                number_of_consecutive_correct_solutions
            ))
        
        else:  # incorrect
            # Reset number of correct solutions to 0
            number_of_consecutive_correct_solutions = 0
            
            # Print message
            print("Incorrect!")
            print(f"The expected answer is {sum_solution}")
        
        # Add an extra space between questions
        print()
    
    # Exit message  
    print("Congratulations! You mastered addition.")
    

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
  
