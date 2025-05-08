"""
Program: Multiply_Two_Numbers.py
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality 
of printing to the console.
"""
def main():
    """
    This block of code after 
    - printing "This program multiplies two numbers."
    - prompt the user to enter the first number.
    - read the input and convert it to an integer.
    - prompt the user to enter the second number.
    - read the input and convert it to an integer.
    - calculate the value of multiplying the two numbers.
    - and print the value to the terminal
    """
    print("This program multiplies two numbers.")
    
    # this collects a text value from the user; storing it in the variable 'first_number'
    first_number = input("Enter first number: ")

    # this converts 'first_number' from string to integer.
    first_number = int(first_number)

    # this collects a text value from the user; storing it in the variable 'second_number'
    second_number = input("Enter second number: ")

    # this converts 'second_number' from string to integer.
    second_number = int(second_number)

    # this multiplies the converted integer values in 'first_number' & 'second_number'; storing it in the variable 'total'
    total = first_number * second_number

    # this prints the string value of the total to the terminal
    print(str(total))


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
