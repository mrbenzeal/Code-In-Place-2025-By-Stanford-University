"""
File: International_Voting_Age.py
----------------------------------
This is a program that prompts a user for their age and 
lets them know if they can or can't vote in the bellow three fictional countries.
"""

PETURKSBOUIPO = 16
STANLAU = 25
MAYENGUA = 48

"""
This main function definition serves as the entry point of the program 
and is responsible for executing the primary functionality such as managing user inputs, 
and calling other helper function definition.
"""
def main():
    age = int(input('How old are you? '))
    global_vote(age)


def global_vote(age: int)->None:
    vote_peturksbouipo(age)
    vote_stanlau(age)
    vote_mayengua(age)


def vote_peturksbouipo(age: int)->None:
    if age >= PETURKSBOUIPO:
        vote = 'can'
    else:
        vote = 'cannot'
    message = f'vote in Peturksbouipo where the voting age is {PETURKSBOUIPO}.'
    print(f'You {vote} {message}')


def vote_stanlau(age: int)->None:
    if age >= STANLAU:
        vote = 'can'
    else:
        vote = 'cannot'
    message = f'vote in Stanlau where the voting age is {STANLAU}.'
    print(f'You {vote} {message}')


def vote_mayengua(age: int)->None:
    if age >= MAYENGUA:
        vote = 'can'
    else:
        vote = 'cannot'
    message = f'vote in Mayengua where the voting age is {MAYENGUA}.'
    print(f'You {vote} {message}')


"""
# This provided line is required at the end of Python file 
  to call the main() function.
# It allows the script to be run as the main program or imported 
  without executing the main function immediately.
"""
if __name__ == '__main__':
    main()
  
