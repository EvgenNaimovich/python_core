"""
Декоратор повторного запуска. Напишите декоратор с параметром retry(count),
который повторно запускает декорируемую функцию указанное количество раз,
пока функция не вернет True. Перед каждой попыткой необходимо выводить её номер.
Если функция вернула True, дальнейшие попытки выполнять не нужно.
Декоратор должен поддерживать передачу позиционных и
именованных аргументов через *args и **kwargs.
"""
import functools


def retry(count):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"вызвана функция {func.__name__}")
            for i in range(count):
                print(f"Попытка {i + 1} из {count}")
                result = func(*args, **kwargs)
                if result:
                    print(f"функция {func.__name__} закончила свою работу досрочно")
                    break
            return None

        return wrapper

    return decorator


@retry(count=3)
def comparison(a, b):
    return a > b


if __name__ == '__main__':
    comparison(2, 5)
    comparison(3, 4)
    comparison(7, 4)
