def is_palindrome():
    number = int(input("Enter a number : " ))
    temp = number
    reverse=0
    
    while(number>0):
        dig = number%10
        reverse = reverse*10 + dig
        number = number//10
        
    if temp==reverse:
        print("Number is a Palindrome")
    else:
        print("not a palindrome")
        
is_palindrome()
    