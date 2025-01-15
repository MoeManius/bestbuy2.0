import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentageDiscount, SecondItemHalfPrice, BuyTwoGetOneFree
from store import Store


@pytest.fixture
def setup_products():
    """Fixture to set up a variety of products."""
    macbook = Product("MacBook Air M2", price=1450, quantity=100)
    bose_earbuds = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel_phone = Product("Google Pixel 7", price=500, quantity=250)
    windows_license = NonStockedProduct("Windows License", price=125)
    shipping = LimitedProduct("Shipping", price=10, quantity=250, max_per_order=1)
    return [macbook, bose_earbuds, pixel_phone, windows_license, shipping]


@pytest.fixture
def setup_promotions():
    """Fixture to set up promotions."""
    percent_discount = PercentageDiscount("30% off!", percentage=30)
    second_half_price = SecondItemHalfPrice("Second Half Price!")
    third_one_free = BuyTwoGetOneFree("Buy 2 Get 1 Free!")
    return percent_discount, second_half_price, third_one_free


@pytest.fixture
def setup_store(setup_products, setup_promotions):
    """Fixture to set up a store with products and promotions."""
    store = Store()
    for product in setup_products:
        store.add_product(product)

    percent_discount, second_half_price, third_one_free = setup_promotions
    setup_products[0].promotion = second_half_price  # MacBook Air M2
    setup_products[1].promotion = third_one_free     # Bose QuietComfort Earbuds
    setup_products[3].promotion = percent_discount   # Windows License

    return store


def test_product_creation():
    product = Product("Test Product", price=100, quantity=10)
    assert product.name == "Test Product"
    assert product.price == 100
    assert product.quantity == 10
    assert product.is_active is True


def test_non_stocked_product():
    product = NonStockedProduct("Non-Stocked Item", price=50)
    assert product.quantity == 0
    assert product.buy(10) == 500


def test_limited_product():
    product = LimitedProduct("Limited Item", price=30, quantity=100, max_per_order=5)
    with pytest.raises(Exception):
        product.buy(10)
    assert product.buy(5) == 150


def test_promotion_application():
    product = Product("Promo Product", price=200, quantity=10)
    product.promotion = PercentageDiscount("20% Off", percentage=20)
    assert product.buy(2) == 320  # (200 - 40) * 2


def test_store_total_quantity(setup_store):
    store = setup_store
    assert store.get_total_quantity() == 1100


def test_store_active_products(setup_store):
    store = setup_store
    active_products = store.get_all_products()
    assert len(active_products) == 5
    assert all(product.is_active for product in active_products)


def test_store_order_success(setup_store):
    store = setup_store
    macbook = store.products[0]
    total_price = store.order([(macbook, 2)])
    assert total_price == 2175  # 1450 + (1450 * 0.5)
    assert macbook.quantity == 98


def test_store_order_failure(setup_store):
    store = setup_store
    macbook = store.products[0]
    with pytest.raises(Exception):
        store.order([(macbook, 200)])


def test_promotion_on_non_stocked_product(setup_store):
    store = setup_store
    windows_license = store.products[3]
    total_price = windows_license.buy(2)
    assert total_price == (125 * 0.7) * 2  # 30% off promotion


def test_store_combination(setup_store):
    store1 = setup_store
    store2 = Store()
    product = Product("Extra Product", price=300, quantity=50)
    store2.add_product(product)

    combined_store = store1 + store2
    assert len(combined_store.products) == len(store1.products) + 1
    assert product in combined_store.products


def test_product_comparison():
    product1 = Product("Product A", price=100, quantity=10)
    product2 = Product("Product B", price=200, quantity=5)
    assert product1 < product2
    assert product2 > product1


def test_product_in_store(setup_store):
    store = setup_store
    macbook = store.products[0]
    assert macbook in store
    product = Product("Non-existent", price=100, quantity=5)
    assert product not in store
