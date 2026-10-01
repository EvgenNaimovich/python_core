"""
Создайте JSON-файл с тестовыми пользователями для проверки авторизации.
Для каждого пользователя должны храниться логин, пароль и ожидаемый результат авторизации.
Напишите программу, которая открывает JSON-файл, загружает данные и выводит информацию
о каждом тестовом пользователе. Программа должна корректно обрабатывать ситуации,
когда файл не существует, содержимое файла невозможно прочитать как JSON или у
пользователя отсутствует обязательное поле. Для обработки ошибок используйте try/except,
соответствующие типы исключений и получение информации об ошибке через as e.
"""

import json

filename = "test_users.json"

try:
    with open(filename, "r", encoding="utf-8") as f:
        users = json.load(f)

except FileNotFoundError as e:
    print(f"Файл не найден: {e}")

except json.JSONDecodeError as e:
    print(f"невозможно прочитать как JSON: {e}")

except OSError as e:
    print(f"Ошибка при чтении файла: {e}")

else:
    for index, user in enumerate(users, start=1):
            try:
                login = user["login"]
                password = user["password"]
                expected_result = user["expected_result"]
            except KeyError as e:
                print(f"У пользака №{index}: отсутствует обязательное поле {e}.")
                continue
            print(
                f"Пользователь: {login}, "
                f"пароль: {password}, "
                f"ожидаемый результат авторизации: {expected_result}"
            )