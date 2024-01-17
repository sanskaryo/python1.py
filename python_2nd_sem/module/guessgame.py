import random

Cnum = random.randint(1,101)

Uinput = int(input("Enter a number between 1 and 100: "))

if Uinput == Cnum:
    print("Yeah You guessed correctly!" , Cnum)
elif Uinput > Cnum:
    print("Too high!", Cnum)
else:
    print("Too low!", Cnum)