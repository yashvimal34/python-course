# Write a file called Rahul.txt
# It should contain data about Rahul.


f = open("Rahul.txt", "w")

string = '''
Rahul is a software developer and he lives in safipur and he is a good guy.
'''

f.write(string)

f.close()