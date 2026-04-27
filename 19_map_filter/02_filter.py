def no_is_greater_than_7(x):
    if x > 7:
        return True
    else:
        return False
    
a = [7, 5, 75, 76, 6, 3, 78, 5]
new = list(filter(no_is_greater_than_7, a))
print(new)

# If you are getting rid of writing above code. 
# You can use simply lambda fumction as shown below which convienent for us.

b = [4, 76, 5, 34, 0, 3, 2, 76]

new = list(filter(lambda x: x > 7, b))
print(new)