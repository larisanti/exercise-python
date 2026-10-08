"""
Curso:
Programação III (Uninter - Bacharelado em Engenharia de Software)

Objetivo:
Praticar estrutura de dados.

Notas:
- bubble sort:
  - compara elementos dentro de um vetor
  - elemento da posição i é comparado com o elemento da posição i + 1
  - se i é encontrado, troca de posições entre os elementos
"""

x = [6, 5, 2, 3, 4, 1]
n = 0
troca = 1

while n < len(x) and troca == 1:
    troca = 0
    for i in range(0, len(x) - 1, 1):
        if x[i] > x[i + 1]:
            troca = 1
            aux = x[i]
            x[i] = x[i + 1]
            x[i + 1] = aux
    n = n + 1

print(x)