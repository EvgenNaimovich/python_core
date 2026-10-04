def status_tests(status_list: list):
    """
    Результаты автотестов. Пользователь вводит количество выполненных автотестов,
    а затем по очереди результат каждого теста: PASS, FAIL или SKIP.
    Программа должна подсчитать количество тестов с каждым статусом и вывести итоговую статистику.
    Если присутствует хотя бы один FAIL, необходимо сообщить о наличии упавших тестов;
    если FAIL отсутствуют - сообщить об успешном прохождении выполненных тестов.
    Любой неизвестный статус необходимо пропустить и не учитывать в статистике.
    """

    if "FAIL" in status_list:
        print(f"Есть упавшие тесты. Их кол-во = {status_list.count('FAIL')}\n"
              f"Кол-во тестов со статусом PASS = {status_list.count('PASS')}\n"
              f"Кол-во тестов со статусом SKIP = {status_list.count('SKIP')}")
    else:
        print("все тесты выполнены успешно\n"
              f"Кол-во тестов со статусом PASS = {status_list.count('PASS')}\n"
              f"Кол-во тестов со статусом SKIP = {status_list.count('SKIP')}")
    return status_list


if __name__ == '__main__':
    count_tests = int(input("Введите кол-во тестов: "))
    results_tests = []
    for test in range(1, count_tests + 1):
        status_test = input(f"Введите результат теста №{test}: PASS, FAIL или SKIP-> ").upper()
        results_tests.append(status_test)
    print(status_tests(results_tests))
