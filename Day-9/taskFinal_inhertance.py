class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def info(self):
		print("Name: " , self.name)
		print("Age: ", self.age)

		
class Student(Person):
	def __init__(self,name,age,course):
		super().__init__(name,age)
		self.course =  course

	def info(self):
		super().info()
		print("Course: ", self.course)
		

student1 = Student("Hasnain",20,"AI/ML")

student1.info()