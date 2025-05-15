"""
File: Even_Numbers.py
----------------------
This is a program that prints the first 20 even numbers.
"""

def main():
    # # This for-loop generates the first 20 even numbers by multiplying the index by 2
    for i in range(20):
        print(i * 2)  # Use the 'i' value inside the for-loop


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == "__main__":
    main()
