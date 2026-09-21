"""
Напишите программу, которая удаляет пробел в начале и в конце строки
"""


def strip_space(text):
    return text.lstrip().rstrip()


if __name__ == '__main__':
    print(strip_space("   функция, которая удаляет пробел в начале и в конце строки   "))
