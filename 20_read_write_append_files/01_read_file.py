f = open("yash.txt", "r") # In this case 'r', means read file or you can also write 'rt'=> 't', means when you wants to read file in text format. 'rb'=> in this 'b', means binary you can use it when you want to read file in binary mode.

content = f.read()

print(content)

f.close()  # It is important to close the file.