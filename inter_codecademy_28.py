"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar polimorfismo.

Notes:
- polymorphism -> apply identical operation ont different types of objects
- inheritance é uma forma de aplicar polimorfismo
"""

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")

# loop pra chamar objetos de tipos diferentes
# cada objeto executa o que está em sua classe
meeting = [Employee(), Admin(), Manager()]
for item in meeting:
  item.say_id()