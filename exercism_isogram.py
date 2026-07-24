"""
Course:
Python (Exercism)

Objective:
Praticar strings e conjuntos.

Notes: 
- conferir se é letra: .isalpha()
"""

def is_isogram(phrase):
    phrase = phrase.lower()
    letras = []

    for x in phrase:
        if x.isalpha():
            if x in letras:
                return False
            letras.append(x)

    return True

# # teste
# print(is_isogram("lumberjack"))
# print(is_isogram("Larissa"))