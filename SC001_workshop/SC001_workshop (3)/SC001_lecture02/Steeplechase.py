"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()

def jump():
        """
        pre-condition:Karel is on the left side of the wall, facing East
        Post-condition: Karel is on the right side of the wall, facing East
        :return:
        """
        while not front_is_clear():
            up()
        cross()
        down()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def up():
        """
        pre-condition: KArel is on the left side of the wall, facing East
        post-condition: KArel is facing East
        """

        while not front_is_clear():
            turn_left()
            move()
            turn_right()
def cross():
    """
    pre-condition; Karel is facing East
    Post-condition : Karel is facing south
    :return:
    """
    move()
    turn_right()
def down():
    """
    pre-condition: Karel is facing south
    post-condition: Karel is facing East
    :return:
    """
    while front_is_clear():
        move()
    turn_left()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
