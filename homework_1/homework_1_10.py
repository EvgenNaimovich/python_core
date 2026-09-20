"""
Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного:
[1, 5, 2, 9, 2, 9, 1] => 5
Напишите программу, которая будет выводить уникальное число
"""


def unique_number_in_dict(digits_list):
    for digit in digits_list:
        if digits_list.count(digit) == 1:
            return digit
    return "Уникальное число не найдено. проверь список"


if __name__ == '__main__':
    list_digits = [1, 5, 2, 9, 2, 9, 1]
    print(unique_number_in_dict(list_digits))
