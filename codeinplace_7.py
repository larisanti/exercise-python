"""
Curso:
Code in Place (Stanford)

Objetivo:
- Resolver um fencepost problem.
"""

from karel.stanfordkarel import *

def main():
    """
    Fills entire bottom row of any sized world with beepers.
    """
    
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


if __name__ == '__main__':
    main()