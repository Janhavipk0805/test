with open("sample.txt","w") as f:
    f.write("I loving python\n")
    f.write("Welcome to world of Python")
with open("sample.txt","r") as f:
    contents = f.readline()
    print(contents )