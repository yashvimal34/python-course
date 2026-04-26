while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"The division of two number is: {a / b}")

    except ValueError:
        print("Please don't perform bad typecasts")

    except ZeroDivisionError:
        print("Hey you cannot divide by 0")

    except Exception as e:
        print("An Unknown error", e)