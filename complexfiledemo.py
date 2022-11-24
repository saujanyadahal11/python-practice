import os

x=0
y=1
with open("find.txt","r") as f:
    while(x==0):
        text=f.readline()
        if 'python' in text:
            print(f"python is present in {y} line")
            x = 2
        else:
            y+=1

name=input("Input the name for new file name")

with open("find.txt", "r") as f:
    text=f.read()

with open(name, "w") as f:
    f.write(text)

os.remove("find.txt")