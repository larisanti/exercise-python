"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar modificação de global scope.

Notes:
- não dá pra alterar variável global dentro da função
^ usar "global" antes do nome
"""

def print_available(color):
  global paint_gallons_available 
  paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
  }
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')

print_available('red')
for color in paint_gallons_available:
  print(color)