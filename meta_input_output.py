"""
Curso:
Programming in Python (Meta - Database Engineer Specialization)

Objetivos: 
Introdução ao uso de input() e de print().
"""

# Solicitar que o user digite os valores

num1 = input('Please enter the first number: ')

num2 = input('Please enter a second number: ')

print(num1, num2)

# Precisa formatar pro python entender como número

# Ver qual tipo é:
print(type(num1))

print(int(num1) + int(num2)) # int = inteiro

print(float(num1) + float(num2)) # float = decimal

# Quando é pra juntar texto (concatenate), deixa string

str1 = input('Please enter your first name: ')

str2 = input('Please enter your second name: ')

print('Hello' + str1 + ' ' + str2)

# "Somou" também os espaços do meu sobrenome (de Santi)