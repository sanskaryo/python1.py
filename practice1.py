# wap to print sum of all numbers from 1 to 10 using
n = int(input("Enter a positive integer: "))

product = 1
for i in range(1, n+1):
    product *= i

print("The product of numbers from 1 to", n, "is", product)