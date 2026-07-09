"""
Curso: Fundamentos de Python (UTFPR)

Objetivo:
Praticar os conceitos básicos de Python.

Note: 
- O curso é uma disciplina obrigatória da especialização 
em "Inteligência Artificial Generativa Aplicada" (UTFPR).
"""

# Ordenação de lista e identificação de valores
elementos = []

for i in range(7):
    item = int(input())
    elementos.append(item)

elementos.sort()

for i in range(7):
    print(f"x[{i}] = {elementos[i]}")
print()
print(f"Menor elemento, x[0] = {elementos[0]}")
print(f"Maior elemento, x[6] = {elementos[6]}")