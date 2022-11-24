spamWords = ["hi", "your name", "program", "interest", "class" , "study", "profession"]

conversation=input("").lower()

if("hi" in conversation):
    print("hi")

elif("your name" in conversation):
    print("My name is saujanya dahal")

elif("program" in conversation):
    print("I study BIT")

elif("interest" in conversation):
    print("i am interested in coding")

elif("class" in conversation):
    print("I am a student of Bachelors")

elif("Study" in conversation):
    print("I study BIT")

elif("profession" in conversation):
    print("I am a student")

else:
    print("Thank You!")