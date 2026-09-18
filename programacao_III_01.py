"""
Curso:
Programação III (Uninter - Bacharelado em Engenharia de Software)

- calcular fatorial
  5! = 5*4*3*2*1
- para de abrir funções quando chegar no valor mínimo da fatorial (1)
"""

# # Criar fatorial iterativo
# def fatorial_iterativo(n):
#     fator = 1
#     if n < 0:
#         return None
#     elif n == 0 or n == 1:
#         return fator
#     else:
#         # iteração
#         for i in range(1, n+1):
#             fator *= i
#         return fator
#
# print(fatorial_interativo(5))

# Criar fatorial recursivo
# função chama ela mesma
def fatorial_recursivo(n):
    fator = 1
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return fator
    else:
        return n * fatorial_recursivo(n-1)

print(fatorial_recursivo(5))