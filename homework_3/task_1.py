"""
Пользователь одной строкой вводит результаты запуска автотестов через пробел,
например: PASS FAIL PASS SKIP PASS FAIL. Программа должна преобразовать введенную строку в список,
подсчитать количество тестов каждого типа и вывести общую статистику.
Логику подсчета необходимо вынести в отдельную функцию get_test_statistics(results),
которая возвращает результат в виде словаря. Дополнительно программа должна вывести процент
успешно пройденных тестов относительно общего количества тестов. Пример вывода:
Всего тестов: 6 PASS: 3 FAIL: 2 SKIP: 1 Успешно: 50.0%
"""


def get_test_statistics(results_list: list) -> dict:
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
    return result_dict


if __name__ == '__main__':
    tests_list = input("Введите результаты запуска автотестов через пробел:").split()
    for key, value in get_test_statistics(tests_list).items():
        print(f"{key}: {value}")
