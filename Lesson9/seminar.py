# import random
# from typing import Callable
# import json
# import os
# #1
# #Создайте функцию-замыкание, которая запрашивает два целых числа:
# # ○ от 1 до 100 для загадывания,
# # ○ от 1 до 10 для количества попыток
# # Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
# def guess_number(low: int = 1, high: int = 100, tries: int = 10):
#     number = random.randint(low,high)
#     def guess_game():
#         count = 1
#         while count <= tries:
#             my_num = int(input(f'{count} try of {tries}. Enter number from {low} to {high}: '))
#             if my_num > number:
#                 print('Lower')
#             elif my_num < number:
#                 print('Higher')
#             else:
#                 result = f'Great! guess number is {number}'
#                 break
#             count +=1
#         else:
#             result = 'Game over! U are lose'
#         print(result)
#         return result
#     return guess_game

# # if __name__ == '__main__':
# #     game = guess_number()
# #     game()

# #2
# # Дорабатываем задачу 1.
# # Превратите внешнюю функцию в декоратор.
# # Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# # Если не входят, вызывать функцию со случайными числами из диапазонов.

# #Внешняя функция
# def check_nums(func: Callable):
#     def wrapper(low_: int, high_: int, tries_: int):
#         if low_ > high_ or low_ < 0 or high_ > 100:
#             low_ = 1
#             high_ = 100
#         if tries_ not in range (1,10):
#             tries_ = random.randint(1, 10)
#             result = func(low_, high_, tries_)
#         return result
#     return wrapper        
# #Декоратор
# @check_nums
# #Функция из прошлой задачи
# def guess_number_new(low: int = 1, high: int = 100, tries: int = 10):
#     number = random.randint(low,high)
#     def guess_game_new():
#         count = 1
#         while count <= tries:
#             my_num = int(input(f'{count} try of {tries}. Enter number from {low} to {high}: '))
#             if my_num > number:
#                 print('Lower')
#             elif my_num < number:
#                 print('Higher')
#             else:
#                 result = f'Great! guess number is {number}'
#                 break
#             count +=1
#         else:
#             result = 'Game over! U are lose'
#         print(result)
#         return result
#     return guess_game_new

# # if __name__ == '__main__':
# #     game2 = guess_number_new(1, 100, 10)
# #     game2()

# #3
# # Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает. 
# # При повторном вызове файл должен расширяться, а не перезаписываться.
# # Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# # Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# # Имя файла должно совпадать с именем декорируемой функции.
# def json_safe(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if not os.path.exists(f'Lesson9/{func.__name__}.json'):
#             with open(f'Lesson9/{func.__name__}.json', 'w', encoding='utf-8') as f:
#                 json.dump({(args, kwargs): result}, f, indent=4, ensure_ascii=False)
#         else:
#             with open(f'Lesson9/{func.__name__}.json', 'r', encoding='utf-8') as f_read:
#                 json_data = json.load(f_read)
#             with open(f'Lesson9/{func.__name__}.json', 'w', encoding='utf-8') as f_write:
#                 json_data[(args, kwargs)] = result
#                 json.dump(json_data, f_write, indent=4, ensure_ascii=False)
#         return result
#     return wrapper

# @json_safe
# def function_(a,b):
#     return a+b

# # if __name__ == '__main__':
# #     function_(random.randint(1,100),random.randint(1,100))
# #     function_(random.randint(1,100),b=random.randint(1,100))
# #     function_(a=random.randint(1,100),b=random.randint(1,100))

# #4
# # Создайте декоратор с параметром.
# # Параметр - целое число, количество запусков декорируемой функции.
# def decor(loop:int):
#     def inner(func):
#         result = []
#         def wrapper(*args, **kwargs):
#             for _ in range(loop):
#                 result.append(func(*args, **kwargs))
#             return result
#         return wrapper
#     return inner

# @decor(10)
# def function_2(a,b):
#     return a+b

# # if __name__ == '__main__':
# #     print(function_2(random.randint(1,100),random.randint(1,100)))

# #5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
import json
import os
import random
from typing import Callable
from functools import wraps

def json_safe(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not os.path.exists(f'result.json'):
            print(result)
            with open(f'result.json', 'w', encoding='utf-8') as f:
                atr = ','.join(list(map(str, args))) + '|' + ','.join(
                list(map(lambda x, y: str(f'{x}={y}'), kwargs.items())))
                json.dump({atr: result}, f, indent=4, ensure_ascii=False)
        else:
            with open(f'result.json', 'r', encoding='utf-8') as f_read:
                json_data = json.load(f_read)
                print(json_data)
            with open(f'result.json', 'w', encoding='utf-8') as f_write:
                atr = ','.join(list(map(str, args))) + '|' + ','.join(
                list(map(lambda x, y: str(f'{x}={y}'), kwargs.items())))
                json_data[atr] = result
                json.dump(json_data, f_write, indent=4, ensure_ascii=False)

        return result

    return wrapper


def decor(loop: int):
    def inner(func):
        
        result = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(loop):
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return inner


def check_nums(func: Callable):
    @wraps(func)
    def wrapper(l_lim: int, h_lim: int, tries_: int):
        if l_lim > h_lim or l_lim < 0 or h_lim > 100:
            l_lim = 1
            h_lim = 100
        if tries_ not in range(1, 11):
            tries_ = random.randint(1, 10)

        result_ = func(l_lim, h_lim, tries_)
        return result_

    return wrapper


@decor(3)
@json_safe
@check_nums
def guess_number(low: int = 10, high: int = 100, tries: int = 10) -> str:
    count = 1
    number = random.randint(low, high)
    while count <= tries:
        my_num = int(input(f'{count} из {tries} попытка. Введите число от {low} до {high}: '))
        if my_num > number:
            print('Я загадал меньше')
        elif my_num < number:
            print('Я загадал больше')
        else:
            result = f'Да ты победил c {count} попытки, я загадал {number}'
            break
        count += 1
    else:
        result = f'Извини, но ты проиграл, все попытки закончились'
    print(result)
    return result

if __name__ == '__main__':
    guess_number(1, 1000, 2)
