num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Which operation do you want to perform: \nPress: '+' for addition, \nPress: '-' for subtraction, \nPress: '*' for multiplication, \nPress: '//' for floor divison: ")
o = input("Enter the opration: ")



if (o == '+'):
    print(f"The result of num1 and num2 is {num1 + num2}")
elif (o == '-'):
    print(f"The result of num1 and num2 is {num1 - num2}")
elif (o == '*' ):
    print(f"The result of num1 and num2 is {num1 * num2}")
elif (o == '//'):
    print(f"The result fo num1 and num2 is {num1 // num2}")
else:
    print("Invalid Number or Operaion")