from src.item import Item


class MixinKeyboard:
    """
    Создаем миксин для проверки языка клавиатуры
    """
    Language = 'EN'

    def __init__(self):
        self.__language = self.Language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self.__language


class Keyboard(Item, MixinKeyboard):
    """
    Инициализируем класс Keyboard с помощью множественного наследия.
    """
    pass
