"""
File: Rainbow.py
----------------------
Karel makes a rainbow!
"""
from karel.stanfordkarel import *

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    paint_corner('red')
    move()
    paint_corner('orange')
    move()
    paint_corner('yellow')
    move()
    paint_corner('green')
    move()
    paint_corner('blue')
    move()
    

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
