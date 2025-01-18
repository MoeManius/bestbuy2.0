from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for promotions.
    """

    def __init__(self, name: str):
        """
        Initialize the promotion.

        Args:
            name (str): The name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """
        Apply the promotion and return the total discounted price.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product being bought.

        Returns:
            float: The total price after applying the promotion.
        """
        pass


class PercentageDiscount(Promotion):
    """
    Represents a percentage-based discount promotion.
    """

    def __init__(self, name: str, percentage: float):
        """
        Initialize the percentage discount promotion.

        Args:
            name (str): The name of the promotion.
            percentage (float): The discount percentage.
        """
        super().__init__(name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Apply percentage discount.

        Args:
            product (Product): The product to apply the discount to.
            quantity (int): The quantity of the product being bought.

        Returns:
            float: The total price after applying the discount.
        """
        discount = product.price * (self.percentage / 100)
        discounted_price = product.price - discount
        return discounted_price * quantity


class SecondItemHalfPrice(Promotion):
    """
    Represents the second item at half price promotion.
    """

    def __init__(self, name: str):
        """
        Initialize the second item half price promotion.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Apply second item at half price.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product being bought.

        Returns:
            float: The total price after applying the promotion.
        """
        pairs = quantity // 2
        remainder = quantity % 2
        return (pairs * 1.5 * product.price) + (remainder * product.price)


class BuyTwoGetOneFree(Promotion):
    """
    Represents the 'Buy 2, Get 1 Free' promotion.
    """

    def __init__(self, name: str):
        """
        Initialize the 'Buy 2, Get 1 Free' promotion.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Apply the 'Buy 2, Get 1 Free' promotion.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product being bought.

        Returns:
            float: The total price after applying the promotion.
        """
        groups_of_three = quantity // 3
        remainder = quantity % 3
        return (groups_of_three * 2 * product.price) + (remainder * product.price)
