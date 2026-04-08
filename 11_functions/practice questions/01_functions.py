# Greet Someone.
def greet(name):
    return f"Hello, {name}!"
print(greet("Yash")) # Hello, Yash

# Types of arguments.
# 1 Postional Arguments.

def add(a, b):
    return a + b
print(add(564, 654))

# 2. Default Arguments.

def greet(name="Yash"):
    return f"Hello, {name}"
print(greet())

# 3 keyword Arguments.

def student(name, age):
    return f"My name is {name} and age is {age}"
print(student("Yash", 20))