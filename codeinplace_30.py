"""
Curso:
Code in Place (Stanford)

Objetivos:
Praticar loops, condicionais e atribuição de variável.
"""

import random

def main():
    print("Khansole Academy")
    
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    result = num1 + num2
    
    print("What is " + str(num1) + " + " + str(num2) + "?")
    answer = int(input("Your answer: "))

    if answer == result:
        print("Correct!")
    else:
        print("Incorrect.")
        print("The expected answer is " + str(result))

if __name__ == '__main__':
    main()