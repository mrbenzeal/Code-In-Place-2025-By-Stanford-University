"""
File: The_Game_Of_Nimm.py
--------------------------
This program lets users play an ancient strategy game of Nimm.
Nimm is an ancient game of strategy that is named after the old German word for "take."
It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China.
Players alternate taking stones until there are zero left.
The game of Nimm goes as follows:
1. The game starts with a pile of 20 stones between the players
2. The two players alternate turns
3. On a given turn, a player may take either 1 or 2 stone from the center pile
4. The two players continue until the center pile has run out of stones.
The last player to take a stone loses.
"""

NUMBER_OF_STONES = 20

def main():
    """
    The main function calls a function nimm_game_play() that lets the users play the game.
    """
    nimm_game_play(NUMBER_OF_STONES)

# This function lets two players play nimm. It calculates the counts it takes for each player to complete the game"""
def nimm_game_play(num_of_stones):
    # count variables keep track of the number of moves it took any player to win
    count1 = 0
    count2 = 0

    """
    pre-condition-num_of_stones is not equal to zero
    post-condition-num_of_stones is equal to zero and the loop terminates
    """
    while(num_of_stones!=0):

        """Player 1 plays"""
        print("There are " + str(num_of_stones) + " stones" + " left"+ ".")

        # num1 asks player 1 for his input
        num1 = int(input("Player 1 would you like to remove 1 or 2 stones? "))
        """
        pre-condition-if num 1 is not equal to 1 and 2
        post-condition-if num 1 is equal to 1 and 2 and the loop terminates
        """
        while num1 != 1 and  num1 != 2:
                print("Please enter either 1 or 2 as input")
                num1 = int(input("Player 1 would you like to remove 1 or 2 stones? "))
        num_of_stones = num_of_stones - num1

        # if num_of_stones is equal to zero is true then the statement runs or it comes outside
        if num_of_stones == 0:
            print("Player 1 wins!")
            break

        count1 = count1 + 1

        """Player 2 plays"""
        print("There are " + str(num_of_stones) + " stones" + " left"+ ".")

        # num2 asks player 2 for his input
        num2 = int(input("Player 2 would you like to remove 1 or 2 stones? "))
        """
        pre-condition-if num 1 is not equal to 1 and 2
        post-condition-if num 1 is equal to 1 and 2 and the loop terminates
        """
        while num2 != 1 and num2 != 2:
            print("Please enter either 1 or 2 as input")
            num2 = int(input("Player 2 would like to remove 1 or 2 stones: "))
        num_of_stones = num_of_stones - num2

        # if num_of_stones is equal to zero is true then the statement runs or it comes outside
        if num_of_stones == 0:
            print("Player 2 wins!")
            break

        count2 = count2 + 1


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
