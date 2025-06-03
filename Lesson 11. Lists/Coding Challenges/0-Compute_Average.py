"""
File: Compute_Average.py
--------------------------
This program computes the average of the values in a text file '0-number_list' 
and prints the result out.
"""

def main():
    number_list = load_numbers_from_file("0-numbers.txt")
    # TODO: your code here 
    if not number_list:
        print("The list is empty, cannot compute average.")
    else:
        total = sum(number_list)
        count = len(number_list)
        average = total / count
        print(f"Average: {average}")


def load_numbers_from_file(filepath):
    """
    Loads numbers from a file into a list and returns it.
    We assume the file to have one number per line.
    Returns a list of numbers. You should not modify this
    function.
    """
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))
    
    return numbers


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
