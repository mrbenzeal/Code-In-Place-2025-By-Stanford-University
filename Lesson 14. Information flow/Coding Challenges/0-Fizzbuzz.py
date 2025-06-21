"""
File: Fizz_Buzz.py
-------------------
This program .
"""

MAX_VALUE = 17

def main():
    # modify this starter code to call fizzbuzz
    # on every number from 1 to MAX_VALUE
    # to_say = fizzbuzz(1)
    # print(to_say)
    for i in range(1, MAX_VALUE + 1):
        print(fizzbuzz(i))

def fizzbuzz(n):
    """
    Takes in a positive integer (n) and returns
    what the player should say at that value.
    Here are a few examples:
    fizzbuzz(3) returns "Fizz"
    fizzbuzz(15) returns "Fizzbuzz"
    fizzbuzz(2) returns 2
    """
    if n % 3 == 0 and n % 5 == 0:
        return "Fizzbuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
