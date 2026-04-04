# Q1. WAP to check if single character is vowel or not take single character input from the user.

vowel = input("enter a vowel: ")
if vowel.lower() in "a, e, i, o, u":
    print("vowel")
else:
    print("It is not vowel")


# Q2. WAP to check if the number is even or odd take the number from the user.

even_odd = int(input("enter the number: "))
if(even_odd % 2 == 0):
    print("it is even no.")
else:
    print("it is a odd no.")


# Q3. Check if the first and last number of a list is same or not. Take a pre-defined list in the code itself.

number = [23, 78, 45, 86, 35, 23]
if(number[0] == number[-1]):
    print("yes it is same")
else:
    print("it is not same")