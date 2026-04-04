age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age ❌")
elif age <= 2:
    print("Category: Baby 👶")
elif age <= 12:
    print("Category: Child 🧒")
elif age <= 19:
    print("Category: Teen 👦👧")
elif age <= 59:
    print("Category: Adult 🧑")
else:
    print("Category: Senior 👴👵")
