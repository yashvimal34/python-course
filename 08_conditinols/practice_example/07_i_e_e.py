'''
WAP to check wheather years is leap year or not
'''

yr = int(input("Enter the year: "))

if (yr % 4 == 0):
    print("It is a leap year")
else:
    print("It is not a leap year")