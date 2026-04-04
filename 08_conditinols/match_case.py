a = int(input("Enter a lucky number between to win prize"))

match a:
    case 1:
        print("You won an Smartphone")
    case 3:
        print("You won an $10")
    case 6:
        print("You won ticket for a Foreign Trip")
    case _:  # case _: => in this ('_:') is default.
        print("Better Luck next time")