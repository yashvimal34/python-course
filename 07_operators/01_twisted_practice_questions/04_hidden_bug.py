a = [1, 2, 3]
b = a
c = a.copy()
a[0] = 100
print(b is a, b == a, c == a) # Outpur: True True False