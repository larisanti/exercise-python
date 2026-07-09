"""
Curso: Fundamentos de Python (UTFPR)

Objetivo:
Praticar os conceitos básicos de Python.

Note: 
- O curso é uma disciplina obrigatória da especialização 
em "Inteligência Artificial Generativa Aplicada" (UTFPR).
"""

# Geração de matriz com caracteres * e @
n = int(input())

for linha in range(n):
    for coluna in range(n):
        if (linha == 0) or (linha == n - 1) or (coluna == 0) or (coluna == n - 1):
            print("*", end=" ")
        else:
            print("@", end=" ")
    print() 