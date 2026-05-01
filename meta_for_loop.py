"""
Curso:
Programming in Python (Meta - Database Engineer Specialization)

Objetivo: 
Praticar o uso de for e range.
"""

# my favorites = ['Pizza', 'Apple Cake', 'Beijinho', 'Yakisoba', 'Melona']

# iterate = repetir
for i in range(10):
    print ('Looping..', i)

# mudar a iteration de números por um itens da lista:

favorites = ['Pizza', 'Apple Cake', 'Beijinho', 'Yakisoba', 'Melona']

for i in favorites:
    print ('Looping..', i)

# mudar i para mostrar o item que está sendo iterado/repetido

for item in favorites:
    print ('Like this ', item)