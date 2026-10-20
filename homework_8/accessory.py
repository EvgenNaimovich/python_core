class Accessory:
    def __init__(self, name: str, price: float | int):
        self.name = name
        self._price = price

    @property
    def get_price_accessory(self):
        return self._price


class Ribbon(Accessory):
    def __init__(self, colour, price=2):
        super().__init__("Ленточка", price)
        self.colour = colour


class PackingPaper(Accessory):
    def __init__(self, colour, price=3.6):
        super().__init__("Упаковочная бумага", price)
        self.colour = colour


class Eucalyptus(Accessory):
    def __init__(self, price=1.4):
        super().__init__("Листья эвкалипта", price)


class Pistachio(Accessory):
    def __init__(self, price=3.6):
        super().__init__("Листья фисташки", price)


class Toppers(Accessory):
    def __init__(self, colour, price=1.0):
        super().__init__("Топпер", price)
        self.colour = colour
