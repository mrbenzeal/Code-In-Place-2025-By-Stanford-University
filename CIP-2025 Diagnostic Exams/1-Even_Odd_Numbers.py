"""
DIAGNOSTIC_EXAM
----------------
File: Even_Odd_Numbers.py
---------------------------
Print out each of the numbers 1 through 100 and whether that number is even or odd.
100 is specified using a constant MAX_NUMBER.
Here is what the output looks like when MAX_NUMBER = 100
1 is odd
2 is even
...
99 is odd
100 is even
"""

# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

def main():
    for number in range(1, MAX_NUMBER + 1):
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")


if __name__ == "__main__":
    main()
