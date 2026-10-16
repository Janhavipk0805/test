with open("activity.txt","a") as f:
    f.write("Today I practised Python file handling\n")

with open("activity.txt","r") as f:
    record = f.read()

print(record)