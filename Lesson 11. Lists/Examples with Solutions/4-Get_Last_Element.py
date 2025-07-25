"""
File: Get_Last_Element.py
---------------------------
This is a program that fill out the function get_last_element(lst)
which takes in a list lst as a parameter and prints the last element in the list.
The list is guaranteed to be non-empty, but there are no guarantees on its length.
"""

def get_last_element(lst):
    """
    Prints the last element of the provided list.
    """
    print(lst[-1])  # Using negative indexing

    # The line code below works too!!
    # Taking the length of the list and minusing 1 since they are zero-indexed (we start counting at 0)
    # print(lst[len(lst) - 1])


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
    get_last_element(lst)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
