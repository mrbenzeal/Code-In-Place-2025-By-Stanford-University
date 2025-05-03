from karel.stanfordkarel import *

"""
this function instructs Karel to follow the beepers path 
on the bottom row and stop when there is no beepers.
"""
def main():
    while beepers_present():
        move()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
