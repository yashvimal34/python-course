# Guess the date of your marriage.

a = int(input("Guess the date of your marriage: "))

match a:
    case 8:
        print("Wow! you guess")
    case 7:
        print("First you successful in your life")
    case 4:
        print("You will never get married.")
    case 10:
        print("You will be single")
    case _:
        print("Better luck next time")