class Student:

    total_students = 0

    def __init__(self, name, course, semester, marks):
        self.name = name
        self.course = course
        self.semester = semester
        self.marks = marks

        Student.total_students += 1

    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Course : {self.course}")
        print(f"Semester : {self.semester}")
        print(f"Marks : {self.marks}")

    def check_result(self):
        if self.marks >= 50:
            return "Pass"
        else:
            return "Fail"

    def show_result(self):
        print(f"Name : {self.name}")
        print(f"Marks : {self.marks}")
        print("Result :", self.check_result())
        print()

    @classmethod
    def show_total_student(cls):
        print("Total Students :", cls.total_students)

    @staticmethod
    def passing_marks():
        print("Passing marks: 40")


student1 = Student("Hasnain", "IMCA", 5, 85)
student2 = Student("Suhem Mirza", "MSCIT", 3, 45)
student3 = Student("Abrar", "BA", 1, 65)

Student.passing_marks()