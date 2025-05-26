"""
File: Double.py
----------------
This program writes a code that ask the user for a number, 
return the result of multiplying the number by 2 , and prints the result..
"""

def double(num):
    return num * 2


def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
