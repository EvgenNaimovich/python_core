"""
Дан файл целых чисел, содержащий не менее четырех элементов.
Вывести первый, второй, предпоследний и последний элементы данного файла.
Если чисел меньше 3 выводить ошибку.
"""
with open('task_1.txt', 'r') as f:
    nmbrs = list(map(int,f.read().split()))
    print(*nmbrs)
    if len(nmbrs) > 3:
        print(nmbrs[0])
        print(nmbrs[1])
        print(nmbrs[-1])
        print(nmbrs[-2])
    else:
        print("Ошибка: в файле меньше трёх чисел")
