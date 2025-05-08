"""
Program: Dog_Year.py
----------------------------------
This is a python program that prompts the user to input an age in human years, 
and converts it to the equivalent age in dog years..
"""

# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality 
of printing to the console.
"""
def main():
    """
    This block of code 
    - first prompt the user to input an age in human years
    - stores the age value in the variable 'human_years'
    - converts 'human_years' from string to float value

    - converts the value of the human year to its equivalent in dog year 
      by multiplying the value of the human year to the constant dog year 
      multiplier
    - the equivalent in dog year value is stored in the variable 
      'dog_years_equivalent' 
    - converts 'dog_years_equivalent' from string to float value

    - and prints a concatenated string of texts including 
      the equivalent age in dog year to the terminal
    """
    human_years = input("Enter an age in calendar years: ")
    human_years = float(human_years)

    dog_years_equivalent = human_years * DOG_YEARS_MULTIPLIER
    dog_years_equivalent = float(dog_years_equivalent)

    print("That's" + " " + str(dog_years_equivalent) + " " + "in dog years!")


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
