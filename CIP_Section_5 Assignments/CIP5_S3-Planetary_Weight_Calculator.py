"""
# Section 3: Console Programming
# Program: Planetary_Weight_Calculator.py
------------------------------------------
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note: the user should type in a planet with 
the first letter as uppercase, and do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

# Below is a list of the gravitational constants for each planet compared to Earth's gravity (i.e, in weight ratio form):
EARTH_TO_MERCURY_WEIGHT_RATIO = 0.376
EARTH_TO_VENUS_WEIGHT_RATIO = 0.889
EARTH_TO_MARS_WEIGHT_RATIO = 0.378
EARTH_TO_JUPITER_WEIGHT_RATIO = 2.360
EARTH_TO_SATURN_WEIGHT_RATIO = 1.081
EARTH_TO_URANUS_WEIGHT_RATIO = 0.815
EARTH_TO_NEPTUNE_WEIGHT_RATIO = 1.140

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality 
of printing to the console.
"""
def main():
    # prompt to take input from user as a string (Earthling weight on Earth)
    earth_weight_string = input("Enter a weight on Earth: ")
    
    # Casting string into a real number (float)
    earth_weight_float = float(earth_weight_string)
    
    # Casting string into a real number (float)
    earth_weight_float = float(earth_weight_string)

    # prompt to enter the name of a planet in our solar system
    planet = input("Enter a planet: ")

    """
    Using the 'if statements' to find the correct gravitational constant for any selected planet; 
    calculating the Earthling's weight on that planet; 
    printing the calculated weight and rounding it to 2 decimal places. 
    """
    if planet == "Mercury":
        Mercury_weight = earth_weight_float * EARTH_TO_MERCURY_WEIGHT_RATIO
        print(f"The equivalent weight on Mercury: {str(round(Mercury_weight, 2))}")
    elif planet == "Venus":
        Venus_weight = earth_weight_float * EARTH_TO_VENUS_WEIGHT_RATIO
        print(f"The equivalent weight on Venus: {str(round(Venus_weight, 2))}")
    elif planet == "Mars":
        Mars_weight = earth_weight_float * EARTH_TO_MARS_WEIGHT_RATIO
        print(f"The equivalent weight on Mars: {str(round(Mars_weight, 2))}")
    elif planet == "Jupiter":
        Jupiter_weight = earth_weight_float * EARTH_TO_JUPITER_WEIGHT_RATIO
        print(f"The equivalent weight on Jupiter: {str(round(Jupiter_weight, 2))}")
    elif planet == "Saturn":
        Saturn_weight = earth_weight_float * EARTH_TO_SATURN_WEIGHT_RATIO
        print(f"The equivalent weight on Saturn: {str(round(Saturn_weight, 2))}")
    elif planet == "Uranus":
        Uranus_weight = earth_weight_float * EARTH_TO_URANUS_WEIGHT_RATIO
        print(f"The equivalent weight on Uranus: {str(round(Uranus_weight, 2))}")
    elif planet == "Neptune":
        Neptune_weight = earth_weight_float * EARTH_TO_NEPTUNE_WEIGHT_RATIO
        print(f"The equivalent weight on Neptune: {str(round(Neptune_weight, 2))}")


"""  
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == "__main__":
    main()
