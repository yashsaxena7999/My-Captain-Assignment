filename = input("Enter Filename: ")
file_ext = filename.split(".")
if file_ext[-1]=='py':
    print("Python file!")
else:
    print("Not a python file!")