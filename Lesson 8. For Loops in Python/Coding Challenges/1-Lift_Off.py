"""
File: Lift_Off.py
------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then outputs “Liftoff!”
"""

# The main function calls the function start_countdown to start the countdown
def main():
    initial_countdown_value = 10
    start_countdown(initial_countdown_value)

# This function starts the liftoff countdown
def start_countdown(current_count):
    """
    pre-condition: 1
    post condition: 10
    """
    for i in range(10):
        # condition true if value of variable is not equal to zero and false if it is equal to zero
        if current_count != 0:
            print(current_count)
            # Reducing the variable by one so the loop can print the liftoff countdown in reverse order
            current_count = current_count - 1

    print("Liftoff!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
