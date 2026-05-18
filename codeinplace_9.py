"""
Curso:
Code in Place (Stanford)

Objetivo:
- Practice while loop.
"""

from karel.stanfordkarel import *

def main():
    """
    Makes Karel travel past the end of a straight line of beepers.
    """
    while beepers_present():
        move()


if __name__ == '__main__':
    main()