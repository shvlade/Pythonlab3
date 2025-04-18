class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            print("Оценка должна быть от 0 до 10.")

    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def display_info(self):
        print(f"Студент: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.get_average():.2f}")

    def __str__(self):
        return f"Student({self.name}, ID: {self.student_id})"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    def __len__(self):
        return len(self.grades)

s1 = Student("g3498", "Женя")

# Добавим оценки
s1.add_grade(9)
s1.add_grade(8)
s1.add_grade(10)

# Выводим информацию
s1.display_info()

# Магические методы
print(s1)
print(len(s1))
print(s1 == Student("g3498", "Женя"))