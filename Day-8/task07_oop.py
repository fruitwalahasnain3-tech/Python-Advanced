class Student:
    def __init__(self,name,course,semester,marks):
        self.name = name
        self.course = course
        self.semester = semester
        self.marks = marks

    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Course : {self.course}")
        print(f"Semester : {self.semester}")
        print(f"Marks : {self.marks}")

    def check_result(self):
        if self.marks >=50:
            return "Pass"
        else:
            return "Fail"

    def show_result(self):
        print(f"Name : {self.name}")
        print(f"Marks : {self.marks}")
        print("Result : ", self.check_result())
        print("\n")

student1 = Student("Hasnain","IMCA",5,85)
student2 = Student("Suhem Mirza","MSCIT",3,45)
student3 = Student("Abrar","BA",1,65)

student1.show_result()
student2.show_result()
student3.show_result()
