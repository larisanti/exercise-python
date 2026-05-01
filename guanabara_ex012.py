"""
Curso: Python 3 - Gustavo Guanabara

Objetivos:
Praticar porcentagem, floats e formatação de strings.
"""

# Ver ex005

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input('Qual é o preço do produto? R$ '))

desconto = preco * 5 / 100 # 5% = 5/100
novo_preco = preco - desconto

print('O produto custava R${:.2f}, na promo com 5% vai custar R${:.2f}.'.format(preco, novo_preco))