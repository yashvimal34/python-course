s = {23, 64, 75, 34, 65, 35}
print(s)

s.add(100)
print(s)

s.add(5467)
print(s)

s.remove(23) # If the element is present it will remove otherwise it throws an error.
print(s)

s.discard(9598) # In this if the given element is present in set it will remove or discard otherwise it dosen't throws an error.



'''
Interview Question

Q. Differ between remove and discard?
A. In remove method if element is present in set it will remove otherwise it throws an error.
   In discard method if element is present in set it will remove or discard otherwise it dosen't throws an error.
'''