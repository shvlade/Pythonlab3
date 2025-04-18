class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Teacher(Person):
    def __init__(self, name,subject,age):
        super().__init__(name,age)
        self.subject = subject
        self.students = []
    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print("Можно добавить только объект класса Student.")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print("Студент не найден.")

    def list_students(self):
        print("Студенты преподавателя", self.name)
        for student in self.students:
            print(f"{student.name} (ID: {student.student_id})")







