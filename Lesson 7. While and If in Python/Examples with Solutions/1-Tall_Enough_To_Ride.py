"""
File: Tall_Enough_To_Ride.py
-----------------------------
program which asks the user how tall they are 
and prints whether or not they're taller than a pre-specified minimum height.
"""

MINIMUM_HEIGHT = 50 # arbitrary units

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality such as managing user inputs, 
comparing the user inputs to pre-specified minimum height 
and printing to the console.
"""
def main():
    height_str = input('How tall are you? ')
    while height_str != "":
        height = int(height_str)
        tall_enough(height)
        height_str = input('How tall are you? ')
    print('Good-bye!')


def tall_enough(height: int)->None:
    if height >= MINIMUM_HEIGHT:
        print('You\'re tall enough to ride!')
    else:
        print('You\'re not tall enough to ride, but maybe next year!')


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
  
