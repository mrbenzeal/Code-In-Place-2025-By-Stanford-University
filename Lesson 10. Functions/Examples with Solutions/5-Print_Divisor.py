"""
File: Print_Divisor.py
-----------------------
This program writes a code that create a helper function print_divisors(num), 
which takes in a number and prints all of its divisors 
(all the numbers from 1 to num inclusive that num can be cleanly divided by 
and there is no remainder to the division).
"""

def print_divisors(num):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)


def main():
    num = int(input("Enter a number: "))
    # Calling my helper function here with `num` as a parameter!
    print_divisors(num)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
