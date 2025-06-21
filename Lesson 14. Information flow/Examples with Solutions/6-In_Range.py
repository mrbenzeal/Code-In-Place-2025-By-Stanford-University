"""
File: In_Range.py
------------------
This program implement a function which takes in 3 integers as parameters.
"""

def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    
    if n >= low and n <= high:
        return True
    
    # we could have also included an else statement, but since we are returning, it's fine without!
    return False

# There is no need to edit code beyond this point

def main():
	n = input("n: ")
	low = input("low: ")
	high = input("high: ")
	if in_range(n, low, high):
		print("n is in range!")
	else:
		print("n is not in range...")


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
