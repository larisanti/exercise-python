"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar raising exceptions.

Notes:
- usar raise pra criar exception de mensagem de erro
- mensagem deve conter a melhor explicação pro user e pra quem ler o código
- raise interrompe a execução do programa
- usar try/except pra continuar execução
- útil pra depurar o código
- ref: https://docs.python.org/3/library/exceptions.html#BaseException
"""

instrument_catalog = {
  'Marimba': 1999,
  'Kora': 499,
  'Flute': 899
}

def print_instrument_price(instrument):
  # acrescentei if/else com raise + tipo de erro
  if instrument in instrument_catalog:
    print('The price of a ' + instrument + ' is ' + str(instrument_catalog[instrument]))
  else:
    raise KeyError(instrument + ' is not found in instrument catalog!')


print_instrument_price('Marimba')
print_instrument_price('Flute')
# KeyError: Piano não está no dict
# print_instrument_price('Piano')