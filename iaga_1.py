"""
Curso: Fundamentos de Python (UTFPR)

Objetivo:
Praticar os conceitos básicos de Python.

Note: 
- O curso é uma disciplina obrigatória da especialização 
em "Inteligência Artificial Generativa Aplicada" (UTFPR).
"""

# Cálculo de desconto de 10%
valor = float(input())

desconto = valor * 0.1
valor_final = valor - desconto

print(f"Valor do Produto  = R$ {valor:.2f}")
print(f"Valor do Desconto = R$ {desconto:.2f}")
print(f"Valor Final       = R$ {valor_final:.2f}")