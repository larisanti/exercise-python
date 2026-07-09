"""
Curso: Fundamentos de Python (UTFPR)

Objetivo:
Praticar os conceitos básicos de Python.

Note: 
- O curso é uma disciplina obrigatória da especialização 
em "Inteligência Artificial Generativa Aplicada" (UTFPR).
"""

# Contagem de palavras em uma frase
string = input("")

if string.endswith('.'):
    string = string[:-1]
    
palavras = string.split()

print(f"Existem {len(palavras)} palavras, são elas:")
print()
for i, palavra in enumerate(palavras, start=1):
    print(f"{i}a. palavra = {palavra}")