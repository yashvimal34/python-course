a = int(input("Enter first number"))
b = int(input("Enter second number"))

try:
    c = a / b
    print(c)

except Exception as e:
    print(e)

# This is always executed no matter if try completely executes or not.
finally:
    print("However you execute this programm")




'''
Interview Question:
Q. In normal program if we cannot write this fancy keyword 'finally' it always print whatever you can. So where basically finally used.

A. This fancy keyword 'finally' basically used in while defining function.
'''
#  let's see it in another file called: ( 05_finally_function.py ).