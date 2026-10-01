"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar iteração.

Notes:
- Infinite iterators: nunca param sozinhos, precisam de condição para parar.
  count(start,[step])
- Input-dependent iterators: param quando o menor iterável acaba.
- Combinatoric iterators: criam combinações matemáticas dos iteráveis.
"""

#Write your code below:
import itertools

max_capacity = 1000
num_bags = 0

for i in itertools.count(start=13.5, step=13.5):
  if i >= max_capacity:
    break
  num_bags += 1

print(num_bags)