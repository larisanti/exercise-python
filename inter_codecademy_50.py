"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar iteração.

Notes:
- iterables = objeto que pode ser iterado, pode ser passado para iter()
- iterators = objeto especial iterable que foi passado pra iter() e tem memória
- for converte por baixo (iterable -> iterator)
- iter() com next() dá mais controle sobre a iteração
^ não precisa percorrer todos os itens, controla manualmente quais pegar
- dir() -> mostra todos os objetos
"""

sku_list = [7046538, 8289407, 9056375, 2308597]

print(dir(sku_list))

sku_iterator_object_one = sku_list.__iter__()
print(sku_iterator_object_one)

sku_iterator_object_two = iter(sku_list)
print(sku_iterator_object_two)