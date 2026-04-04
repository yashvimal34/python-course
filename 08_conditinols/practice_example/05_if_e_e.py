'''
WAP to check wheather the last digit of a number is entererd by user is divisible by 3 or  not
'''

a =  int(input("Enter the number"))
b = a % 10
if(b % 3 == 0):
    print("It is divisible")
else:
    print("It is not divisibl")