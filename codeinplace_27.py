"""
Curso:
Code in Place (Stanford)

Objetivo:
Revisar control flow e variables.

Notes:
Como em tópicos anteriores, o conteúdo continua bem básico.
Mas continuo achando importante reforçar esses conceitos
porque está me ajudando a perceber onde preciso melhorar.
Preciso melhor na lógica por trás dos panos,
tenho pensado em estudar Rust.
"""

import random

def main():
    secret_number = random.randint(1, 50)
    
    print("I am thinking of a number between 1 and 50...")
    
    guess = int(input("Enter a guess: "))
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

        guess = int(input("Enter a guess: "))
        
    print("Congrats! The number was: " + str(secret_number))
    
if __name__ == '__main__':
    main()