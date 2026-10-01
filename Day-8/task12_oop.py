class Student:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

student1 = Student("Hasnain")
student2 = Student("Hasnain")
student3 = Student("Abrar")

print(student1 == student2)
print(student1 == student3)