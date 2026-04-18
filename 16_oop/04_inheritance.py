class Animal: # This parent class or (super class)
    location = "India"

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("speanking now...")


class Dog(Animal): # This is how inheritance done in python
    def speak(self):
        super().speak()  # We are using speak function of the parent class
        print("woof!")

# a = Animal("Dog")
# a.speak()
d = Dog("Bruno")
d.speak()
print(d.location)