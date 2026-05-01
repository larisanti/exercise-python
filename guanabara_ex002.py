"""
Curso: Python 3 - Gustavo Guanabara

Objetivo: 
Pedir o nome do usuário e exibir uma mensagem de boas-vindas com o nome informado.
"""

# declarar variável pra receber input
nome = input('Digite seu nome: ')

# inserir saída formatada pra nome
print('É um prazer te conhecer {}!'.format(nome)) # nome é formatado pra caber na máscara {}