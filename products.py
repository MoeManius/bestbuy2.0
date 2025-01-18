from promotions import Promotion


class Product:
    """
    Represents a product in the store.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize the product.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.
        """
        if not name or price <= 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self._name = name
        self._price = price
        self._quantity = quantity
        self._promotion = None

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    @property
    def promotion(self):
        return self._promotion

    @promotion.setter
    def promotion(self, promo: Promotion):
        self._promotion = promo

    @property
    def is_active(self):
        return self._quantity > 0

    def buy(self, quantity: int) -> float:
        """
        Buy a certain quantity of the product.

        Args:
            quantity (int): The quantity of the product to buy.

        Returns:
            float: The total price after applying any promotions.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if quantity > self._quantity:
            raise Exception("Not enough quantity in stock")

        self._quantity -= quantity
        if self._promotion:
            return self._promotion.apply_promotion(self, quantity)
        return self._price * quantity

    def __str__(self):
        promo_info = f" (Promotion: {self._promotion.name})" if self._promotion else ""
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}{promo_info}"

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self._price < other.price

    def __gt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self._price > other.price


class NonStockedProduct(Product):
    """
    Represents a non-stocked product.
    """

    def __init__(self, name: str, price: float):
        """
        Initialize a non-stocked product.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
        """
        super().__init__(name, price, quantity=0)

    @property
    def quantity(self):
        return 0  # Always zero for non-stocked products

    def buy(self, quantity: int) -> float:
        """
        Buy a certain quantity of the product.

        Args:
            quantity (int): The quantity of the product to buy.

        Returns:
            float: The total price after applying any promotions.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if self._promotion:
            return self._promotion.apply_promotion(self, quantity)
        return self._price * quantity

    def __str__(self):
        promo_info = f" (Promotion: {self._promotion.name})" if self._promotion else ""
        return f"{self._name} (Non-Stocked), Price: {self._price}{promo_info}"


class LimitedProduct(Product):
    """
    Represents a limited-quantity product.
    """

    def __init__(self, name: str, price: float, quantity: int, max_per_order: int):
        """
        Initialize a limited-quantity product.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.
            max_per_order (int): The maximum quantity that can be bought per order.
        """
        super().__init__(name, price, quantity)
        self._max_per_order = max_per_order

    @property
    def max_per_order(self):
        return self._max_per_order

    def buy(self, quantity: int) -> float:
        """
        Buy a certain quantity of the product.

        Args:
            quantity (int): The quantity of the product to buy.

        Returns:
            float: The total price after applying any promotions.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if quantity > self._max_per_order:
            raise Exception(f"Cannot buy more than {self._max_per_order} per order")
        if quantity > self._quantity:
            raise Exception("Not enough quantity in stock")
        self._quantity -= quantity
        if self._promotion:
            return self._promotion.apply_promotion(self, quantity)
        return self._price * quantity

    def __str__(self):
        promo_info = f" (Promotion: {self._promotion.name})" if self._promotion else ""
        return f"{self._name} (Limited to {self._max_per_order} per order), Price: {self._price}, Quantity: {self._quantity}{promo_info}"
