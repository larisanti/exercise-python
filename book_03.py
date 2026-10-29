"""
Referência:
The Recursive Book of Recursion (Al Sweigart) - p. 6

Notes:
- quando chama a função em chain, termina na ordem inversa
- cada função lembra de onde foi chamada pra voltar quando termina
^ stack = LIFO
"""

def a():
    print('a() was called')
    b()
    print('a() is returning')

def b():
    print('b() was called')
    c()
    print('b() is returning')

def c():
    print('c() was called')
    print('c() is returning')

a()

#console
#a() was called
#b() was called
#c() was called
#c() is returning #quando retorna a ordem é reversa
#b() is returning
#a() is returning