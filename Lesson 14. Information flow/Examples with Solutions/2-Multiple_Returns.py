"""
File: Multiple_Returns.py
--------------------------
This program demonstrates .
"""

def get_user_info():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")
    
    return first_name, last_name, email_address

########## No need to edit code past this point :) ##########

def main():
    user_data = get_user_info()
    print("Received the following user data:", user_data)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == "__main__":
    main()
