# write in file
with open("newfile.txt","w") as f:
    f.write("Hello World!")
    
count=0

#read from file
with open("newfile.txt","r") as f:
    
    text=f.read()
    for ch in text:
        if ch.lower() in "aeiou":
            count+=1

#print count of vowels           
print("total vowels:",count)