"""
File: Haiku.py
---------------
A haiku is a kind of poem which is comprised of 3 lines of 5, 7, 
and 5 syllables respectively. 
Here's a famous haiku, “An Old Silent Pond” by Bashō: 
An old silent pond...  
A frog jumps into the pond,  
splash! Silence again. 
This program write this haiku onto the screen in three lines, in the font 'Courier'.
"""

from graphics import Canvas

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
FIRST_LINE_LEFT_X = 50
FIRST_LINE_TOP_Y = 50
FONT_SIZE = 24

def main():
    my_canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    second_line_left_x = FIRST_LINE_LEFT_X
    second_line_top_y = FIRST_LINE_TOP_Y + 25

    third_line_left_x = FIRST_LINE_LEFT_X
    third_line_top_y = FIRST_LINE_TOP_Y + 50
    
    # 
    my_canvas.create_text(FIRST_LINE_LEFT_X, FIRST_LINE_TOP_Y, 
        "An old silent pond..." ,
        font="Courier", 
        font_size=FONT_SIZE, 
        color="blue")

    my_canvas.create_text(second_line_left_x, second_line_top_y, 
       "A frog jumps into the pond,",
        font="Courier", 
        font_size=FONT_SIZE, 
        color="blue")

    my_canvas.create_text(third_line_left_x, third_line_top_y, 
        "splash! Silence again.",
        font="Courier", 
        font_size=FONT_SIZE, 
        color="blue")
    



"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
