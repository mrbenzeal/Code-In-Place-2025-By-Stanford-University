"""
DIAGNOSTIC_EXAM
----------------
File: Non_Decreasing_Numbers.py
--------------------------------
Write a program that asks the user to enter a sequence of "non-decreasing" numbers one at a time. 
Numbers are non-decreasing if each number is greater than or equal to the last.
When the user enters a number which is smaller than their previously entered value, the program is over. 
Tell the user how long their sequence was.

A few notes:
- Include the intro message, Enter a sequence of non-decreasing numbers.
- Include the exit message, Thanks for playing!.
- Include the exit message, Sequence length: followed by the length of the sequence.
- The length of the sequence does not include the very last number entered as it is "decreasing"
- Your program should accept floating point numbers.
- The sequence only ends when one number is strictly less than the last.
- You do not have to handle the case where the user enters a value which is not a number (say "abc").
- The user can start with any number, positive or negative.
- Note that the shortest possible sequence is 1. A sequence with a single number can't be decreasing. 
A sequence with two numbers can be decreasing.

A simple way to achieve great things in life is to make small forward progress every day. 
Non-decreasing progress is one of the principles behind modern AI.
"""

def main():
    print("Enter a sequence of non-decreasing numbers.")
    
    # Initialize the sequence list and the previous number as None
    sequence = []
    previous_num = None
    
    while True:
        try:
            num = float(input("Enter num: "))
            # Check if the entered number is less than the previous number
            if previous_num is not None and num < previous_num:
                break
            sequence.append(num)
            previous_num = num
        except ValueError:
            print("Please enter a valid number.")
    
    print("Thanks for playing!")
    print(f"Sequence length: {len(sequence)}")


# below are other solutions
"""   
def main():
    sequence = []
    i = 0
    print("Enter a sequence of non-decreasing numbers.")
    g = float(input("Enter num: "))
    sequence.append(g)
    for i in range(100):
        c = float(input("Enter num: "))
        sequence.append(c)
        if sequence[-2] > sequence[-1]:
            print("Thanks for playing!")
            print("Sequence length: "+ str(i+1))
            break
        else: 
            i += 1
"""

"""
def main():
    print("Enter a sequence of non-decreasing numbers.")   

    sequence = []

    a = float(input("Enter num: "))
    sequence.append(a)

    for i in range(100):
        b = float(input("Enter num: "))
        if a > b:
            print("Thanks for playing!")
            print("Sequence length:", len(sequence))
            break
        else:
            a = b
            sequence.append(a)
"""


if __name__ == "__main__":
    main()
