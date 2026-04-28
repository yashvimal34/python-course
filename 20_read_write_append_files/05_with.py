# There is another way to read file and there is no need to close the file. Let's see how.

with open("yash.txt", "r") as f:  # This is Context Manager.
    content = f.read()
    print(content)  # Here there is no need to write f.close() for closing file because the file already closed using 'with', syntax.