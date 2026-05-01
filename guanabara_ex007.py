"""
Curso: Python 3 - Gustavo Guanabara

Objetivos:
Calcular e exibir a média entre duas notas.
"""

# Ver ex005

# Desenvolva um programa que leia as duas notas de um aluno, calcule a mostre a sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# importante: a divisão deve vir por último
media = (n1 + n2) / 2 

print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, media))