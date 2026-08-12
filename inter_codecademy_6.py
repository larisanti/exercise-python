"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivos:
Praticar combinação de argumento posicional + **kwargs

Notes:
- argumento posicional sempre vem antes
- .get busca valor de uma key/chave do dicionário
^ não quebra se a chave não existir
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

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

assign_table(2, 'Douglas', True)
print('--- tables with Douglas --- \n', tables)

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

print('\n --- tables after update --- \n')
# 2 vai pra table_number e food e drink viram dicionário em order_items
assign_food_items(2, food='Seabass, Gnocchi, Pizza', drinks='Margarita, Water')
print(tables)