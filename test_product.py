import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentageDiscount, SecondItemHalfPrice, BuyTwoGetOneFree


@pytest.fixture
def product_setup():
    """
    Fixture to set up initial products and promotions for tests.
    """
    # Create products
    products = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, max_per_order=1),
    ]

    # Create promotions
    second_half_price = SecondItemHalfPrice("Second Half Price!")
    third_one_free = BuyTwoGetOneFree("Buy Two, Get One Free!")
    thirty_percent = PercentageDiscount("30% Off!", discount_percentage=30)

    # Add promotions to products
    products[0].set_promotion(second_half_price)  # MacBook Air
    products[1].set_promotion(third_one_free)     # Bose QuietComfort Earbuds
    products[3].set_promotion(thirty_percent)     # Windows License

    return products


def test_product_promotion_macbook(product_setup):
    macbook = product_setup[0]  # MacBook Air M2
    # Test promotion: Second item at half price
    assert macbook.buy(2) == 1450 + 725  # 1450 + 50% of 1450
    assert macbook.get_quantity() == 98  # Quantity reduced correctly


def test_product_promotion_bose_earbuds(product_setup):
    bose = product_setup[1]  # Bose QuietComfort Earbuds
    # Test promotion: Buy two, get one free
    assert bose.buy(3) == 250 * 2  # Third one is free
    assert bose.get_quantity() == 497  # Quantity reduced correctly


def test_product_promotion_windows_license(product_setup):
    windows = product_setup[3]  # Windows License
    # Test promotion: 30% discount
    assert windows.buy(1) == 125 * 0.7  # 30% off
    assert windows.get_quantity() == 0  # Quantity remains 0 for NonStockedProduct


def test_limited_product_promotion_shipping(product_setup):
    shipping = product_setup[4]  # Shipping
    # Test limited purchase restriction
    with pytest.raises(Exception):
        shipping.buy(2)  # Max per order is 1

    # Valid purchase
    assert shipping.buy(1) == 10
    assert shipping.get_quantity() == 249  # Quantity reduced correctly


def test_product_without_promotion(product_setup):
    pixel = product_setup[2]  # Google Pixel 7
    # Test regular product without promotion
    assert pixel.buy(1) == 500  # No discount
    assert pixel.get_quantity() == 249  # Quantity reduced correctly
