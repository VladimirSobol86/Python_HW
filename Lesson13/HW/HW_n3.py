##В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
## Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.
# Ваша задача:
##Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.
## Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID). Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
## Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).
# Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно при передаче неверных данных.

from random import randint

class InvalidIdError(Exception):
    def __init__(self, text):
        self.txt = text    

class InvalidNameError(Exception):
    def __init__(self, text):
        self.txt = text

class InvalidAgeError(Exception):
    def __init__(self, text):
        self.txt = text
        
class Person:
    
    def __init__(self, first_name, middle_name, last_name, age: int):
        if len(first_name) != 0:
            self.first_name = first_name
        else:
            raise InvalidNameError ('Invalid name: . Name should be a non-empty string.')

        if isinstance(middle_name, str) and len(middle_name) != 0:
            self.middle_name = middle_name
        else:
            raise InvalidNameError ('Некорректное имя')

        if isinstance(last_name, str) and len(last_name) != 0:
            self.last_name = last_name
        else:
            raise InvalidNameError ('Некорректное имя')                  
        
        if isinstance(age, int):     
            if age > 0:   
                self.age = age
            else:
                raise InvalidAgeError(f'Invalid age: {age}. Age should be a positive integer.')
        else:
            raise InvalidAgeError('Некорректный формат ввода')
        
    def birthday(self):
        self.age += 1
        
    def get_age(self):
        return self.age    
        
class Employee(Person):
    def __init__(self, age: int, first_name: str, middle_name: str, last_name: str, ID = None):
        super().__init__(age, first_name, middle_name, last_name)
        if ID == None:
            self.ID = str(randint(1, 999999)).zfill(0)
        else:
            if len(str(ID)) == 6:
                self.ID = ID
            else:
                raise InvalidIdError(f'Invalid id: {ID}. Id should be a 6-digit positive integer between 100000 and 999999.')

    def get_level(self):
        self.level = int(self.ID) % 7
        # print(self.level)

a = Employee("Имя", "Фамилия", "Отчество", 5, 155555)
print(a.get_age())
# a.birthday()
# print(a.get_level())
print(a.__dict__)
# b = Person(12, "Имя", "Фамилия", "Отчество")
# print(b.__dict__)
