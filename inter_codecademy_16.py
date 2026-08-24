"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar enclosing scope.

Notes:
- enclosing scope = nonlocal scope
- funções aninhadas -> função dentro de função
^ fluxo de acesso é de baixo pra cima
"""

def calc_paint_amount(width, height):

  square_feet = width * height

  def calc_gallons():
      return square_feet / 400

  return calc_gallons()

print('Number of paint gallons needed: ')
print(str(calc_paint_amount(30,20)))