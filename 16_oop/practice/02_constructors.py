class Emp:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def get_all_info(self):
        return f"My name is {self.name} and my age is {self.age}, and my salary is {self.salary}"
    
e1 = Emp("Yash", 20, 200000)
print(e1.get_all_info())