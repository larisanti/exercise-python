"""
Curso: Python 3 - Gustavo Guanabara

Objetivos:
Praticar porcentagem e formatação de strings.
"""

# Ver ex005

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Digite o salário atual: R$ '))

aumento = salario * 15 / 100 # 15% = 15/100
novo_salario = salario + aumento

print('Ganhava R${:.2f} e com 15% de aumento passa a ganhar R${:.2f}.'.format(salario, novo_salario))