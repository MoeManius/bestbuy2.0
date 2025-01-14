from products import Product, NonStockedProduct, LimitedProduct
from store import Store


def setup_store() -> Store:
    """Setup the initial stock of inventory with different product types."""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=150),
        LimitedProduct("Shipping Fee", price=10, quantity=100, max_per_order=1),
    ]

    store = Store()
    for product in product_list:
        store.add_product(product)
    return store


def handle_list_products(store: Store):
    """Display all active products in the store."""
    print("\nAll active products in the store:")
    for product in store.get_all_products():
        print(product.show())


def handle_total_quantity(store: Store):
    """Display the total quantity of items in the store."""
    print("\nTotal quantity of items in the store:", store.get_total_quantity())


def handle_make_order(store: Store):
    """Handle the process of making an order."""
    shopping_list = []
    while True:
        product_name = input("Enter the product name (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        try:
            quantity = int(input(f"Enter the quantity for {product_name}: "))
            product = next((p for p in store.products if p.name == product_name), None)
            if product:
                shopping_list.append((product, quantity))
            else:
                print(f"Product {product_name} not found in the store.")
        except ValueError:
            print("Invalid input. Quantity must be a number.")

    try:
        total_price = store.order(shopping_list)
        print("Total price for the order:", total_price)
    except Exception as e:
        print("An error occurred while processing the order:", e)


def start(store: Store):
    """Main menu loop for the store."""
    while True:
        print("\nWelcome to the Store!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            handle_list_products(store)
        elif choice == '2':
            handle_total_quantity(store)
        elif choice == '3':
            handle_make_order(store)
        elif choice == '4':
            print("Thank you for visiting the store!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Initialize the store with products
    best_buy = setup_store()
    start(best_buy)
