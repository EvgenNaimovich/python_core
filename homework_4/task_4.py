import json
import os.path
import random
import string
from time import sleep


def generate_file_txt(count_lines: int = 10):
    filename = "random_file.txt"
    with open(filename, 'w') as f_txt:
        for _ in range(count_lines):
            line = "".join(random.sample(string.ascii_letters + string.digits, k=random.randint(10, 40))) + "\n"
            f_txt.write(line)
    print(f"{filename} has been created")
    sleep(2)
    return filename


def generate_file_json():
    filename = "random_file.json"
    with open(filename, 'w') as f_json:
        data_about_me = {
            "name": "Evgen",
            "age": 36,
            "city": "Minsk",
            "skills": ["python", "java", "performance testing"],
            "active": True
        }
        json.dump(data_about_me, f_json)
    print(f"{filename} has been created")
    sleep(2)
    return filename


def swap_data_files(file_1, file_2):
    if not (os.path.isfile(file_1) and os.path.isfile(file_2)):
        print(f"{file_1} and {file_2} are not exist")
        return

    swap_file = "swap_file.txt"

    with open(swap_file, 'w+') as f_swap:  # создаю временный файл на чтение и запись
        with open(file_1, 'r') as f1:  # открываю 1-й файл на чтиние
            f_swap.write(f1.read())  # запись данных из 1-го файла во временный

        f_swap.seek(0)  # курсор в начало файла, чтобы читать с начала

        with open(file_2, 'r') as f2:  # открываю 2-й файл на чтение
            with open(file_1, 'w') as f1:  # открываю 1-й файл на запись
                json.dump(json.load(f2), f1)  # в 1-й файл пишу данные 2-го файла

        with open(file_2, 'w') as f2:  # открываю 2-й файл на запись
            f2.write(f_swap.read())  # в 2-й файл пишу данные временного файла

    os.remove(swap_file)  # kill -9


if __name__ == '__main__':
    swap_data_files(generate_file_txt(23), generate_file_json())
