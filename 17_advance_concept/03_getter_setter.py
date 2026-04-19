class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property  # This is the property decorator
    def first_name(self):                   # @property decorator is used
        list = self.name.split(" ")         # basically of this property
        return list[0]
    
    @first_name.setter
    def first_name(self, first):
        list = self.name.split(" ")
        new_name = f"{first} {list[1]}"
        self.name = new_name

    # def new_first_name(self, first):      # You can also
    #     list = self.name.split(" ")       # do like
    #     new_name = f"{first} {list[1]}"   # this
    #     self.name = new_name
    

# e = Employee("Yash Vimal", 200000)
# print(e.first_name())                     # By executing this method
# e.new_first_name("Rahul")
# print(e.name)

e = Employee("Yash Vimal", 200000)
print(e.first_name)
e.first_name = "Rahul"
print(e.name)