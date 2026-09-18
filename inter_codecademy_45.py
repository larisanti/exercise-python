"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Criar teste unitário.

Note:
ver tipos dde assert: 
https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
"""

import unittest
import entertainment

# Write your code below: 
class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    #sintaxe: self.assertIn(value, container)
    self.assertIn (daily_movie, licensed_movies)
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()


  def test_wifi_status(self):
    # self.assertTrue(value)
    self.assertTrue(wifi_enabled)
    wifi_enabled = entertainment.get_wifi_status()

# rodar testes
unittest.main()