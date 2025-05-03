class Student:
    def __init__(self, name, student_id):
        self.name = name  # имя студента
        self.student_id = student_id  # номер студенческого билета

    def study(self):
        print(f"{self.name} учится.")


# Родительский класс Преподаватель
class Teacher:
    def __init__(self, subject):
        self.subject = subject  # предмет преподавания

    def teach(self):
        print(f"Преподаватель ведет занятие по предмету: {self.subject}")


# Класс Ассистент, наследуется и от Student, и от Teacher
class Assistant(Student, Teacher):
    def __init__(self, name, student_id, subject):
        # Инициализация родительских классов
        Student.__init__(self, name, student_id)  # вызываем конструктор Student
        Teacher.__init__(self, subject)           # вызываем конструктор Teacher

    def help_student(self):
        print(f"Ассистент {self.name} помогает студентам по предмету {self.subject}.")
