"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar iteração.

- método __next__() retorna próximo valor
- função next() faz o mesmo ^
- StopIteration -> não tem mais valor no dict
- for usa internamente iter() e next()
^ for não mostra 
"""

dog_foods = {
  "Great Dane Foods": 4,
  "Min Pip Pup Foods": 10,
  "Pawsome Pup Foods": 8
}

# Write your code below:
dog_food_iterator = iter(dog_foods)
#print(dog_food_iterator) # retorna endereço na memória 0x7f7c59ca4188 
next_dog_food1 = next(dog_food_iterator)
next_dog_food2 = next(dog_food_iterator)
next_dog_food3 = next(dog_food_iterator)

print(next_dog_food1)
print(next_dog_food2)
print(next_dog_food3)

next(dog_food_iterator) # erro: StopIteration