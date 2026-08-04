"""
Course:
Python (Exercism)

Objective:
Praticar tratamento de strings.

Notes: 
- isbn: 0 a 9
- conferir se é nro: .isdigit()
"""

def is_valid(isbn):
    no_hifen = isbn.replace("-", "")

    if (len(no_hifen) != 10 or
        not no_hifen[:9].isdigit() or
        no_hifen[9] not in "0123456789X"):
        return False
    # return True

    valores = [10 if char == "X" else int(char) for char in no_hifen]
    soma = sum(valores[i] * (10 - i) for i in range(10))
    return soma % 11 == 0

# print(is_valid("3-598-21508-8"))
# print(is_valid("3-598-21508-"))