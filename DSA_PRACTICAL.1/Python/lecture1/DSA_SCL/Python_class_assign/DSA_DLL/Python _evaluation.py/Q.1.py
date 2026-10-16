with open("sample.txt","w") as f:
    f.write("Python is easy\n")
    f.write("I love programming\n")
    
    with open("sample.txt","r") as f:
     lines = f.readline()
     print("First line:",lines)

     print("1st line:",lines[2].strip())
