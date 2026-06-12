"""
Course:
Python (Exercism)

Objective:
Praticar operações matemáticas em loops if.

Notes:
- modulo (%) -> retorna o resto da divisão
- math.remainder() -> algoritmo que retorna o resto da divisão mais próximo do zero
"""
def convert(number):

    result = ""

    if number % 3 == 0:
        result += "Pling"
        
    if number % 5 == 0:
        result += "Plang"

    if number % 7 == 0:
        result += "Plong"

    return result or str(number)