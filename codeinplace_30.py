"""
Curso:
Code in Place (Stanford)

Objetivos:
Praticar loops, condicionais e atribuição de variável.
"""

import random

GOAL = 3

def main():
    print("Khansole Academy")
    count = 0
    
    while count < GOAL:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        result = num1 + num2
        
        print("What is " + str(num1) + " + " + str(num2) + "?")
        answer = int(input("Your answer: "))
        
        if answer == result:
            count += 1
            print("Correct!")
            print("You've gotten " + str(count) + " correct in a row.")
            print("")
        else:
            count = 0
            print("Incorrect.")
            print("The expected answer is " + str(result))
            print("")
            
    print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()