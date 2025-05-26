"""
File: Averages_Function.py
---------------------------
This program writes a code that that takes two numbers and finds the average between the two.
"""

def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    final = average(avg_1, avg_2)
    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("final", final)
    

def average(a, b):
    """
    Returns the number which is half way between a and b
    """
    sum = a + b
    return sum / 2


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
  
