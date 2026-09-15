"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Criar exceção personalizada herdando de Exception.

Notes:
- padrão: nome da exceção deve terminar com Error
- raise -> lança a exceção
- personalizar deixa o erro mais claro de entender
- ajuda documentar regras do programa
"""

inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}


#Write your code below (Checkpoint 2):
class InventoryError(Exception): # custom error é subclass da builtin Exception
  pass

def submit_order(instrument, quantity):
  supply = inventory[instrument]
  
  # Write your code below (Checkpoint 3 & 4): 
  if quantity > supply:
    raise InventoryError
  else:
    inventory[instrument] -= quantity
    print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

instrument = 'Piano'
quantity = 5
submit_order(instrument, quantity)
