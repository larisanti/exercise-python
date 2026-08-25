"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar global scope.

Notes:
- criar fora das funções (sem identação)
- global scope = todos os arquivos podem ler
- local scope = dentro da função
"""

# variável global, pode ser dict
paint_gallons_available = {
  'red': 50,
  'blue': 72,
  'green': 99,
  'yellow': 33
}

def print_available(color):
  
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')

def print_all_colors_available():
  for color in paint_gallons_available:
    print(color)

print_available('red')
print_all_colors_available()
  