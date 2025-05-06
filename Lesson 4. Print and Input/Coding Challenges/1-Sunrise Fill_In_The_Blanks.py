"""
File: Sunrise Fill_In_The_Blanks.py
------------------------------------
Thi is a Fill in the Blank program, like the one from the lesson.
The user will enter three strings (a color, an adjective and a goal).
Which will then be turned into a one sentence story.
"""

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality 
of printing to the console.
"""
def main():
    color = input("A color: ")
    adjective = input("An adjective: ")
    goal = input("A goal you would like to achieve: ")

    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.")


# Run the main function when this file is executed. No need to edit these lines!
if __name__ == "__main__":
    main()
