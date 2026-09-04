"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar conceito de operator overloading.

Notes:
- operator overloading -> definr como operadores vão funcionar pra objetos
- dunder métodos pra mudar comportamento dos operadores:
  __sub__()
  __add__()
- retorna lenght -> __len__()
"""

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)

  def __len__(self):
    return len(self.attendees) #attendees é lista
    
e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
# adicionar employees ao meeting
m1 + e1
m1 + e2
m1 + e3
print(len(m1))