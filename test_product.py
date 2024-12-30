import pytest
from products import Product


def test_create_normal_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active()


def test_create_product_invalid_details():
    with pytest.raises(ValueError, match="Name cannot be empty."):
        Product("", price=1450, quantity=100)
    with pytest.raises(ValueError, match="Price cannot be negative."):
        Product("MacBook Air M2", price=-10, quantity=100)
    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        Product("MacBook Air M2", price=1450, quantity=-5)


def test_product_reaches_zero_quantity():
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.set_quantity(0)
    assert product.get_quantity() == 0
    assert not product.is_active()


def test_product_purchase_modifies_quantity():
    product = Product("MacBook Air M2", price=1450, quantity=10)
    total_price = product.buy(2)
    assert product.get_quantity() == 8
    assert total_price == 2900  # 2 * 1450


def test_buying_larger_quantity_than_exists():
    product = Product("MacBook Air M2", price=1450, quantity=5)
    with pytest.raises(Exception, match="Not enough quantity in stock."):
        product.buy(10)
