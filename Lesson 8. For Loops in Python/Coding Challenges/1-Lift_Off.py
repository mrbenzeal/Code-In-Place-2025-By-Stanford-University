"""
File: Lift_Off.py
-------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""

COUNT=10
def main():
    """
    The main function calls the function countdown_start to start the countdown
    """

    countdown_start(COUNT)

"""This function starts the liftoff countdown"""
def countdown_start(number_of_counts):
    """pre-condition -1
       post condition-10
    """
    for i in range(10):

        """condition true if value of variable is not equal to zero and false if it is equal to zero"""
        if number_of_counts!= 0:
            print(number_of_counts)
            """Reducing the variable by one so the loop can print the liftoff countdown in reverse order"""
            number_of_counts = number_of_counts-1




    print("Liftoff!")
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
  
