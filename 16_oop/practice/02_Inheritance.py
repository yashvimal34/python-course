class Animal:  # This is super class.
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Generic Animal Sound")
    
class Dog(Animal):  # This is Sub-class. Dog is inherits from Animal.
    def speak(self):
        print("Woof!")

class Cat(Animal):  # This is also sub-class. Cat is also inherits form animal.
    def speak(self):
        print("Meow!")

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan
    

my_dog = Dog("Sheru")
my_cat = Cat("Lucy")

print(my_dog.name)
print(my_cat.name)

my_dog.speak()
my_cat.speak()

my_bird = Bird("Tweety", 10)
print(my_bird.name)
print(my_bird.wingspan)