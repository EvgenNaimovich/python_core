"""
Создайте класс CreditCard, описывающий кредитную карту. При
создании объекта необходимо передавать номер счёта и начальный
баланс карты. Реализуйте метод deposit(amount), который пополняет
баланс на указанную сумму, метод withdraw(amount), который снимает
указанную сумму, и метод show_info(), который выводит номер счёта и
текущий баланс.
Создайте три объекта класса CreditCard с разными номерами счетов и
начальными балансами. Пополните баланс первой и второй карты, а с
третьей карты снимите некоторую сумму. После выполнения операций
выведите информацию о состоянии всех трёх карт.
"""


class CreditCard:
    def __init__(self, number, amount):
        self.number = number
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount
        print(f"Вы пополнили свой баланс на {amount}. Ваш баланс {self.amount}")

    def withdraw(self, amount):
        if amount > self.amount:
            print(f"Не достаточно средств. Ваш баланс {self.amount}, Пытаетесь снять {amount}")
            return None
        self.amount -= amount
        print(f"Вы сняли со своего баланса {amount} средств. Ваш баланс {self.amount}")
        return None

    def show_info(self):
        print(f"На счете {self.number} {self.amount} попугаев")


user_1 = CreditCard("3012ALFABY", 100)
user_1.deposit(123)
user_1.show_info()

user_2 = CreditCard("3012SBERBY", 1000)
user_2.deposit(456)
user_2.withdraw(456)
user_2.show_info()

user_3 = CreditCard("3012MTBBY", 695)
user_3.withdraw(700)
user_3.show_info()
