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

    def speak(self):
        return "Vuf"
    
class Cat(Animal):
    def __init__(self, name: str, age: int, **kwargs):
        super().__init__(name, age, kwargs.get('color', None))

    def speak(self):
        return "Meow"
    
class Fish(Animal):
    def __init__(self, name: str, age: int, **kwargs):
        super().__init__(name, age, kwargs.get('habitat', None))

    def speak(self):
        return "Bul bul"

class AnimalFactory:
    def create_animal(self, animal_type, name, age):
        if animal_type.lower() == "cat":
            return Cat(name, age)
        elif animal_type.lower() == "dog":
            return Dog(name, age)
        elif animal_type.lower() == "fish":
            return Fish(name, age)
        else:
            raise ValueError("Invalid animal type")
        
my_animal = AnimalFactory()

spanky = my_animal.create_animal("dog", 'Спанки', 3)
tom = my_animal.create_animal("cat", 'Том', 15)
dorry = my_animal.create_animal("Fish", 'Дорри', 4)

print(spanky.speak())
print(tom.speak())
print(dorry.speak())