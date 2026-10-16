"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar funções geradoras (generator functions)

Notes:
- .send() -> envia valor ao generator usando yield
- só com yield o generator só produz valores, não recebe dados
"""

MAX_STUDENTS = 50

def get_student_ids():
  student_id = 1
  while student_id <= MAX_STUDENTS:
    # Write your code below
    n = yield student_id
    if n is not None:
      student_id = n
      continue
          
    student_id += 1

student_id_generator = get_student_ids()
for i in student_id_generator:
  # Write your code below
  if i == 1:
    i = student_id_generator.send(25)
  
  print(i)