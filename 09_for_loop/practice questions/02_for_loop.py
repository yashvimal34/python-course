# Python program to print a multiplication table of a given number

i = 5
for i in range(11):
    print(5*i)

# Python program to display numbers from a list using a for loop.
print("list")
list = [20, 30, 40, 50, 60]

for i in list:
    print(i)


# Python program to count the total number of digits in a number.

print("digitts")

digits = 13278947
digits = str(digits)

count = 0

for i in digits:
    count += 1
print(count)


# Python program to check if the given string is a palindrome.
print("Palindrome")
string = "madam"
reverseString = ""
for i in string:
    reverseString = i+reverseString

if(string == reverseString):
        print("This string", reverseString, "is palindrome")
else:
        print("This string", string, "is not palindrome")


# Python program that accepts a word from the user and reverses it.

print("reverse")
word = str(input("Enter the Word: "))

reverseString = ""
for i in word:
     reverseString = i+reverseString
print(reverseString)

# WAP to check the how many even odd are there in given series.

even_odd = [1,2,3,4,5,6,7,8,9,0]

for i in even_odd:
    if(i % 2 == 0):
         print(i,"is an even number")
    else:
         print(i,"is an odd number")