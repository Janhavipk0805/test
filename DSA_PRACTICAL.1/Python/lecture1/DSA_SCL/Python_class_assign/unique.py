# write in file
with open("words.txt","w") as f:
    f.write("python is easy and python is fun")

# read from file and split into words
with open("words.txt","r") as f:
    text=f.read()
    words=text.split()

# i. print total number of words
print("Total number of words:",len(words))

# ii. print all unique words
unique=[]
for w in words:
    if w not in unique:
        unique.append(w)

print("Unique words:",unique)