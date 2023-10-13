"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone


def test_item():
    """
    Проверяем инициализацию класса
    """
    item = Item('Television', 20000, 3)
    assert item.name == 'Television'
    assert item.price == 20000
    assert item.quantity == 3
    assert item + 5 == ValueError


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
    phone1 = Phone("iPhone 14", 120_000, 5, 0)
    assert ValueError
