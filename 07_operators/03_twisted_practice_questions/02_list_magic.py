a = [1, 2, 3]
b = a
a += [4]
c = a
b += [5]
print(a, b, c, a is b, b is c)

# output: [1, 2, 3, 4, 5]  [1, 2, 3, 4, 5]  [1, 2, 3, 4, 5]  True, True