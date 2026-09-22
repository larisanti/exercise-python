"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Resolver erro diferentes erros com try/except.

Note: 
- rever sintaxe:
https://docs.python.org/3/tutorial/errors.html
"""

sales = {
  'Violin': {'price': 299, 'sold': '10'},
  'Cello': {'price': 899, 'sold': 5},
  'Drums': {'price': 450, 'sold': 0},
  'Flute': {'sold': 7},
}

def calculate_revenue(instrument, data):
  price = data['price']
  sold = int(data['sold'])
  revenue = price * sold
  avg = revenue / sold
  print('Instrument World - ' + instrument + ':')
  print('Total revenue: $' + str(revenue))
  print('Average sale price: $' + str(avg))
  print()

for instrument, data in sales.items():
  # Write your code below:
  try:
    calculate_revenue(instrument, data)
  except KeyError as e:
    print('Missing data for ' + instrument + ': ' + str(e))
  except ValueError as e:
    print('Invalid data for ' + instrument + ': ' + str(e))
  except ZeroDivisionError as e:
    print('Cannot calculate average for ' + instrument + ': ' + str(e))
