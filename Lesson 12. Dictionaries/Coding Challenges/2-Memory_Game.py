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
    truth_list = create_truth_list()
    random.shuffle(truth_list)
    displayed_list = create_displayed_list(truth_list)
    
    while '*' in displayed_list:
        print (displayed_list)
        first_index, second_index = get_two_valid_indices(displayed_list) 
        check_if_numbers_match(first_index, second_index, truth_list, displayed_list)

    print("Congratulations! You won!")


def check_if_numbers_match(first_index, second_index, truth_list, displayed_list):
    if truth_list[first_index] == truth_list [second_index]:
        displayed_list [first_index] = truth_list [first_index]
        displayed_list [second_index] = truth_list [second_index]
        print ("Match!")
        
    elif truth_list[first_index] != truth_list [second_index]:
        print("Value at index " + str(first_index)+ " is " + str(truth_list[first_index]))
        print("Value at index " + str(second_index)+ " is " + str(truth_list[second_index]))
        print("No match. Try again.")
        input("Press Enter to continue...")

    clear_terminal()
    return (displayed_list)


def get_two_valid_indices(displayed_list):
    index1 = get_a_valid_index(displayed_list)
    index2 = get_a_valid_index(displayed_list)
    while index2 == index1:
        print("You entered the same index twice. Try again.")
        index2 = get_a_valid_index(displayed_list)   
    return (index1, index2)


def get_a_valid_index(displayed_list):
    while True:
        user_input =input("Enter an index: ")
        if not user_input.isdigit():
            print("Not a number. Try again.")
            continue
        
        if int(user_input) > len(displayed_list):
            print ("Invalid index. Try again.")
            continue 

        if not displayed_list[int(user_input)] == "*": 
            print ("This number has already been matched. Try again.")
            continue
        break

    return (int(user_input))


def create_displayed_list(truth_list):
    displayed_list = []
    for i in range (len(truth_list)):
        displayed_list.append("*")
    return displayed_list


def create_truth_list():
    truth_list = []
    for i in range (NUM_PAIRS):
        truth_list.append(i)
    return (2*truth_list)


def clear_terminal():
    for i in range(20):
      print('\n')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
     
