"""
File: Pop-up_Shop.py
---------------------
This program loops through a dictionary of fruits, 
prompting the user to see how many of each fruit they want to buy, 
and then prints out the total combined cost of all of the fruits.
"""

def main():
    # fruits is a dictionary with keys being fruit names and values being the price of the corresponding fruit
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
        total_cost += (price * amount_bought)
    
    print("Your total is $" + str(total_cost))


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main() 
