# Задание №1
# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
import json

class Factorial:
    def __init__(self, limit: int = 1):
        self.limit = limit
        self.function = []
    
    @property
    def fact(self):
        fact = 1
        values = []
        for i in range(1, self.limit + 1):
            fact *= i
            values.append(fact)
        return values

    def __call__(self, number: int = 1):
        self.function = self.fact[-number:]
        return self.function
#Добавили во 2 задании   
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        file = open('Lesson12/factorial_result.json', 'w', encoding='utf-8')
        json.dump(self.function, file)
        file.close()


# a = Factorial(10)
# print(a(3))

# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

# with Factorial(10) as fact_10:
#     print(fact_10(4))

# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.
class FactorialNew:
    def __init__(self, a: int = None, b: int = None, c: int = None):
        variables = {a, b, c} - {None}
        if len(variables) == 1:
            self.start, self.stop, self.step = 1, a, 1
        elif len(variables) == 2:
            self.start, self.stop, self.step = a, b, 1
        else:
            self.start, self.stop, self.step = a, b, c 
        self.fact = self.factorial()
    
    def factorial(self):
        fact_list = []
        num = 1
        for i in range(self.start, self.stop + 1, self.step):
            num *= i
            fact_list.append(num)
        return fact_list

    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.fact:
            return self.fact.pop(0)
        raise StopIteration
        
# first = FactorialNew(10)
# second = FactorialNew(4, 8)
# third = FactorialNew(5, 12, 3)

# for i in first:
#     print(i)
# print()
# for i in second:
#     print(i)
# print()
# for i in third:
#     print(i)
# print()

# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

#задание 6
class PositiveValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name
        
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError
        setattr(instance, self.name, value)
#задание 6 ^
class Rectangle:
    #задание 5
    __slots__ = ('_side_a', '_side_b')
    #задание 6
    side_a = PositiveValue()
    side_b = PositiveValue()
    #задание 6 ^
    def __init__(self, side_a: float, side_b: float = None):
        # if side_a <= 0 | side_b <= 0:
        #     raise ValueError
        self.side_a = side_a
        self.side_b = side_b
        if side_b is None:
            self._side_b = side_a

    # @property
    # def side_a(self):
    #     return self._side_a
    
    # @property
    # def side_b(self):
    #     return self._side_b
    
    # @side_a.setter
    # def side_a(self, value):
    #     if value <= 0:
    #         raise ValueError
    #     self._side_a = value

    # @side_b.setter
    # def side_b(self, value):
    #     if value <= 0:
    #         raise ValueError
    #     self._side_b = value

    def __str__(self):
        return f'Прямоугольник со сторонами {self.side_a} и {self.side_b}'

rec = Rectangle(4,6)
# rec.side_a = -7
# rec.side_b = 8
# print(rec)


# Задание №5
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.
# print(rec.__slots__)

# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.