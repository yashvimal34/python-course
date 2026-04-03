x = 256
y = 256
print(x is y) # True

x = 257
y = 257
print(x is y) # True

def check():
    x = 257
    y = 257
    print(x is y) # True
check()

def check():
    x = int("257")
    y = int("257")
    print(x is y) # False
check()

# In python integer varies from  -5 to 256
# This is how you can check it correct answer.