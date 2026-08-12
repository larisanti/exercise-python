"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar funções com **kwargs.

Notes:
- **kwargs = keyword arguments
^ pode usar outro nome
- gera o tipo dict -> pares chave=valor (nome='Larissa')
"""

tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)

def assign_food_items(**order_items):
    print(order_items)
    food = order_items.get('food')
    drinks = order_items.get('drinks')
    print(food)
    print(drinks)

assign_food_items(food='Pancakes, Poached Egg', drinks='Water')