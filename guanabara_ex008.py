"""
Curso: Python 3 - Gustavo Guanabara

Objetivos:
Ler um valor em metros e exibir convertido em centímetros e milímetros.
"""

# Ver ex005

# Escreva um programa que leia um valor am metros co exiba convertido em centimetros milimetros.

metros = float(input('Digite uma distância em metros: ')) # números quebrados: float

# Converter metros para centímetros e milímetros
cm = metros * 100
mm = metros * 1000

print('A medida de {}m corresponde a {}cm e {}mm.'.format(metros, cm, mm))