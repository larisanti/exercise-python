"""
Curso:
Code in Place (Stanford)

Objetivos:
Praticar loops, condicionais e atribuição de variável.

Notes:
Ainda está fácil e estou quase finalizando o curso.
Na próxima semana vou focar meu tempo de estudo de python
nos exercícios do Exercism, pois são desafiadores pra mim.
Embora este curso não tenha certificado e seja básico,
está valendo a pena revisar e quero concluir.
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