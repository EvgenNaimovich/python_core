from abc import ABC


class Flower(ABC):
    def __init__(self, name: str, price: float | int, lifetime: int):
        self._name = name
        self._price = price
        self._lifetime = lifetime

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def lifetime(self):
        return self._lifetime


class Orchid(Flower):
    def __init__(self, price=30, lifetime=10):
        super().__init__("Орхидея", price, lifetime)


class Rose(Flower):
    def __init__(self, price=10, lifetime=7):
        super().__init__("Роза", price, lifetime)


class Alstroemeria(Flower):
    def __init__(self, price=12.50, lifetime=15):
        super().__init__("Альстромерия", price, lifetime)


class Hydrangea(Flower):
    def __init__(self, price=10, lifetime=15):
        super().__init__("Гортензия", price, lifetime)


class Gypsophila(Flower):
    def __init__(self, price=7, lifetime=12):
        super().__init__("Гипсофила", price, lifetime)


class Lisianthus(Flower):
    def __init__(self, price=22, lifetime=9):
        super().__init__("Лизиантус", price, lifetime)


class Eustoma(Flower):
    def __init__(self, price=23.7, lifetime=22):
        super().__init__("Эустома", price, lifetime)