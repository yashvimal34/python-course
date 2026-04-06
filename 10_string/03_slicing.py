name = "Sarthak"

print(name[0:2]) # To resolve this [0:2], we have formula "n-1", in this [0:2] => 2 is 'n', means, 2-1=1, that goes from 0 to 1. # The Output will be: "Sa".

# Now will print -ive indexex using formula "n-1".

print(name[0:-3]) # To resolve this [0:-3] we have take the total length of 'name', i.e. 7, and subtract 7 from -3, which means it will be [0:4], will use formula i.e is 'n-1', 'n is 4', i.e 4-1=3 now it will be [0:3] that goes from 0 to 3. # The Output will be 'Sart'.

print(name[2:-3]) # The output will be 'rt'.

# Now will print three numbers.
namea = "Yashsarthakvimal"
# print(name[0:10:n]) # Skip n-1 in place of 'n' will use numbers.
print(namea[0:10:1]) # Skip   1-1 which is 0 characters. # The Output will be: "Yashsartha".
print(namea[0:10:2]) # Skip   2-1 which is 1 characters. # The Output will be: "Yssrh".
print(namea[0:10:3]) # SKip   3-1 which is 2 characters. # The Output will be: "Yhra".


# Now print characters using only any one number let's see how.
print(namea[:7]) # Replace the first empty number with 0 # namea[0:4]. # The output will be: "Yashsar".
print(namea[7:]) # Replace the second empty number with length of string. # namea[7:16] #Output:"thakvimal".
print(len(namea[::-1])) # Replace the first and second number with 0. # Output: "Reverse String".