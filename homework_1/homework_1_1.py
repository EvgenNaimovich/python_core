"""
Привести к целому типу -1.6, 2.99
"""


def int_digits(nubbers):
    return int(nubbers)


if __name__ == '__main__':
    number_1 = -1.6
    number_2 = 2.99
    print(int_digits(number_1))
    print(int_digits(number_2))
