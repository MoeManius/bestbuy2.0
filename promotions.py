from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """Apply the promotion and return the total discounted price."""
        pass


class PercentageDiscount(Promotion):
    def __init__(self, name: str, percentage: float):
        super().__init__(name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity: int) -> float:
        """Apply percentage discount."""
        discount = product.price * (self.percentage / 100)
        discounted_price = product.price - discount
        return discounted_price * quantity


class SecondItemHalfPrice(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        """Apply second item at half price."""
        pairs = quantity // 2
        remainder = quantity % 2
        return (pairs * 1.5 * product.price) + (remainder * product.price)


class BuyTwoGetOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        """Apply 'Buy 2, Get 1 Free' promotion."""
        groups_of_three = quantity // 3
        remainder = quantity % 3
        return (groups_of_three * 2 * product.price) + (remainder * product.price)
