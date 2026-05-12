"""
Curso:
Code in Place (Stanford)

Objetivo:
- Praticar decomposição (modularização).

Notes:
- Criei uma subtarefa para completar a task do exercício.
- Reforcei a importância de diminuir o "problema" em partes,
  invés de resolver tudo na main.
  """

from karel.stanfordkarel import *

# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    move()
    pick_10_beepers()
    move()
    pick_10_beepers()
    move()
    pick_10_beepers()

def pick_10_beepers():
    pick_beeper()
    pick_beeper()
    pick_beeper()
    pick_beeper()
    pick_beeper()
    pick_beeper()
    pick_beeper()
    pick_beeper()
    pick_beeper()
    pick_beeper()
    move()
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()