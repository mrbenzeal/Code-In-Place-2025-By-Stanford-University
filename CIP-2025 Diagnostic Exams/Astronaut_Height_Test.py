"""
DIAGNOSTIC_EXAM
----------------
File: Astronaut_Height_Test.py
-------------------------------
Write a console program which asks the user for their height in meters 
and prints whether or not they are the correct height to be a NASA astronaut.
- If their height is greater than 1.6 meters and less than 1.9 meters, print 
  "Correct height to be an astronaut".
- If their height is less than or equal to 1.6 meters, print 
  "Below minimum astronaut height".
- If their height is greater than or equal to 1.9 meters, print 
  "Above maximum astronaut height".
  
You may assume that the user enters a valid input (a non-negative number). 
Each time the program is run, the user is asked for their height only once.

Aside: If you are not the right height to be an astronaut, that is fine! Space is dangerous anyways. 
Chris is not the right height, but found a happy alternative job here on earth 🌱.
"""

def main():
    # Ask the user for their height in meters
    height = float(input("Enter your height in meters: "))

    # Determine and print the appropriate message based on the height
    if height > 1.6 and height < 1.9:
        print("Correct height to be an astronaut")
    elif height <= 1.6:
        print("Below minimum astronaut height")
    elif height >= 1.9:
        print("Above maximum astronaut height")

if __name__ == "__main__":
    main()
