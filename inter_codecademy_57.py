"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar funções geradoras (generator functions)

Notes:
- generator function -> retorna objeto iterador
- objeto iterador -> valores que podem ser percorridos
- diferença yield vs next:
  - yield -> produz valores dentro do gerador
  - next -> recupera esses valores do gerador (um por vez)
"""

def student_standing_generator():
  student_standings = ['Freshman','Senior', 'Junior', 'Freshman']
  # Write your code below:
  for student in student_standings:
    if student == 'Freshman':
      yield 500

standing_values = student_standing_generator()
print(next(standing_values))
print(next(standing_values))
print(next(standing_values)) # StopIteration