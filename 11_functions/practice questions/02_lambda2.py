square = lambda x: x *x
print(square(20))

lists = [1, 2, 3, 4, 5, 6, 7]
square = list(map(lambda x: x*x, lists))
print(square)

# Recursion in python

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(5))