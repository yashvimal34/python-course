# Q1. Print 1 to 5 number using for loop?

for i in range(1, 6):
    print(i)  # the range function goes from 1 to (6-1) i.e is 5 in this case

# Q2. Print the table of 5 using for loop?

for i in range(1, 11):
    print("5x",i,"=",(5*i))
    # OR
for i in range(1,11):    
    print(5*i)

# Q3. Print the fruits.
fruits = ["apple", "banana", "cherry", "kiwi"]
for fruit in fruits:
    print(fruit)