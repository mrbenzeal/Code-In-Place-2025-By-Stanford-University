"""
File: Heads_Up.py
------------------
This programm creates a random word from a txt file with a list of words.
The Guesser has to close the eyes while the other players try to describe the word.
The Guesser has to enter the response into the terminal to see wether or not it was correct.
Our next goal is to learn how to read data from files. 
Loading data from a file can be useful for many final projects. 
In writing this program that runs a console version of the phone game Heads Up, 
We did the following:
Milestone #1: First, we loaded all of the words from the file cswords.txt into a list.
Milestone #2: Then, we showed a randomly chosen word from the list
Milestone #3: Repeat: waited for the user to hit enter, then we showed another word.
"""

import random

# Name of the file to read in!
FILE_NAME = 'CIP5_S6-cswords1.txt'

def main():
    words = get_words_from_file()
    play_game(words)


def get_words_from_file():
    """
    This function  opens a file, stores all of the lines into a list of strings 
    and returns a list of all lines in the file. 
    """
    f = open(FILE_NAME)

    lines = []
    with open(FILE_NAME) as f:
        for line in f:
            # removes whitespace characters (\n) from the start and end of the line
            line = line.strip() 
            # if the line was only whitespace characters, skip it 
            if line != "":
                lines.append(line)          
    return lines


def play_game(words):
    while True:
        random_word = random.choice(words)
        input(random_word)
    

if __name__ == '__main__':
    main()
  
