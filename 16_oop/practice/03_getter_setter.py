class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_age(self):  # Getters for age
        return self.age
    
    def set_age(self, new_age):
        if new_age >= 0 and new_age <=150:  # Validation.
            self.age = new_age
        else:
            print("Invalid age")

person = Person("Yash", 20)
print(person.get_age())

person.set_age(17)
print(person.get_age())

person.set_age(153)
print(person.get_age())  #   age wasen't changed