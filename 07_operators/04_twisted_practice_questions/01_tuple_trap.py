x = (1, 2)
y = (1, 2)
z = x
x += (3,)
print(x, y, z, x is z)

# x is (1, 2, 3)
# y is (1, 2)
# z is (1, 2)
#  x is y => False  