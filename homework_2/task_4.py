def guess_number(hidden_number: int):
    """
    Секретное число. В программе хранится секретное число 37. Пользователь должен вводить числа до тех пор,
    пока не угадает его. После каждой неправильной попытки программа должна сообщать,
    больше или меньше введенное число относительно секретного.
    После правильного ответа необходимо вывести сообщение об успехе и количество совершенных попыток.
    """

    count = 0
    while True:
        desired_number = int(input("Введите число: "))
        count += 1
        if desired_number > hidden_number:
            print(f"Число {desired_number} больше секретного")
        elif desired_number < hidden_number:
            print(f"Число {desired_number} меньше секретного")
        else:
            return f"Число {desired_number} верное. У вас ушло {count} попыток."


if __name__ == "__main__":
    print("Загадал число. Угадай его!")
    print(guess_number(37))
