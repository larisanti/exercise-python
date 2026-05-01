"""
Curso:
Programming in Python (Meta - Database Engineer Specialization)

Objetivo: 
Praticar o uso de break em loops.
"""

# break serve para parar o loop quando encontrar o item

favorites = ['Pizza', 'Apple Cake', 'Beijinho', 'Yakisoba', 'Melona']

for food in favorites:
    if food == 'Sushi':
        print('Yes one of my favorite is', food)
        break 
    else:
        print('No sorry, not a food on my list')
