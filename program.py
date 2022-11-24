import random

def calculations(c, u):
    if(c=='s' and u=='r'):
        won = True
    elif(c=='p' and u=='s'):
        won = True
    elif(c=='r' and u=='p'):
        won = True
    elif(c == u):
        won = None
    else:
        won = False
    return won

def show_result(result):
    if(result is None):
        print("Draw")
    elif (result):
        print("You Won")
    else:
        print("You Lose")

options=('s','p','r')
comp_choice = options[random.randint(0,2)]
print(comp_choice)
user_choice=input("enter your choice: ").lower()

result = calculations(comp_choice, user_choice)
show_result(result)

print(f"since you choose {user_choice} and computer choose {comp_choice}")
