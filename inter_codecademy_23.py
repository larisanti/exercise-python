"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar conceito de herança entre classes.

Notes:
- inheritance -> quando a classe (child) herda propriedades e métodos de outra (parent)
- útil:
  * reutilizar código
  * criar relações parent-child
"""

# superclass
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1
  # method
  def say_id(self):
    print("My id is {}.".format(self.id))

# subclass (herda de Employee)
class Admin(Employee):
  pass

e1 = Employee()
e2 = Employee()
e3 = Admin() # objeto 1
e3.say_id() # objeto 2