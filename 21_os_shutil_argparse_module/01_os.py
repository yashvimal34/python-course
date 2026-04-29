import os

a = os.listdir("dir")
print(a)
print(os.getcwd())   # Here cwd means current working dirctory. It shows the path where present.
print(os.path.exists("dir")) # Output: True
# print(os.remove("sample.txt"))  # The txt removed form file