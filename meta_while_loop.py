"""
Curso:
Programming in Python (Meta - Database Engineer Specialization)

Objetivo: 
Introdução ao while.
"""

# while vai repetir menos do que o tamanho da lista

favorites = ['Pizza', 'Apple Cake', 'Beijinho', 'Yakisoba', 'Melona']

count = 0

while count < len(favorites):
    print ('I like this', favorites) # precisa usar index invés de item (não entendi essa parte)

# Gerou infinitamente, incluir count

while count < len(favorites):
    print ('I like this', favorites[count])
    count += 1
    