"""
File: Haiku_Generator.py
------------------
This is a program that creates a Haiku, using AI.
It prompts the user to enter their name, and a topic. 
Then it makes use of call_gpt to turn the name and topic into a haiku.
"""

# Import the AI library "call_gpt"
from ai import call_gpt

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality 
of printing to the console.
"""
def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print("Creating your haiku...")
    response = call_gpt(f"Create a haiku based on {name} and {topic}")
    print(response)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == "__main__":
    main()
