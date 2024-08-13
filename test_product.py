import pytest
from products import Product


# Test that creating a normal product works.
def test_product_creation_works():
    product = Product("Test Product", price=100.0, quantity=10)
    assert product.name == "Test Product"
    assert product.price == 100.0
    assert product.quantity == 10
    assert product.is_active()


# Test that creating a product with invalid details (empty name,
# negative price) invokes an exception.
def test_product_creation_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=100.0, quantity=10)
    with pytest.raises(ValueError):
        Product("Test Product", price=-100.0, quantity=10)
    with pytest.raises(ValueError):
        Product("Test Product", price=100.0, quantity=-10)


# Test that when a product reaches 0 quantity, it becomes inactive.
def test_product_becomes_inactive():
    product = Product("Test Product", price=100.0, quantity=10)
    product.buy(10)
    assert product.quantity == 0
    assert not product.is_active()


# Test that product purchase modifies the quantity and returns the
# right output.
def test_modifies_quantity_after_purchase():
    product = Product("Test Product", price=100.0, quantity=10)
    assert product.buy(5) == 500.0
    assert product.quantity == 5


# Test that buying a larger quantity than exists invokes exception.
def test_purchase_too_large_exception():
    product = Product("Test Product", price=100.0, quantity=5)
    with pytest.raises(Exception):
        product.buy(10)


pytest.main()
