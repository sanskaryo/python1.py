n = int(input("enter the number: "))

sum = 0
even = 0
for i in range(1, n+1):
    if i%2==0:
        print(f"{i} is even number")
        even += i
        print(f"the sum of first  even  number is {even} ")
    else:
        sum  += i
        print(f"the sum of first  n odd  number is {sum} ")
    
        