"""
Course:
Python (Exercism)

Objective:
Praticar operações com números inteiros em loop for.

Notes:
- Armstrong condition: n = aⁿ + bⁿ + cⁿ 
- Para 3 dígitos: 153 = 1³ + 5³ + 3³
"""

def is_armstrong_number(number):
    digits = str(number)
    power = len(digits)
    
    total_sum = sum(int(digit) ** power for digit in digits)

    return total_sum == number

#print(is_armstrong_number(153))