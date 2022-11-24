oxford = {
            "gift": "something willingly given to someone to appreciate",
            "this": "A keyword in c++",
            "Youtube": "A video sharing platform",
            "instagram": "A picture sharing platform",
            "mylist": [1, 3, 45],
            "mynum": 999
        }

print(oxford.items())

for a,b in oxford.items(): 
    print(a, ":=:", b)

for key in oxford.keys():
    print(key)

oxford.update ({"name": "saujanya"})
oxford.update ({"mynum": 111})

for a,b in oxford.items(): 
    print(a, ":=:", b)

print(oxford['name'])  
print(oxford.get('incorrectKey'))