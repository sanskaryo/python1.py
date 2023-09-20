n=int(input("entera number: "))
if n<2:
    print("number is not prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("not a prime")
            break
    else:
        print("it is a prime number")
    