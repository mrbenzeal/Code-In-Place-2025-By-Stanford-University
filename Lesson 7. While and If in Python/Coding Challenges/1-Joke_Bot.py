"""
File: Joke_Bot.py
-------------------
This is a simple joke bot. This bot starts by asking the user what they want. 
However, this program will only respond to one response: "Joke". 
If the user enters "Joke" then it will print out a single joke. 
Each time the joke is always the same.
"""

PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Karel is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Karel returns with 13 liters of milk. The programmer asks why and Karel replies: 'because they had eggs'"
SORRY = "Sorry I only tell jokes"

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality such as managing user input, 
compares the user input to and will only respond to the predetermined word: "Joke",
and printing to the console the same joke if "Joke" is entered.
"""
def main():
    # Capture user input
    user_input = input(PROMPT)
    
    # Input for string comparison
    if user_input == "Joke":
        print(JOKE)
    elif str.upper(user_input) == "JOKE": # Uppercase input for string comparison
        print(JOKE)
    elif str.lower(user_input) == "joke": # Lowercase input for string comparison
        print(JOKE)
    else:
        print(SORRY)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == "__main__":
    main()
  
