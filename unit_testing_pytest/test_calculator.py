import pytest
from source.calculator import Calculator


# Fixture to create a Calculator instance before each test
@pytest.fixture
def calculator():
    print("Setting up Calculator")
    calc = Calculator()
    yield calc  # Provide the Calculator instance to the test
    print("Tearing down Calculator")


# Test case using the fixture
def test_add(calculator):
    calculator.add(2, 3)
    assert calculator.result == 5


def test_subtract(calculator):
    calculator.subtract(5, 3)
    assert calculator.result == 2


def test_multiply(calculator):
    calculator.multiply(2, 3)
    assert calculator.result == 6


def test_divide(calculator):
    calculator.divide(6, 3)
    assert calculator.result == 2


# Test case to demonstrate teardown logic
def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(6, 0)
