"""
File: Choosing_Returns.py
--------------------------
This program demonstrates .
"""

ADULT_AGE = 18 # U.S. adult age 

def is_adult(age):
    if age >= ADULT_AGE:
        return True
    
    return False
    
########## No need to edit code beyond this point :) ##########

def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))
    

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == "__main__":
    main()
