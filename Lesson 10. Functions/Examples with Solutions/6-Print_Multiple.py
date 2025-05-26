"""
File: Print_Multiple.py
------------------------
This program writes a code that fills out print_multiple(message, repeats), 
which takes as parameters a string message to print, 
and an integer repeats number of times to print message.
"""

def print_multiple(message, repeats):
    for i in range (repeats):
        print(message)


def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)
    

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
