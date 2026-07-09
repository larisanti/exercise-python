"""
Curso: Fundamentos de Python (UTFPR)

Objetivo:
Praticar os conceitos básicos de Python.

Note: 
- O curso é uma disciplina obrigatória da especialização 
em "Inteligência Artificial Generativa Aplicada" (UTFPR).
"""

# Classificação de elementos em lista (negativo/nulo/positivo)
n = int(input())

lista1 = []
for i in range(n):
    lista1.append(int(input()))

lista2 = []
for x in lista1:
    if x < 0:
        lista2.append(-1)
    elif x == 0:
        lista2.append(0)
    else:
        lista2.append(1)

print(lista1)
print(lista2)