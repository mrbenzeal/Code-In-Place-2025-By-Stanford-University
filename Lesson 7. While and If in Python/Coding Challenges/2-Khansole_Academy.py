"""
File: Khansole_Academy.py
--------------------------
This program randomly generates simple addition problems for the user,
(2-digit integers (i.e., the numbers 10 through 99))
reads in the answer from the user, and then checks to see
if they got it right or wrong, until the user appears to
have got problem correct.
The program keeps giving the user problems until the user get problem correct.
"""

import random 

def main():
    # Initialise the Khansole
    print("Khansole Academy")
    # Calculate two random number 
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    # Print two random numbers between 10 and 99 as an adition
    print(f"What is {num1} + {num2}?")
    # Ask the user type the result
    answer = input("Your answer: ")
    result = int(num1) + int(num2)
    # If the answer type for th user is correct show a message "correct!"
    if int(answer) == result:
        print("Correct!")
    else:
        print(f"Incorrect.\nThe expected answer is {result}")
    # If the answer type for the user is incorrect, print the value of the expected value
    

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
  
