try:
    num = int(input("Enter the number: "))
    result = 20 / num
    print(result)
except ValueError:
    print("bad typecasts")
except ZeroDivisionError:
    print("Hey you cannot divide by zero.")
else:
    print("hey what are you doing")