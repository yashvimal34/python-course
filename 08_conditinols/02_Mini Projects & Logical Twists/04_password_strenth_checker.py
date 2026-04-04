password = input("Enter your password: ")

if len(password) < 6:
    print("Too short ❌")
else:
    has_letter = False
    has_digit = False

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True

    if has_letter and has_digit:
        print("Password strength: Strong ✅")
    else:
        print("Password strength: Weak ❗")
