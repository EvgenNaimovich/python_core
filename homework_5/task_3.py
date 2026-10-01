"""
Напишите функцию, которая принимает количество повторных запусков теста и значение таймаута.
Количество повторных запусков должно находиться в диапазоне от 0 до 5,
а таймаут должен быть положительным числом. Если переданные значения не соответствуют этим требованиям,
самостоятельно создайте исключение ValueError с помощью raise и добавьте понятное описание причины ошибки.
Вызов функции необходимо поместить в try/except и корректно обработать созданные исключения.
Проверьте работу программы минимум на трёх наборах данных: корректные значения,
отрицательный таймаут и слишком большое количество повторных запусков
"""

def validate_count_tests(number_repeated_tests, timeout):
    if not isinstance(number_repeated_tests, int) or isinstance(number_repeated_tests, bool):
        raise ValueError("Количество повторных запусков должно быть целым числом")

    if not 0 <= number_repeated_tests <= 5:
        raise ValueError(
            "Количество повторных запусков должно находиться в диапазоне от 0 до 5"
        )

    if (
        not isinstance(timeout, (int, float))
        or isinstance(timeout, bool)
        or timeout <= 0
    ):
        raise ValueError("Таймаут должен быть положительным конечным числом.")
    return number_repeated_tests, timeout



if __name__ == "__main__":
    test_list = [(3, 1.78), (5, -2), (6, 1)]
    for count, timeout_value in test_list:
        try:
            validate_count_tests(count, timeout_value)
            print(f"все ок. кол-во вызывов теста {count} таймаут {timeout_value}")
        except ValueError as e:
            print(f"Ошибка в данных: ({count}, {timeout_value}) : {e}")

