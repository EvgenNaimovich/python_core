import random
from time import sleep

"""
Дан список тестов: tests = [ "test_login", "test_logout", "test_registration", "test_profi le", "test_payment", "test_search" ]
Пользователь вводит количество тестов, которые необходимо запустить.
Программа должна случайным образом выбрать указанное количество уникальных тестов из списка
и каждому выбранному тесту случайно назначить статус PASS, FAIL или SKIP.
Результаты необходимо объединить и вывести в виде отчёта.
Если пользователь запросил больше тестов, чем существует в списке, программа должна вывести сообщение об ошибке.
"""


def print_report(tests_list: list, statuses_list: list):
    numbers_start_tests = int(input("Введите кол-во тестов, которые необходимо запустить: "))
    if numbers_start_tests > len(tests_list):  # обработка на другие условия по задаче не требуются)
        print(f"Запрошено {numbers_start_tests} тестов, но в списке тестов = {len(tests_list)}")
        print_report(tests, statuses)
    selected_tests = random.sample(tests_list, k=numbers_start_tests)
    new_statuses_list = random.choices(statuses_list, k=numbers_start_tests)
    perort = zip(selected_tests, new_statuses_list)
    print("----Отчет о запуске тестов----")
    for test, status in perort:
        print(f"{test}: {status}")
        sleep(0.3)
    return None


if __name__ == "__main__":
    tests = ["test_login", "test_logout", "test_registration", "test_profi le", "test_payment", "test_search"]
    statuses = ["PASS", "FAIL", "SKIP"]
    print_report(tests, statuses)