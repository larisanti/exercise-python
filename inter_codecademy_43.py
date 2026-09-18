"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Criar teste unitário.

Notes:
- teste unitário: testa um único comportamento (função/loop/variável)
- test case: valida se um set de inputs produz o output esperado
"""

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    #location = 'middle'
    location = 'back'
  return location

# testar saída de emergÊncia
def test_row_1():
  assert get_nearest_exit(1) == 'front', 'The nearest exit to row 1 is in the front!'

# testar fileira do meio
def test_row_20():
  assert get_nearest_exit(20) == 'middle', 'The nearest exit to row 20 is in the middle!'

# testar fileira do fundo
def test_row_40():
 assert get_nearest_exit(40) == 'back', 'The nearest exit to row 40 is in the back!'

# investigar erros
test_row_1()
test_row_20()
test_row_40()