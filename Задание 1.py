class Student:
    def __init__(self, student_id, name):
        self.name = name
        self.student_id = student_id
        self.grades = []
    def add_grade(self,grade):
        if (grade >= 0) and (grade <= 10):
            self.grades.append(grade)
        else:
            print('цифры от 0 до 10')
    def get_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0
    def display_info(self):
        print(f"Студент: {self.name}")
        print(f"Уникальный идентификатор: {self. student_id}")
        print(f"Оценки студента: {self.grades}")
        print(f"Средняя оценка: {self.get_average()}")


name = input("Введите имя студента: ")
student_id = input("Введите ID студента: ")
student = Student(student_id, name)

while True:
    grade_input = input("Введите оценку (или 'стоп' для завершения): ")
    if grade_input.lower() == "стоп":
        break
    try:
        grade = float(grade_input)
        student.add_grade(grade)
    except ValueError:
        print("Ошибка: введите число от 0 до 10.")

student.display_info()












