"""
Curso:
Code in Place (Stanford)

Objetivo:
- Criar for loops para repetir comandos.

Notes:
- Criei as funções para resolver os exercícios da Lesson 2.
- Até então estou achando bem fácil, mas vou seguir com o curso porque
  continuo com a ideia de revisitar os conceitos básicos com outra metodologia.
- Tenho aproveitado as explicações de boas práticas, como control flow.
- O professor frisou a importância de control flow para tornar o código legível.
- Escrevemos códigos para humanos, não apenas para computadores.
"""

from karel.stanfordkarel import *

# Exercise a
def backflip():
    for i in range(4):
        turn_left()

# Exercise b
def put_five_beepers():
    move()
    for i in range(5):
        put_beeper()
    move()

# Exercise c
def square_of_beepers():
    for i in range(4):
        put_beeper()
        move()
        turn_left()