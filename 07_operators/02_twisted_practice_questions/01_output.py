a = [10]
b = a
a += a
print(a, b, a is b) # Output:  [10, 10] [10, 10] True