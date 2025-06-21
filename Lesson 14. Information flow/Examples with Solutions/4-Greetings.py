"""
File: Greetings.py
-------------------
This program .
"""

def main():
    name = input("What's your name? ")
    print(greet(name))

# There is no need to edit code beyond this point

def greet(name):
	return "Greetings " + name + "!"
	

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
