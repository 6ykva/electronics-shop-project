import pytest

from src.item import Item
from src.phone import Phone


def test_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == "iPhone 14"
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Магнитофон", 10500, 10)
    assert item1 + phone1 == 15


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        Phone("iPhone 14", 120_000, 5, 0)