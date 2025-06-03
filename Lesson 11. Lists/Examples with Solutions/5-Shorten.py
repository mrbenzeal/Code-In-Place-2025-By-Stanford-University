"""
File: Shorten.py
-----------------
This is a program that fill out the function shorten(lst) 
which removes elements from the end of lst, 
which is a list, and prints each item it removes until lst is MAX_LENGTH items long. 
If lst is already shorter than MAX_LENGTH, it would be left unchanged.
"""

MAX_LENGTH = 3

def shorten(lst):
    """
    Takes the provided list and removes elements from the end of the list--
    printing each removed element out--until the list has at most MAX_LENGTH
    elements inside of it.
    """
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop() # Remove and get last element
        print(last_elem)
    

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
    shorten(lst)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
