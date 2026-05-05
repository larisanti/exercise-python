"""
Curso:
College Algebra with Python (freeCodeCamp)

Objetivos:
- Converter frações e decimais em porcentagem.

Notes:
- Continuação de: algebra_decimals.py
- Fazer casting para float (não int) é uma boa prática em códigos para cálculos
- length -1 para subtrair o ponto decimal

"""


# Get string input, which will include a decimal point
digits = input("Enter a decimal number to convert: ")

# Get number of decimal places as an integer
exponent = int(len(digits))-1 # subtract the decimal (ponto decimal)

# Convert the input to a float number
n = float(digits)

# Use the exponent to get the numerator
numerator = int(n * 10**exponent) # decimal para fração

# Use the expoent to get the denominator
denominator = 10**exponent

# percent is the first two decimal places
percent = n * 100

# Output
print("The decimal is ", n)
print("The fraction is ", numerator, "/", denominator)
print("The percent is ", percent, "%")

