"""
Curso:
Code in Place (Stanford)

Objetivos:
- Praticar refinamento sucessivo (stepwise refinement/top-down design).

Notes:
- É uma metodologia de dividir um problema maior em subproblemas menores.
- Iterative testing: escrever uma parte do código e testar antes de ir para a próxima.
- Top down: começar do highest (most abstract).
- Preconditions: o que deve ser True antes da função ser chamada.
- Postconditions: o que deve ser aplicado/True depois que a função for chamada.
"""

# This tells PyCharm who Karel is
from karel.stanfordkarel import *

def main():
    """
    Clear the world, row by row. Each time a row is
    cleared, reset to the start of the row to create
    a consistent pre/post of the while loop
    Left is clear until you are on the top row
    """
    while left_is_clear():
        # precondition: facing right (east)
        clear_row()
        reset_to_next_row()
    clear_row() # fencepost problem: precisava de postcondition
    
    
def clear_row():
    """
    Clear an entire row
    Pre: Karel is either facing East in column 1, or facing West in the last column
    Post: If Karel started in column 1 they are now in the last column.
          If Karel started in the last column they are now in column 1.
          The row Karel is on has no beepers in it.
    """
    while front_is_clear():
        clear_corner()  
        move()
    clear_corner()
    
    
def clear_corner():
    """
    Cleans a corner so that there are no beepers on it.
    Pre: The corner Karel is on has zero or one beepers present.
    Post: The corner Karel is on has zero beepers present.
    """
    if beepers_present():
        pick_beeper()
        
        
def reset_to_next_row():
    """
    Pre: Karel is at the end of a row, facing right (East)
    Post: Karel is at the start of the next row, facing right (East)
    """
    turn_around()
    move_to_wall()
    turn_right()
    move()
    turn_right()
    

def move_to_wall():
    while front_is_clear():
        move()
    
    
def turn_right():
    for i in range(3):
        turn_left()
        
        
def turn_around():
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()
