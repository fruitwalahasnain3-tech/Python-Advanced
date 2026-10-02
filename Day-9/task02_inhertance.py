class Animal:
    def sound(self):
        print("Animal makes a sound")

    def eat(self):
    	print("Animal Eating")


class Dog(Animal):
    pass


dog = Dog()

dog.sound()
dog.eat()
