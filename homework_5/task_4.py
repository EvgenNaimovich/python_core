"""
Создайте собственное исключение InvalidTestStatusError, наследуемое от Exception.
Напишите функцию, которая принимает статус теста и проверяет его значение.
Допустимыми считаются только PASS, FAIL и SKIP. Если передан любой другой статус,
функция должна с помощью raise создать InvalidTestStatusError и передать в него сообщение с некорректным значением.
В основной программе обработайте это исключение через try/except и выведите понятное сообщение пользователю.
Проверьте программу как с корректными, так и с некорректными статусами.
"""


class InvalidTestStatusError(Exception):
    """Класс для собственного исключения"""
    pass


def validate_status(status_test):
    acceptable_statuses = ["PASS", "FAIL", "SKIP"]
    if status_test not in acceptable_statuses:
        raise InvalidTestStatusError(
            f"Некорректный статус теста: {status_test}"
        )
    return status_test


if __name__ == "__main__":
    for test_status in ("PASS", "FAIL", "SKIP", "asdf"):
        try:
            print(validate_status(test_status))
        except InvalidTestStatusError as error:
            print(f"Ошибка: {error}")
