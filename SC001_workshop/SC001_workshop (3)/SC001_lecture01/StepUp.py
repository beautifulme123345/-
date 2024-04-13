"""
File: StepUp.py
Name: TODO:
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *


def main():
    move()
    pick_beeper()
    turn_left()
    move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
