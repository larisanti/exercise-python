"""
Curso: Fundamentos de Python (UTFPR)

Objetivo:
Praticar os conceitos básicos de Python.

Note: 
- O curso é uma disciplina obrigatória da especialização 
em "Inteligência Artificial Generativa Aplicada" (UTFPR).
"""

# Busca sequencial em lista de inteiros
a = [10, 2, 7, 8, 5, 3, 22, 17, 18]

item = int(input())
#print(a[1])
print({i: a[i] for i in range(len(a))})

for i in range(len(a)):

    if item == a[i]:
        print(f"Item: {item}, foi encontrado na posição {i}")
        break
else:
    print(f"Item: {item}, não foi encontrado.")