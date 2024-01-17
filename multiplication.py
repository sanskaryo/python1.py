#wap to print the multiplication table of a  


num = int(input("enter the number: "))
if num<=0:
    print("invalid")
else:
    for i in range(1 , 11):
        print(num,  'x ',i,'=',num*i)
    