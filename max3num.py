# Take user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find maximum number using conditional expression
max_num = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)

print("The maximum number is", max_num)
