class Employee:

    def __init__(self, name, age, address, salary, phone): # __init__(self)  is constructer, whenever you write __init__ it is constructer. And Constructer is used to initialise an object.
        self.name = name 
        self.age = age  # Create an instance attribute of name age and assign it with age
        self.address = address
        self.salary = salary
        self.phone = phone

    def get_name(self):
        return self.name

    def get_all_info(self):
        print(f"The name of Employee is {self.name}, and his age is {self.age}, his birth place is {self.address}, his salary is {self.salary}, and his phone number is {self.phone}")

e1 = Employee("Rahul", 20, "Unnao", 50000, 6307663945)
print(e1.get_name())
e1.get_all_info()



'''
Interview Question.
Q1. How will  you create constructer and what is constructer?
A1.  __init__(self)  is constructer, whenever you write __init__ it is constructer. And Constructer is used to initialise an object.
'''