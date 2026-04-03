x = True
y = False
z = False
print(x and not y or z and not x) # True.

# In this I respect operator precedence.
# (x and not y or z and not x)
# x and True or z and not x
#  True or z and False
#  True or False
#  True