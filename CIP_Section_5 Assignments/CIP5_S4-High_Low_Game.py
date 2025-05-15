"""
File: High_Low_Game.py
-----------------------
This program lets a user play a High-Low game with the computer.
The game is called High-Low and the way it's played goes as follows:
1. Two numbers are generated from 1 to 100 (inclusive on both ends): 
one for the user and one for a computer, who will be the user's opponent. 
The user gets to see his number, but not the computer's!
2. The user make a guess, saying his number is either 
higher than or lower than the computer's number
3. If the user's guess matches the truth (ex. he guess his number is higher, 
and then his number is actually higher than the computer's), the user gets a point!

These steps make up one round of the game. 
The game is over after all rounds of 5 have been played.
"""

import random

# The number of rounds constant (the game is over after all rounds of 5)
NUM_ROUNDS = 5


def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Declaring the round count and the user's score as global variables
    global round_count
    global your_score
    
    # Play the High or Low game
    Play_High_Low_Game()


def Play_High_Low_Game():
    # Initialise the round count and the user's score
    round_count = 1
    your_score = 0

    # iterate through the number of rounds to play the game
    for i in range (NUM_ROUNDS):
        # Repeat this loop until the loop condition is false
        while round_count > 0 and round_count < 6:
            
            # Print the Rounds and increment it
            print(f"Round {round_count}")
            round_count += 1

            # Generate the user's and the computer's random numbers
            your_random_number = random.randint(1,100)
            computer_random_number = random.randint(1,100)
            
            # Print the user's random numbers to console
            print(f"Your number is {your_random_number}")

            # Capture user's choise of either higher or lower
            your_choice = input("Do you think your number is higher or lower than the computer's?: ")


            if your_choice.lower() == 'higher' or your_choice.lower() == 'lower':
                true_guess_1 = your_choice.lower() == 'lower' and your_random_number < computer_random_number
                true_guess_2 = your_choice.lower() == 'higher' and your_random_number > computer_random_number

                if true_guess_1 or true_guess_2: # correct
                    print(f"You were right! The computer's number was {computer_random_number}")
                    your_score += 1
                    print(f"Your score is now {your_score}")

                else: # incorrect
                    print(f"Aww, that's incorrect. The computer's number was {computer_random_number}")
                    print(f"Your score is now {your_score}")

            else:
                print("Invalid Input")

            # Add an extra space between questions
            print()
        
    # Print exit message  
    print("Thanks for playing!")
    

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == "__main__":
    main()
