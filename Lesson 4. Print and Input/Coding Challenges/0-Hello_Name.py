"""
File: Hello_Name.py
--------------------
This is a customizable version of the classic "hello world!" program in main.py 
which, instead of saying "hello world!", prompts the user for their name 
and then says hello to them!
"""

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality 
of printing to the console.
"""
def main():
    """
    This prints to the console the prompt: What is your name? 
    any name keyed in by the user is stored as a value of the variable 'user_name'
    """
    user_name = input("What is your name? ")

    """
    This prints to the console the string: 'Hello' and the stored name from the user
    if the user key in a string like the name 'Obinna',
    it will prints to the console the string: 'Hello Obinna'
    """
    print(f"Hello {user_name}") 


# Run the main function when this file is executed. No need to edit these lines!
if __name__ == '__main__':
    main()
  
