class Product:

    def __init__(self, name, price, quantity):
        if not (isinstance(name, str) and name != ""):
            raise ValueError(f"Name expected, string can't be empty")
        self.name = name
        if not (isinstance(price, (int, float)) and price > 0):
            raise ValueError(f"Positive price expected, can't be "
                             f"negative")
        self.price = price
        if not (isinstance(quantity, int) and quantity > 0):
            raise ValueError(f"Quantity needs to be a positive "
                             f"number")
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return (f"{self.name}, Price: {self.price}, Quantity:"
                f" {self.quantity}")

    def buy(self, quantity):
        if not self.active:
            raise Exception("Product is not active")
        if quantity > self.quantity:
            raise Exception(f"There are not enough in stock, "
                             f"the available quantity is"
                             f" {self.quantity}")
        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price
