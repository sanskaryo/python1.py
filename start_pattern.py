n=int(input("enter the number of rows:"))
for i in range(n+1):
   if(i%2!=0):
       for j in range(i):
           print("*", end=" ")
   print()



n=int(input("enter the number of rows:"))
for i in range(n+1):

        for j in range(i):
            print(j+1, end=" ")
        print()
    