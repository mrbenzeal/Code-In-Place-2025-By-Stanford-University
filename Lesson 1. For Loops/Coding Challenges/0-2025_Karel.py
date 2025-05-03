from karel.stanfordkarel import *

"""
When you finish writing this file, Karel should be able to 
place 20 beepers, then 25 beepers, and end facing East to 
the right of the 25 beepers.
"""

def main():
    """
    The "for loops" work by placing 20 beepers, 
    moving Karel one step, 
    placing 25 beepers, 
    and moving Karel one more step.
    """
    for i in range(20):
        put_beeper()
    move()
    for i in range(25):
        put_beeper()
    move()

if __name__ == '__main__':
    main()
