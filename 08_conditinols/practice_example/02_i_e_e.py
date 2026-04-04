'''
Q2. Create a simple calculator that takes two numbers and an operator (+, -, *, /) as input, then performs the operation and prints the result.
'''

a = float(input("Enter first number"))
o = input("Enter operator (+, -, *, /)")
b = float(input("Enter Second number"))

if(o == '+'):
    print(a + b)
elif (o == '-'):
    print(a - b)
elif (o == '*'):
    print(a * b)
elif (o == '/'):
    print(a / b)
else:
    print("Invalid  number")