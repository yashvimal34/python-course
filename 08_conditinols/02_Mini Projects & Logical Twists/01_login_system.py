username = "admin"
password = "12345"

user = input("user: ")
passw = input("pass: ")

if (user == username and passw == password):
    print("Login done")
elif (user == username and password != passw):
    print("Wrong Password")
else:
    print("Invalid username and password")  