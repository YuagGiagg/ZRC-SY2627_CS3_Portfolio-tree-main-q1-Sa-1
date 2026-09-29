class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def attendClass(self):
        print(self.name, "is attending class.")


class Course:
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title
        self.students = []

    def addStudent(self, student):
        self.students.append(student)