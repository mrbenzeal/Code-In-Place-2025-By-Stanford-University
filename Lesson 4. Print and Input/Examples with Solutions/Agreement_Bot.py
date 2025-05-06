"""
File: Agreement_Bot.py
-----------------------
This is a program which asks the user what their favorite animal is, 
and then always responds with "My favorite animal is also ___!" 
(the blank should be filled in with the user-inputted animal, of course).
"""

def main():
    user_input = input("What's your favorite animal? ")
    print(f"My favorite animal is also {user_input}!")


"""
This is a boilerplate code which launches our code
when we hit the run button.
# There is no need to edit code beyond this point
"""

if __name__ == '__main__':
    main()
  
