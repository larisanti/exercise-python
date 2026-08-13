"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivos:
Praticar a ordem dos argumentos na função.

Notes:
- ordem correta pra declarar os parâmetros na função:
^ positional -> *args -> keyword -> **kwargs
- parâmetro = placeholder/variável da def pra receber o valor
- argumento = valor que vai ser enviado pra função
"""

# Write your code below: 
def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
    print(appetizer)
    print(entrees)
    print(sides)
    print(dessert_scoops)

single_prix_fixe_order(
  'Baby Beets', #positional
  'Salmon', 'Scallops', #*args (tupla)
  sides='Mashed Potatoes', #keyword/obrigatório
  ice_cream_scoop1='Vanilla', ice_cream_scoop2='Cookies and Cream' #**kwargs (dicionário)
)