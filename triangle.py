side1=eval(input("enter the value of first side : "))
side2=eval(input("enter the value of second side : "))
side3=eval(input("enter the value of third side : "))
if(side1==side2==side3):
    print("it is a equilateral triangle")
elif(side1==side2 or side3==side1 or side2==side3):
    print("it is an isoceles triangle")

else:
    print("it is a scalene triangle")