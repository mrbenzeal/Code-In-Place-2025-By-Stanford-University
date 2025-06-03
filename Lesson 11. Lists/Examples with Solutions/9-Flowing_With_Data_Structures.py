"""
File: Flowing_With_Data_Structures.py
--------------------------------------
This is a program that .
"""

def add_three_copies(my_list, data):
    """Adds three copies of data to the list"""
    for _ in range(3):
        my_list.append(data)


def main():
    # Get user input
    message = input("Enter a message to copy: ")

    # Initialize empty list
    my_list = []
    print("List before:", my_list)

    # Add three copies to list
    add_three_copies(my_list, message)

    # Show modified list
    print("List after:", my_list)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == "__main__":
    main()
