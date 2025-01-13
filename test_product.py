import pytest
from products import Product

def test_create_product_success():
    """Test that a product is created successfully with valid inputs."""
    product = Product("Test Product", price=100.0, quantity=10)
    assert product.name == "Test Product"
    assert product.price == 100.0
    assert product.quantity == 10
    assert product.is_active() is True

def test_create_product_invalid_details():
    """Test that creating a product with invalid details raises a ValueError."""
    with pytest.raises(ValueError, match="Name cannot be empty."):
        Product("", price=100.0, quantity=10)
    with pytest.raises(ValueError, match="Price cannot be negative."):
        Product("Test Product", price=-10.0, quantity=10)
    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        Product("Test Product", price=100.0, quantity=-5)

def test_product_becomes_inactive_when_quantity_zero():
    """Test that a product becomes inactive when its quantity reaches zero."""
    product = Product("Test Product", price=50.0, quantity=5)
    product.set_quantity(0)
    assert product.is_active() is False

def test_product_purchase_updates_quantity_and_returns_price():
    """Test that buying a product reduces its quantity and returns the correct total price."""
    product = Product("Test Product", price=20.0, quantity=10)
    total_price = product.buy(3)
    assert total_price == 60.0
    assert product.get_quantity() == 7

def test_buying_more_than_available_quantity_raises_exception():
    """Test that attempting to buy more than the available stock raises an exception."""
    product = Product("Test Product", price=30.0, quantity=5)
    with pytest.raises(Exception, match="Not enough quantity in stock."):
        product.buy(10)
