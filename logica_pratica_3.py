"""
Curso:
Lógica de Programação e Algoritmos (Uninter - Bacharelado em Engenharia de Software)

Objetivos:
Praticar operadores aritméticos, variáveis e formatação de strings.
"""

# Calcular aluguel de carro

# Ler os quilômetros e dias alugados e converter as respostas para números inteiros (int)
km = int(input("Quantos km foram percorridos? "))
dias = int(input("Quantos dias foram percorridos? "))

# Calcular o preço considerando que a diária é 60 e o km rodado é 0.15
preco = (60 * dias) + (0.15 * km)

# Imprimir os resultados na tela utilizando F-strings
print(f"Quantidade de quilômetros rodados foram {km}, quantidade de dias foram {dias}")
print(f"Valor a ser pago: {preco}")