"""
Course:
Python (Exercism)

Objective:
Praticar processamento de strings.

Notes:
- considerar alfabeto: 0 a 26
- ord() = mostra o nro ascii da letra
- chr() = transforma nro ascii em letra
- str.maketrans = cria tabela de tradução
- str.translate = método pra traduzir string:
    - mais rápido que loop for por caractere 
    - imutável: não altera string original, retorna uma nova
"""
# a = ord('a')
# A = ord('A')
# print(a, A)

def rotate(text, key):
    """ Transformar texto em código Caesar Cipher."""
    minuscula = "abcdefghijklmnopqrstuvwxyz"
    maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    minuscula_rotacionada = minuscula[key:] + minuscula[:key]
    maiuscula_rotacionada = maiuscula[key:] + maiuscula[:key]

    todas = minuscula + maiuscula
    todas_rotacionadas = minuscula_rotacionada + maiuscula_rotacionada

    traducao = str.maketrans(todas, todas_rotacionadas)

    return text.translate(traducao)

# print(rotate("omg", 5))
# print(rotate("a", 0))
# print(rotate("Cool", 26))
