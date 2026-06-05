"""
Curso:
Code in Place (Stanford)

Objetivos:
- Praticar refinamento sucessivo (stepwise refinement/top-down design).

- Notes:
Como em todos os exercícios de "stepwise refinement",
eu dividi o problema em subproblemas:
1. Encontrar o caule
2. Subir o caule
3. Desenhar a flor
4. Voltar para o chão
"""

from karel.stanfordkarel import *

def main():
    """Karel plants two flowers."""
    for i in range(2):  # usei for loop porque sei a quantidade exata (2 flores)
        move_to_wall()
        bloom_flower()
    move_to_wall()  # fencepost problem fix

def bloom_flower():
    """Karel blooms the flower"""
    go_up_stem()
    draw_flower()
    move_to_wall()
    turn_left()

def go_up_stem():
    """Karel climbs the stem"""
    turn_left()
    while right_is_blocked():
        move()

def draw_flower():
    """Karel draws a 2x2 flower and ends facing South."""
    for i in range(3):
        put_beeper()
        move()
        turn_right()
    put_beeper()
    turn_left()  # vira para south pra poder descer


def move_to_wall():
    """Karel moves until blocked."""
    while front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()