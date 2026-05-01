"""
Curso: Python 3 - Gustavo Guanabara

Objetivos:
Praticar divisão, floats e formatação de strings.
"""

# Ver ex005

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira a mostra quantos dólares ela poda comprar.
# Considere US$1.00 = R$3.27

carteira = float(input('Quanto dinheiro tem na carteira? R$')) # receber em reais e entender como float
dolares = carteira / 3.27 # dividir o valor da carteira pela cotação do dólar

print('Com R${:.2f} você pode comprar US${:.2f}'.format(carteira, dolares))