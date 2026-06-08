"""
Curso:
Code in Place (Stanford)

Objetivos:
- Praticar stepwise refinement e decomposition.

Notes:
- Usei while e if na main, mas dividi os subproblemas em funções menores.
- Consegui usar while porque separei a lógica das colunas e todas as colunas
terminam com uma parede no final.
"""

from karel.stanfordkarel import *

def main():
    # Preenche a primeira row
    fill_row_and_return()
    
    # Precisa virar para north para saber se tem mais rows
    turn_left()
    while front_is_clear():
        move()
        # Vira para o leste para preencher a próxima row
        turn_right()
        fill_row_and_return()
        turn_left()
        
    # Última row
    turn_right()
    move_to_wall()


def fill_row_and_return():
    """
    Preenche a linha atual com beepers e volta.
    """
    safe_put_beeper()
    while front_is_clear():
        move()
        safe_put_beeper()
    
    # Retorna para a coluna 1
    turn_around()
    move_to_wall()
    turn_around()

def safe_put_beeper():
    """
    Coloca um beeper apenas se ainda não houver nenhum no local.
    """
    if no_beepers_present():
        put_beeper()

def move_to_wall():
    """
    Move para frente até ser bloqueado por uma parede.
    """
    while front_is_clear():
        move()

def turn_around():
    """
    Vira o Karel 180 graus.
    """
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
