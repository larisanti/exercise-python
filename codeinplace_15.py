"""
Curso:
Code in Place (Stanford)

Objetivos:
- Praticar refinamento sucessivo (stepwise refinement/top-down design).

Notes:
Dividi o problema usando refinamento sucessivo:
1. Construir uma coluna de 5 beepers de altura
2. Mover até a próxima coluna (4 passos)
3. Repetir o processo usando loops for para as 4 colunas
"""

from karel.stanfordkarel import *

def main():
    """
    Karel builds columns in the Temple of Artemis.
    There are 4 columns in total, located at the 1st, 5th, 9th, and 13th avenues.
    Each column is exactly 5 units high.
    """
    for i in range(3):
        build_column()
        move_to_next_column()
    build_column()

def build_column():
    """
    Builds a single column of 5 beepers, returning to the bottom 
    of the column and facing East.
    """
    turn_left()
    for i in range(4):
        put_beeper()
        move()
    put_beeper()
    turn_around()
    for i in range(4):
        move()
    turn_left()

def move_to_next_column():
    """
    Moves Karel 4 steps forward to the next column.
    """
    for i in range(4):
        move()

def turn_around():
    """
    Turns Karel 180 degrees.
    """
    turn_left()
    turn_left()

def turn_right():
    """
    Turns Karel 90 degrees to the right.
    """
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
