number = int(input("Enter a number : " ))
reverse=0

while(number>0):
    dig = number%10
    reverse = reverse*10 + dig
    number = number//10
    
print(reverse)