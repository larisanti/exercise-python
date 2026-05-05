"""
Curso:
Code in Place (Stanford)

Objetivos:
- Introdução ao Karel e à lógica de programação.

Notes:
- Estou revisando conceitos básicos com uma metodologia diferente,
  meu objetivo é reforçar minha base de lógica de programação.
- O professor comentou que essa metodologia é utilizada desde 1980,
  imagino que seja porque o Karel torna "materializa" conceitos abstratos.
- O professor recomendou usar PyCharm, assim como meu professor da Uninter.
- Aprendi a anatomia básica de um código: 1) main; 2)helping
^ antes eu colocava helping functions primeiro
"""

from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""

def main():
    """
    This function was created to solve the problem "Jigsaw Karel".
    """
    move()
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    move()
    put_beeper()
    turn_left()
    turn_left()
    move()
    move()
    turn_left()  # turn right = turn left 3x
    turn_left()
    turn_left()
    move()
    move()
    move()
    turn_left()
    turn_left()


# Executing the code
if __name__ == '__main__':
    main()