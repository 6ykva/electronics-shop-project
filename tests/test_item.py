"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item():
    """
    Проверяем инициализацию класса
    """
    item = Item('Television', 20000, 3)
    assert item.name == 'Television'
    assert item.price == 20000
    assert item.quantity == 3


def test_calculate_total_price():
    """
    Проверяем метод расчёта общей стоимости товара по конкретному товару
    """
    item = Item('Television', 20000, 3)
    assert item.calculate_total_price() == 60000


def test_apply_discount():
    """
    Проверяем метод применения скидки на конкретный товар
    """
    item = Item('Television', 20000, 3)
    Item.pay_rate = 1.5
    item.apply_discount()
    assert item.price == 30000


def test_name():
    item = Item('Television', 20000, 3)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'


def test_string_to_number():
    assert Item.string_to_number('1') == 1
    assert Item.string_to_number('5.0') == 5


def test_repr():
    item1 = Item("Магнитофон", 10500, 10)
    assert repr(item1) == "Item('Магнитофон', 10500, 10)"


def test_str():
    item1 = Item('Магнитофон', 10500, 10)
    assert str(item1) == 'Магнитофон'
