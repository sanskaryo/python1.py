user1=input("Wants to starts a new game yes/no  ")
if user1=="yes":
    user2=input("Wants to starts a new game yes/no  ")
    if user2=="yes":
        print("starting the game")        
        user1=input("rock,paper,scissor ")
        user2=input("rock,paper,scissor ")
        if user1=="rock"and user2=="paper":
           print("user2 wins")
        elif user1=="rock"and user2=="scissor" :
            print("user1 wins")
        elif user1=="paper" and user2=="rock":
            print("user1 wins")
        elif user1=="paper" and user2=="scissor":
            print("user2 wins")
        elif user1=="scissor" and user2=="rock":
            print("user2 wins")    
        elif user1=="scissor" and user2=="paper":
            print("user1 wins")    
        else:
            print("no one wins")
    else:
        print("ok")
else:
    print("ok")