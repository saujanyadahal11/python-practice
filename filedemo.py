f = open("student.txt", "w")
text = "My name is Saujanya Dahal"
f.write(text)
f.close()
f = open("student.txt", "r")
text1= f.read()
print(text1)
f.close()
