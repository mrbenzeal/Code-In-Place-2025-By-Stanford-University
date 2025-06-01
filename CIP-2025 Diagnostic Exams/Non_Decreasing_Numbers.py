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


# below is another solution
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



if __name__ == "__main__":
    main()
  
