"""
Curso:
Code in Place (Stanford)

Objetivos:
- Praticar refinamento sucessivo (stepwise refinement/top-down design).
"""

from karel.stanfordkarel import *

def main():
    draw_stripe()
    while front_is_clear():
        for i in range(4):
            move()
        draw_stripe()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def beeper_column():
    """Karel coloca os beepers em uma coluna."""
    put_beeper()  
    while front_is_clear():  
        move()
        put_beeper()

def draw_stripe():
    """Karel desenha a zebra crossing."""
    turn_left()
    beeper_column()
    turn_right()
    move()
    beeper_column()
    turn_left() 

if __name__ == '__main__':
    main()