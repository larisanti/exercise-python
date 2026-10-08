"""
Curso:
Programação III (Uninter - Bacharelado em Engenharia de Software)

Objetivo:
Praticar notação/complexidade Big-O.

Notas:
- notação Big-O -> usada pra mostrar como a complexidade de tempo e de espaço cresce
  à medida que a entrada também cresce
"""

# O(n) -> 1 laço de repetição
def ordenar(dados):
    for i in range (0, len(dados) // 2, 1):
        dados[i] = i * 2

lista = [10, 20, 30, 40, 50, 60]
ordenar(lista)
print(lista)