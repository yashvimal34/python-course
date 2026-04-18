class Employee:
    company = "Asus"  # This is class attribute.

    def __init__(self, name, age, salary, company):
        self.name = name
        self.age = age
        self.salary = salary
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_all_info(self):
        print(f"name is {self.name}, age is{self.age}, salary {self.salary}, company {self.company}")


e1 = Employee("Yash", 20, 50000, "Tesla")
# print(e1.get_all_info())
print(e1.company)  # It will always print instance attribute whenever it is present. But when instance attribute is not present it will print class attribute.
print(Employee.company)

# Now will understand Object Introsepection.

print(dir(e1))  # This method can print all attributes and modules which is present behind and outside the sences.



'''
Interview Questions.
Q1. Difference between class attribute and instance attribute?
A1. When instance attribute is present so it will print instance, but if instance attribute is not present it will print class attribute as it is before given

Q2. However but we want to print both instance attribute, class attribute so we can print that.
A2. Yes, here's solution to print class attribute also with instance attribute. To print we have to write 
    print(class_name.class attribute_name), Eg. print(Employee.company).

Q3. What is 'dir'?
A3. This method can print all attributes and modules which is present behind and outside the sences.
'''        