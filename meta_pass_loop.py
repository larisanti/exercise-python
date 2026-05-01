"""
Curso:
Programming in Python (Meta - Database Engineer Specialization)

Objetivos: 
Praticar o uso de pass em loops.
"""

# pass serve pra inserir um bloco vazio no loop (pode ser usado em função também)
# Não executa nada

favorites = ['Pizza', 'Apple Cake', 'Beijinho', 'Yakisoba', 'Melona']

for food in favorites:
    if food == 'Beijinho':
        pass # pula essa parte
    print('Other foods I like are', food) # Mostrou tudo, como se pass não existisse

# Não dá erro