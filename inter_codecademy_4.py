"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivos:
Praticar combinação de argumentos e dicionário.

Notes:
- elementos normais/obrigatórios: antes de *args
- usar for pra percorrer cada item da tupla (já salvada com *args)
"""

tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)

# syntax: nested keys
def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = ''

def assign_and_print_order(table_number, *order_items):
  tables[table_number]['order'] = order_items
  for order_item in order_items:
    print(order_item)

# chamar a funções e printar
assign_table(2, 'Arwa', True)
assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')
print(tables)