number = 556

number = str(number)

length = len(number)

sum = 0

for i in number:
    sum += int(i)**length

if(sum == int(number)):
    print("The given number is", number," an armstron number")
else:
    print("It is not an", number, "armstrong number")