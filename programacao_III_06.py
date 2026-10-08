
"""
Curso:
Programação III (Uninter - Bacharelado em Engenharia de Software)

Objetivo:
Praticar recursão e bubble sort.

Notas:
- notação Big-O -> usada pra mostrar como a complexidade de tempo e de espaço cresce
  à medida que a entrada também cresce
- especificar a ordem de grandeza da função = encontra a complexidade Big-O
- ações sequenciais no algoritmo -> usar adição
- ações aninhadas no algoritmo -> usar multiplicação
  ^ exceto pra PG (crescimento exponencial)
"""

# algoritmo bubble sort pra busca sequencial crescente
def bubble_sort(dados):
    n = len(dados)

    # controla quantas vezes percorre a lista
    for i in range(0, n, 1):

        # comparar elementos vizinhos 1 a 1
        for j in range(0, n - i - 1, 1):

            # esquerda > direita = eles trocam (swap)
            if dados[j] > dados[j + 1]:
                dados[j], dados[j + 1] = dados[j + 1], dados[j]

    return dados

lista = [43, 6, 32, 15, 21]
lista_ = bubble_sort(lista)
print("dados ordenados:", lista)