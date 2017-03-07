Class Mall(object):
    pass

class shop(mall)
    def __init__(self, name,product,product_id,price):
        self.name = name
        self.product =product
        self.product_id = product_id
        self.price = price



class shoppingCart(shop):
    """Creates shopping car objects
    for users of our fine website."""

    items_in_cart = {}

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print (product + " added to cart.")
        else:
            print (product + " is already in the cart.")

    def remove_item(self):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print (product + " is not in the cart.")



my_cart.add_item("dress", 450)