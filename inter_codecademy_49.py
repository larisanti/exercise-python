"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar testes unitários.

Notes:
- test fixtures -> seta o teste pra um estado conhecido
^ pra rodar os testes nas mesmas condições
- evita falsos negativos/positivos
- não é recomendado quando o custo for alto
"""

import unittest
import kiosk

class CheckInKioskTests(unittest.TestCase):

  def test_check_in_with_flight_number(self):
    print('Testing the check-in process based on flight number')

  def test_check_in_with_passport(self):
    print('Testing the check-in process based on passport')

  @classmethod
  # seta o ambiente e limpa
  def setUpClass(cls):
    kiosk.power_on_kiosk()
    
  @classmethod
  def tearDownClass(cls):
    kiosk.power_off_kiosk()
    
  # volta pra home page, onde devem começar os testes  
  def setUp(self):
    kiosk.return_to_welcome_page()

unittest.main()