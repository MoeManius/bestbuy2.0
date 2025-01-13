import products  # Make sure the products module is imported

class Store:
    def __init__(self, product_list=None):
        self.products = product_list if product_list else []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products:
            if isinstance(product, products.NonStockedProduct):
                continue  # Skip non-stocked products
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
