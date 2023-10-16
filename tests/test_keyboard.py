from src.keyboard import Keyboard


def test_keyboard():
    """
    Тест инициализации класса Keyboard через множественное наследие.
    Тест миксина
    """
    keyboard = Keyboard('Papa Jon 1232', 9600, 5)
    assert str(keyboard) == 'Papa Jon 1232'
    assert str(keyboard.language) == "EN"
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"
    keyboard.change_lang()
    assert str(keyboard.language) == "EN"
