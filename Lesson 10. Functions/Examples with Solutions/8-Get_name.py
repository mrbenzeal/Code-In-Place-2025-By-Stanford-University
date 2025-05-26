"""
File: Get_name.py
------------------
This program writes a code that returns the user's name as a string 
and then prints it in a greeting.
"""

def get_name():
    return "Karel"


def main():
    name = get_name() # get_name() will return a string which we store to the 'name' variable here
    print("Howdy", name, "! 🤠")


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
