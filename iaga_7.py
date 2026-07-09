"""
Curso: Fundamentos de Python (UTFPR)

Objetivo:
Praticar os conceitos básicos de Python.

Note: 
- O curso é uma disciplina obrigatória da especialização 
em "Inteligência Artificial Generativa Aplicada" (UTFPR).
"""

# Alternância de valores par/ímpar em lista
n = int(input())
l = []

for i in range(n):
    l.append(i % 2)

#print(i)

resultados = ", ".join(str(x) for x in l)
print("{" + resultados + "}")