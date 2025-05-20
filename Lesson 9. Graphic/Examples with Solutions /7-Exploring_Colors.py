"""
File: Exploring_Colors.py
--------------------------
This is a program that uses "hex codes" to explore the use of more colors 
with much more nuance than "red", "brown", or any other string on drawn objects.
Hex codes are formatted as a string in the form of "#RRGGBB".
Each color component is individual from one another and are written in base-16. 
For example, red is equivalent to the hex code "#FF0000". 
"""

from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # TODO: Replace the "#FFFFFF" (white) color parameter to make a purple circle!
    canvas.create_oval(CANVAS_WIDTH/2 - 75, 225, CANVAS_WIDTH/2 + 75, 375, color="#800080")
    
    # There is no need to edit code beyond this point
    
    # Draw a red circle
    canvas.create_oval(25, 25, 175, 175, color="#990000")
    
    # Draw a plus sign
    canvas.create_line(190, 100, 210, 100)
    canvas.create_line(200, 90, 200, 110)
    
    # Draw a blue circle
    canvas.create_oval(CANVAS_WIDTH/2 + 25, 25, CANVAS_WIDTH/2 + 175, 175, color="#000099")
    
    # Draw an arrow
    canvas.create_line(200, 170, 200, 210)
    canvas.create_line(200, 210, 190, 190)
    canvas.create_line(200, 210, 210, 190)
    

"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
