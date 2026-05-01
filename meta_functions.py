"""
Curso:
Programming in Python (Meta - Database Engineer Specialization)

Objetivo: 
Praticar a criação de funções.
"""

# function = modular piece of code
# Uma função precisa ser definida com "def" antes de poder ser usada

# Declare variables

bill = 175.00
tax_rate = 15

total_tax = (bill * tax_rate) / 100.00

print('Total tax', total_tax)

# Se precisar fazer a mesma conta várias vezes com valores diferentes, é melhor criar uma função

def calculate_tax(bill, tax_rate):
    return (bill * tax_rate) / 100.00

# A função responde com o valor (return), mas não mostra na tela

print('Total Tax:', calculate_tax(175.00, 15))