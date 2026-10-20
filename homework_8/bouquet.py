from statistics import mean

from accessory import Toppers, PackingPaper, Eucalyptus, Accessory, Pistachio
from flowers import Orchid, Alstroemeria
from flowers import Rose
from flowers import Flower


class Bouquet:
    def __init__(self,
                 flowers_list: list[Flower],
                 accessories: list[Accessory]):
        self.__flowers: list[Flower] = flowers_list
        self.__accessories: list[Accessory] = accessories

    @property
    def get_flowers(self):
        return self.__flowers

    @property
    def get_accessories(self):
        return self.__accessories

    def add_flowers(self, flower_obj: Flower):
        if not isinstance(flower_obj, Flower):
            raise TypeError("В букет можно добавлять только цветы. Аксессуары добавляются отдельно")
        self.__flowers.append(flower_obj)

    def add_accessory(self, accessory_obj: Accessory):
        if not isinstance(accessory_obj, Accessory):
            raise TypeError("Для выбранного букета нужно добавить аксессуары, а не цветы")
        self.__accessories.append(accessory_obj)

    def get_bouquet_price(self):
        flowers_price = sum(map(lambda f: f.get_price_flower, self.__flowers))
        accessories_price = sum(map(lambda a: a.get_price_accessory, self.__accessories))
        return flowers_price + accessories_price

    def get_mean_bouquet_lifetime(self):
        return mean(map(lambda f: f.get_lifetime, self.__flowers))

    def sorted_flowers_price(self):
        return sorted(map(lambda f: f.get_price_flower, self.__flowers))

    def flower_is_bouquet(self, flower_obj: Flower):
        return flower_obj in self.__flowers


if __name__ == '__main__':
    orchid = Orchid("Азиан Коралл", 80, 54)
    alstroemeria = Alstroemeria()
    bouquet = Bouquet(
        [
            orchid,
            Orchid("Бронзовый Будда", 75, 180),
            # Orchid("Дикий Кот", price=44),
            Rose("yellow", 12)
        ],
        [
            PackingPaper("red"),
            Eucalyptus(),
            Eucalyptus()
        ],
    )
    bouquet.add_accessory(Toppers("зеленый"))
    bouquet.add_flowers(Rose("зеленый", 12))
    print(f"Стоимость букета составит {bouquet.get_bouquet_price()} BYN")
    print(f"Время увядания букета составит {bouquet.get_mean_bouquet_lifetime()} дня ")
    print(bouquet.sorted_flowers_price())
    print(bouquet.flower_is_bouquet(orchid))
    print(bouquet.flower_is_bouquet(alstroemeria))