class Employee():
    compamy = "HP"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    # This is Instance method
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)
    
    # This is static method
    @staticmethod
    def sum(a, b):     # There will be error given we cannot do using self but we don't.
        return a + b   # we want to sum without using self we will us static decorator.


# We write static method when we don't want association with instance attribute.

    # This is class method.
    @classmethod
    def print_company(cls):  # cls is random name you can give any random name.
        print(cls.compamy)

    # Change company using class method.
    @classmethod
    def change_company(cls, new_company):
        cls.compamy = new_company


e1 = Employee("Yash", 250000)
e2 = Employee("Rahul", 200000)
e1.print_info()
e2.print_info()

print(e2.sum(35, 65))  # output: 100

print(Employee.compamy)  # output: HP
e1.change_company("Acer")   # It changed company name
print(Employee.compamy)     # output: Acer



'''
Interview Question
Q. How sum two or three number or an number without using self in function
A. We can sum any number without using self in function we will use static method decorator.

Q. What does class method usually do?
A. class method decorator usually print the name of class attribute or it helps in changing class attribute also.
'''