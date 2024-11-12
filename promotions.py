from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract class representing a general promotion.

    Attributes:
    name (str): The name of the promotion.
    """

    def __init__(self, name):
        """
        Initialize the promotion with a name.

        Parameters:
        name (str): The name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Abstract method to apply promotion.

        Parameters:
        product (Product): The product the promotion is applied to.
        quantity (int): The quantity of the product to apply the promotion.

        Returns:
        float: The price after applying the promotion.
        """
        pass


class PercentDiscount(Promotion):
    """
    Class representing a percentage discount promotion.

    Attributes:
    name (str): The name of the promotion.
    percent (float): The percentage discount to be applied.
    """

    def __init__(self, name, percent):
        """
        Initialize the percentage discount promotion.

        Parameters:
        name (str): The name of the promotion.
        percent (float): The percentage discount to apply.
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Apply the percentage discount to the product.

        Parameters:
        product (Product): The product to apply the discount to.
        quantity (int): The quantity of the product being purchased.

        Returns:
        float: The total price after applying the percentage discount.
        """
        discount = (self.percent / 100) * product.price
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    """
    Class representing a second item at half price promotion.

    Attributes:
    name (str): The name of the promotion.
    """

    def __init__(self, name):
        """
        Initialize the second item at half price promotion.

        Parameters:
        name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Apply the second item at half price promotion to the product.

        Parameters:
        product (Product): The product to apply the promotion to.
        quantity (int): The quantity of the product being purchased.

        Returns:
        float: The total price after applying the promotion.
        """
        full_price_count = quantity // 2 + quantity % 2
        half_price_count = quantity // 2
        return (full_price_count * product.price) + (
                half_price_count * product.price * 0.5)


class ThirdOneFree(Promotion):
    """
    Class representing a buy two, get one free promotion.

    Attributes:
    name (str): The name of the promotion.
    """

    def __init__(self, name):
        """
        Initialize the buy two, get one free promotion.

        Parameters:
        name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Apply the buy two, get one free promotion to the product.

        Parameters:
        product (Product): The product to apply the promotion to.
        quantity (int): The quantity of the product being purchased.

        Returns:
        float: The total price after applying the promotion.
        """
        free_count = quantity // 3
        payable_count = quantity - free_count
        return payable_count * product.price
