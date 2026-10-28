"""
Referência:
Python Programming Exercises, Gently Explained (Al Sweigart) - p.79

Notes:
- pra não repetir e tirar index vazio -> -1
  porque a última pessoa nunca inicia, E já cumprimentou todos
"""

def printHandshakes(people):
    numberOfHandshakes = 0
    for i in range(len(people) - 1):
        for j in range(i + 1, len(people)):
            print(people[i], 'shakes hands with', people[j])
            numberOfHandshakes += 1
    return numberOfHandshakes
    
assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6