"""
Curso: Python 3 - Gustavo Guanabara

Objetivos:
Praticar operadores matemáticos e formatação de strings.
"""

# Calcular a raiz quadrada elevando um número a meio (1/2)
# Raiz quadrada de 81
print(81 ** (1/2)) # operador: ** -> exponenciação

# Calcular a raiz cúbica elevando um número a um terço (1/3)
# Raiz cúbica de 127
print(127 ** (1/3))

# Usando a função interna de potência (4 ao cubo)
print(pow(4, 3)) # função interna: pow(base, expoente)

# Aplicar operadores aritiméticos em texto
print('Oi' + 'Olá') # somar = concatenar
print('Oi' * 5)
print('=' * 20)



# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor a seu antecessor.

n = int(input('Digite um número inteiro: '))

print('Considerando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))