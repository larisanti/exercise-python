"""
Curso: Python 3 - Gustavo Guanabara

Objetivos:
Identificar os tipos primitivos do Python (str, int, float, bool) 
e utilizar métodos de string para analisar o conteúdo de uma entrada.
"""

# Como saber o tipo da variável
n = input('Digite um valor: ')
print(type(n))

# Tipos primitivos do python: str, int, float, bool

# Exemplo de float
n = float(input('Digite um valor: ')) 

# Exemplo de bool
n = bool(input('Digite um valor: '))

# Como saber o tipo com teste is (método is)
n = input('Digite algo: ')

print(n.isnumeric())

print(n.isalpha())

print(n.isalnum())

print(n.islower())

print(n.isupper())



# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo: ')

print('O tipo primitivo desse valor é', type(n))

print('É numérico? ', n.isnumeric())

print('É alfabético? ', n.isalpha())

print('É alfanumérico? ', n.isalnum())

print('Está somente em maiúsculas? ', n.isupper())

print('Está somente em minúsculas? ', n.islower())