"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Introdução aos gotchas em Python.

Notes:
- não usar [] como argumento padrão
^ ou outro objeto mutável
- definir como None
- acrescentar if x is None
- None é imutável, não é um problema quando altera o objeto na memória]
"""

# # INCORRETO:
# # todas as chamadas da função compartilham a mesma memória 
# def update_order(new_item, current_order=[]):
#   current_order.append(new_item)
#   return current_order

# order1 = update_order({'item': 'burger', 'cost': '3.50'})
# order2 = update_order({'item': 'soda', 'cost': '1.50'})

# print(order2)

# CORRETO:
def update_order(new_item, current_order=None):
  if current_order is None:
    current_order = [] # cria uma lista nova na memória a cada chamada

  current_order.append(new_item)
  return current_order

order1 = update_order({'item': 'burger', 'cost': '3.50'})
order2 = update_order({'item': 'soda', 'cost': '1.50'})

print(order2)