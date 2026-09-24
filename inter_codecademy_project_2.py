"""
Curso:
Learn Intermediate Python 3 (Codecademy)

PROJECT: UNIT TESTING

Objectives:
- Implemented a suite of unit tests for existing software.
- Ran and modified the tests according to results.
- Improved the existing software.
"""

import unittest
import surfshop

class TestCart(unittest.TestCase):

  def setUp(self):
    self.cart = surfshop.ShoppingCart()
  
  def test_add_surfboards(self):
    num_surfboards = self.cart.add_surfboards(1)
    self.assertEqual(num_surfboards, 'Successfully added 1 surfboard to cart!')

  def test_add_many_surfboards(self):
    for surfboards in [2, 3, 4]:
        with self.subTest(surfboards=surfboards):
            total = self.cart.add_surfboards(surfboards)
            expected = f'Successfully added {surfboards} surfboards to cart!'
            self.assertEqual(total, expected)

  @unittest.skip
  def test_too_many_surfboards(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)
  
  #@unittest.expectedFailure
  def test_apply_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

unittest.main()