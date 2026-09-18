"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Criar teste unitário.

Notes:
- módulo unittest -> tem um test runner
steps:
1. criar uma classe que herda de unittest.TestCase
2. refatorar/alterar as funções de teste pra que sejam métodos da classe
  (funções devem começar com test)
3. alterar assert statements -> assertEqual (método de unittest.TestCase)
   self.assertEqual(<function call>, <value to compare function call to>, <error message>)
4. rodar -> unittest.main()
"""

# Write your code below:
import unittest

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    location = 'back'
  return location

class NearestExitTests(unittest.TestCase):
  def test_row_1(self):
    self.assertEqual(get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')
  def test_row_20(self):
    self.assertEqual(get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')
  def test_row_40(self):
    self.assertEqual(get_nearest_exit(40),'back', 'The nearest exit to row 40 is in the back!')

test_row_1()
test_row_20()
test_row_40()