"""
Curso:
Lógica de Programação e Algoritmos (Uninter - Bacharelado em Engenharia de Software)

Objetivos:
Praticar operadores aritméticos, variáveis e formatação de strings.
"""

# Calcular desconto

# Ler o preço e o percentual e converte as entradas para números com vírgula (float)
preco = float(input("Digite o preço do produto: "))
percentual = float(input("Digite o percentual de desconto: "))

# Calcular o desconto dividindo o percentual por 100 (10/100 = 0.1) e multiplicando pelo preço
desconto = preco * (percentual / 100)

# O valor final é o preço original menos o desconto
valor_final = preco - desconto

# Usar strings pra exibir todas as variáveis calculadas formatadas na tela
print(f"O preço do produto é {preco} e o desconto de {percentual}%")
print(f"Valor calculado de desconto: {desconto}. Valor final do produto: {valor_final}")