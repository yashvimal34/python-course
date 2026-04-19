def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

def exclaim(func):
    def wrapper():
        return func() + " vimal"
    return wrapper

@uppercase
@exclaim
def greet():
    return "yash"
print(greet())