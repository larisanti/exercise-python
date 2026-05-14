"""
Curso:
Code in Place (Stanford)

Objetivo:
- Praticar while e for loops.

Notes:
- Resolvi o fencepost bug no início porque
  o Karel precisava mover e depois put beepers.  
  """


from karel.stanfordkarel import *

def main():
    """
    Put 10 beepers in every cell in the bottom row.
    """
    put_10_beepers() # resolvi o fencepost bug no início
    while front_is_clear():
        move()
        put_10_beepers()

def put_10_beepers():
    for i in range(10):
        put_beeper()

if __name__ == '__main__':
    main()