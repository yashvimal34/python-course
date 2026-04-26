a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if b == 0:
    raise ValueError("Please don't write bad typecasts")
print(f"The divisio of {a / b}")