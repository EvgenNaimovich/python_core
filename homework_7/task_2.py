"""
Создайте класс ATM, описывающий работу банкомата. Банкомат должен
хранить количество купюр номиналом 20, 50 и 100. Начальное количество
купюр каждого номинала передается при создании объекта через
__init__().
Реализуйте метод add_money(), позволяющий добавить в банкомат
купюры каждого номинала. Также реализуйте метод withdraw(amount)
для снятия указанной суммы. Метод должен определить, может ли
банкомат выдать запрошенную сумму имеющимися купюрами. Если
операция возможна, необходимо уменьшить количество купюр в
банкомате, вывести, сколько купюр каждого номинала было выдано, и
вернуть True. Если указанную сумму выдать невозможно — вернуть False
и оставить содержимое банкомата без изменений.
Создайте объект ATM, добавьте в него несколько купюр и выполните
несколько операций снятия денег.
"""


class ATM:
    def __init__(self, count_20, count_50, count_100):
        self.count_20 = count_20
        self.count_50 = count_50
        self.count_100 = count_100

    def add_money(self, amount):
        if amount == 20:
            self.count_20 += 1
        elif amount == 50:
            self.count_50 += 1
        elif amount == 100:
            self.count_100 += 1
        else:
            raise ValueError

    def withdraw(self, money):
        balance_atm = self.count_20 * 20 + self.count_50 * 50 + self.count_100 * 100
        if money <= balance_atm:
            if money >= 100:
                count_100 = money // 100
                self.count_100 -= count_100
                money -= count_100 * 100
                if money >= 50 or money >= 20:
                    count_50 = money // 50
                    self.count_50 -= count_50
                    money -= count_50 * 50
                    if money >= 20 and money % 20 == 0:
                        count_20 = money // 20
                        self.count_20 -= count_20
                        money -= count_20 * 20
                        print(f"выдало 20 - {count_20}, 50 - {count_50}, 100 - {count_100}")
                        return True
        else:
            print(f"Сумму {money:.2f} не может выдать. Нет столько денег в АТМ")
            return False
        return ("В Банкомате нет таких купюр, чтобы выдать требуемую сумму\n"
                "Есть купюры номиналом 20, 50 и 100 попугаев")


atm_1 = ATM(2, 5, 10)
atm_1.add_money(20)
print(atm_1.withdraw(570))
print(atm_1.withdraw(220))
print(atm_1.withdraw(5900))
print(atm_1.withdraw(56))
