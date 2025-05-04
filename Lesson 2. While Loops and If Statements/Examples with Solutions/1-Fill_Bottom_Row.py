"""
This is a worked example. It shows an example of Karel
using a while loop to place a row of beepers
"""

from karel.stanfordkarel import *

def main():
    """
    this main function fills entire bottom row of any sized world with beepers.
    """
    while front_is_clear():
        put_beeper()
        move()
    # this is a "fence-post" or an "off by one error" bug correction
    put_beeper()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
