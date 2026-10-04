"""
Замыкание для проверки времени выполнения. Напишите функцию create_time_checker(max_time),
которая возвращает вложенную функцию для проверки времени выполнения теста.
Вложенная функция принимает фактическое время выполнения и сообщает,
превышен установленный лимит или нет. Создайте два независимых замыкания
с разными значениями max_time и продемонстрируйте их работу.
"""

import time


def create_time_checker(max_time):
    def time_checker(time_work_func):
        return time_work_func - max_time < 3

    return time_checker


if __name__ == '__main__':
    start_time = time.time()
    foo = create_time_checker(start_time)
    time.sleep(1)
    time_true = time.time()
    print(f"Время ответа операции не привышает SLA(3cек)" if foo(time_true)
          else "Время ответа операции привышает SLA(3cек)")
    time.sleep(2.1)
    time_false = time.time()
    print(f"Время ответа операции не привышает SLA(3cек)" if foo(time_false)
          else "Время ответа операции привышает SLA(3cек)")
