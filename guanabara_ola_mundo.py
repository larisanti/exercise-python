"""
Curso: Python 3 - Gustavo Guanabara

Objetivos:
Compreender conceitos básicos de Python.
"""

print('Olá, Mundo!')

# erro: mensagem precisa estar entre aspas (simples ou duplas)
print('Olá, Mundo!)


print(7+4)

# com aspas vai "somar" o texto
print('7' + '4')


# vírgula junta o texto com o número
print('Olá', 5)


# variáveis fixas
nome = 'Santi'
idade = 28
peso = 85.8
altura = 1.73

# erro quando somar string com número sem aspas
print(nome+ idade+ peso) 

# forma correta
print(nome, idade, peso, altura)


# mudar variáveis fixas perguntando ao usuário
nome = input('Qual é o seu nome? ')
idade = input('Quantos anos vc tem? ')
peso = input('Qual é o seu peso? ')

print(nome, idade, peso)