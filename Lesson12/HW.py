class NameDescriptor:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            raise ValueError("Имя должно начинаться с заглавной буквы и содержать только буквы.")
        setattr(instance, self._name, value)
        
import csv

# Основной класс
class Student:
    first_name = NameDescriptor()
    middle_name = NameDescriptor()
    last_name = NameDescriptor()

    def __init__(self, first_name, middle_name, last_name, csv_path):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

        # Загрузка предметов из CSV файла
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            self.subjects = {row[0]: {"grades": [], "test_scores": [], } for row in reader}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден.")
        if grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть от 2 до 5.")
        self.subjects[subject]["grades"].append(grade)

    def add_test_score(self, subject, score):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден.")
        if score < 0 or score > 100:
            raise ValueError("Результат теста должен быть от 0 до 100.")
        self.subjects[subject]["test_scores"].append(score)

    def average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден.")
        scores = self.subjects[subject]["test_scores"]
        return f'Средний результат тестов по предмету {subject}: {sum(scores) / len(scores)}' if scores else f'Тестов по предмету еще небыло'

    def average_grade(self):
        total_grades = [grade for subj in self.subjects.values() for grade in subj["grades"]]
        return f'Средняя оценка по всем предметам: {sum(total_grades) / len(total_grades)}' if total_grades else 'Оценок еще небыло'

#positive tests:    
a = Student('Соболь', 'Владимир', 'Юрьевич', 'Lesson12/subjects.csv')
# b = Student('Иванов', 'Иван', 'Иванович', 'Lesson12/subjects.csv')
# c = Student('Иванов', 'Иван', 'Владимирович', 'Lesson12/subjects.csv')
# a.add_grade("Math", 5)
# a.add_grade("Physics", 2)
# a.add_grade("Chemistry", 4)
# a.add_grade("Biology", 5)
# a.add_test_score("Math", 99)
# a.add_test_score("Math", 25)
# a.add_test_score("Math", 55)
# a.add_test_score("Math", 44)
# a.add_test_score("Math", 33)
# print(a.average_grade())
# print(a.average_test_score("Math"))
# print(a.average_test_score("Geography"))

#negative tests:
# bad = Student('cоболь', 'Владимир', 'Юрьевич', 'Lesson12/subjects.csv')
# bad = Student('Соболь', 'владимир', 'Юрьевич', 'Lesson12/subjects.csv')
# bad = Student('Соболь', 'Владимир', 'юрьевич', 'Lesson12/subjects.csv')
# bad = Student('Соболь', 'Владимир', '1рьевич', 'Lesson12/subjects.csv')
# a.add_grade("Math1233", 5)
# a.add_grade("Math", 6)
# a.add_grade("Math", 1)
# a.add_test_score("Mathrwer", 99)
# a.add_test_score("Math", 101)
# a.add_test_score("Math", -101)
# print(a.average_test_score("Math2"))