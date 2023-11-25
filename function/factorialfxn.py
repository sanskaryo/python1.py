def fact(n):
    ans = 1
    if n == 0:
        ans =  1
    else:
        for i in range(1,n+1):
            ans *= i
                
    return ans
n = int(input(" enter number "))
output = fact(n)
print("the factorial is" , output)