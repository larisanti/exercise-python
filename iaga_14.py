"""
Curso: Fundamentos de Python (UTFPR)

Objetivo:
Praticar os conceitos básicos de Python.

Note: 
- O curso é uma disciplina obrigatória da especialização 
em "Inteligência Artificial Generativa Aplicada" (UTFPR).
"""

# Vetor com inteiros (intervalo 0 a 99)
a = []

for n in range(8):
    a.append(int(input()))

for i in range(8):
    print(f"a[{i}] = {a[i]}")

menor = min(a)
print()
print(f"Menor valor = {menor}")