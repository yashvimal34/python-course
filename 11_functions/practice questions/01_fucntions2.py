def greet(name):
    return f"Hello, {name}"
print(greet("Yash"))


def sum(a, b):
    return a + b
print(sum(233, 654))

# Default Arguments.

def greet(name="Yash"):
    return f"Hello, {name}"
print(greet())

# keywords arguments.

def student(name, age):
    print(f"{name}, {age}")

print(student(name="Yash", age=20))