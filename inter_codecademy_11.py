"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar namespace do tipo built-in.

Notes:
- namespace -> sistema do Python para garantir que cada nom de variável seja único
- é criado quando o intepretador é iniciado
- regra de ordem de busca de variáveis (LEGB):
  L = local ou
  E = enclosing
  G = global
  B = built-in
"""

import builtins

# ver todas as variáveis built-in
# print(dir(__builtins__))

numbers = [10, 25, 5, 40]

print(len(numbers))
print(max(numbers))
print(sum(numbers))
