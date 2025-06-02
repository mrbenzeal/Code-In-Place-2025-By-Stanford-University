"""
File: Get_First_Element.py
---------------------------
This is a program that fill out the function get_first_element(lst)
which takes in a list lst as a parameter and prints the first element in the list.
The list is guaranteed to be non-empty.
"""

def get_first_element(lst):
    """
    Prints the first element of the list.
    """
    print(lst[0])


def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst


def main():
    lst = get_lst()
    get_first_element(lst)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
