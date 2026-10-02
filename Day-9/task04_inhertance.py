class Animal:
	def __init__(self,name,age):
		self.name = name
		self.age = age

class Dog(Animal):
	def __init__(self,name,age,breed):
		super().__init__(name,age)
		self.breed = breed

dog = Dog("Bruno","3","Labrado")

print(dog.name)
print(dog.age)
print(dog.breed)