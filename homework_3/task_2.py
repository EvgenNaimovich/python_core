"""
test_cases = ["Login", "Registration", "Checkout", "Logout"] statuses = ["PASS", "FAIL", "PASS", "SKIP"]
Необходимо с помощью zip() объединить название каждого тест-кейса с его статусом.
Создайте функцию print_report(test_cases, statuses), которая принимает два списка и выводит отчёт
в формате Login — PASS.
После формирования отчета программа должна определить количество успешных и неуспешных тестов и сообщить,
можно ли считать тестовый запуск успешным: если есть хотя бы один FAIL, запуск считается неуспешным.
"""


def print_report(test_cases_list: list, statuses_list: list):
    report_list = zip(test_cases_list, statuses_list)
    passed_tests = statuses_list.count("PASS")
    failed_tests = statuses_list.count("FAIL")
    status_all_tests = "успешный" if failed_tests <= 0 else "неуспешный"
    print(f"----Запуск {status_all_tests}----\n"
          f"Количество успешных тестов: {passed_tests} \n"
          f"Количество неуспешных тестов: {failed_tests}")
    for test_case, status in report_list:
        print(f"{test_case} - {status}")
    return None


if __name__ == "__main__":
    test_cases = ["Login", "Registration", "Checkout", "Logout"]
    statuses_not_ok = ["PASS", "SKIP", "PASS", "FAIL"]
    statuses_ok = ["PASS", "PASS", "PASS", "SKIP"]
    print_report(test_cases, statuses_not_ok)
    print_report(test_cases, statuses_ok)
