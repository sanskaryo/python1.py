def find_max(a, b):
    if a > b:
        return a


num1=eval(input("enter the first number "))
num2=eval(input("enter the second number "))

if (num1<1) or (num2<1):
    print("invalid")
    
elif(num1 > num2):
    print(f"num1 {num1} is greater than num2 {num2}")
elif(num2 > num1):
    print(f"num2 {num2} is greater than num1 {num1}")
    

    
else:
    print(f"num2 {num2} is equal to {num1}")
    
print("  ")
max_num = (num1, num2)
print(f"The maximum of {num1} and {num2} is: {max_num}")
