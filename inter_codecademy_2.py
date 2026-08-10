"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Revisar argumentos em Python.

Notes:
- positional arguments: 
  print_name('Lari', 'Santi')
- keyword arguments: 
  (nome_parametro=valor)
- default arguments: 
  (def func(param=valor_padrao)
"""

tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables)

# Checkpoint 2 & 5
def assign_table(table_number, name, vip_status=False): 
  tables[table_number] =  [name, vip_status]

# Checkpoint 3
assign_table(6, 'Yoni', False)
print(tables)

# Checkpoint 4
assign_table(table_number=3, name='Martha', vip_status=True)
print(tables)

# Checkpoint 6
assign_table(4, 'Karla')
print(tables)
