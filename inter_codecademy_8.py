"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivos:
Revisar operadores * e ** para desempacotar chamadas de função.

Notes:
- ordem: positional -> *args -> keyword -> **kwargs
- unpacking transforma uma coleção de dados em argumentos separados
- unpacking: 
  - com *args: desempacota tuplas/listas
  - com **kwargs: desempacota dicionários
- útil quando a função exige argumentos separados, mas os dados estão dentro 
de estrutura de lista/dict
"""

def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  split_price = (total + total_tip) / split
  print(split_price)

table_7_total= [534.50, 20.0, 5]

calculate_price_per_person(*table_7_total)