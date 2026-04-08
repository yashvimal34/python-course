x = 50  # This is globla scope.

def my_func():
    x = 6  # This is local scope
    print(x)

my_func()
print(x)

# Using the global keyword.

x = 10
def modify_global():
    global x
    x = 5  # Modifies the global x

modify_global()
print(x) # output 5
