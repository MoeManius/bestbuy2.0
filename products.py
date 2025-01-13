class Product:
    def __init__(self, name: str, price: float, quantity: int):
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

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return (f"Product: {self.name}, Price: ${self.price:.2f}, "
                f"Quantity: {self.quantity}, Active: {self.active}")

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if not self.active:
            raise Exception("Product is not active.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)
        self.active = True

    def set_quantity(self, quantity: int):
        raise Exception("Cannot set quantity for non-stocked products.")

    def show(self) -> str:
        return (f"Non-Stocked Product: {self.name}, Price: ${self.price:.2f}, "
                f"Active: {self.active}")

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if not self.active:
            raise Exception("Product is not active.")

        return self.price * quantity


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, max_per_order: int):
        super().__init__(name, price, quantity)
        self.max_per_order = max_per_order

    def buy(self, quantity: int) -> float:
        if quantity > self.max_per_order:
            raise Exception(f"Cannot buy more than {self.max_per_order} of {self.name} in one order.")
        return super().buy(quantity)

    def show(self) -> str:
        return (f"Limited Product: {self.name}, Price: ${self.price:.2f}, "
                f"Quantity: {self.quantity}, Max per Order: {self.max_per_order}, Active: {self.active}")
