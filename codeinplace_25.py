"""
Curso:
Code in Place (Stanford)

Objetivo:
- Praticar lógica de random number generation.

Notes:
- Na verdade não existe true randomness na computação
- pseudorandom -> pseudorandom numbers
- por trás dos panos o python:
    1. pega o int -> seed -> random.seed(x)
    2. usa um algoritmo complexo
    3. gera pseudorandom number 
- Se não definir seed, ele usa timestamp
"""

import random

def main():
    SIDES = int(input("How many sides does your dice have? "))
    
    roll = random.randint(1, SIDES)

    print(f"Your roll is {roll}")

if __name__ == '__main__':
    main()
