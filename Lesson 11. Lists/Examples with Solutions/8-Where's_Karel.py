"""
File: Where's_Karel.py
-----------------------
This is a program that fill in the function find_karel(roster) 
which takes in a list, roster, and prints "Karel is here!" 
if 'karel' is an element in roster, or prints "Karel isn't here." 
if 'karel' isn't an element in roster. 
You can assume all elements in roster will be lowercase.
"""

def find_karel(roster):
    """
    Prints "Karel isn't here." if 'karel' is not in the list `roster` and "Karel is here!" if 'karel' is present in `roster`.
    """
    if 'karel' in roster:
        print("Karel is here!")
    else:
        print("Karel isn't here.")


def get_list():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list. All elements will be lowercase.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem.lower())
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst


def main():
    roster = get_list()
    find_karel(roster)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
