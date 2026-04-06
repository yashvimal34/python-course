text = "Python is fun"
print(text.find("is"))  # output: 7  "find methods to know the postion of string or you can say index"
print(text.replace("fun", "easy to learn"))  # output: Python is easy to learn

# Split and Join method.

text1 = "apple,banana,orange"
fruits = text1.split(",")
print(fruits)

new_text = "+".join(fruits)
print(new_text)