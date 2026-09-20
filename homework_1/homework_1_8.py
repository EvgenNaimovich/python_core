"""
Вывести, входит ли строка1 в строку2
Пример: employ и employment
"""


def included_word_in_row(word, row):
    if word in row:
        return "входит"
    return "не входит"


if __name__ == '__main__':
    word = "employ"
    row = "employment"
    print(f"Слово {word} {included_word_in_row(word, row)} в {row}")
