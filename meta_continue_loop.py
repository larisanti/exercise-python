"""
Curso:
Programming in Python (Meta - Database Engineer Specialization)

Objetivo: 
Praticar o uso de continue em loops
"""

# continue = pula uma parte do loop e continua o resto

favorites = ['Pizza', 'Apple Cake', 'Beijinho', 'Yakisoba', 'Melona']

for food in favorites:
    if food == 'Beijinho':
        continue
    print('Other foods I like are', food) # mostra o resto pulando o item do if
