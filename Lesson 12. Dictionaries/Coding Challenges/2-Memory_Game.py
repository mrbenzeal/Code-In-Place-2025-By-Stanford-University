'''
File: Memory_Game.py
---------------------
This program

steps:
1. Create the truth_list using for loop and NUM_PAIRS as the range
2. Call the random shuffle function on the truth_list
3. Create a displayed_list by displaying '*' for each item in truth_list
4. helper function to get one valid index. order of conditions to check: 
    # non-number
    # Number is out-of-bounds
    # Inputting an index that has already been revealed
5. helper function to get 2 indices, and make sure that the user didn't enter the same index twice
6. check if the numbers at user_input indices matches or not. Print message accordingly and update & return displayed_list.
7. in the main function loop the get indices function and check match function until there's no "*" left
8. insert clear terminal function  
'''

import random

NUM_PAIRS = 3

def main():
    truth = create_truth_list(NUM_PAIRS)
    random.shuffle(truth)

    displayed = ['*'] * len(truth)

    while '*' in displayed:
        display_board(displayed)

        index1 = get_valid_index(displayed, "Enter an index: ")
        index2 = get_valid_index(displayed, "Enter an index: ", exclude_index=index1)

        if truth[index1] == truth[index2]:
            displayed[index1] = truth[index1]
            displayed[index2] = truth[index2]
            print("Match!")
            clear_terminal()
        else:
            print(f"Value at index {index1} is {truth[index1]}")
            print(f"Value at index {index2} is {truth[index2]}")
            print("No match. Try again.")
            input("Press Enter to continue...")  # wait for enter
            clear_terminal()

    display_board(displayed)
    print("Congratulations! You won!")


def get_valid_index(displayed, prompt, exclude_index=None):
    while True:
        index_input = input(prompt)

        if not index_input.isdigit():
            print("Not a number. Try again.")
            continue

        index = int(index_input)

        if index < 0 or index >= len(displayed):
            print("Invalid index. Try again.")
            continue

        if displayed[index] != '*':
            print("This number has already been matched. Try again.")
            continue

        if exclude_index is not None and index == exclude_index:
            print("You entered the same index twice. Try again.")
            continue

        return index


def display_board(displayed):
    print(displayed)


def create_truth_list(num_pairs):
    truth = []
    for i in range(num_pairs):
        truth.append(i)
        truth.append(i)
    return truth


def clear_terminal():
    print()  # ✅ safe in all environments


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
  
