from typing import List, Tuple
from products import Product


class Store:
    """
    Represents a store that holds and manages products.
    """

    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Adds a product to the store.

        Args:
            product (Product): The product to be added.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store.

        Args:
            product (Product): The product to be removed.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculates the total quantity of all products in the store.

        Returns:
            int: Total quantity of all active products.
        """
        return sum(product.quantity for product in self.products if product.is_active)

    def get_all_products(self) -> List[Product]:
        """
        Retrieves all active products in the store.

        Returns:
            List[Product]: List of all active products.
        """
        return [product for product in self.products if product.is_active]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order for a list of products and quantities.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of tuples where each tuple contains a product and a quantity.

        Returns:
            float: Total price of the order.

        Raises:
            Exception: If a product in the shopping list is not available or cannot fulfill the requested quantity.
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception(f"Product '{product.name}' is not available in the store.")
            if not product.is_active:
                raise Exception(f"Product '{product.name}' is not active.")

            # Attempt to buy the product and accumulate the total price
            total_price += product.buy(quantity)

        return total_price

    def __contains__(self, product: Product) -> bool:
        """
        Checks if a product exists in the store using the `in` operator.

        Args:
            product (Product): The product to check.

        Returns:
            bool: True if the product exists in the store, False otherwise.
        """
        return product in self.products

    def __add__(self, other: 'Store') -> 'Store':
        """
        Combines two stores into a new store.

        Args:
            other (Store): Another store to combine with.

        Returns:
            Store: A new store containing products from both stores.
        """
        combined_store = Store()
        combined_store.products = self.products + other.products
        return combined_store
