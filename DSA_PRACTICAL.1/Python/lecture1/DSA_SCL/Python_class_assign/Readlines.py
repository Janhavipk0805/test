# write in file
with open("lines.txt","w") as f:
    f.write("Python is easy\n")
    f.write("I love programming\n")
    f.write("Coding is fun\n")
    f.write("Practice makes perfect\n")
    f.write("Learning never stops\n")

# read all lines into a list
with open("lines.txt","r") as f:
    lines=f.readlines()

# print total lines
print("Total number of lines:",len(lines))

# print 2nd and 4th line
print("2nd line:",lines[1].strip())
print("4th line:",lines[3].strip())