"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar iteração.

Notes:
- iterator protocol: __iter__() and __next__() methods
- custom iterator class: não dá pra inserir for nas classes, 
  pra ser uma classe iteravel precisa usar os métodos do iterator protocol
"""

class FishInventory:
  def __init__(self, fishList):
      self.available_fish = fishList

fish_inventory_cls = FishInventory(["Bubbles", "Finley", "Moby"])

# Write your code below:
for fish in fish_inventory_cls:
  print(fish)
# gerou TypeError, que é esperado quanto tento iterar sobre 
# uma classe apenas com for, sem implementar o iterator protocol