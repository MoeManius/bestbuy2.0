from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for product promotions.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: "Product", quantity: int) -> float:
        """
        Abstract method to apply a promotion to a product.
        """
        pass


class PercentageDiscount(Promotion):
    """
    Applies a percentage discount to the product price.
    """

    def __init__(self, name: str, discount_percentage: float):
        super().__init__(name)
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.discount_percentage = discount_percentage

    def apply_promotion(self, product: "Product", quantity: int) -> float:
        return product.price * quantity * (1 - self.discount_percentage / 100)


class SecondItemHalfPrice(Promotion):
    """
    Applies a promotion where the second item is half price.
    """

    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: "Product", quantity: int) -> float:
        pairs = quantity // 2
        remainder = quantity % 2
        return (pairs * 1.5 + remainder) * product.price


class BuyTwoGetOneFree(Promotion):
    """
    Applies a promotion where buying two items gives the third one free.
    """

    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: "Product", quantity: int) -> float:
        groups_of_three = quantity // 3
        remainder = quantity % 3
        return (groups_of_three * 2 + remainder) * product.price
