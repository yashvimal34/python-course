class Dog:
    species = "Canis familiries"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says woof!")
    
my_dog = Dog("Sheru", "Golden Retriver")
another_dog = Dog("Lucy", "Labrader")

my_dog.bark()
print(Dog.species)