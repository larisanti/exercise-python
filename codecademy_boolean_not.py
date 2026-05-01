
"""
Curso: 
Learn Python 3 (Codecademy)

Objetivos:
Praticar operador booleano and not e if statement.
"""

# Se for True e aplicar not, vira False

statement_one = False

statement_two = True

credits = 120
gpa = 1.8

if credits >= 120:
  print("You do not have enough credits to graduate.")

if gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")
