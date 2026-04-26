a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

try:
    c = a / b
    print(c)

except Exception as e:
    print(e)

else:
    print("Hey I am good")