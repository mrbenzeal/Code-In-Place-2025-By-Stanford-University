"""
File: Double_It.py
-------------------
This is a program which prompts the user to enter a number; 
the program will then double that number and print out the result. 
It will repeat that process until the value is 100 or greater. 
"""

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality such as managing user input, 
doubling of the user entered number if it is less than 100 untill is 100 or greater
and printing to the console.
"""
def main():
    # Take user input
    curr_value = int(input("Enter a number: "))
    
    # Double as long as number is smaller than 100
    while curr_value < 100:
        curr_value = curr_value * 2  # Double value
        print(curr_value)
    

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
