"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar iteração.

Notes:
- self.index -> track the position in the list
- raise StopIteration -> se index ultrapassar o lenght da lista
- return self -> geralmente retorna a si mesmo
"""

# Write your code below:
class CustomerCounter:
  def __iter__(self): 
    self.count = 0
    return self

  def __next__(self):
    self.count +=1 
 
    if self.count > 100:
      raise StopIteration
    return self.count

customer_counter = CustomerCounter()

for customer_count in customer_counter:
  print(customer_count)