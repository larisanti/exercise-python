"""
Curso:
Lógica de Programação e Algoritmos (Uninter - Bacharelado em Engenharia de Software)

Objetivos:
Praticar estruturas condicionais (if/elif/else) aninhadas.
"""

# Calcular preço da conta de luz de acordo com o consumo em kwh e tipo de instalação

# O kwh pode ser um número quebrado, então usa float
kwh = float(input("Quantos kWh consumidos? "))

# Ler o input string (R, I ou C) para o tipo de instalação
tipo = input("Qual o tipo da instalação (R, C ou I)? ")

# Condicional pra definir o preço baseado no tipo de instalação
if tipo == 'R':
    # Usar mais um if e um else pra verificar a faixa de consumo
    if kwh >= 500:
        preco = 0.65
    else:
        preco = 0.40

    # Multiplicar o consumo pelo preço definido na condicional
    print(f"Total a pagar: R$ {kwh * preco}")

# Repetir a lógica da primeira condicional, mas para C
elif tipo == 'C':
    if kwh > 1000:
        preco = 0.60
    else:
        preco = 0.55

    print(f"Total a pagar: R$ {kwh * preco}")

# Repetir a lógica da primeira condicional, mas para I
elif tipo == 'I':
    if kwh > 5000:
        preco = 0.60
    else:
        preco = 0.55

    print(f"Total a pagar: R$ {kwh * preco}")

# Se o usuário digitar algo diferente de R, C ou I
else:
    print("Tipo de instalação inválido.")