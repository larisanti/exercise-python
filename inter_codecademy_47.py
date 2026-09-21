"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar testes unitários.

Notes:
- não é fácil testar função só com assert
- usar métodos do unittest: assertRaises, assertWarns
ver sintaxes:
https://docs.python.org/3/library/unittest.html#unittest.TestCase.output
"""

import unittest
import alerts

# Write your code here:
class SystemAlertTests(unittest.TestCase):

  def test_power_outage_alert(self):
    self.assertRaises(alerts.PowerError, alerts.power_outage_detected, True)

  def test_water_levels_warning(self):
    self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check, 150)

unittest.main()