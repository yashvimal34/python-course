class Dog:
    def __init__(self, name):
        self.name = name # This is Instance attribute.
    
    def speak(self):
        return f"{self.name} says Woof!!"
    
dog = Dog("Sheru")
print(dog.speak())