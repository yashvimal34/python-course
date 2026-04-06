# Spliting and Joining.
# Spliting.
text = "apple,banana,mango"
fruits = text.split(",")
print(fruits) # The output will be ['apple', 'banana', 'mango']

#  Joining.
new_text = " - ".join(fruits)
print(new_text) # output: apple-banana-mango

# Checking string properties.
text_two = "Python123"
print(text_two.isalpha()) # output: False.
print(text_two.isdigit()) # output: False.
print(text_two.isalnum()) # output: True.
print(text_two.isspace()) # output: False.