# Задание №6
# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import os
from collections import namedtuple
from sys import argv
import logging

def directory_walker(dir_path):
    results = []
    logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            Object_info = namedtuple('File', 'file_name extension parent_directory')
            obj_info = Object_info(name.split('.')[0], name.split('.')[1], root)
            results.append(obj_info)
            logging.info(obj_info)


        for name in dirs:
            Object_info2 = namedtuple('Folder', 'folder_name parent_directory')
            obj_info2 = Object_info2(name, root)
            results.append(obj_info2)    
            logging.info(obj_info2) 

    print(results)

if __name__ == '__main__':
    if len(argv) > 1:
        print(argv)
    else:
        data = input('Введите путь до директории на ПК: ')
        directory_walker(data)
#c:/Users/vsobo/Desktop/dsa