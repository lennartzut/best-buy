class Product:
    """A class to represent a product in the store."""
    def __init__(self, name, price, quantity):
        """Create the instance variables (active is set to True)."""
        if not (isinstance(name, str) and name):
            raise ValueError(f"Name expected, string can't be empty")
        self.name = name
        if not (isinstance(price, (int, float)) and price > 0):
            raise ValueError(f"Positive price expected, can't be "
                             f"negative")
        self.price = price
        if not (isinstance(quantity, int) and quantity >= 0):
            raise ValueError(f"Quantity needs to be a non-negative "
                             f"number")
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Getter function for quantity. Return the quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0,
        deactivate the product."""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Getter function for active. Return True if the product
        is active, otherwise False."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Return a string that represents the product."""
        return (f"{self.name}, Price: {self.price}, Quantity: "
                f"{self.quantity}")

    def buy(self, quantity):
        """Buy a given quantity of the product. Return the total
        price (float) of the purchase. Update the quantity of the
        product."""
        if not self.active:
            raise Exception("Product is not active")
        if quantity <= 0:
            raise ValueError("Quantity to buy must be a "
                             "non-negative number")
        if quantity > self.quantity:
            raise Exception(f"Quantity larger than available stock")
        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price
