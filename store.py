from typing import List, Tuple
from products import Product, NonStockedProduct, LimitedProduct

class Store:
    """
    Represents a store containing various products, handling inventory management and orders.
    """

    def __init__(self):
        """Initialize the store with an empty list of products."""
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Add a product to the store.
        :param product: The product to add.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Remove a product from the store.
        :param product: The product to remove.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculate the total quantity of all products in the store.
        :return: The total quantity of products in the store.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """
        Retrieve all active products in the store.
        :return: A list of active products.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Process an order for multiple products.
        :param shopping_list: A list of tuples, where each tuple contains a product and the desired quantity.
        :return: The total price for the order.
        :raises Exception: If a product is not in the store or the order cannot be fulfilled.
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception(f"Product {product.name} is not in the store.")
            # Let the product's own logic handle the purchase (polymorphism in action)
            total_price += product.buy(quantity)

        return total_price
