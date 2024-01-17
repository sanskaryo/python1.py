def prime(num):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    return count==2
a = prime(10)
print(a)