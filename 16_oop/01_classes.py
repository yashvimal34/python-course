# Class: Class is a blueprint or a template. E.g. Form for an Exam that contains name, age, electives, father's name etc.

# Object: Specific instances created from the template (class.). Eg, Form which contains date for any person e.g.(John Doe).

class Employee:
    compamy = "HP"

    def get_salary(self): # Self: Self is important here because self is a way to   reference the object of the class is being created. And also it is mandatory to give first parameter as self.
        return 50000
    
e1 = Employee()  # An object of class Employee is created here.
print(e1.get_salary())  # Employee 'e' is get_salary method is called.

e2 = Employee()
print(e2.get_salary())
print(e2.compamy)


'''
Interview Question
Q1. What is Class?
A1. Class is a blueprint or a template. E.g. Form for an Exam that contains name, age, electives, father's name etc.

Q2. What is Object?
A2. Specific instances created from the template (class.). Eg, Form which contains date for John Doe.

Q3. What is Self?
A3. Self basically refers to the object of class which is being created.

OR

A3. Self is important here because self is a way to   reference the object of the class is being created. And also it is mandatory to give first parameter as self.
'''