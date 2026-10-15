# take sentence from user
sentence=input("Enter a sentence: ")

# split into words and store in list
words=sentence.split()

longest=""

# find longest word
for w in words:
    if len(w)>len(longest):
        longest=w

# print longest word
print("Longest word:",longest)