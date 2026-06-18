"""
Curso:
Code in Place (Stanford)

Objetivos:
- Praticar operações e concatenação de string.

Notes:
- Precedência de operadores:
() em (fahrenheit - 32) é obrigatório pra subtrair antes de multiplicar
- fórmula pra converter: celsius = (fahrenheit - 32) * 5.0/9.0
"""

# This program converts Fahrenheit to Celsius
def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # formula
    celsius = (fahrenheit - 32) * 5.0/9.0

    print("Temperature: " + str(fahrenheit) + "F = " + str(celsius) + "C")


if __name__ == '__main__':
    main()
