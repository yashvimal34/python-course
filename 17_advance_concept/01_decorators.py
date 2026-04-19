# Decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then its return that new function.

def decorator(func):
    def wrapper():
        print("I am about to execute the function...")
        func()
        print("I have executed the program")
    return wrapper

@decorator
def say_hello():
    print("Hello!")
say_hello()

# You can also print.
# f = decorator(say_hello)
# f()

'''
f will look something like this
def f():
    print("I am about execute the function...")
    print("Hello")
    print("I have executed the function...")
'''