# Append to an existing file called Rahul.txt
# It should add data about Rahul HomeTown.

f = open("Rahul.txt", "a")

string = '''
Rahul's home town is Kanpur where currently he is living and studying about python.
'''

f.write(string)

f.close()