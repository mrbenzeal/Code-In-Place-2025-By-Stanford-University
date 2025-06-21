"""
File: Subtract_7.py
--------------------
This program .
"""

def main():
	num = 7
	num = subtract_seven(num)
	print("this should be zero: ", num)

def subtract_seven(num):
	num = num - 7
	return num


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
