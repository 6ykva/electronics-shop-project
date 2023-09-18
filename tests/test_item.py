"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_Item():
    item = Item('Television', 20000, 3)
    assert item.name == 'Television'
    assert item.price == 20000
    assert item.quantity == 3


def test_calculate_total_price():
    item = Item('Television', 20000, 3)
    assert item.calculate_total_price() == 60000


def test_apply_discount():
    item = Item('Television', 20000, 3)
    Item.pay_rate = 1.5
    item.apply_discount()
    assert item.price == 30000
