"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar conceito de herança entre classes (Part 1).

Notes:
- multiple inheritance: classe herda features de + de 1 parent
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

# herda de Employee e Admin
class Manager(Admin):
  def say_id(self):
   super().say_id()
   print("I am a manager.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()
e4.say_id()