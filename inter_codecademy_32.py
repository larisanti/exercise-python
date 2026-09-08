"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar métodos get, set, delete.

Notes:
- get, set, delete: tipos de funções pra implementar encapsulamento
^ controlam o acesso e a modificação dos atributos da classe
- protegem e validam os dados
- encapsulamento melhora organização e segurança
"""

class Employee():
  new_id = 1
  def __init__(self, name=None):
    self.id = Employee.new_id
    Employee.new_id += 1
    self._name = name

  # getter method
  def get_name(self):
    return self._name
  
  # setter
  def set_name(self, name="Lari"):
    self._name = name
  
  # deleter
  def del_name(self):
    del self._name

e1 = Employee("Maisy")
e2 = Employee()

# e1 = Employee("Maisy")
# e2 = Employee()
# print(e1.get_name())

# e2.set_name("Fluffy")
# print(e2.get_name())

# e2.del_name()
# print(e2.get_name())
