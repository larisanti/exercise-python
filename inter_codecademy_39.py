"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Resolver erro com try/except/else/finally.

Notes:
- finaly -> sempre executa, com ou sem erro
- finally vai por último:
  try/except/else/finally
"""

import database

instrument = 'Kora'
database.connect_to_database()

try:
  database.display_instrument_info(instrument)
except KeyError:
  print('Oh no! This instrument does not exist.')
else:
  print(instrument)
finally:
  database.disconnect_from_database()
