"""
Program: Fahrenheit_To_Celsius.py
----------------------------------
This is a python program that prompts the user for a 
temperature in Fahrenheit (this can be a number with decimal places!) 
and outputs the temperature converted to Celsius.
"""

"""
This main function definition serves as the entry point of the program and is responsible for executing the primary functionality 
of printing to the console.
"""
def main():
    # this collects a string value in fahrenheit from the user; 
    # and storing it in the variable 'degrees_fahrenheit'.
    degrees_fahrenheit = input("Enter temperature in Fahrenheit: ")

    # this converts 'degrees_fahrenheit' from string to float value.
    degrees_fahrenheit = float(degrees_fahrenheit)

    # this converts from fahrenheit float value to celsius value
    # and storing it in the variable 'degrees_celsius'.
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

    """
    this prints the concatenated texts of: 
    - " Temperature: " 
    - " the converted string values of the variables 'degrees_fahrenheit' & 'degrees_celsius' " 
    - " 'F', 'C', and the whitespace ' ' " to the terminal
    """
    print("Temperature: " + str(degrees_fahrenheit) + "F" + " " + "="  + " " + str(degrees_celsius) + "C")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
