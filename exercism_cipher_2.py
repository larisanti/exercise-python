"""
Course:
Python (Exercism)

Objective:
Criar módulo para codificar e decodificar mensagens usando a cifra Atbash.

Notes:
abcdefghijklmnopqrstuvwxyz -> zyxwvutsrqponmlkjihgfedcba
"""

def encode(plain_text):
    """Codifica o texto de entrada usando a cifra Atbash."""
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    translated = ""

    for letra in plain_text:
        letra_minuscula = letra.lower()
        if letra_minuscula in plain:
            indice = plain.index(letra_minuscula)
            translated += cipher[indice]
        elif letra_minuscula.isdigit():
            translated += letra_minuscula
    
    blocos = []
    for indice in range(0, len(translated), 5):
        blocos.append(translated[indice : indice + 5])
        
    return " ".join(blocos)


def decode(ciphered_text):
    """Decodifica a mensagem cifrada."""
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    decoded = ""
    
    for letra in ciphered_text:
        letra_minuscula = letra.lower()
        if letra_minuscula in cipher:
            indice = cipher.index(letra_minuscula)
            decoded += plain[indice]
        elif letra_minuscula.isdigit():
            decoded += letra_minuscula
            
    return decoded
