import random

def check(comp,user):
    if comp == user:
        return 0
    if(comp == 0 and user == 1):
        return -1
    if(comp == 1 and user == 2):
        return -1
    if(comp == 2 and user == 0):
        return -1
    
    return 1

comp = random.randint(0,2)


user = int(input("enter 0 for Snake, 1 for water , 2 for Gun :"))

score = check(comp,user)
if score == 0:
    print("Game Draw" " computer = " ,comp)
elif score == 1:
    print("You Win" "   computer = ",comp)
else:
    print("You Lose""  computer = ", comp)
    
