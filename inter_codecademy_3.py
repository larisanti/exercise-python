"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar função com qualquer quantidade de argumentos.

Notes:
- operador * -> positional argument packing
- junta os argumentos em uma única tupla
- nome padrão: *args (mas pode ser outro)
"""

def print_order(*order_items):
  print(order_items)

# não importa a ordem em que passo os argumentos
print('Orange Juice', 'Pancakes', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')