from store import Store
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentageDiscount, SecondItemHalfPrice, BuyTwoGetOneFree


def setup_store() -> Store:
    """
    Setup the initial store inventory and assign promotions to products.
    Returns:
        Store: The initialized store instance.
    """
    # Initialize products
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping Fee", price=10, quantity=250, max_per_order=1),
    ]

    # Create promotions
    second_item_half_price = SecondItemHalfPrice("Second Item Half Price")
    buy_two_get_one_free = BuyTwoGetOneFree("Buy 2, Get 1 Free")
    thirty_percent_off = PercentageDiscount("30% Off", percentage=30)

    # Assign promotions to products
    product_list[0].promotion = second_item_half_price  # MacBook Air M2
    product_list[1].promotion = buy_two_get_one_free    # Bose QuietComfort Earbuds
    product_list[3].promotion = thirty_percent_off      # Windows License

    # Initialize and populate store
    store = Store()
    for product in product_list:
        store.add_product(product)

    return store


def main():
    """
    Entry point for the program. Displays the menu and handles user input.
    """
    store = setup_store()

    while True:
        print("\nWelcome to the Best Buy Store!")
        print("1. List all products in store")
        print("2. Show total quantity in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAvailable products:")
            for product in store.get_all_products():
                print(product)  # Uses the __str__ method
        elif choice == '2':
            print(f"\nTotal quantity in store: {store.get_total_quantity()}")
        elif choice == '3':
            shopping_list = []
            while True:
                product_name = input("Enter the product name (or 'done' to finish): ")
                if product_name.lower() == 'done':
                    break

                quantity = int(input(f"Enter the quantity for {product_name}: "))
                product = next((p for p in store.products if p.name == product_name), None)

                if product:
                    shopping_list.append((product, quantity))
                else:
                    print(f"Product '{product_name}' not found in the store.")

            try:
                total_price = store.order(shopping_list)
                print(f"Order processed successfully! Total price: ${total_price:.2f}")
            except Exception as e:
                print(f"An error occurred while processing the order: {e}")
        elif choice == '4':
            print("Thank you for visiting the Best Buy Store!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
