"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar conceito de encapsulation.

Notes:
- encapsulation: esconde detalhes internos do objeto
- protege dados
- membros protegidos: _
- membros privados: __
- a convenção de uso do python controla isso,
^ não por restrição da linguagem (não tem inbuilt mechanism)
"""

class Employee():
    def __init__(self):
        self.id = None
        self._id = None
        self.__id = "Lari"
        

e = Employee()
print(dir(e))