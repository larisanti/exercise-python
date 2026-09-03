"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar conceito de herança entre classes (Part 2).

Notes:
- quando criar o objeto precisa chamar o construtor pra iniciar os atributos:
  dunder method: __init__
- método super é só para a 1a classe herdada
"""

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

# herda atributos e métodos de 2 parent
class Admin(Employee, User):
  def __init__(self):
    super().__init__()
    User.__init__(self, self.id, "Admin")

  def say_id(self):
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()