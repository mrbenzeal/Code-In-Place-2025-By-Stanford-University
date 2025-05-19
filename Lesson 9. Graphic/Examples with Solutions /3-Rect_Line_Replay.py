"""
File: Rect_Line_Replay.py
-------------------------
This project is meant to help us practice using the Replay tool.
"""

import graphics

def main():
    # Makes a canvas
    canvas = graphics.create_canvas(300, 300)
    
    # Make 20 blue squares
    for i in range(20):
        value = i * 10
        
        # It can be helpful to store each coordinate into its own variable!
        left_x = value
        top_y = value
        right_x = value + 10
        bottom_y = value + 10
        
        # Create rectangle
        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
        
        # Keep tracks of i and prints it out
        print(i)


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
