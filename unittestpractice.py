import datetime
import unittest
import datetime

class TooManyBoardsError(Exception):
    pass

class CheckoutDateError(Exception):
    pass

class ShoppingCart:
    def __init__(self):
        self.num_surfboards = 0
        self.checkout_date = None
        self.locals_discount = False

    def add_surfboards(self, quantity=1):
        if self.num_surfboards + quantity > 4:
            raise 'Cart cannot have more than surfboards in it!'
        else:
            self.num_surfboards += quantity
            suffix = '' if quantity == 1 else 's'
            return f'Successfully added {quantity} surfboard{suffix} to cart!'

    def set_checkout_date(self, date):
        if date <= datetime.datetime.now():
            raise CheckoutDateError
        else:
            self.checkout_date = date

    def apply_locals_discount(self):
        self.locals_discount = True


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_surfboards(self):
        message = self.cart.add_surfboards(quantity=2)
        self.assertEqual(message, 'Successfully added 2 surfboards to cart!')
    
    def test_add_too_many_surfboards(self):
        self.assertRaises(BaseException, self.cart.add_surfboards, 6)



unittest.main()
