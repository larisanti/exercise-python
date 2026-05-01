"""
Curso: Python 3 - Gustavo Guanabara

Objetivo:
Receber dois números e mostrar a soma entre eles.
"""

# o sinal de + não vai somar porque o input está em formato de string
n1 = input('Digite um número: ')
n2 = input('Digite mais um número: ')
s = n1 + n2
print('A soma vale', s)

# corrigido
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print('A soma vale', s)


# sintax do método "format"
print('A soma entre {} e {} vale {}'.format(n1, n2, s)) # máscaras: {} 
# máscaras são os espaçoes no meio do texto para substituir os valores em ordem


# Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2

print('A soma entre {} e {} vale {}'.format(n1, n2, s))

