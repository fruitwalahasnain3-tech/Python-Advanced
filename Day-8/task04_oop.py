class Student:
    def __init__(self,name,course,semester):
        self.name = name
        self.course = course
        self.semester = semester

    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Course : {self.course}")
        print(f"Semester : {self.semester}")


student1 = Student("Hasnain","IMCA",5)
student2 = Student("Suhem Mirza","MSCIT",3)
student3 = Student("Abrar","BA",1)

student1.show_details()
student2.show_details()
student3.show_details()