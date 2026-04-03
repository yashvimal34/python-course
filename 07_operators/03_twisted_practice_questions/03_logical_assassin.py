x = False
y = True
z = False
print((x or y) and not (y and z or x)) # True

# ((x or y) and not (y and z or x))
# (True and not False)
#  True and True
#  Trues