"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar funções geradoras (generator functions)

Notes:
- yield (/jiːld/) -> pausa a função e mantém as variáveis locais
- return -> para/encerra a função
"""

# Write your code below: 
def class_standing_generator():
  yield 'Freshman'
  yield 'Sophomore'
  yield 'Junior'
  yield 'Senior'

class_standings = class_standing_generator()
for x in class_standings:
  print(x)
