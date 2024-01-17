import random

def play():
  for i in range(1,6):
    user_choice = int(input("Enter 0 for Rock, 1 for Paper or 2 for Scissors: "))
    choices = ["Rock", "Paper", "Scissors"]
  
    computer_choice = random.randint(0,2)
    print(f"Computer chose: {choices[computer_choice]}")
  
    print(f"You chose: {choices[user_choice]}")
  
    if user_choice == 0:
      if computer_choice == 2:
        print("You win!")
      elif computer_choice == 1:
        print("You lose!")
      else:
        print("It's a draw")
  
    elif user_choice == 1:  
      if computer_choice == 0:
        print("You win!")
      elif computer_choice == 2:  
        print("You lose!")
      else:
        print("It's a draw")
  
    elif user_choice == 2:
      if computer_choice == 1:
        print("You win!")  
      elif computer_choice == 0:
        print("You lose!")
      else:
        print("It's a draw")
  
    else:
      print("Invalid input, you lose!")
  
play()
  