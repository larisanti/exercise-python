"""
Curso:
Lógica de Programação e Algoritmos (Uninter - Bacharelado em Engenharia de Software)

Objetivo:
Desenvolver um script que calcule o preço final de um produto, aplicando descontos progressivos.
"""

print("Bem-vindo à Loja da Larissa de Santi")

valor_unitario = float(input("Entre com o valor do produto: ")) # Permite centavos
quantidade = int(input("Entre com a quantidade do produto: "))
x = valor_unitario * quantidade
y = 2500
z = 6000
w = 10000

# Condição 1
if (x < y):
  print(f"O valor SEM desconto: R$ {x:.2f}") # Duas casas decimais (.2f)
  print(f"O valor COM desconto: R$ {x:.2f}")

# Condição 2
elif (x >= y) and (x < z):
  print(f"O valor SEM desconto: R$ {x:.2f}")
  print(f"O valor COM desconto: R$ {x * 0.96:.2f}") # Desconto de 4% (1-0.04)

# Condição 3
elif (x >= z) and (x < w):
  print(f"O valor SEM desconto: R$ {x:.2f}")
  print(f"O valor COM desconto: R$ {x * 0.93:.2f}") # Desconto de 7% (1-0.07)

# Condição 4
elif (x >= w):
  print(f"O valor SEM desconto: R$ {x:.2f}")
  print(f"O valor COM desconto: R$ {x * 0.89:.2f}") # Desconto de 11% (1-0.11)
else:
  print("Desconto válido para compras a partir de R$ 2500.")
