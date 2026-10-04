import random
from time import sleep


def generate_random_floats(filename: str, count: int = 15, start: float = -100.0, end: float = 100.0):
    with open(filename, 'w') as f:
        for _ in range(count):
            number = random.uniform(start, end)
            f.write(f"{number:.2f}\n")


def square_numbers(filename: str):
    with open(filename, 'r') as f_num:
        numbers_str_list = f_num.readlines()  # если файл большой, упадет с ошибкой по памяти
        sqr_list = list(map(lambda x: f"{float(x) ** 2:.2f}\n", numbers_str_list))
    with open(filename, 'w') as f_sqr:
        f_sqr.writelines(map(str, sqr_list))


if __name__ == '__main__':
    generate_random_floats("random_floats.txt")  # генерю файл с вещ.числами, чтобы самому не писать
    sleep(5)  # можно переключиться на random_floats.txt и глянуть рез-т
    square_numbers("random_floats.txt")
