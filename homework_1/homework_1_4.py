"""
В строке "Ivanou Ivan" поменяйте местами слова:
"Ivanou Ivan" => "Ivan Ivanou"
"""


def swap_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])


if __name__ == '__main__':
    print(swap_words("Ivanou Ivan"))
