def sum(a, b):
    c = a + b
# let's see how to use a local variable to global variable.    
    global z # Please modify global z
    z = 34 # to use this local variable to global you have to write 'global z'.
    return c

z = 23  # you know it is a global variable.
print(sum(64, 65))
print(z)

# Note:
# The excessive use of global is discourged as it can make debugging harder.



'''
Interview Question.
Ques. Can we use a local variable as a global variable inside a function.
Ans. Answer is YES, you can use global variable by writing a word 'global z', z is a variable which is shown above.
'''