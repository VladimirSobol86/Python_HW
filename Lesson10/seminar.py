#1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
from math import pi
class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    def lenght(self):
        return 2 * pi * self.radius
    
    def area(self):
        return pi * self.radius ** 2
    
# krug = Circle(5)

# print(krug.lenght())
# print(krug.area())

#2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
class Rectangle:
    def __init__(self, side_a: float, side_b: float = None):
        self.side_a = side_a
        self.side_b = side_a if side_b is None else side_b

    def length(self):
        return (self.side_a + self.side_b) * 2
    
    def area(self):
        return self.side_a * self.side_b
    
# rec1 = Rectangle(5)
# rec2 = Rectangle(5, 6)

# print("Периметр равнобедренного =", rec1.length(), "Периметр второго =", rec2.length())
# print("Площадь равнобедренного =", rec1.area(), "Площадь второго =", rec2.area())

#3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.
class Human:
    def __init__(self, last_name: str, name: str, age: int, patronymic: str = None):
        self._name = name
        self._last_name = last_name
        self._patronymic = patronymic
        self._age = age

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age
    
    def full_name(self):
        return f'{self._last_name} {self._name} {"" if self._patronymic is None else self._patronymic + " "}ему {self._age} лет'
    
# stone = Human('Панфилов', 'Кирилл', 39, 'Владимирович')
# vova = Human('Соболь', 'Владимир', 27, 'Юрьевич')

# print(stone.full_name())
# print(vova.full_name())
# stone.birthday()
# print(stone.full_name())
# print(vova.full_name())

#4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
from random import randint
class Employee(Human):
    def __init__(self, last_name, name, age, patronymic):
        super().__init__(last_name, name, age, patronymic)
        self.u_id = str(randint(1, 999999)).zfill(0)
        self.lvl_access = int(self.u_id) % 7

# stone = Employee('Панфилов', 'Кирилл', 39, 'Владимирович')

# print(stone.u_id)
# print(stone.lvl_access)

#5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
#6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.
class Animal:
    def __init__(self, name: str, age: int, special: str):
        self._name = name
        self._age = age
        self._special = special

    def get_special(self):
        return self._special       

class Dog(Animal):
    def __init__(self, name: str, age: int, **kwargs):
        super().__init__(name, age, kwargs.get('breed', None))

class Cat(Animal):
    def __init__(self, name: str, age: int, **kwargs):
        super().__init__(name, age, kwargs.get('color', None))

class Fish(Animal):
    def __init__(self, name: str, age: int, **kwargs):
        super().__init__(name, age, kwargs.get('habitat', None))
    
spanky = Dog('Спанки', 3, breed='York')
tom = Cat('Том', 15, color='blue')
dorry = Fish('Дорри', 4, habitat='Дом')

for animal in (spanky, tom, dorry):
    print(animal.get_special())