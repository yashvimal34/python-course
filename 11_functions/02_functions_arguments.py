def add(a, b, plus=0):  # Here (a, b) => these are Parameters. Since we know a and b are Postionol arguments, but now we use default argumnets now here plus=0 , this is default args which we can use at last.
    x = a + b + plus
    return x

c = add(3, 5, 2)  # Here (3, 5) => these are Arguments.
print(c)

# now we will use keyword arguments.
c1 = add(b=5, a=3, plus=2)
print(c1)