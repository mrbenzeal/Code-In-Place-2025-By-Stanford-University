"""
File: Double_List.py
---------------------
This is a program that doubles each element in a list of numbers.
"""

def main():
    numbers = [1, 2, 3, 4]  # Creates an Original list of numbers

    # Double each number using list comprehension
    numbers = [num * 2 for num in numbers]

    # Double each number using the for loop
    """
    for i in range(len(numbers)):  # Loop through the indices of the list
        elem_at_index = numbers[i]  # Get the element at index i in the numbers list
        numbers[i] = elem_at_index * 2  # Set the element at index i to be equal to the previous element times 2
    """
    print(numbers) # This should print the doubled list


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
