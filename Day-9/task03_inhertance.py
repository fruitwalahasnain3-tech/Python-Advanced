class Animal:
    def sound(self):
        print("Animal makes a sound")

    def eat(self):
    	print("Animal Eating")


class Dog(Animal):
    def bark(self):
    	print("Dog is barking")


dog = Dog()

dog.sound()
dog.eat()
dog.bark()