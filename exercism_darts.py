"""
Course:
Python (Exercism)

Objective:
Develop functions to calculate score in a dart game.

Notes:
- distância euclidiana: (x**2 + y**2)**0.5
^ elevar 0.5 = tirar a raiz quadrada
- testar do maior circle para o maior separadamente
"""

def score(x, y):
    distance = (x**2 + y**2)**0.5
    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0

#print("inner circle (0,0):", score(0, 0)) 
#print("middle circle (3,4):", score(3, 4))
#print("outer circle (0,10):", score(0, 10)) 
#print("outside (11,0):", score(11, 0)) 