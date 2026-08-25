"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar a regra LEGB (Scope Resolution).

Notes:
- LEGB = local -> enclosing -> global -> built-in
- é a ordem que o python procura variáveis (de dentro pra fora)
- o primeiro que ele achar, ele usa e para de procurar
"""

color = 'green'

# Fix the function below:
def change_color(new_color):
  to_update = new_color

  def disp_color():
    print('The original color was: ' + color)

  disp_color()

  global color
  color = to_update

  print('The new color is: ' + color)

change_color('blue')