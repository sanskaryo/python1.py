limit = int(input("Enter the number: "))
num1 = 0
num2 = 1

print(num1, end=" ")

for num in range(1, limit):
    print(num2, end=" ")
    num1, num2 = num2, num1 + num2
