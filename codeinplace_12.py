"""
Curso:
Code in Place (Stanford)

Objetivos:
- Praticar refinamento sucessivo (stepwise refinement/top-down design).
"""

from karel.stanfordkarel import *

def main():
    """
    Places beepers in a zig zag pattern.
    """
    while front_is_clear():  
        zig_one_zag()  
        move_to_next_zigzag_spot()  

def zig_one_zag():
    """
    Places two beepers at a time.
    """
    put_beeper()
    turn_left()  
    move()  
    turn_right() 
    if front_is_clear(): 
        move()
        put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

def move_to_next_zigzag_spot():
    """
    Moves Karel to the next spot.
    """
    turn_right()  
    move()  
    turn_left()  
    if front_is_clear():  
        move()

if __name__ == '__main__':
    main()