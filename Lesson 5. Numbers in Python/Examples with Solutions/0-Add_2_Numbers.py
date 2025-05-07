"""
Program: add_2_numbers.py
--------------------------
This is a python program to get some practice with
variables.  This program asks the user for two
integers and prints their sum.
"""

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality 
of printing to the console.
"""
def main():
    # this prints the text "This program adds two numbers." to the terminal
    print("This program adds two numbers.")

    # this collects a text value from the user; storing it in the variable 'num_1'
    num_1 = input("Enter first number: ")

    # this converts 'num1' from string to integer.
    num_1 = int(num_1)

    # this collects a text value from the user; storing it in the variable 'num_2'
    num_2 = input("Enter second number: ")

    # this converts 'num_2' from string to integer.
    num_2 = int(num_2)
    
    # this sums up the converted integer values in 'num_1' & 'num_2';
    # storing it in the variable 'total'
    total = num_1 + num_2

    """
    # this prints the concatenated texts of: 
    " The total is " 
    " a converted textual value of the variable 'total' " 
    and " the period sign '.' " to the terminal
    """
    print("The total is " + str(total) + ".")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
  
