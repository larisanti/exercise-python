"""
Course:
Python (Exercism)

Objective:
Praticar strings e conjuntos.

Notes: 
- set.issubset() -> é subconjunto?
"""

def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    minusculas = sentence.lower()
    letras = set(minusculas)
    analise = alphabet.issubset(letras)
    #print(analise)
    return analise

## teste
#is_pangram("The quick brown fox jumps over the lazy dog")
#is_pangram("Esta frase nao é um pangram")