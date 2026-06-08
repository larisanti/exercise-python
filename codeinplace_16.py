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
    while True:
        # Fill a row e retorna para a primeira coluna
        fill_row_and_return()
        
        # Precisa virar pro north para saber se pode mover
        turn_left()
        if front_is_clear():
            move()
            # Virar para ir pra próxima row
            turn_right()
        else:
            # Última row
            turn_right()
            move_to_wall()
            break

def fill_row_and_return():
    """
    Preenche a linha atual com beepers movendo-se para o Leste,
    então retorna para a primeira coluna (Oeste) e vira para o Leste.
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
    """
    Vira o Karel 90 graus para a direita.
    """
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
