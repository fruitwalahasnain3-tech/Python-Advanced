class Student:
	collage = "GLS University"
	def __init__(self, name,course,semester,marks):
		self.name = name
		self.course = course
		self.semester = semester
		self.marks = marks
		self.collage = collage

	def __str__(self):
		return f"{self.name} | {self.course} | {self.semester} | {self.marks} | {self.collage}"


student1 = Student("Hasnain", "BCA", 5, 75)
student2 = Student("Furkan", "BBA", 1, 45)

print(student1)
print(student2)

		