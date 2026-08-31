"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar Programação Orientada a Objetos.

Notes:
- POO -> paradigma baseado em classes e objetos
- Classes definem a estrutura e comportamento
^ propriedades e métodos
- Objetos = instâncias das classes
"""

# definição da classe
class Employee:
  new_id = 1 # atributo compartilhado por todos obj
  
  # construtor
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1
  
  # método pra mostrar o id do obj
  def say_id(self):
    print("My ID is: {}".format(self.id))

# criam objetos/instâncias
e1 = Employee()
e2 = Employee()
e1.say_id()
e2.say_id()