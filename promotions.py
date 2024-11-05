from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract class representing general promotion."""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Abstract method to apply promotion."""
        pass


class PercentDiscount(Promotion):
    """Class representing percentage discount promotion."""
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = (self.percent / 100) * product.price
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    """Class representing second item half price promotion."""
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_count = quantity // 2 + quantity % 2
        half_price_count = quantity // 2
        return (full_price_count * product.price) + (
            half_price_count * product.price * 0.5)


class ThirdOneFree(Promotion):
    """Class representing buy two, get one free promotion."""
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        free_count = quantity // 3
        payable_count = quantity - free_count
        return payable_count * product.price
