"""
File: Print_10.py
------------------
This is a program that prints the first 10 numbers in order using a for loop.
"""


def main():
    # This for-loop generates the first 10 numbers by increasing the index by 1
    for i in range(10):
        print(i + 1)  # Use the 'i' value inside the for-loop


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
    
