from typing import Optional
from promotions import Promotion


class Product:
    """
    Represents a generic product with basic properties such as name, price, quantity, and active status.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """Initialize a product with name, price, and quantity."""
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion: Optional[Promotion] = None  # Promotion instance variable

    def set_promotion(self, promotion: "Promotion"):
        """Set a promotion for the product."""
        self.promotion = promotion

    def get_promotion(self) -> Optional["Promotion"]:
        """Get the current promotion for the product."""
        return self.promotion

    def get_quantity(self) -> int:
        """Return the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Set the quantity of the product and deactivate if it reaches zero."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Check if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self) -> str:
        """Return a string representation of the product."""
        promotion_desc = f", Promotion: {self.promotion}" if self.promotion else ""
        return f"Product: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Active: {self.active}{promotion_desc}"

    def buy(self, quantity: int) -> float:
        """
        Process a purchase for a given quantity of the product.
        :param quantity: The quantity to purchase.
        :return: The total price for the quantity purchased.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if not self.active:
            raise Exception("Product is not active.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        # Apply promotion if available
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        # Deduct quantity and return price
        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    """Represents a product that is not physically stocked."""

    def __init__(self, name: str, price: float):
        """Initialize a non-stocked product with zero quantity."""
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        """Override to prevent setting a quantity for non-stocked products."""
        raise Exception("Cannot set quantity for non-stocked products.")

    def buy(self, quantity: int) -> float:
        """
        Process a purchase for a non-stocked product.
        :param quantity: The quantity to purchase.
        :return: The total price for the quantity purchased.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if not self.active:
            raise Exception("Product is not active.")
        # Use promotion or standard price
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def show(self) -> str:
        """Override to include special description for non-stocked products."""
        return f"Non-Stocked Product: {self.name}, Price: ${self.price:.2f}"


class LimitedProduct(Product):
    """Represents a product with a maximum quantity allowed per order."""

    def __init__(self, name: str, price: float, quantity: int, max_per_order: int):
        """Initialize a limited product with a maximum quantity per order."""
        super().__init__(name, price, quantity)
        if max_per_order <= 0:
            raise ValueError("Maximum per order must be greater than zero.")
        self.max_per_order = max_per_order

    def buy(self, quantity: int) -> float:
        """
        Process a purchase for a limited product.
        :param quantity: The quantity to purchase.
        :return: The total price for the quantity purchased.
        """
        if quantity > self.max_per_order:
            raise Exception(f"Cannot buy more than {self.max_per_order} of this product per order.")
        return super().buy(quantity)

    def show(self) -> str:
        """Override to include special description for limited products."""
        return f"Limited Product: {self.name}, Price: ${self.price:.2f}, Max per Order: {self.max_per_order}"
