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
        self.promotion = None

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

    def set_promotion(self, promotion):
        """Setter function for promotion."""
        self.promotion = promotion

    def get_promotion(self):
        """Getter function for promotion."""
        return self.promotion

    def show(self):
        """Return a string that represents the product, including
        any promotion if available."""
        promo_text = f", Promotion: {self.promotion.name}" if (
            self.promotion) else ""
        return (f"{self.name}, Price: {self.price}, Quantity:"
                f" {self.quantity}{promo_text}")

    def buy(self, quantity):
        """Buy a given quantity of the product. Return the total
        price (float) of the purchase. Update the quantity of the
        product."""
        if not self.active:
            raise Exception("Product is not active")
        if quantity <= 0:
            raise ValueError(
                "Quantity to buy must be a non-negative number")
        if quantity > self.quantity:
            raise Exception("Quantity larger than available stock")
        if self.promotion:
            print(
                f"Applying promotion: {self.promotion.name} to"
                f" {self.name}")
            total_price = self.promotion.apply_promotion(self,
                                                         quantity)
        else:
            total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    """A class to represent a non-stocked product, such as a
    digital item."""
    def __init__(self, name, price):
        """Initialize the non-stocked product with a quantity of
        0."""
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        """Override the set_quantity method to prevent changing
        the quantity."""
        raise Exception("Cannot set quantity for a non-stocked "
                        "product")

    def buy(self, quantity):
        """Override the buy method to allow unlimited purchases."""
        if not self.is_active():
            raise Exception("Product is not active")
        if quantity <= 0:
            raise ValueError(
                "Quantity to buy must be a positive number")
        if self.promotion:
            print(
                f"Applying promotion: {self.promotion.name} to"
                f" {self.name}")
            total_price = self.promotion.apply_promotion(self,
                                                         quantity)
        else:
            total_price = self.price * quantity
        return total_price

    def show(self):
        """Return a string that represents the non-stocked
        product, including any promotion."""
        promo_text = f", Promotion: {self.promotion.name}" if (
            self.promotion) else ""
        return (f"{self.name}, Price: {self.price}, "
                f"Available: Unlimited{promo_text}")


class LimitedProduct(Product):
    """A class to represent a limited product that can only be
    purchased X times in an order."""
    def __init__(self, name, price, quantity, max_quantity_per_order):
        """Initialize the limited product with a max quantity per
        order."""
        super().__init__(name, price, quantity)
        if not (isinstance(max_quantity_per_order, int) and
                max_quantity_per_order > 0):
            raise ValueError("Max quantity per order must be a "
                             "positive integer")
        self.max_quantity_per_order = max_quantity_per_order

    def buy(self, quantity):
        """Override the buy method to enforce max quantity per
        order."""
        if quantity > self.max_quantity_per_order:
            raise Exception(f"Cannot buy more than "
                            f"{self.max_quantity_per_order} of "
                            f"this item in one order")
        return super().buy(quantity)

    def show(self):
        """Return a string that represents the limited product,
        including any promotion."""
        base_show = super().show()
        return (f"{base_show}, Max per order:"
                f" {self.max_quantity_per_order}")
