def divide(a, b):
    try:
        c = a / b
        print(c)
        return c
    
    except Exception as e:
        print(e)
        return e
    
    finally:
        print("However you execute the program")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
divide(a, b)

