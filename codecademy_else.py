"""
Curso: 
Learn Python 3 (Codecademy)

Objetivo:
Compreender a lógica das condicionais if/else/elif.
"""

# Add an additional check to a previous if statement

credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")

###

# Convert the grades to letters grades
grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")