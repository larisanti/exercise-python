"""
Course:
Python (Exercism)

Objective:
Praticar processamento de strings.

Notes:
- alfabeto: 0 a 26
- ord() = mostra o nro ascii da letra
- chr() = transforma nro ascii em letra
- steps:
   1. identificar se a letra é maiúscula ou minúscula (definir a base)
   2. encontrar a posição da letra de 0 a 25 (subtrair a base)
   3. somar a key e usar resto da divisão pra jogar pro início da lista
   4. transformar em letra novamente (somar a base de volta)
   5. manter espaços e pontuações
"""
# a = ord('a')
# A = ord('A')
# print(a, A)

def rotate(text, key):
    """ Transformar texto em código Caesar Cipher."""
    resultado = []
    for letra in text:
        if letra.isalpha():
            if letra.islower():
                base = ord("a")
            else:
                base = ord("A")
            posicao = ord(letra) - base
            nova_posicao = (posicao + key) % 26
            letra_cifrada = chr(nova_posicao + base)
            resultado.append(letra_cifrada)
        else:
            resultado.append(letra)

    return "".join(resultado)

# print(rotate("omg", 5))
# print(rotate("a", 0))
# print(rotate("Cool", 26)) #saiu Wool
