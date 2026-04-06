# Changing Cases.
text = "hello world"
print(text.upper()) # The output will be "HELLO WORLD"
print(text.lower()) # The Output will be "hello world"
print(text.title()) # The Output will be "Hello World"
print(text.capitalize()) # the output will be "Hello world"

# Removing Whitespaces using strips.
txt = " hello world "
print(txt.strip()) # The output will be "hello world"
print(txt.lstrip()) # the output will be "hello world "
print(txt.rstrip()) # The output will be " hello world"

# Finding and Replacing
txt1 = "Python is fun"
print(txt1.find("is"))
print(txt1.replace("fun", "easy to learn"))