from random import uniform, randint, seed, sample, randbytes
import string
import os
#1 
#✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции. 
def write_in_file(num_of_str, file_name):
    with open(f'{file_name}.txt', 'a', encoding='utf-8') as f:
        f.writelines('\n'.join([f'{randint(-1000, 1000)} | {uniform(-1000, 1000)}' for i in range(num_of_str)]))

# if __name__ == '__main__':
#     write_in_file(12, 'n1_sem')

#2
# Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
def write_names_in_file():
    names = []
    while len(names) < 4:
        res = ''.join(sample(string.ascii_lowercase, randint(4,7) )).title()
        if len(set(string.ascii_lowercase) & set('aeiouy')) > 0:
            names.append(res)
    with open('file_names.txt', 'a', encoding = 'utf-8') as f:
        f.writelines('\n'.join(names))

# if __name__ == '__main__':
#     num_of_names = randint(3,10)
#     vowels = 'aeiouy'
#     write_names_in_file()

#3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.
def open_files(file_name1, file_name2):
    names, numbers = None, None
    with (
        open(file_name1, 'r', encoding='utf-8') as f1,
        open(file_name2, 'r', encoding='utf-8') as f2,
    ):
        names = f1.readlines()
        numbers = f2.readlines()

    numbers = list(map(lambda x: int(x.strip().split(' | ')[0]) * float(x.strip().split(' | ')[1]), numbers))
    names = list(map(lambda x: x.strip(), names))
    list_to_write = list(zip(names, numbers))

    with open("results.txt", 'a', encoding='utf-8') as f:
        for st in list_to_write:
            if st[1] > 0:
                f.write(f'{st[0].upper()} -> {round(st[1])} \n')
            else:
                f.write(f'{st[0].lower()} -> {abs(st[1])} \n')

# if __name__ == '__main__':
#     open_files('file_names.txt', 'n1_sem.txt')

#4
# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
def create_files(extension, min_len = 6, max_len = 30, min_bytes = 256, 
                 max_bytes = 4096, num_of_files = 3):
    for i in range(num_of_files):
        name = ''.join(sample(string.ascii_lowercase+string.ascii_lowercase, randint(min_len, max_len)))
        with open (f'{name}.{extension}', 'wb') as f:
            f.write(randbytes(randint(min_bytes, max_bytes)))

# if __name__ == '__main__':
#     create_files(extension='txt')

#5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
def extensions_and_num(ext_num):
    for tu in ext_num:
        create_files(extension=tu[0], num_of_files=tu[1])

# if __name__ == '__main__':
#     extensions_and_num([('py', 2), ('txt', 3)])