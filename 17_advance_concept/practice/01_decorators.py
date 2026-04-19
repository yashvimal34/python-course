def my_dec(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_dec
def say_hello():
    print("Hello Yash")
    
say_hello()