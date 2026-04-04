num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")

if num % 5 == 0:
    print("Divisible by 5")

if num > 50:
    print("Greater than 50")

if num % 2 != 0 and num % 5 != 0 and num <= 50:
    print("Nothing special")
