"""
File: Rainbow.py
-----------------
This program has Karel paint a rainbow!
What colors does Karel know? So many! 
In fact any "html" color will work. 
Here is a link with a few:

https://htmlcolorcodes.com/color-names/
"""

from karel.stanfordkarel import *

def main():
    """
    Karel starts in the left corner of a world with 1 row and 6 columns, 
    Karel paints the squares with, in order: 
    the colors "red" , "orange", "yellow", "green", and "blue", 
    and then Karel moves to end in the rightmost spot.
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
    

"""
# This is "boilerplate" code which launches your code
  when you hit the run button
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
    
