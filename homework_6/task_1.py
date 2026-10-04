"""
Рекурсивный подсчет результатов тестов.
Дан список результатов автотестов со статусами PASS, FAIL и SKIP.
Напишите рекурсивную функцию, которая подсчитывает количество тестов со статусом PASS.
Функция должна обрабатывать список с помощью рекурсии.
Использовать циклы for и while нельзя.
"""


def count_pass(list_status):
    if not list_status:
        return 0
    else:
        if list_status[0] == "PASS":
            count = 1
        else:
            count = 0
    return count + count_pass(list_status[1:])


if __name__ == "__main__":
    status_list = ["PASS", "FAIL", "SKIP", "PASS", "FAIL", "SKIP", "PASS", "FAIL", "SKIP"]
    print(count_pass(status_list))
