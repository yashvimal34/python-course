def sum(a, b):
    # Here a and b are local variables which means you can access only inside the functions not outside the functions.
    c = a + b
    z = 34 # It creates a local variable called z which is destroyed after this fucntion returns.
    return c   # Once it is return 'a, b, c', will be wiped out of the memory.

z = 20 # It will print because z is global variable which you can access throughout the program
print(z)
print(sum(6, 4))
print(z)
# print(c) # but when you write "print(c)", it will throw error.
# Functions keep variables untill it returns.