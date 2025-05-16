"""
File: High_Low_Game.py
-----------------------
This program lets a player play a High-Low game with the computer.
The game is called High-Low and the way it's played goes as follows:
1. Two numbers are generated from 1 to 100 (inclusive on both ends): 
one for the player and one for a computer, who will be the player's opponent. 
The player gets to see his number, but not the computer's!
2. The player make a guess, saying his number is either 
higher than or lower than the computer's number
3. If the player's guess matches the truth (ex. he guess his number is higher, 
and then his number is actually higher than the computer's), the player gets a point!

These steps make up one round of the game. 
The game is over after all rounds of 5 have been played.
"""

import random

# The number of rounds constant (the game is over after all rounds of 5)
NUM_ROUNDS = 5

"""
The main function prints the name of the game to console, 
declares the round count and the player's score as global variables 
and calls the function Play_High_Low_Game() to start the game
"""
def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Declaring the round count and the player's score as global variables
    global round_count
    global player_score
    
    # Play the High or Low game
    Play_High_Low_Game()


# This function starts the High Low Game
def Play_High_Low_Game():
    # Initialise the round count and the player's score
    round_count = 1
    player_score = 0

    # iterate through the number of rounds to play the game
    for i in range (NUM_ROUNDS):
        # Repeat this loop until the loop condition is false
        while round_count > 0 and round_count < 6:
            
            # Print the Rounds and increment it
            print(f"Round {round_count}")
            round_count += 1

            # Generate the player's and the computer's random numbers
            player_number = random.randint(1,100)
            computer_random_number = random.randint(1,100)
            
            # Print the player's random numbers to console
            print(f"Your number is {player_number}")

            # Capture player's guess of either 'higher' or 'lower' than the computer's number
            player_guess = input("Do you think your number is higher or lower than the computer's?: ")

            # This 'if condition' is for the player's guess to be in lower case  
            if player_guess.lower() == 'higher' or player_guess.lower() == 'lower':
                
                # This captures the 2 possible true guesses of the player
                is_lower_correct = player_guess.lower() == 'lower' and player_number < computer_random_number
                is_higher_correct = player_guess.lower() == 'higher' and player_number > computer_random_number

                # The 'if condition' for the player's guess to be correct
                if is_lower_correct or is_higher_correct: 

                    # this captures what happens if the player guesses right
                    print(f"You were right! The computer's number was {computer_random_number}")
                    
                    player_score += 1 # Increment number of player's score by 1
                    print(f"Your score is now {player_score}")

                # this captures what happens if the player fails to guess right
                else: 
                    print(f"Aww, that's incorrect. The computer's number was {computer_random_number}")
                    print(f"Your score is now {player_score}")
            
            # this captures what happens if the player inputs an invalid responds
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
