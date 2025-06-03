"""
File: Get_List.py
------------------
This is a program that continuously asks the user to enter values 
which are added one by one into a list. 
When the user presses enter without typing anything, print the list.
"""

def main():
    # Initialize an empty list to store things in
    my_list = []
    
    # Get first input
    value = input("Enter a value: ")
    
    # Keep asking for input until empty string
    while value != "": # While the user input isn't an empty value
        # Add value to list
        my_list.append(value)
        # Get the next value to add
        value = input("Enter a value: ")
    
    # Print the final list
    print("Here's the list:", my_list)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
