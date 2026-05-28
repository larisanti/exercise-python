"""
Curso:
Code in Place (Stanford)

Objetivos:
- Practice decomposition and pre/post conditions.

Notes:
- Pre/post conditions should always match.
- A good function should do "one conceptual thing"
- Know what it does by looking at its name
- Less than 10 lines, 3 levels of indentation (complex programs need more)
- Reusable and easy to modify
- Well commented
"""

from karel.stanfordkarel import *

# Karel climbs a mountain of any size
# and plants a beeper at the top

def main():
    climb_mountain()
    put_beeper()
    descend_mountain()
    

def climb_mountain():
    """
    pre: Karel is at the base of a mountain
    post: Karel is standing at the top
    """
    while front_is_blocked():
        step_up()
        
        
def descend_mountain():
    """
    pre: Karel is at the top of a mountain
    post: Karel is on the other side
    """
    while front_is_clear():
        step_down()


def step_down():
    """
    pre: Karel is facing right/east
    post: Karel is facing right/east
    """
    move()
    turn_right()
    move()
    turn_left()
    
    
def step_up():
    """
    pre: Karel is facing right/east
    post: Karel is facing right/east
    """
    turn_left()
    move()
    turn_right()
    move()


def turn_right():
    """
    pre: Karel is facing any direction
    post: Karel is facing right/east
    """
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    main()