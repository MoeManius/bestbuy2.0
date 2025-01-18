import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentageDiscount, SecondItemHalfPrice, BuyTwoGetOneFree
from store import Store


@pytest.fixture
def setup_products():
    """
    Fixture to set up products for testing.
    """
    return [
        Product("MacBook Pro", 1450, 5),
        Product("Gaming Monitor", 300, 10),
        Product("Keyboard", 100, 20),
        NonStockedProduct("Windows License", 150),
        LimitedProduct("Graphics Card", 700, 5, 2)
    ]


@pytest.fixture
def setup_promotions():
    """
    Fixture to set up promotions for testing.
    """
    return (
        PercentageDiscount("10% Off", 10),
        SecondItemHalfPrice("Second Item Half Price"),
        BuyTwoGetOneFree("Buy 2 Get 1 Free")
    )


@pytest.fixture
def setup_store(setup_products):
    """
    Fixture to set up a store for testing.
    """
    return Store(setup_products)


def test_product_creation(setup_products):
    """
    Test creating products.
    """
    assert len(setup_products) == 5


def test_promotion_catalog_and_application(setup_store):
    """
    Test adding promotions to products and catalog functionality.
    """
    store = setup_store

    # Create promotion catalog
    second_half_price = SecondItemHalfPrice("Second Half Price!")
    third_one_free = BuyTwoGetOneFree("Third One Free!")
    thirty_percent = PercentageDiscount("30% off!", percentage=30)

    # Add promotions to products
    store.products[0].set_promotion(second_half_price)
    store.products[1].set_promotion(third_one_free)
    store.products[3].set_promotion(thirty_percent)

    # Setup initial stock of inventory
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel = Product("Google Pixel 7", price=500, quantity=250, maximum=1)

    best_buy = Store([mac, bose])

    # Test invalid price (should raise error)
    with pytest.raises(ValueError):
        mac.price = -100  # Negative price should raise an error

    # Test string representation of a product
    assert str(mac) == "MacBook Air M2, Price: $1450 Quantity:100"

    # Test comparison of products based on price
    assert mac > bose  # MacBook Air is more expensive than Bose earbuds

    # Test product presence in the store inventory
    assert mac in best_buy  # MacBook Air should be in the store
    assert pixel not in best_buy  # Google Pixel should not be in the store
