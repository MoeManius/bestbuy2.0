from products import Product
from store import Store

# setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = Store()
for product in product_list:
    best_buy.add_product(product)

def start(store: Store):
    while True:
        print("\nWelcome to the Store!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAll active products in the store:")
            for product in store.get_all_products():
                print(product.show())
        elif choice == '2':
            print("\nTotal quantity of items in the store:", store.get_total_quantity())
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
                    print(f"Product {product_name} not found in the store.")
            try:
                total_price = store.order(shopping_list)
                print("Total price for the order:", total_price)
            except Exception as e:
                print("An error occurred while processing the order:", e)
        elif choice == '4':
            print("Thank you for visiting the store!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    start(best_buy)
