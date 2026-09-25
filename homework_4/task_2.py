"""
Дан файл целых чисел. Создать два новых файла, первый из которых содержит четные числа из исходного файла,
а второй — нечетные (в том же порядке). Если четные или нечетные числа в исходном файле отсутствуют,
то соответствующий результирующий файл оставить пустым.
"""

with (open('task_1.txt', 'r', encoding='utf-8') as f_in,
      open('even_numbers.txt', 'w') as f_even,
      open('odd_numbers.txt', 'w') as f_odd):
    even_list = []
    odd_list = []

    for line in f_in:
        numbers_list = line.split()

        for number_str in numbers_list:
            try:
                if int(number_str) % 2 == 0:
                    even_list.append(number_str)
                else:
                    odd_list.append(number_str)
            except ValueError:
                print(f"{number_str} не число. пропускаем")
                continue

    f_even.write('\n'.join(even_list))
    f_odd.write('\n'.join(odd_list))
