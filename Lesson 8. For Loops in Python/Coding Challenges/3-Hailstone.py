"""
File: Hailstone.py
-------------------
This program writes a code that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    n = int(input("Enter a number: "))

    while n != 1:
        if n % 2 == 0:
            n = n // 2 # If even, divide by 2
            print(f"{n} is even, so I take half: {n}")
        elif n % 2 == 1:
            n = (3 * n) + 1 # If odd, multiply by 3 and add 1
            print(f"{n} is odd, so I make 3n + 1: {n}")


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == "__main__":
    main()
