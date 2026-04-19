class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"My name is {self.name} and my age is {self.age}"
    
    def __repr__(self):
        return f"Name: {self.name}\nAge: {self.age}"

person = Person("Yash Vimal", 20)
print(person.__str__())
print(person.__repr__())


# len() magic dunder method.

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __len__(self):
        return self.pages
    
b = Book("Python 101", 360)
print(len(b))