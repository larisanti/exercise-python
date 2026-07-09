"""
Curso: Fundamentos de Python (UTFPR)

Objetivo:
Praticar os conceitos básicos de Python.

Note: 
- O curso é uma disciplina obrigatória da especialização 
em "Inteligência Artificial Generativa Aplicada" (UTFPR).
"""

# Matriz figura com diagonal (caractere @)
n = int(input())

for i in range(n):
    for j in range(n):
        if i == j:
            print("@", end=" ")
        else:
            print(".", end=" ")
    print()