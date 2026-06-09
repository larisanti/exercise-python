"""
Curso:
Code in Place (Stanford)

Objetivos:
- Praticar resolução de algorithmic problems.

Notes:
- A dificuldade estava em encontrar o meio da "rua" em rows
e fazer a lógica funcionar para todos os casos de "mundos" (2x2, 5x5, 6x6)
- Para encontrar o meio da rua: Karel avança 2 casas e volta 1 -> proporção 2:1
- call stack: pilha de chamadas da recursão
^ cada chamada da função guarda seu próprio estado
"""

from karel.stanfordkarel import *

def main():
    find_midpoint()
    put_beeper()

def find_midpoint():
    """
    Função recursiva para encontrar o meio da rua:
    1. Se a frente estiver livre: move 1
    2. Se a frente continuar livre: move mais 1 e chama a si mesma
    3. Depois da recursão: vira, move 1 e vira novamente
    """
    if front_is_clear():
        move()
        if front_is_clear():
            move()
            find_midpoint()
        go_back()
        move()
        go_back()

def go_back():
    """
    Vira o Karel para voltar.
    """
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()