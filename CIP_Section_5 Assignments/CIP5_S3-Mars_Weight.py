"""
# Section 3: Console Programming
# Program: Mars_Weight.py
----------------------------------
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

# using the constant (i.e, the weight ratio of the earth & mars: 37.8%)
EARTH_TO_MARS_WEIGHT_RATIO = 0.378

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality 
of printing to the console.
"""
def main():
    # Takes input from user as a string (Earthling weight on Earth)
    earth_weight_string = input("Enter a weight on Earth: ")
    
    # Casting string into a real number (float)
    earth_weight_float = float(earth_weight_string)
    
    # Calculating Earthling weight on Mars
    mars_weight = earth_weight_float * EARTH_TO_MARS_WEIGHT_RATIO

    # Rounded to two decimal places
    rounded_mars_weight = round(mars_weight, 2)
    
    # converting the Earthling weight on mars to string and Print it using f-string   
    print(f"The equivalent weight on Mars: {str(rounded_mars_weight)}")


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == "__main__":
    main()
