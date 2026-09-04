"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar conceito de abstração. 

Notes:
- abstraction: esconde detalhes interno
^ mostra o essencial pra uso da classe/objeto
- métodos abstratos usam o decorator:
  @abstractmethod
  ^ precisa ser implementado na subclasse
- classes abstratas servem pra organizar o código
"""

from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod
  def say_id(self):
    pass

# add AbstractEmployee faz com que Employee herde tudo
# incluindo @abstractmethod
class Employee(AbstractEmployee):
    # pode modificar método say_id
    def say_id(self):
      print("The ID is {}".format(self.id))

e1 = Employee()
e1.say_id()