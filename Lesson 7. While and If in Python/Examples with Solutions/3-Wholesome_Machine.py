"""
File: Wholesome_Machine.py
-----------------------------
This is a program which prompts the user to type an affirmation of my choice 
(I'll use "I am capable of doing anything I put my mind to.") until they type it correctly. 
"""

AFFIRMATION = "I am capable of doing anything I put my mind to."

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality such as managing user inputs, 
comparing the user inputs to pre-specified affirmation 
and printing to the console.
"""
def main():
    while get_affirmation() != AFFIRMATION:
        print('That was not the affirmation.')
    print('That\'s right! :)')

def get_affirmation()->str:
    return input(f'Please type the following affirmation: {AFFIRMATION}\n')


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
