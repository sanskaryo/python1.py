# create a program to calculate factorial of a number
# to compute factorial
num = int(input("enter the number: "))
factorial = 1

for i in range(1, num+1):
	factorial = factorial * i

print(f"The factorial of {num} is : ", end="")
print(factorial)
