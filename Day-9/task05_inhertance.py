class Animal:
	def sound(self):
		print("Animals make sound.")

class Dog(Animal):
	def sound(self):
		print("Dog Barks.")


dog = Dog()
dog.sound()