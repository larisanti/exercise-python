"""
Curso:
Code in Place (Stanford)

Objetivos:
- Revisar input function, numbers e conversão de str para int.

Notes:
- Ser consistente e usar:
    - "Double quotes" when text contains single quotes
    - 'Single quotes' when text contains double quotes
"""

# This program asks the user for two numbers and then subtracts them
def main():
    print("This program subtracts two numbers.")
    num1 = input("Enter first number: ")
    num1 = int(num1)
    num2 = input("Enter second number: ")
    num2 = int(num2)
    diff = num1 - num2
    print("The difference is " + str(diff) + ".")
