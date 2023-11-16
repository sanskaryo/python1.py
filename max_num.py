def find_max(a, b):
    if a < 1 or b < 1:
        print("Both numbers should be greater than 0")
        return
    elif a > b:
        return a
    else:
        return b

# Usage
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))

max_num = find_max(num1, num2)
if max_num is not None:
    print(f"The maximum of {num1} and {num2} is: {max_num}")
