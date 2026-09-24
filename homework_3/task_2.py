"""
test_cases = ["Login", "Registration", "Checkout", "Logout"] statuses = ["PASS", "FAIL", "PASS", "SKIP"]
Необходимо с помощью zip() объединить название каждого тест-кейса с его статусом.
Создайте функцию print_report(test_cases, statuses), которая принимает два списка и выводит отчёт
в формате Login — PASS.
После формирования отчета программа должна определить количество успешных и неуспешных тестов и сообщить,
можно ли считать тестовый запуск успешным: если есть хотя бы один FAIL, запуск считается неуспешным.
"""

test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]

def print_report(test_cases_list: list, statuses_list: list):
    report_list = zip(test_cases_list, statuses_list)
    for test_case, status in report_list:
        print(f"{test_case} - {status}")
    passed_tests = statuses_list.count("PASS")
    failed_tests = statuses_list.count("FAIL")
    skipped_tests = statuses_list.count("SKIP")
    if "FAIL" in report_list:
        print(f"Запуск неуспешный"
              f"Количество успешных тестов: {passed_tests} \n"
              f"Количество неуспешных тестов: {failed_tests} \n")
    else:
        print(f"Запуск успешный")

    return  (f"Количество успешных тестов: {passed_tests} \n"
             f"Количество неуспешных тестов: {failed_tests} \n")


if __name__ == "__main__":
    print(print_report(test_cases, statuses))
