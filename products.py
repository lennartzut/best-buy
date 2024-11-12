class Product:
    """
    A class to represent a product in the store.

    Attributes:
    name (str): The name of the product.
    price (float): The price of the product.
    quantity (int): The available quantity of the product.
    active (bool): Indicates if the product is active.
    promotion (Promotion): The promotion applied to the product.
    """

    def __init__(self, name, price, quantity):
        """
        Initialize the product with name, price, quantity.
        Set the product to active by default.

        Parameters:
        name (str): The name of the product.
        price (float): The price of the product (must be positive).
        quantity (int): The initial quantity of the product
                       (must be non-negative).

        Raises:
        ValueError: If name is empty, price is not positive, or
                    quantity is negative.
        """
        if not (isinstance(name, str) and name):
            raise ValueError("Name expected, string can't be empty")
        self.name = name
        if not (isinstance(price, (int, float)) and price > 0):
            raise ValueError(
                "Positive price expected, can't be negative")
        self.price = price
        if not (isinstance(quantity, int) and quantity >= 0):
            raise ValueError(
                "Quantity needs to be a non-negative number")
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self):
        """
        Get the quantity of the product.

        Returns:
        int: The available quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Set the quantity of the product. If quantity is zero,
        deactivate the product.

        Parameters:
        quantity (int): The quantity to set.
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """
        Check if the product is active.

        Returns:
        bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activate the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivate the product.
        """
        self.active = False

    def set_promotion(self, promotion):
        """
        Set a promotion for the product.

        Parameters:
        promotion (Promotion): The promotion to apply to the product.
        """
        self.promotion = promotion

    def get_promotion(self):
        """
        Get the current promotion of the product.

        Returns:
        Promotion: The promotion applied to the product.
        """
        return self.promotion

    def show(self):
        """
        Display product details, including the promotion if available.

        Returns:
        str: The product details.
        """
        promo_text = f", Promotion: {self.promotion.name}" if (
            self.promotion) else ""
        return (f"{self.name}, Price: {self.price}, Quantity: "
                f"{self.quantity}{promo_text}")

    def buy(self, quantity):
        """
        Purchase a given quantity of the product.

        Parameters:
        quantity (int): The quantity to purchase (must be positive).

        Returns:
        float: The total price for the purchased quantity.

        Raises:
        Exception: If the product is not active or if the requested
                   quantity exceeds the available stock.
        ValueError: If quantity is non-positive.
        """
        if not self.active:
            raise Exception("Product is not active")
        if quantity <= 0:
            raise ValueError(
                "Quantity to buy must be a positive number")
        if quantity > self.quantity:
            raise Exception("Quantity larger than available stock")

        if self.promotion:
            print(
                f"Applying promotion: {self.promotion.name} to {self.name}")
            total_price = self.promotion.apply_promotion(self,
                                                         quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    """
    A class to represent a non-stocked product, such as a digital item.
    """

    def __init__(self, name, price):
        """
        Initialize the non-stocked product with a quantity of 0.

        Parameters:
        name (str): The name of the product.
        price (float): The price of the product.
        """
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        """
        Prevent setting the quantity for a non-stocked product.

        Raises:
        Exception: Always raised because non-stocked products cannot
                   have a set quantity.
        """
        raise Exception(
            "Cannot set quantity for a non-stocked product")

    def get_quantity(self):
        """
        Indicate that the product is always available (unlimited).

        Returns:
        float: Infinite availability.
        """
        return float('inf')

    def buy(self, quantity):
        """
        Buy a given quantity of the non-stocked product.

        Parameters:
        quantity (int): The quantity to buy (must be positive).

        Returns:
        float: The total price for the purchased quantity.

        Raises:
        Exception: If the product is not active.
        ValueError: If quantity is non-positive.
        """
        if not self.is_active():
            raise Exception("Product is not active")
        if quantity <= 0:
            raise ValueError(
                "Quantity to buy must be a positive number")

        if self.promotion:
            print(
                f"Applying promotion: {self.promotion.name} to {self.name}")
            total_price = self.promotion.apply_promotion(self,
                                                         quantity)
        else:
            total_price = self.price * quantity

        return total_price

    def show(self):
        """
        Display non-stocked product details, including promotion.

        Returns:
        str: The non-stocked product details.
        """
        promo_text = f", Promotion: {self.promotion.name}" if (
            self.promotion) else ""
        return (
            f"{self.name}, Price: {self.price}, Available: Unlimited"
            f"{promo_text}")


class LimitedProduct(Product):
    """
    A class to represent a limited product that can only be purchased
    a limited number of times per order.
    """

    def __init__(self, name, price, quantity,
                 max_quantity_per_order):
        """
        Initialize the limited product with a maximum quantity per order.

        Parameters:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The available quantity of the product.
        max_quantity_per_order (int): The max quantity allowed per order.

        Raises:
        ValueError: If max_quantity_per_order is not a positive integer.
        """
        super().__init__(name, price, quantity)
        if not (isinstance(max_quantity_per_order, int) and
                max_quantity_per_order > 0):
            raise ValueError(
                "Max quantity per order must be a positive integer")
        self.max_quantity_per_order = max_quantity_per_order

    def buy(self, quantity):
        """
        Purchase a given quantity of the limited product.

        Parameters:
        quantity (int): The quantity to purchase (must not exceed the
                       max per order).

        Returns:
        float: The total price for the purchased quantity.

        Raises:
        Exception: If quantity exceeds the max allowed per order.
        """
        if quantity > self.max_quantity_per_order:
            raise Exception(
                f"Cannot buy more than {self.max_quantity_per_order} "
                f"of this item in one order")
        return super().buy(quantity)

    def show(self):
        """
        Display limited product details, including promotion and
        max per order.

        Returns:
        str: The limited product details.
        """
        base_show = super().show()
        return f"{base_show}, Max per order: {self.max_quantity_per_order}"
