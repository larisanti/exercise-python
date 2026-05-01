"""
Curso: 
Learn Python 3 (Codecademy)

Objetivos:
Praticar operador booleano and e if statement.
"""

# Mesmo que uma parte seja True, o statement será False se uma das partes for False

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120
gpa = 3.4

if gpa >= 2.0 and credits >= 120:
    print("You meet the requirements to graduate!")
