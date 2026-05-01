"""
Curso: Python 3 - Gustavo Guanabara

Objetivo:
Ler um número e mostrar o seu dobro, triplo e raiz quadrada.
"""

# Ver ex005

# Cria um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro de {} vale {}.'.format(n, d))

print('O triplo de {} vale {}.'.format(n, t))

# usar : para iniciar a formatação e f para indicar float (2 casas)
print('A raiz quadrada de {} é igual a {:.2f}.'.format(n, r))