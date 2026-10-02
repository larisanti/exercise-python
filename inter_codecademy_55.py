"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar iteração.

Notes:
- input-dependent iterator = terminate based on the length of one or more input values
^ usar quando precisa modificar um iterator
- sintax
  itertools.chain(*iterables)
"""

import itertools

great_dane_foods = [2439176, 3174521, 3560031]
min_pin_pup_foods = [6821904, 3302083]
pawsome_pup_foods = [9664865]

# Write your code below: 
all_skus_iterator = itertools.chain(great_dane_foods, min_pin_pup_foods, pawsome_pup_foods)

for i in all_skus_iterator:
  print(i)