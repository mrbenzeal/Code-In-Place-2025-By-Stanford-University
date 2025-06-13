# This tells Python who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality 
of printing to the console.
"""
def main():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
