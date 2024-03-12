class TooManyBoardsError(Exception):
    def __str__(self):
      message = "Cart cannot have more than 4 surfboards in it!"
      return message

class ShoppingCart:
    def __init__(self):
        self.num_surfboards = 0
        self.checkout_date = None
        self.locals_discount = False

    def add_surfboards(self, quantity=1):
        if self.num_surfboards + quantity > 4:
            raise TooManyBoardsError
        else:
            self.num_surfboards += quantity
            suffix = '' if quantity == 1 else 's'
            return f'Successfully added {quantity} surfboard{suffix} to cart!'

    def apply_locals_discount(self):
        self.locals_discount = True
