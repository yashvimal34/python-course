a = {23, 54, 34, 65, 43}
b = {34, 55, 23, 90, 12}

c = a.union(b) # Contain all the elements in 'a' along with all the elements in 'b'.
print(c, type(c))

d = a.intersection(b) # Contain only the elements that are present in 'a' as well as in  'b'
print(d, type(d))