"""
Curso: 
Learn Python 3 (Codecademy)

Objetivos:
Praticar operador booleano or e if statement.
"""

# Se um é True, o outro é False

statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

credits = 118
gpa = 2.0

if gpa >= 2.0 or credits >= 118:
  print("You have met a least one of the requirements.")