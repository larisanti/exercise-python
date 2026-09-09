"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objective:
Create a digital school catalog.

Requisites:
- Create a parent class called School with properties: name, level ('primary', 'middle', or 'high'), and numberOfStudents.
- Add getters for all properties and a setter for numberOfStudents.
- Implement a __repr__ method in School to display school information.
- Create a PrimarySchool class that inherits from School and adds a pickupPolicy property, its getter, and overrides __repr__.
- Create a MiddleSchool class that inherits from School (no extra properties).
- Create a HighSchool class that inherits from School, adds a sportsTeams property, its getter, and overrides __repr__.
- Test each class by creating objects and using their methods.
"""

class School():
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name
  
  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents
  
  def set_numberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents
  
  # imprimir
  def __repr__(self):
    return f'A {self.level} school named {self.name} with {self.numberOfStudents} students.'
  
class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return f'{parentRepr} pickup policy: {self.pickupPolicy}'

# sem métodos adicionais
class MiddleSchool(School):
  pass

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams
  
  def get_sportsTeams(self):
    return self.sportsTeams
  
  def __repr__(self):
    parentRepr = super().__repr__()
    return f'{parentRepr} sport teams: {self.sportsTeams}'

# testar objetos, passar valores
school1 = School('School One', 'high', 100)
print(school1)
print(school1.get_name())
print(school1.get_level())
school1.set_numberOfStudents(500)
print(school1.get_numberOfStudents())

school2 = PrimarySchool('School Two', 150, 'Pickup Allowed')
print(school2.get_pickupPolicy())
print(school2)

school3 = HighSchool('School Three', 500, ["Soccer", "Basketball"])
print(school3.get_sportsTeams())
print(school3)
