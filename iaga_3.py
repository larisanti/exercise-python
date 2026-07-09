"""
Curso: Fundamentos de Python (UTFPR)

Objetivo:
Praticar os conceitos básicos de Python.

Note: 
- O curso é uma disciplina obrigatória da especialização 
em "Inteligência Artificial Generativa Aplicada" (UTFPR).
"""

# Cálculo de desconto condicional (10% ou 15%)
valor = float(input())
print(f"Valor do Produto = R$ {valor:.2f}")

desconto10 = valor * 0.10
desconto15 = valor * 0.15

#print(f"{valor:.2f}, {desconto10:.2f}, {desconto15:.2f}")

if valor < 5000:
    print(f"Valor do Desconto (10%) = R$ {desconto10:.2f}")
    print(f"Valor Final = R$ {valor - desconto10:.2f}")
else:
    valor > 5000
    print(f"Valor do Desconto (15%) = R$ {desconto15:.2f}")
    print(f"Valor Final = R$ {valor - desconto15:.2f}")