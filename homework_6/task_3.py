"""
Декоратор для логирования автотестов. Напишите декоратор log_test,
который перед запуском тестовой функции выводит её имя,
после выполнения сообщает о завершении и выводит полученный результат.
Декоратор должен поддерживать функции с произвольным количеством позиционных и
именованных аргументов с помощью *args и **kwargs.
Используйте functools.wraps(), чтобы сохранить метаданные исходной функции.
"""
from functools import wraps


def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Стартанула функция {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} завершила свою работу")
        return result

    return wrapper


@log_test
def get_test_statistics(results_list: list) -> None:
    """
    Очень вожная дока. Не пропустить!!!
    Декоратор для логирования автотестов
    """
    all_tests = len(results_list)
    passed_tests = results_list.count("PASS")
    failed_tests = results_list.count("FAIL")
    skipped_tests = results_list.count("SKIP")
    procent = (passed_tests / all_tests * 100) if all_tests > 0 else 0.0
    result_dict = {
        "Всего тестов": all_tests,
        "PASS": passed_tests,
        "FAIL": failed_tests,
        "SKIP": skipped_tests,
        "Успешно": f"{procent:.2f}%"
    }
    for key, value in result_dict.items():
        print(f"{key}: {value}")
    return None


if __name__ == '__main__':
    tests_list = ["PASS", "FAIL", "SKIP", "PASS", "FAIL", "SKIP", "PASS", "FAIL", "SKIP"]
    print(get_test_statistics.__doc__)
    get_test_statistics(tests_list)
