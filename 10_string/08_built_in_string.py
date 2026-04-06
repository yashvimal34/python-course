# Useful Built-in String methods.

# 1. len() - Get a length of a string.
# 2. ord() and chr() - Character Encoding
# 3. format() and f-strings.

# 1. len() method.
name = "Yash Sarthak"
print(len(name))

# 2. ord() and chr()
name1 = "yash"
print(ord('a'))
print(chr(3))

# 3. .format() method.
name2 = "Yash Sarthak"
age = 20
print("My name is {} and I am {} years old" .format(name2, age))

# 4. f-strings method
name3 = "Yash Vimal"
age1  = 20
print(f"My name is {name3} and I am {age1} years old.")

# Using expressions in f-strings.
x = 10
y = 40
print(f"the x is {10} and y is {40} sum is {x + y}")

# formatting numbers.
pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi: .2f}")

# Padding and Alignment.
text = "Python is easy to learn an understand"
print(f"{text:>10}")  # Right align
print(f"{text:<10}")  # Left align
print(f"{text:^10}")  # Center align