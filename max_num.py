def find_max(a, b):
    if a > b:
        return a
    elif(a < 1 or b < 1):
    print()
    else:
        return b

# Usage
num1=eval(input("enter the first number "))
num2=eval(input("enter the second number "))

max_num = find_max(num1, num2)
print(f"The maximum of {num1} and {num2} is: {max_num}")
