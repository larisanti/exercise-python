"""
Curso: 
College Algebra with Python (freeCodeCamp)

Objetivo: 
Resolver equações de proporção (regra de três) utilizando Python.

Notes:
Como orientado pelo professor, copiei o código e depois testei trocando o valor das variáveis.
Entendi que é a lógica da regra de três. 
Achei interessante como fica simples resolver usando python. Deve facilitar muito pra números complexos.
"""

# Put a zero in for the unknown value
n1 = 1
d1 = 2
n2 = 4
d2 = 0

if n2==0:
    answer = d2 * n1 / d1
    print("n2 = ", answer)
if d2==0:
    answer = n2 * d1 / n1
    print("d2 = ", answer)
