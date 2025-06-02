"""
File: Add_Many_Numbers.py
--------------------------
This is a program that write a function that takes a list of numbers 
and returns the sum of those numbers.
"""

def add_many_numbers(numbers):
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total = 0
    for num in numbers:
        total += num
    return total


def main():
    # Test case
    numbers = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum above
    

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
