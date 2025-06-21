"""
File: Update_Function_X=Change.py
----------------------------------
This program demonstrates the demo code for the problem Mehran covered in lecture.
"""

def add_five(x):
    x += 5
    return x
    
def add_five_buggy(x):
    x += 5
    
def main():
    x = 3
    print("original:", x)
    
    add_five_buggy(x)
    print("after add_five_buggy:", x)
    
    x = add_five(x)
    print("after add_five:", x)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
