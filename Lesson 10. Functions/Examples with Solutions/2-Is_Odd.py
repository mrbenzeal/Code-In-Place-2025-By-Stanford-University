"""
File: Is_Odd.py
----------------
This program writes a code that checks numbers in the range of 10 - 20 
& prints if they are even or odd.
"""

def main():
    for i in range(10, 20):
        if is_odd(i):
            print('odd')
        else:
            print('even')
            
def is_odd(value):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1 


# v1 - v3 of the is_odd function are other ways of calling the is_odd function in the main function
"""
def is_odd_v1(value):
    # Checks to see if a value is odd. If it is, returns true.
    remainder = value % 2 
    to_return = remainder == 1
    return to_return
"""


"""
def is_odd_v2(value):
    # Truly more complex than necessary & does not work for numbers < 2.
    while value > 2:
        value = value - 2

    if value == 2:
        return False
    return True
"""


"""
def is_odd_v3(value):
    # Slightly too complex.
    remainder = value % 2 
    if remainder == 1:
        return True
    else:
        return False 
"""


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
