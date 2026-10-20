from abc import ABC


class Flower(ABC):
    def __init__(self, name: str, price: float | int, lifetime: int):
        self._name = name
        self._price = price
        self._lifetime = lifetime

    @property
    def get_name(self):
        return self._name

    @property
    def get_price_flower(self):
        return self._price

    @property
    def get_lifetime(self):
        return self._lifetime


class Orchid(Flower):
    def __init__(self, name, price=30, lifetime=10):
        super().__init__(name, price, lifetime)


class Rose(Flower):
    def __init__(self, color: str, price=10, lifetime=7):
        super().__init__("Роза", price, lifetime)
        self.color = color


class Alstroemeria(Flower):
    def __init__(self, price=12.50, lifetime=15):
        super().__init__("Альстромерия", price, lifetime)


class Hydrangea(Flower):
    def __init__(self, color, price=10, lifetime=15):
        super().__init__("Гортензия", price, lifetime)
        self.color = color


class Gypsophila(Flower):
    def __init__(self, price=7, lifetime=12):
        super().__init__("Гипсофила", price, lifetime)