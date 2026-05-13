"""
Curso:
Code in Place (Stanford)

Objetivo:
- Praticar while loops com if statements.

Notes:
- Quebrei o problema em partes de acordo com os valores 
  que eu sabia (if) e os que eu não sabia (while).
- Usei if porque eu sabia da condição do beeper (presente ou não).
- Usei while porque eu não sabia a altura do steeple, executa até que a condição seja false
- fence-post bug: quando o loop termina sem executar uma última ação.
  ^ para processar n espaços eu preciso executar a ação n+1 vezes
  """


from karel.stanfordkarel import *

def main():
    """
    Inverts the pattern of beepers in a single row world.
    """
    
    while front_is_clear():
        invert_beeper()
        move()
    invert_beeper() # avoid fencepost bug (n+1)
    
def invert_beeper():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()

if __name__ == '__main__':
    main()