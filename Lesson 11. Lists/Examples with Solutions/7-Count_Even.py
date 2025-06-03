"""
File: Count_Even.py
--------------------
This is a program that fill out the function count_even(lst) which 
- first populates a list by prompting the user for integers until they press enter 
  (please use the prompt "Enter an integer or press enter to stop: "), 
- and then prints the number of even numbers in the list. 
"""

def main():
    lst = get_list_of_ints()
    count_even(lst)
    

def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = 0  # Stores the count of even numbers in the list
    for num in lst:  # Loop through the numbers in the list
        if num % 2 == 0:  # If the current number in the list is even (divisible by 2)
            count += 1  # Add one to our count!

    # Here's another way to do this same thing, with a different kind of for-loop:
    # for i in range(len(lst)):
    #     num = lst[i]
    #     if num % 2 == 0:
    #         count += 1

    print(count)  # Print out how many even numbers we counted above


def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  # Make an empty list to store integers
    user_input = input("Enter an integer or press enter to stop: ")  # Get user input for an integer
    while user_input != "":  # While the user doesn't enter nothing...
        lst.append(int(user_input))  # Cast the user input into an integer and add it to our list
        user_input = input("Enter an integer or press enter to stop: ")  # Get the next user input

    return lst


"""
def count_even(lst):
    
    # Counts and prints the number of even integers in a list.
    
    # Args:
        # lst: List of integers to check
        
    # Returns:
        # None (prints the count directly)
    
    even_count = sum(1 for num in lst if num % 2 == 0)
    print(f"Number of even numbers: {even_count}")

def get_list_of_ints():
    
    # Collects integers from user until empty input is received.
    
    # Returns:
        # List of integers entered by user
    
    numbers = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ").strip()
        if not user_input:  # Empty input ends collection
            break
        try:
            numbers.append(int(user_input))
        except ValueError:
            print(f"'{user_input}' is not a valid integer. Please try again.")
    return numbers

def main():
    print("Even Number Counter")
    print("-------------------")
    numbers = get_list_of_ints()
    
    if numbers:  # Only proceed if list is not empty
        print(f"\nYou entered: {numbers}")
        count_even(numbers)
    else:
        print("\nNo numbers were entered.")
"""


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
