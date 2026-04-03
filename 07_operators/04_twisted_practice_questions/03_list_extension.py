a = [1]
b = a
a = a + [2]
b += [3]
print(a, b)
# a = [1, 2]
# b = [1, 3]