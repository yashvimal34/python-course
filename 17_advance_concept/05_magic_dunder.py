class Employee():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return f"The name is {self.name} and his salary is {self.salary}"
    
    def __repr__(self):
        return f"name: {self.name}\nsalary: {self.salary}"
    
    def __len__(self):
        return len(self.name)

e = Employee("Yash", 20000)
print(e.name, e.salary)
print(str(e))
print(repr(e))
print(len(e))


'''
Note:
__str__ and __repr__ these both dunder methods basically they are same but bit different also
__str__ method is used for users who interacting with it.
__repr__ method is use for developers who wants know how it is working.
'''