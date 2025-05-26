"""
File: Ones_Digit.py
--------------------
This program writes a function called print_ones_digit , 
which takes as a parameter an integer num, 
finds the modulo (%) of the num, 
by dividing the num by 10 
and prints its ones digit or modulo (remainder).
"""

def print_ones_digit(num):
    print("The ones digit is", num % 10)


def main():
    num = int(input("Enter a number: "))
    # Calling my helper function with `num` as a parameter!
    print_ones_digit(num)
    
    
"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
