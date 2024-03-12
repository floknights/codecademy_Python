import surfshop
import unittest

class Tests(unittest.TestCase):
  
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboards1(self):
    self.assertEqual(self.cart.add_surfboards(quantity = 1), "Successfully added 1 surfboard to cart!")

  def test_add_surfboards2(self):
    for i in range(2, 5):
            with self.subTest(i=i):
                self.assertEqual(self.cart.add_surfboards(i), "Successfully added {} surfboards to cart!".format(i))
                self.cart = surfshop.ShoppingCart()

  def test_too_many_boards(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

  def test_apply_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

unittest.main()
