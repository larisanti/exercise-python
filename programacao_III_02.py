"""
Curso:
Programação III (Uninter - Bacharelado em Engenharia de Software)

Objetivo:
Praticar recursão

Notas:
"Como podemos comparar o desempenho de diferentes algoritmos para uma mesma aplicação? Podemos mensurar isso?"
- algoritmo: quanto menos complexo, mais eficiente é
- complexidade aumenta com o conjunto de dados (n)
^ mais memória e mais tempo
- notação Big-O: O(n)
                   ^ nro de operações
- função recursiva, chama ela mesma = sempre big-o(n)
"""

# nível de complexidade da chamada da função: constante, big-o -> O(1)
# não tem laço, não tem recursividade
def fatorial(n):
    fator = 1
    if n == 0 or n == 1:
        return fator
    else:
        return n * fatorial(n-1)

# programa principal
x = fatorial(5)
print(fatorial(5))