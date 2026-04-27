a = [23, 54, 27, 75, 47, 36]

def square(x):
    return x * x

new = list(map(square, a))
print(new)

# If you are getting rid of writing above code. 
# You can use simply lambda fumction as shown below which is convienent for us.

b = [5, 33, 75, 43, 87]

new = list(map(lambda x: x*x, b))
print(new)