"""
3. Напишите программу, которая добавляет "ing" к слову "stroka"
"""


def add_ing(words: str):
    return words + "ing"


if __name__ == '__main__':
    word = "stroka"
    print(add_ing(word))
