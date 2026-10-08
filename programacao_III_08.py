"""
Curso:
Programação III (Uninter - Bacharelado em Engenharia de Software)

Objetivo:
Praticar notação/complexidade Big-O.

Notas:
- especificar a ordem de grandeza da função = encontra a complexidade Big-O
- ações sequenciais no algoritmo -> usar adição
- ações aninhadas no algoritmo -> usar multiplicação
  ^ exceto pra PG (crescimento exponencial)
"""

def ordenar(dados):
    for i in range(0, len(dados), 1):
        dados[i] = i + 1
    for i in range(0, len(dados), 1):
        dados[i] = i - 1