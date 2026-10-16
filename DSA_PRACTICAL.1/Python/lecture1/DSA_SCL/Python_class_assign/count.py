with open("demo.txt","w") as f:
    f.write("Pizza\n")
    f.write("Pasta\n")
    f.write("Dosa\n")
with open("demo.txt","r") as f:
    food = f.read()
    print("Count letter words:",len(food))