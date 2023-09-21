import csv
import json
import random
import math
from functools import wraps
from typing import Callable

# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def generate_csv():
    with open("Lesson9/output.csv", "w", encoding='UTF-8') as file:
        writer = csv.writer(file)
        for _ in range(random.randint(100, 1001)):
            writer.writerow([random.randint(0,100) for _ in range(3)])

# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
def from_csv_decorator(func: Callable):
    generate_csv()
    def wrapper():
        with open("Lesson9/output.csv", 'r', encoding='UTF-8') as file:
            data = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for row in data:
                if row and row[0] != 0:
                    func(*row)

    return wrapper

# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('Lesson9/log.json', 'a') as f:
            json.dump({'args': args, 'result': result}, f, indent=4, ensure_ascii=False)
        return result
    return wrapper

# Нахождение корней квадратного уравнения

@from_csv_decorator
@log_decorator
def find_roots(*args):
    a, b, c = args
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)
    else:
        return "Discriminant < 0, no solutions"
    
find_roots()