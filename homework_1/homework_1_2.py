"""
Заменить символ "#" на символ "/" в строке:
www.my_site.com#about
"""


def replace_text(text_str: str):
    return text_str.replace("#", "/")


if __name__ == '__main__':
    text = "www.my_site.com#about"
    print(replace_text(text))
