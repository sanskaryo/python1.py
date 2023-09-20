## Program to display the Fibonacci sequence up to n-th term
#
#nterms = int(input("How many terms? "))
#
## first two terms
#n1, n2 = 0, 1
#count = 0
#
## check if the number of terms is valid
#if nterms <= 0:
#   print("Please enter a posit     

limit = int(input("enter the number : "))
num1 = 0
num2 = 1 
num3 = 0
print(num1)

for num in range(1, limit+1):
    num1 = num2
    num2 = num3
    num3 = num1 + num2 
    print(num3)