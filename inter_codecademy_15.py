"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivos:
Praticar o conceito de escopo local (Local Scope) e corrigir erro de acessibilidade (NameError).

Notes:
- local scope -> criado quando uma função é chamada
- Variáveis locais não podem ser acessadas por códigos fora da função
- "any names created in a local namespace are usually also locally scoped"
"""

def painting(paint_colors, picture):
  painting_statement = "To paint the " + picture + " we need the following colors: "
  print(painting_statement)
  for color in paint_colors:
      print(color)

painting(['Saffron', 'White', 'Green'], 'Indian Flag')