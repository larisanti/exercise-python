"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Resolver erro diferentes erros com try/except.

Notes: 
- pode usar vários blocos de except
- não precisa de "as e:"
- erro genérico por último -> tipo de erro: Exception
"""

instrument_prices = {
  'Banjo': 200,
  'Cello': 1000,
  'Flute': 100,
}

def display_discounted_price(instrument, discount):
  full_price = instrument_prices[instrument]
  discount_percentage = discount / 100
  discounted_price = full_price - (full_price * discount_percentage)
  print("The instrument's discounted price is: " + str(discounted_price))

instrument = 'Banjo' # causa TypeError
discount = '20'

# Write your code below:
try:
  display_discounted_price(instrument, discount)
except KeyError:
  print('An invalid instrument was entered!')
except TypeError:
  print('Discount percentage must be a number!')
except Exception:
  print('Hit an exception other than KeyError or TypeError!')
