class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age >= 0 and new_age <=150:
            self._age = new_age
        else:
            print("Invalid age")
        
person = Person("Rahul", 20)
print(person.age)