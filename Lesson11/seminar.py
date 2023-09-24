#1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания# (time.time)

# from time import time

class MyString(str):
    """It is help for MyString"""
    def __new__(cls, st, author):
        """It is help for new"""
        instance = super().__new__(cls, st)
        instance.author = author
        instance.st = st
        instance.time_ = time()
        return instance
    
# stroki = MyString('wfqfgwefgeg', 'Vladimir')
# print(f'{stroki}, {stroki.author =}, {stroki.time_ =}')

#2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра
class Archive:
    """ This class is neccessary for archieving """
    _instance = None

    def __new__(cls, number: int, string: str):
        """ This is refactored new """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.numbers = []
            cls._instance.strings = []
        else:
            cls._instance.numbers.append(cls._instance.number)
            cls._instance.strings.append(cls._instance.string)
        return cls._instance
    
    def __init__(self, number: int, string: str):
        """ This is refactored init """
        self.number = number
        self.string = string

    def __str__(self):
        """ This is printing """
        return f'{self.number} {self.string} {self.numbers} {self.strings}'
    
# a = Archive(10, 'ten')
# print(a)
# b = Archive(20, 'twelve')
# print(b)
# c = Archive(1, 'one')
# print(c)

#3
# Добавьте к задачам 1 и 2 строки документации для классов.
# help(MyString)
# help(Archive)

#4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.
class Archive:
    """ This class is neccessary for archieving """
    _instance = None

    def __new__(cls, number: int, string: str):
        """ This is refactored new """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.numbers = []
            cls._instance.strings = []
        else:
            cls._instance.numbers.append(cls._instance.number)
            cls._instance.strings.append(cls._instance.string)
        return cls._instance
    
    def __init__(self, number: int, string: str):
        """ This is refactored init """
        self.number = number
        self.string = string

    def __str__(self):
        """ This is printing """
        return f'{self.number} {self.string} {self.numbers} {self.strings}'
    
    def __repr__(self):
        return f'Archive({self.number}, "{self.string}")'

a = Archive(4, 'stroka')
# print(f'{a=}')

#5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.
class Rectangle:
    def __init__(self, side_a: float, side_b: float = None):
        self.side_a = side_a
        self.side_b = side_a if side_b is None else side_b

    def length(self):
        return (self.side_a + self.side_b) * 2
    
    def area(self):
        return self.side_a * self.side_b
    
    def __sub__(self, other):
        res = (self.length() - other.length())/4
        if res >= 0:
            return Rectangle((self.length() - other.length())/4)
        else:
            raise ValueError
        
    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.side_a + other.side_a, self.side_b + other.side_b)
        else:
            raise TypeError
        
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        else:
            raise TypeError
    
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            raise TypeError
        
rec1 = Rectangle(2)
rec2 = Rectangle(3, 5)
# rec3 = rec2 - rec1
# rec4 = rec1 + rec2
# print(f'Сторона нового квадрата равна {rec3.side_a}')
# print(f'Сторона нового квадрата равна {rec4.side_a}')
print(rec1 < rec2)
print(rec1 == rec2)
print(rec1 > rec2)

#6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения (добавили равно и меньше)