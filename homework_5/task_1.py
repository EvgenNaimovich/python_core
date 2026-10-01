"""
Дан список результатов автотестов. Для каждого теста известны его название,
статус выполнения (PASS, FAIL или SKIP) и время выполнения.
Напишите программу, которая с помощью filter() получает все упавшие тесты,
с помощью map() формирует список их названий, а с помощью reduce()
рассчитывает общее время выполнения всех тестов.
Дополнительно с помощью генератор списка сформируйте
список названий успешно пройденных тестов.
В результате программа должна вывести количество тестов каждого статуса,
список названий упавших тестов, список успешно пройденных тестов и общее время
выполнения всех тестов.
"""
from functools import reduce

tests = [
    {"name": "login", "status": "PASS", "time": 1.2},
    {"name": "kredit", "status": "FAIL", "time": 3.5},
    {"name": "kredit_2", "status": "FAIL", "time": 3.5},
    {"name": "logout", "status": "PASS", "time": 1.2}

]

def filter_test(test_list):
    failed_tests = list(filter(lambda test: test["status"] == "FAIL", test_list))
    print(f"Список упавших тестов: {failed_tests}")
    name_failed_tests = list(map(lambda test: test["name"], failed_tests))
    print(f"Названия упавших тестов: {name_failed_tests}")
    total_time_all_testes = reduce(lambda x, y: x + y, map(lambda x: x["time"], test_list))
    print(f"Общее время выоплнения всех тестов: {total_time_all_testes:.2f} секунды")
    name_passed_tests = [test["name"] for test in test_list if test["status"] == "PASS"]
    print(f"Список удачных тестов: {name_passed_tests}")
    return None

if __name__ == "__main__":
    print(f"Список для работы: {tests}", sep="\n")
    filter_test(tests)